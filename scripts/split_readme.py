#!/usr/bin/env python3
"""Split README.md into per-section docs/ files for MkDocs."""

import os
import re

README = "README.md"
DOCS = "docs"

# Section mapping: (## heading text) -> (filename, nav_group)
SECTION_MAP = [
    ("Understanding AI, AGI, and ASI", "understand/ai-agi-asi.md", "Understand"),
    ("ASI and Superintelligence Research", "understand/asi-research.md", "Understand"),
    ("Frameworks and Platforms", "build/frameworks.md", "Build"),
    ("Agents", "build/agents.md", "Build"),
    ("Physical AI & Embodied Intelligence", "build/physical-ai.md", "Build"),
    ("Paper-to-Code Automation", "build/paper-to-code.md", "Build"),
    ("LLM Application Frameworks", "infrastructure/llm-frameworks.md", "Infrastructure"),
    ("RAG and Vector Databases", "infrastructure/rag-vector-db.md", "Infrastructure"),
    ("Data Infrastructure for AI at Scale", "infrastructure/data-infra.md", "Infrastructure"),
    ("LLM Fine-Tuning Techniques", "infrastructure/fine-tuning.md", "Infrastructure"),
    ("LLM Deployment and Serving", "infrastructure/deployment.md", "Infrastructure"),
    ("Distributed Training Frameworks", "infrastructure/distributed-training.md", "Infrastructure"),
    ("Prompt Engineering", "infrastructure/prompt-engineering.md", "Infrastructure"),
    ("Safety, Alignment and Governance", "safety/safety-alignment.md", "Safety & Governance"),
    ("Papers, Blogs, Courses and Lectures", "research/papers-blogs.md", "Research & Learn"),
    ("Tutorials and Guides", "research/tutorials.md", "Research & Learn"),
    ("Top Conferences", "research/conferences.md", "Research & Learn"),
    ("Contributing", "contributing.md", None),
]

def slugify(heading):
    """Normalize heading for matching."""
    return re.sub(r'[^a-z0-9 ]', '', heading.lower()).strip()

def build_lookup():
    lookup = {}
    for heading, filepath, group in SECTION_MAP:
        lookup[slugify(heading)] = (filepath, group, heading)
    return lookup

def split_readme():
    with open(README, "r") as f:
        lines = f.readlines()

    lookup = build_lookup()
    sections = []
    current = None

    # Extract everything before first ## (for index.md)
    preamble_lines = []

    for i, line in enumerate(lines):
        m = re.match(r'^## (.+)', line)
        if m:
            heading = m.group(1).strip()
            slug = slugify(heading)

            if slug == "table of contents":
                # Skip the ToC section - we don't need it, MkDocs has nav
                current = {"skip": True, "lines": []}
                continue

            if slug in lookup:
                filepath, group, original = lookup[slug]
                if current and not current.get("skip"):
                    sections.append(current)
                current = {
                    "filepath": filepath,
                    "group": group,
                    "heading": original,
                    "lines": [line],
                    "skip": False,
                }
                continue
            elif slug == "license":
                # Skip license section
                if current and not current.get("skip"):
                    sections.append(current)
                current = {"skip": True, "lines": []}
                continue

        if current is None:
            preamble_lines.append(line)
        elif current is not None:
            current["lines"].append(line)

    if current and not current.get("skip"):
        sections.append(current)

    # Write section files
    for sec in sections:
        fpath = os.path.join(DOCS, sec["filepath"])
        os.makedirs(os.path.dirname(fpath), exist_ok=True)

        content = "".join(sec["lines"])
        # Convert ## heading to # (top-level for each page)
        content = re.sub(r'^## ', '# ', content, count=1)

        with open(fpath, "w") as f:
            f.write(content)
        print(f"  -> {fpath} ({len(sec['lines'])} lines)")

    # Write index.md (landing page)
    write_index(preamble_lines)

    # Print nav structure for mkdocs.yml
    print("\nNav structure:")
    groups = {}
    for sec in sections:
        g = sec.get("group")
        if g:
            groups.setdefault(g, []).append((sec["heading"], sec["filepath"]))
        else:
            print(f"  - {sec['heading']}: {sec['filepath']}")
    for g, items in groups.items():
        print(f"  - {g}:")
        for heading, fp in items:
            print(f"      - {heading}: {fp}")

def write_index(preamble_lines):
    os.makedirs(DOCS, exist_ok=True)
    fpath = os.path.join(DOCS, "index.md")

    # Clean up preamble: keep title, badges, quote, description
    content = "".join(preamble_lines).rstrip() + "\n"

    with open(fpath, "w") as f:
        f.write(content)
    print(f"  -> {fpath} (landing page)")

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)) or ".")
    os.chdir("..")  # Go to repo root
    split_readme()
