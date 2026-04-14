#!/usr/bin/env python3
"""Parse README.md and extract structured resource data into YAML files.

Converts the monolithic README into a set of typed YAML data files under data/.
Narrative/prose sections are preserved as markdown templates; resource tables
are extracted into structured YAML with typed schemas.

YAML Schema
-----------
Each file under data/ follows this structure:

    section:
      title: str
      description: str           # section intro (blockquote)
      badges: list[str]          # shields.io badge URLs (optional)

    subsections:
      - title: str
        description: str         # optional subsection intro
        type: str                # framework | tool | paper | book | method |
                                 # conference | blog | organization | benchmark |
                                 # technique | platform | model
        items:
          - name: str
            url: str             # primary URL
            github: str          # org/repo slug (optional)
            description: str
            links: list[{label, url}]
            # Type-specific fields:
            #   framework: notes, stars_badge
            #   paper/book: author, year
            #   method: paper_url, code_url
            #   conference: full_name, when, website, relevance
"""

import json
import os
import re
import sys
import textwrap
from collections import OrderedDict
from pathlib import Path

import yaml


# ---------------------------------------------------------------------------
# Custom YAML dumper that preserves insertion order and uses block style
# ---------------------------------------------------------------------------

class OrderedDumper(yaml.SafeDumper):
    pass

def _dict_representer(dumper, data):
    return dumper.represent_mapping('tag:yaml.org,2002:map', data.items())

OrderedDumper.add_representer(OrderedDict, _dict_representer)
OrderedDumper.add_representer(dict, _dict_representer)

# Use literal block style for long strings
def _str_representer(dumper, data):
    if '\n' in data or len(data) > 120:
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)

OrderedDumper.add_representer(str, _str_representer)


# ---------------------------------------------------------------------------
# Markdown parsing helpers
# ---------------------------------------------------------------------------

# Match markdown links: [text](url)
MD_LINK = re.compile(r'\[([^\]]*)\]\(([^)]+)\)')
# Match shields.io badge images
BADGE_RE = re.compile(r'!\[([^\]]*)\]\((https://img\.shields\.io/badge/[^)]+)\)')
# Match GitHub star badges
STAR_BADGE_RE = re.compile(r'!\[GitHub Repo stars\]\((https://badgen\.net/github/stars/[^)]+)\)')
# Blockquote
BLOCKQUOTE_RE = re.compile(r'^>\s*(.+)', re.MULTILINE)


def extract_links(text: str) -> list[dict]:
    """Extract all markdown links from text."""
    links = []
    for m in MD_LINK.finditer(text):
        label, url = m.group(1), m.group(2)
        if 'img.shields.io' in url or 'badgen.net' in url:
            continue
        links.append({"label": label, "url": url})
    return links


def strip_md_links(text: str) -> str:
    """Replace [text](url) with just text."""
    return MD_LINK.sub(r'\1', text)


def clean_cell(cell: str) -> str:
    """Clean a table cell."""
    return cell.strip().strip('|').strip()


def parse_table(lines: list[str]) -> list[dict]:
    """Parse a markdown table into a list of row dicts."""
    if len(lines) < 3:
        return []
    # Header row
    headers = [clean_cell(c) for c in lines[0].split('|') if c.strip()]
    # Skip separator row (lines[1])
    rows = []
    for line in lines[2:]:
        cells = [clean_cell(c) for c in line.split('|')]
        # Filter empty leading/trailing cells from pipe splitting
        cells = [c for c in cells if c or cells.index(c) > 0]
        # Pad or trim to match header count
        while len(cells) < len(headers):
            cells.append("")
        cells = cells[:len(headers)]
        rows.append(dict(zip(headers, cells)))
    return rows


# ---------------------------------------------------------------------------
# Section parsers — convert parsed table rows into typed YAML items
# ---------------------------------------------------------------------------

