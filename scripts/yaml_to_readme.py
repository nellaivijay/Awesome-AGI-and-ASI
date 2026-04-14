#!/usr/bin/env python3
"""Generate README.md from YAML data files and markdown templates.

Reads:
  - templates/header.md          (title, badges, ToC)
  - templates/understand-ai-agi-asi.md  (narrative section)
  - data/*.yaml                  (structured resource data)
  - templates/footer.md          (contributing, license)

Writes:
  - README.md
"""

import sys
from pathlib import Path

import yaml


# ---------------------------------------------------------------------------
# Section ordering — must match the ToC in templates/header.md
# ---------------------------------------------------------------------------

SECTION_ORDER = [
    "asi-research.yaml",
    "frameworks.yaml",
    "agents.yaml",
    "physical-ai.yaml",
    "paper-to-code.yaml",
    "llm-frameworks.yaml",
    "rag-vector-db.yaml",
    "data-infra.yaml",
    "fine-tuning.yaml",
    "deployment.yaml",
    "distributed-training.yaml",
    "prompt-engineering.yaml",
    "safety-alignment.yaml",
    "papers-blogs.yaml",
    "tutorials.yaml",
    "conferences.yaml",
]

YAML_TO_H2 = {
    "asi-research.yaml": "ASI and Superintelligence Research",
    "frameworks.yaml": "Frameworks and Platforms",
    "agents.yaml": "Agents",
    "physical-ai.yaml": "Physical AI & Embodied Intelligence",
    "paper-to-code.yaml": "Paper-to-Code Automation",
    "llm-frameworks.yaml": "LLM Application Frameworks",
    "rag-vector-db.yaml": "RAG and Vector Databases",
    "data-infra.yaml": "Data Infrastructure for AI at Scale",
    "fine-tuning.yaml": "LLM Fine-Tuning Techniques",
    "deployment.yaml": "LLM Deployment and Serving",
    "distributed-training.yaml": "Distributed Training Frameworks",
    "prompt-engineering.yaml": "Prompt Engineering",
    "safety-alignment.yaml": "Safety, Alignment and Governance",
    "papers-blogs.yaml": "Papers, Blogs, Courses and Lectures",
    "tutorials.yaml": "Tutorials and Guides",
    "conferences.yaml": "Top Conferences",
}

# Table types that use compact formatting (no spaces in cells)
COMPACT_TYPES = {"framework", "enterprise"}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def shield_badge(badge) -> str:
    """Render a shields.io badge.

    Accepts either a string (legacy: just the path) or a dict with 'alt' and 'path' keys.
    """
    if isinstance(badge, dict):
        alt = badge.get("alt", "")
        path = badge.get("path", "")
    else:
        # Legacy: badge is just the path string
        path = badge
        # Reconstruct label from badge path
        parts = path.split("?")[0]
        alt = parts.split("-")[0].replace("_", " ")
    return f"![{alt}](https://img.shields.io/badge/{path})"


def render_links(links: list) -> str:
    """Render a list of link dicts as markdown."""
    if not links:
        return ""
    return ", ".join(f"[{lnk['label']}]({lnk['url']})" for lnk in links)


# ---------------------------------------------------------------------------
# Cell rendering — maps column name + table type → cell content
# ---------------------------------------------------------------------------

def render_name_cell(item: dict, table_type: str) -> str:
    """Render the first column (the 'name' cell) based on table type.

    Uses raw_name if available (preserves original bold/link/plain formatting).
    Falls back to heuristic rendering based on table type.
    """
    # Use raw_name for faithful round-trip reconstruction
    raw = item.get("raw_name", "")
    if raw:
        return raw

    name = item.get("name", "")
    github = item.get("github", "")
    url = item.get("url", "")

    # Types where name is a GitHub link
    if table_type == "framework":
        if github:
            return f"[{name}](https://github.com/{github})"
        if url:
            return f"[{name}]({url})"
        return name

    # Types where name is plain text (paper title)
    if table_type == "paper":
        return name

    # Types where name is bold
    if table_type in (
        "organization", "book", "conference_full", "conference_simple",
        "model", "benchmark", "signal", "metric",
    ):
        return f"**{name}**"

    # Types where name is a URL link
    if url:
        return f"[{name}]({url})"
    if github:
        return f"[{name}](https://github.com/{github})"
    return name


