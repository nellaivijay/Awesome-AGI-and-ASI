#!/usr/bin/env python3
"""Extract new URLs from git diff of markdown files.

Parses the diff between the current commit and its parent to find URLs
that were added (ArXiv, GitHub, HuggingFace, blogs, papers, etc.),
classifies them, and writes structured JSON to an output directory.
"""

import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone


# ---------------------------------------------------------------------------
# URL classification
# ---------------------------------------------------------------------------

URL_PATTERN = re.compile(
    r'https?://[^\s\)\]\>\"\'\,\`\*]+'
)

# Markdown link pattern: [text](url)
MD_LINK_PATTERN = re.compile(
    r'\[([^\]]*)\]\((https?://[^\s\)]+)\)'
)

CATEGORY_RULES: list[tuple[str, re.Pattern]] = [
    ("arxiv",        re.compile(r'arxiv\.org')),
    ("github",       re.compile(r'github\.com')),
    ("huggingface",  re.compile(r'huggingface\.co')),
    ("paper",        re.compile(r'(openreview\.net|aclanthology\.org|papers\.nips\.cc|proceedings\.mlr\.press|semanticscholar\.org|dl\.acm\.org|ieeexplore\.ieee\.org|sciencedirect\.com)')),
    ("youtube",      re.compile(r'(youtube\.com|youtu\.be)')),
    ("docs",         re.compile(r'(readthedocs|docs\.|\.readthedocs\.io)')),
    ("blog",         re.compile(r'(medium\.com|blog\.|substack\.com|towardsdatascience\.com|\.ai/blog)')),
]


def classify_url(url: str) -> str:
    """Return a category string for the given URL."""
    for category, pattern in CATEGORY_RULES:
        if pattern.search(url):
            return category
    return "other"


# ---------------------------------------------------------------------------
# Diff parsing
# ---------------------------------------------------------------------------

def get_diff(base_ref: str | None = None) -> str:
    """Return the unified diff for markdown files only.

    In a GitHub Actions context we use the environment variables provided
    by the event payload.  Falls back to ``HEAD~1..HEAD``.
    """
    if base_ref:
        diff_range = f"{base_ref}..HEAD"
    else:
        diff_range = "HEAD~1..HEAD"

    result = subprocess.run(
        ["git", "diff", diff_range, "--", "*.md"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"[warn] git diff failed: {result.stderr.strip()}", file=sys.stderr)
        return ""
    return result.stdout


def current_section_heading(diff_lines: list[str], index: int) -> str:
    """Walk backwards through diff context to find the nearest markdown heading."""
    for i in range(index, -1, -1):
        line = diff_lines[i]
        # Unified diff context lines start with ' ', added lines with '+'
        text = line[1:] if line and line[0] in (' ', '+', '-') else line
        m = re.match(r'^(#{1,6})\s+(.*)', text)
        if m:
            return m.group(2).strip()
    return "Unknown"


def extract_urls_from_diff(diff_text: str) -> list[dict]:
    """Parse the diff and return a list of URL records from *added* lines."""
    if not diff_text:
        return []

    urls_seen: set[str] = set()
    records: list[dict] = []
    lines = diff_text.splitlines()

    current_file = None

    for idx, line in enumerate(lines):
        # Track which file we're in
        if line.startswith("+++ b/"):
            current_file = line[6:]
            continue
        if line.startswith("--- "):
            continue

        # Only look at added lines (skip the diff header "+++" already handled)
        if not line.startswith("+") or line.startswith("+++"):
            continue

        added_text = line[1:]  # strip the leading '+'

        # First try markdown links to capture link text
        for match in MD_LINK_PATTERN.finditer(added_text):
            link_text, url = match.group(1), match.group(2)
            url = url.rstrip(".,;:!?)")
            if url in urls_seen:
                continue
            urls_seen.add(url)
            section = current_section_heading(lines, idx)
            records.append({
                "url": url,
                "category": classify_url(url),
                "link_text": link_text or None,
                "section": section,
                "source_file": current_file,
            })

        # Then catch bare URLs not already captured via markdown links
        for match in URL_PATTERN.finditer(added_text):
            url = match.group(0).rstrip(".,;:!?)")
            if url in urls_seen:
                continue
            urls_seen.add(url)
            section = current_section_heading(lines, idx)
            records.append({
                "url": url,
                "category": classify_url(url),
                "link_text": None,
                "section": section,
                "source_file": current_file,
            })

    return records


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    base_ref = os.environ.get("INPUT_BASE_REF")  # set by the workflow
    diff = get_diff(base_ref)

    records = extract_urls_from_diff(diff)

    commit_sha = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        capture_output=True, text=True,
    ).stdout.strip()

    payload = {
        "extracted_at": datetime.now(timezone.utc).isoformat(),
        "commit": commit_sha,
        "url_count": len(records),
        "urls": records,
    }

    # Write output
    out_dir = os.environ.get("OUTPUT_DIR", "queue")
    os.makedirs(out_dir, exist_ok=True)

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_path = os.path.join(out_dir, f"urls-{timestamp}-{commit_sha[:8]}.json")

    with open(out_path, "w") as f:
        json.dump(payload, f, indent=2)

    print(f"Extracted {len(records)} new URL(s) -> {out_path}")

    # Also write to GitHub Actions output if available
    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output:
        with open(github_output, "a") as fh:
            fh.write(f"url_count={len(records)}\n")
            fh.write(f"output_file={out_path}\n")

    # Print summary for the workflow log
    for r in records:
        tag = f"[{r['category']}]"
        label = f" ({r['link_text']})" if r.get("link_text") else ""
        print(f"  {tag:14s} {r['url']}{label}")

    if not records:
        print("  (no new URLs found in this diff)")


if __name__ == "__main__":
    main()