def parse_framework_row(row: dict) -> dict:
    """Parse a framework/agent table row (Name | Stars | Intro | Notes)."""
    name_cell = row.get("Name", "")
    links = extract_links(name_cell)
    name = strip_md_links(name_cell).strip()
    github_url = links[0]["url"] if links else ""
    github_slug = ""
    if "github.com/" in github_url:
        parts = github_url.rstrip("/").split("github.com/")[1]
        github_slug = parts

    intro = row.get("Introduction", row.get("Description", ""))
    notes_raw = row.get("Notes", row.get("notes", ""))

    item = OrderedDict()
    item["name"] = name
    if github_slug:
        item["github"] = github_slug
    elif github_url:
        item["url"] = github_url
    item["description"] = strip_md_links(intro).strip()
    if notes_raw and notes_raw.strip() != "-":
        extra_links = extract_links(notes_raw)
        # Keep raw notes for faithful reconstruction
        item["raw_notes"] = notes_raw.strip()
        item["notes"] = strip_md_links(notes_raw).strip()
        if extra_links:
            item["links"] = extra_links
    return item


def parse_tool_row(row: dict) -> dict:
    """Parse a tool/resource table row (Name | Description | Links)."""
    # Broad column name fallback chain
    name_cell = row.get("Name", row.get("Tool", row.get("Tool/Method", row.get("Resource",
        row.get("Network", row.get("Platform", row.get("Company",
        row.get("Method", row.get("Topic", row.get("Approach",
        row.get("Technique", row.get("Signal", row.get("Metric",
        row.get("Trend", row.get("Challenge", row.get("Benchmark", ""))))))))))))))))
    desc_cell = row.get("Description", row.get("Focus", row.get("What It Means",
        row.get("Current State", ""))))
    links_cell = row.get("Links", row.get("Link", ""))

    name_links = extract_links(name_cell)
    all_links = extract_links(links_cell) if links_cell else []

    raw_name = name_cell.strip()
    name = strip_md_links(name_cell).strip().lstrip("**").rstrip("**")
    # Only set url from name column links (preserves bold vs link distinction)
    url = name_links[0]["url"] if name_links else ""

    item = OrderedDict()
    item["name"] = name
    item["raw_name"] = raw_name
    if url:
        item["url"] = url
    item["description"] = strip_md_links(desc_cell).strip()
    if all_links:
        item["links"] = all_links
    # Preserve raw links cell text when it contains non-link text (e.g. plain text sources)
    if links_cell and links_cell.strip():
        raw_text = links_cell.strip()
        plain_text = strip_md_links(raw_text).strip()
        if plain_text and plain_text != "-":
            # Only store if there's meaningful text beyond just the links
            link_labels = " ".join(lnk["label"] for lnk in all_links)
            if plain_text != link_labels and plain_text.replace(",", "").strip() != link_labels:
                item["links_text"] = raw_text
    return item


def parse_paper_row(row: dict) -> dict:
    """Parse a paper table row (Paper | Authors | Year | Description | Links)."""
    paper_cell = row.get("Paper", row.get("Concept / Paper", ""))
    author_cell = row.get("Author(s)", row.get("Authors", row.get("Authors / Org", row.get("Org", ""))))
    year_cell = row.get("Year", "")
    desc_cell = row.get("Description", "")
    links_cell = row.get("Links", "")

    name = strip_md_links(paper_cell).strip()
    all_links = extract_links(links_cell) if links_cell else extract_links(paper_cell)

    item = OrderedDict()
    item["name"] = name
    if author_cell:
        item["author"] = author_cell.strip()
    if year_cell:
        try:
            item["year"] = int(year_cell.strip())
        except ValueError:
            item["year"] = year_cell.strip()
    item["description"] = strip_md_links(desc_cell).strip()
    if all_links:
        item["links"] = all_links
    return item