def render_cell(item: dict, column: str, table_type: str, is_first: bool) -> str:
    """Render a single table cell based on column name and table type."""
    col = column.strip()

    # First column is always the name/title
    if is_first:
        return render_name_cell(item, table_type)

    # --- Stars ---
    if col == "Github Stars":
        github = item.get("github", "")
        return f"![GitHub Repo stars](https://badgen.net/github/stars/{github})" if github else ""

    # --- Description-like columns ---
    if col in ("Introduction", "Description", "Focus", "What It Means", "Key Notes", "Current State"):
        # For conference_simple, "Description" content is stored in full_name
        if col == "Description" and table_type in ("conference_simple", "conference_full"):
            return item.get("full_name", item.get("description", ""))
        return item.get("description", "")

    # --- Notes ---
    if col in ("Notes", " Notes "):
        # Use raw_notes if available for faithful reconstruction
        raw_notes = item.get("raw_notes", "")
        if raw_notes:
            return raw_notes
        notes = item.get("notes", "-")
        if table_type in ("framework", "enterprise"):
            note_links = item.get("links", [])
            if note_links:
                link_parts = [f"[{lnk['label']}]({lnk['url']})" for lnk in note_links]
                if notes and notes != "-":
                    notes = notes + " " + ", ".join(link_parts)
                else:
                    notes = ", ".join(link_parts)
        return notes

    # --- Author columns ---
    if col in ("Authors / Org", "Author(s)", "Authors"):
        return item.get("author", "")

    # --- Year ---
    if col == "Year":
        val = item.get("year", "")
        return str(val) if val else ""

    # --- Links column ---
    if col == "Links":
        # Use links_text if available (preserves plain text + link mixtures)
        links_text = item.get("links_text", "")
        if links_text:
            return links_text
        result = render_links(item.get("links", []))
        return result if result else "-"

    # --- Website (conference tables) ---
    if col == "Website":
        url = item.get("url", "")
        if url:
            # Use stored label from converter if available
            label = item.get("website_label", "")
            if not label:
                try:
                    label = url.split("//")[1].rstrip("/").split("/")[0]
                except (IndexError, AttributeError):
                    label = "Link"
            return f"[{label}]({url})"
        # Plain text website field (no URL)
        return item.get("website_text", "")

    # --- Paper column (non-first, in method/technique tables) ---
    if col == "Paper":
        links = item.get("links", [])
        if not links:
            return "-"
        # If there's no separate Code column, render all links in Paper column
        columns = []  # caller should pass columns but we can check table_type
        if table_type in ("technique", "approach"):
            return render_links(links)
        # For method tables with separate Code column, only show Paper links
        paper_links = [lnk for lnk in links if lnk.get("label", "").lower() == "paper"]
        return render_links(paper_links) if paper_links else "-"

    # --- Code column ---
    if col == "Code":
        for lnk in item.get("links", []):
            if lnk.get("label", "").lower() in ("code", "code example"):
                return f"[Code]({lnk['url']})"
        return "-"

    # --- Full Name (conference) ---
    if col == "Full Name":
        return item.get("full_name", "")

    # --- When (conference) ---
    if col == "When":
        return item.get("when", "")

    # --- AGI Relevance (conference) ---
    if col == "AGI Relevance":
        return item.get("relevance", "")

    # --- Org / Provider / Organizer (model/conference tables) ---
    if col in ("Org", "Provider", "Organizer"):
        return item.get("org", item.get("full_name", ""))

    # --- Current Data (metric tables) ---
    if col == "Current Data":
        return item.get("description", "")

    # --- Why It Matters (metric tables) ---
    if col.startswith("Why It Matters"):
        return item.get("description", "")

    # --- Source column ---
    if col == "Source":
        links_text = item.get("links_text", "")
        if links_text:
            return links_text
        return render_links(item.get("links", []))

    # --- Current Status ---
    if col == "Current Status":
        return item.get("description", "")

    # --- Example Systems ---
    if col == "Example Systems":
        return item.get("notes", "")

    # Fallback
    return item.get("description", "")


# ---------------------------------------------------------------------------
# Table rendering
# ---------------------------------------------------------------------------

def render_table(subsection: dict) -> str:
    """Render a markdown table from subsection metadata."""
    columns = subsection.get("columns", [])
    table_type = subsection.get("type", "tool")
    items = subsection.get("items", [])

    if not columns or not items:
        return ""

    compact = table_type in COMPACT_TYPES
    lines = []

    # Header row
    if compact:
        # Preserve original column spacing — " Notes " should keep spaces
        raw_cols = []
        for c in columns:
            if c == "Notes":
                raw_cols.append(" Notes ")
            else:
                raw_cols.append(c)
        header = "|" + "|".join(raw_cols) + "|"
        sep = "|" + "|".join("-" for _ in columns) + "|"
    else:
        header = "| " + " | ".join(columns) + " |"
        # Generate separator with dashes (minimum 3 for valid markdown)
        dashes = ["-" * max(len(c) + 2, 3) for c in columns]
        sep = "|" + "|".join(dashes) + "|"

    lines.append(header)
    lines.append(sep)

    # Data rows
    for item in items:
        cells = []
        for i, col in enumerate(columns):
            cells.append(render_cell(item, col, table_type, is_first=(i == 0)))

        if compact:
            row = "|" + "|".join(cells) + "|"
        else:
            row = "| " + " | ".join(cells) + " |"
        lines.append(row)

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Section rendering
# ---------------------------------------------------------------------------

def render_section(yaml_filename: str, data: dict) -> str:
    """Render a complete section from YAML data."""
    lines = []

    section = data.get("section", {})
    title = YAML_TO_H2.get(yaml_filename, section.get("title", ""))
    desc = section.get("description", "")
    badges = section.get("badges", [])

    # H2 heading
    lines.append(f"## {title}")
    lines.append("")

    # Description as blockquote
    if desc:
        for desc_line in desc.split("\n"):
            lines.append(f"> {desc_line}")
        lines.append("")

    # Badges
    if badges:
        badge_line = " ".join(shield_badge(b) for b in badges)
        lines.append(badge_line)
        lines.append("")

    # Subsections — track parent headings for h4 groups
    subsections = data.get("subsections", [])
    last_parent = None

    for sub in subsections:
        sub_title = sub.get("title", "")
        sub_desc = sub.get("description", "")
        sub_level = sub.get("level", 3)
        parent = sub.get("parent_heading", "")
        items = sub.get("items", [])

        if not items:
            continue

        # Emit parent h3 heading for h4 groups (only once per parent)
        if sub_level == 4 and parent and parent != last_parent:
            lines.append(f"### {parent}")
            lines.append("")
            # Emit parent heading description if available
            parent_desc = sub.get("parent_description", "")
            if parent_desc:
                for desc_line in parent_desc.split("\n"):
                    lines.append(f"> {desc_line}")
                lines.append("")
            last_parent = parent

        # Emit subsection heading
        heading_emitted = False
        if sub_level == 4:
            lines.append(f"#### {sub_title}")
            heading_emitted = True
        elif sub_title != title:
            lines.append(f"### {sub_title}")
            last_parent = None  # Reset parent tracking for h3s
            heading_emitted = True

        if heading_emitted:
            lines.append("")

        # Subsection description as blockquote
        if sub_desc:
            for desc_line in sub_desc.split("\n"):
                lines.append(f"> {desc_line}")
            lines.append("")

        # Pre-table text (e.g., "**Why this matters:** ...")
        pre_text = sub.get("pre_table_text", "")
        if pre_text:
            lines.append(pre_text)
            lines.append("")

        # Render table
        lines.append(render_table(sub))
        lines.append("")

    # Trailing separator
    lines.append("---")
    lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    repo_root = Path(__file__).resolve().parent.parent
    data_dir = repo_root / "data"
    templates_dir = repo_root / "templates"
    output_path = repo_root / "README.md"

    # Read templates
    header = (templates_dir / "header.md").read_text()
    understand = (templates_dir / "understand-ai-agi-asi.md").read_text()
    footer = (templates_dir / "footer.md").read_text()

    # Build README
    parts = []

    # 1. Header (title, badges, description, ToC) — template already ends with ---
    parts.append(header.rstrip())
    parts.append("")

    # 2. Understanding AI, AGI, and ASI (narrative template) — template already ends with ---
    parts.append(understand.rstrip())
    parts.append("")

    # 3. YAML-generated sections in order
    for yaml_file in SECTION_ORDER:
        filepath = data_dir / yaml_file
        if not filepath.exists():
            print(f"  [skip] {yaml_file} not found", file=sys.stderr)
            continue

        with open(filepath) as f:
            data = yaml.safe_load(f)

        section_md = render_section(yaml_file, data)
        parts.append(section_md)

    # 4. Footer (contributing, license)
    parts.append(footer.rstrip())
    parts.append("")  # blank line at end of file
    parts.append("")  # trailing newline

    # Write
    readme_text = "\n".join(parts)
    # Ensure trailing newline matches original (ends with \n)
    if not readme_text.endswith("\n"):
        readme_text += "\n"
    output_path.write_text(readme_text)

    line_count = readme_text.count("\n") + 1
    print(f"Generated {output_path} ({line_count} lines)")


if __name__ == "__main__":
    main()