def parse_book_row(row: dict) -> dict:
    """Parse a book table row (Book | Author | Year | Description)."""
    book_cell = row.get("Book", "")
    author_cell = row.get("Author(s)", "")
    year_cell = row.get("Year", "")
    desc_cell = row.get("Description", "")

    name = strip_md_links(book_cell).strip().lstrip("**").rstrip("**")

    item = OrderedDict()
    item["name"] = name
    if author_cell:
        item["author"] = author_cell.strip()
    if year_cell:
        try:
            item["year"] = int(year_cell.strip())
        except ValueError:
            item["year"] = year_cell.strip()
    item["description"] = desc_cell.strip()
    return item


def parse_method_row(row: dict) -> dict:
    """Parse a fine-tuning method row (Method | Description | Paper | Code)."""
    method_cell = row.get("Method", row.get("Technique", row.get("Approach",
        row.get("Tool/Method", row.get("Concept / Paper", "")))))
    desc_cell = row.get("Description", "")
    paper_cell = row.get("Paper", "")
    code_cell = row.get("Code", "")
    links_cell = row.get("Links", "")

    method_links = extract_links(method_cell)
    raw_name = method_cell.strip()
    name = strip_md_links(method_cell).strip().lstrip("**").rstrip("**")

    item = OrderedDict()
    item["name"] = name
    item["raw_name"] = raw_name
    if method_links:
        item["url"] = method_links[0]["url"]
    item["description"] = strip_md_links(desc_cell).strip()

    links = []
    if paper_cell and paper_cell.strip() != "-":
        for lnk in extract_links(paper_cell):
            # Preserve the original link label (don't hardcode "Paper")
            links.append({"label": lnk["label"], "url": lnk["url"]})
    if code_cell and code_cell.strip() != "-":
        for lnk in extract_links(code_cell):
            links.append({"label": lnk.get("label", "Code"), "url": lnk["url"]})
    # Handle generic "Links" column (for Approach tables without Paper/Code)
    if not links and links_cell and links_cell.strip() != "-":
        for lnk in extract_links(links_cell):
            links.append(lnk)
    if links:
        item["links"] = links
    return item


def parse_conference_row(row: dict) -> dict:
    """Parse a conference row."""
    conf_cell = row.get("Conference", "")
    full_name = row.get("Full Name", "")
    conf_desc = row.get("Description", "")
    organizer = row.get("Organizer", "")
    when = row.get("When", "")
    website_cell = row.get("Website", "")
    relevance = row.get("AGI Relevance", "")

    raw_name = conf_cell.strip()
    name = strip_md_links(conf_cell).strip().lstrip("**").rstrip("**")
    website_links = extract_links(website_cell)

    item = OrderedDict()
    item["name"] = name
    item["raw_name"] = raw_name
    if full_name:
        item["full_name"] = full_name.strip()
    elif conf_desc:
        item["full_name"] = conf_desc.strip()
    if organizer:
        item["full_name"] = organizer.strip()
    if when:
        item["when"] = when.strip()
    if website_links:
        item["url"] = website_links[0]["url"]
        item["website_label"] = website_links[0]["label"]
    elif website_cell and website_cell.strip():
        # Plain text in Website column (no link), e.g. "At NeurIPS (Dec) and ICML (Jul)"
        item["website_text"] = website_cell.strip()
    if relevance:
        item["relevance"] = strip_md_links(relevance).strip()
    return item


def parse_blog_row(row: dict) -> dict:
    """Parse a blog/resource row (Resource | Description)."""
    name_cell = row.get("Resource", row.get("Name", ""))
    desc_cell = row.get("Description", "")

    name_links = extract_links(name_cell)
    raw_name = name_cell.strip()
    name = strip_md_links(name_cell).strip()

    item = OrderedDict()
    item["name"] = name
    item["raw_name"] = raw_name
    if name_links:
        item["url"] = name_links[0]["url"]
    item["description"] = strip_md_links(desc_cell).strip()
    return item


def parse_org_row(row: dict) -> dict:
    """Parse an organization row."""
    org_cell = row.get("Organization", "")
    focus_cell = row.get("Focus", "")
    links_cell = row.get("Links", "")

    raw_name = org_cell.strip()
    name = strip_md_links(org_cell).strip().lstrip("**").rstrip("**")
    all_links = extract_links(links_cell)

    item = OrderedDict()
    item["name"] = name
    item["raw_name"] = raw_name
    item["description"] = strip_md_links(focus_cell).strip()
    if all_links:
        item["links"] = all_links
    return item


def parse_benchmark_row(row: dict) -> dict:
    """Parse a benchmark row."""
    name_cell = row.get("Benchmark", row.get("Name", ""))
    desc_cell = row.get("Description", "")
    links_cell = row.get("Links", "")

    raw_name = name_cell.strip()
    name = strip_md_links(name_cell).strip().lstrip("**").rstrip("**")
    all_links = extract_links(links_cell)

    item = OrderedDict()
    item["name"] = name
    item["raw_name"] = raw_name
    item["description"] = strip_md_links(desc_cell).strip()
    if all_links:
        item["links"] = all_links
    return item


def parse_model_row(row: dict) -> dict:
    """Parse a model/VLA row."""
    model_cell = row.get("Model", row.get("Model / Architecture", ""))
    org_cell = row.get("Org", row.get("Provider", ""))
    year_cell = row.get("Year", "")
    desc_cell = row.get("Description", row.get("Key Notes", ""))
    links_cell = row.get("Links", "")

    raw_name = model_cell.strip()
    name = strip_md_links(model_cell).strip().lstrip("**").rstrip("**")
    all_links = extract_links(links_cell)

    item = OrderedDict()
    item["name"] = name
    item["raw_name"] = raw_name
    if org_cell:
        item["org"] = org_cell.strip()
    if year_cell:
        try:
            item["year"] = int(year_cell.strip())
        except ValueError:
            item["year"] = year_cell.strip()
    item["description"] = strip_md_links(desc_cell).strip()
    if all_links:
        item["links"] = all_links
    return item


def parse_enterprise_row(row: dict) -> dict:
    """Parse an enterprise agent row (Name | Intro | Notes)."""
    name_cell = row.get("Name", "")
    intro_cell = row.get("Introduction", "")
    notes_cell = row.get("Notes", "")

    name_links = extract_links(name_cell)
    name = strip_md_links(name_cell).strip()

    item = OrderedDict()
    item["name"] = name
    if name_links:
        item["url"] = name_links[0]["url"]
    item["description"] = strip_md_links(intro_cell).strip()
    if notes_cell and notes_cell.strip() != "-":
        item["notes"] = strip_md_links(notes_cell).strip()
    return item


# Router: detect table type from headers
PARSER_MAP = {
    frozenset(["Name", "Github Stars", "Introduction", "Notes"]): parse_framework_row,
    frozenset(["Name", "Github Stars", "Introduction"]): parse_framework_row,
    frozenset(["Name", "Introduction", "Notes"]): parse_enterprise_row,
}


def detect_table_type(headers: list[str]) -> str:
    """Determine the logical table type from its column headers."""
    hs = frozenset(h.strip() for h in headers)
    if "Github Stars" in hs and "Introduction" in hs:
        if "Notes" not in hs:
            return "framework"
        return "framework"
    if "Introduction" in hs and "Notes" in hs and "Github Stars" not in hs:
        return "enterprise"
    if "Organization" in hs:
        return "organization"
    if "Book" in hs:
        return "book"
    if "Benchmark" in hs:
        return "benchmark"
    if "Conference" in hs:
        if "AGI Relevance" in hs:
            return "conference_full"
        return "conference_simple"
    if "Paper" in hs and ("Authors" in hs or "Author(s)" in hs or "Authors / Org" in hs):
        return "paper"
    if "Concept / Paper" in hs:
        return "paper"
    if "Method" in hs and "Paper" in hs:
        return "method"
    if "Technique" in hs and "Paper" in hs:
        return "technique"
    if "Approach" in hs:
        return "approach"
    if "Model" in hs or "Model / Architecture" in hs:
        return "model"
    if "Tool/Method" in hs or "Tool" in hs:
        return "tool_method"
    if "Company" in hs:
        return "company"
    if "Platform" in hs:
        return "platform"
    if "Network" in hs:
        return "network"
    if "Resource" in hs and "Links" in hs:
        return "resource"
    if "Resource" in hs and "Links" not in hs:
        return "blog"
    if "Challenge" in hs:
        return "challenge"
    if "Signal" in hs:
        return "signal"
    if "Metric" in hs:
        return "metric"
    return "tool"


def detect_parser(headers: list[str]):
    """Auto-detect the right parser for a table based on its headers."""
    hs = frozenset(h.strip() for h in headers)
    if hs in PARSER_MAP:
        return PARSER_MAP[hs]
    if "Author(s)" in hs and "Year" in hs and ("Book" in hs or "Paper" not in hs):
        if "Book" in hs:
            return parse_book_row
        return parse_paper_row
    if "Paper" in hs and ("Authors" in hs or "Author(s)" in hs or "Authors / Org" in hs):
        return parse_paper_row
    if "Concept / Paper" in hs:
        return parse_paper_row
    if "Method" in hs and "Paper" in hs:
        return parse_method_row
    if "Technique" in hs and ("Paper" in hs or "Links" in hs):
        return parse_method_row
    if "Conference" in hs and ("Full Name" in hs or "AGI Relevance" in hs):
        return parse_conference_row
    if "Conference" in hs and "Description" in hs:
        return parse_conference_row
    if "Benchmark" in hs:
        return parse_benchmark_row
    if "Organization" in hs:
        return parse_org_row
    if "Model" in hs or "Model / Architecture" in hs:
        return parse_model_row
    if "Approach" in hs and "Description" in hs:
        return parse_method_row
    if "Resource" in hs and "Description" in hs and "Links" not in hs:
        return parse_blog_row
    if "Tool/Method" in hs or "Tool" in hs:
        return parse_tool_row
    # Default
    return parse_tool_row


# ---------------------------------------------------------------------------
# Section mapping: README ## headings -> data file + subsection structure
# ---------------------------------------------------------------------------

# Maps (h2_heading, optional_h3_heading) to (yaml_file, subsection_type)
# If h3 is None, the entire section is one logical group.

SECTION_FILE_MAP = {
    "ASI and Superintelligence Research": "asi-research.yaml",
    "Frameworks and Platforms": "frameworks.yaml",
    "Agents": "agents.yaml",
    "Physical AI & Embodied Intelligence": "physical-ai.yaml",
    "Paper-to-Code Automation": "paper-to-code.yaml",
    "LLM Application Frameworks": "llm-frameworks.yaml",
    "RAG and Vector Databases": "rag-vector-db.yaml",
    "Data Infrastructure for AI at Scale": "data-infra.yaml",
    "LLM Fine-Tuning Techniques": "fine-tuning.yaml",
    "LLM Deployment and Serving": "deployment.yaml",
    "Distributed Training Frameworks": "distributed-training.yaml",
    "Prompt Engineering": "prompt-engineering.yaml",
    "Safety, Alignment and Governance": "safety-alignment.yaml",
    "Papers, Blogs, Courses and Lectures": "papers-blogs.yaml",
    "Tutorials and Guides": "tutorials.yaml",
    "Top Conferences": "conferences.yaml",
}


# ---------------------------------------------------------------------------
# Main parser
# ---------------------------------------------------------------------------

def parse_readme(readme_path: str) -> dict:
    """Parse README.md into a structured dict of sections."""
    with open(readme_path) as f:
        lines = f.readlines()

    sections = OrderedDict()
    current_h2 = None
    current_h3 = None
    current_h4 = None
    current_table_lines = []
    in_table = False

    def flush_table():
        nonlocal current_table_lines, in_table
        if not current_table_lines:
            return None
        rows = parse_table(current_table_lines)
        current_table_lines = []
        in_table = False
        return rows

    def ensure_section(h2):
        if h2 not in sections:
            sections[h2] = OrderedDict([
                ("title", h2),
                ("description", ""),
                ("badges", []),
                ("subsections", []),
            ])

    def add_subsection(h2, title, rows, description="", level=3, parent_heading="", parent_description="", pre_text=""):
        ensure_section(h2)
        if not rows:
            return
        # Detect parser from first row's keys
        headers = list(rows[0].keys())
        parser = detect_parser(headers)
        table_type = detect_table_type(headers)
        items = [parser(r) for r in rows]

        sub = OrderedDict()
        sub["title"] = title
        sub["type"] = table_type
        sub["level"] = level
        if parent_heading:
            sub["parent_heading"] = parent_heading
            if parent_description:
                sub["parent_description"] = parent_description
        if description:
            sub["description"] = description
        if pre_text:
            sub["pre_table_text"] = pre_text
        sub["columns"] = headers
        sub["items"] = items
        sections[h2]["subsections"].append(sub)

    subsection_desc = ""
    pre_table_text = ""  # Non-blockquote text between heading/description and table
    h3_descriptions = {}  # h3 title -> blockquote description (for parent headings)

    def current_level():
        return 4 if current_h4 else 3

    def current_parent():
        return current_h3 if current_h4 and current_h3 else ""

    def current_parent_desc():
        parent = current_parent()
        return h3_descriptions.get(parent, "") if parent else ""

    for i, line in enumerate(lines):
        stripped = line.rstrip()

        # Detect h2
        m2 = re.match(r'^## (.+)', stripped)
        if m2:
            # Flush any pending table
            rows = flush_table()
            if rows and current_h2:
                title = current_h4 or current_h3 or current_h2
                add_subsection(current_h2, title, rows, subsection_desc,
                               level=current_level(), parent_heading=current_parent(),
                               parent_description=current_parent_desc(),
                               pre_text=pre_table_text)
                subsection_desc = ""
                pre_table_text = ""

            current_h2 = m2.group(1).strip()
            current_h3 = None
            current_h4 = None
            ensure_section(current_h2)
            continue

        # Detect h3
        m3 = re.match(r'^### (.+)', stripped)
        if m3:
            rows = flush_table()
            if rows and current_h2:
                title = current_h4 or current_h3 or current_h2
                add_subsection(current_h2, title, rows, subsection_desc,
                               level=current_level(), parent_heading=current_parent(),
                               parent_description=current_parent_desc(),
                               pre_text=pre_table_text)
                subsection_desc = ""
                pre_table_text = ""

            current_h3 = m3.group(1).strip()
            current_h4 = None
            continue

        # Detect h4
        m4 = re.match(r'^#### (.+)', stripped)
        if m4:
            rows = flush_table()
            if rows and current_h2:
                title = current_h4 or current_h3 or current_h2
                add_subsection(current_h2, title, rows, subsection_desc,
                               level=current_level(), parent_heading=current_parent(),
                               parent_description=current_parent_desc(),
                               pre_text=pre_table_text)
                subsection_desc = ""
                pre_table_text = ""

            current_h4 = m4.group(1).strip()
            continue

        # Collect section descriptions from blockquotes
        bq = re.match(r'^> (.+)', stripped)
        if bq and current_h2:
            text = bq.group(1).strip()
            # Skip source references and very short quotes
            if text.startswith("**Source:**") or text.startswith("*\""):
                continue
            if current_h4:
                # Blockquote under h4 — belongs to this h4 subsection
                subsection_desc = text
            elif current_h3:
                # Blockquote under h3 (no h4 yet) — could be:
                # 1. Description for an h3 that has its own table
                # 2. Description for an h3 that's a parent of h4 groups
                # Store in both places; subsection_desc will be consumed when a
                # table is flushed, h3_descriptions will be used for parent headings
                subsection_desc = text
                h3_descriptions[current_h3] = text
            elif not sections.get(current_h2, {}).get("description"):
                ensure_section(current_h2)
                sections[current_h2]["description"] = text

        # Collect badges
        for badge_match in BADGE_RE.finditer(stripped):
            if current_h2 and current_h2 in sections:
                badge_alt = badge_match.group(1)
                badge_url = badge_match.group(2)
                # Extract just the badge path
                badge_path = badge_url.split("img.shields.io/badge/")[1] if "img.shields.io/badge/" in badge_url else badge_url
                sections[current_h2]["badges"].append({"alt": badge_alt, "path": badge_path})

        # Capture standalone bold paragraphs between heading/blockquote and table
        # (e.g., "**Why this matters:** ...")
        if (stripped and not stripped.startswith('|') and not stripped.startswith('#')
                and not stripped.startswith('>') and not stripped.startswith('!')
                and not stripped.startswith('---')
                and stripped.startswith('**') and (current_h3 or current_h4)):
            pre_table_text = stripped

        # Table detection
        if stripped.startswith('|') and not stripped.startswith('||'):
            if not in_table:
                in_table = True
                current_table_lines = [stripped]
            else:
                current_table_lines.append(stripped)
        else:
            if in_table:
                rows = flush_table()
                if rows and current_h2:
                    title = current_h4 or current_h3 or current_h2
                    add_subsection(current_h2, title, rows, subsection_desc,
                                   level=current_level(), parent_heading=current_parent(),
                                   parent_description=current_parent_desc(),
                                   pre_text=pre_table_text)
                    subsection_desc = ""
                    pre_table_text = ""

    # Flush final table
    rows = flush_table()
    if rows and current_h2:
        title = current_h4 or current_h3 or current_h2
        add_subsection(current_h2, title, rows, subsection_desc,
                       level=current_level(), parent_heading=current_parent(),
                       parent_description=current_parent_desc(),
                       pre_text=pre_table_text)

    return sections


def write_yaml_files(sections: dict, output_dir: str):
    """Write each mapped section to a YAML file."""
    os.makedirs(output_dir, exist_ok=True)

    for h2, section_data in sections.items():
        filename = SECTION_FILE_MAP.get(h2)
        if not filename:
            continue

        # Clean up: remove empty badges
        if not section_data.get("badges"):
            section_data.pop("badges", None)

        # Remove empty subsections
        if not section_data.get("subsections"):
            continue

        output = OrderedDict()
        output["section"] = OrderedDict([
            ("title", section_data["title"]),
            ("description", section_data.get("description", "")),
        ])
        if section_data.get("badges"):
            output["section"]["badges"] = section_data["badges"]

        output["subsections"] = section_data["subsections"]

        filepath = os.path.join(output_dir, filename)
        with open(filepath, "w") as f:
            yaml.dump(
                dict(output),
                f,
                Dumper=OrderedDumper,
                default_flow_style=False,
                allow_unicode=True,
                width=120,
                sort_keys=False,
            )
        item_count = sum(len(s.get("items", [])) for s in section_data["subsections"])
        print(f"  -> {filepath} ({len(section_data['subsections'])} subsections, {item_count} items)")


def main():
    repo_root = Path(__file__).resolve().parent.parent
    readme_path = repo_root / "README.md"
    output_dir = repo_root / "data"

    print(f"Parsing {readme_path}...")
    sections = parse_readme(str(readme_path))

    print(f"\nFound {len(sections)} top-level sections:")
    for h2, data in sections.items():
        n_sub = len(data.get("subsections", []))
        mapped = "-> " + SECTION_FILE_MAP[h2] if h2 in SECTION_FILE_MAP else "(skipped - narrative)"
        print(f"  [{n_sub:2d} tables] {h2}  {mapped}")

    print(f"\nWriting YAML files to {output_dir}/...")
    write_yaml_files(sections, str(output_dir))

    # Summary
    total_items = 0
    total_files = 0
    for h2, data in sections.items():
        if h2 in SECTION_FILE_MAP and data.get("subsections"):
            total_files += 1
            total_items += sum(len(s.get("items", [])) for s in data["subsections"])
    print(f"\nDone: {total_files} YAML files, {total_items} total items extracted.")


if __name__ == "__main__":
    main()
