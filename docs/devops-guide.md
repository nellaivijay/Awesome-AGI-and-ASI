---
description: "Developer and DevOps guide for the Awesome AGI and ASI site -- GitHub Actions CI/CD, MkDocs Material configuration, SEO setup, and local development."
keywords: "MkDocs Material, GitHub Actions, CI/CD, GitHub Pages, DevOps, site deployment, developer guide"
---
# Developer & DevOps Guide

This document explains how the Awesome AGI and ASI website is built, deployed, and maintained. It covers the CI/CD pipeline, MkDocs configuration, SEO setup, and how to run things locally.

---

## Architecture Overview

```
┌──────────────┐     push to main     ┌────────────────────┐
│  README.md   │ ──────────────────>  │  GitHub Actions    │
│  docs/*.md   │                      │                    │
└──────────────┘                      │  1. deploy-site    │
                                      │  2. ingest-new-urls│
                                      └────────┬───────────┘
                                               │
                              ┌────────────────┼────────────────┐
                              │                │                │
                              v                v                v
                      ┌──────────────┐  ┌────────────┐  ┌────────────┐
                      │  gh-pages    │  │  Artifact   │  │  Social    │
                      │  branch      │  │  (JSON)     │  │  Cards     │
                      │              │  │             │  │  (PNG)     │
                      │  Live site   │  │  New URLs   │  │  OG images │
                      └──────────────┘  └────────────┘  └────────────┘
```

**Live site:** [https://nellaivijay.github.io/Awesome-AGI-and-ASI/](https://nellaivijay.github.io/Awesome-AGI-and-ASI/)

---

## Project Structure

```
Awesome-AGI-and-ASI/
├── .github/workflows/
│   ├── deploy-site.yml          # Builds + deploys MkDocs to GitHub Pages
│   └── ingest-new-urls.yml      # Extracts new URLs from markdown diffs
├── docs/                         # MkDocs source pages
│   ├── index.md                  # Home / landing page
│   ├── understand/               # AI/AGI/ASI explainers
│   ├── build/                    # Frameworks, agents, physical AI
│   ├── infrastructure/           # LLM frameworks, RAG, training, deployment
│   ├── safety/                   # Safety, alignment, governance
│   ├── research/                 # Papers, tutorials, conferences
│   ├── blog/                     # Blog posts (MkDocs blog plugin)
│   ├── contributing.md           # Contribution guidelines
│   ├── robots.txt                # SEO: search engine crawler rules
│   └── stylesheets/custom.css    # Theme overrides + responsive CSS
├── overrides/
│   └── main.html                 # Template override: OG tags, Twitter Cards, JSON-LD
├── scripts/
│   ├── extract_urls.py           # URL extraction from git diffs
│   └── split_readme.py           # One-time script to split README into doc pages
├── mkdocs.yml                    # MkDocs Material configuration
├── requirements.txt              # Python dependencies
├── README.md                     # Source of truth (the awesome-list)
└── .gitignore
```

---

## GitHub Actions Workflows

### 1. Deploy Site (`deploy-site.yml`)

Builds the MkDocs Material site and deploys it to the `gh-pages` branch.

| Setting | Value |
|---------|-------|
| **Triggers** | Push to `main`, daily cron (6:00 AM UTC), manual `workflow_dispatch` |
| **Runner** | `ubuntu-latest` |
| **Python** | 3.12 |
| **Deploy target** | `gh-pages` branch via `mkdocs gh-deploy --force` |

**Workflow steps:**

1. **Checkout** with `fetch-depth: 0` (full git history required for last-updated timestamps)
2. **Set up Python 3.12**
3. **Install system dependencies** -- `libcairo2-dev` and `libffi-dev` for social card image generation
4. **Install Python dependencies** from `requirements.txt`
5. **Build and deploy** -- `mkdocs gh-deploy --force` builds the site and force-pushes to `gh-pages`

**Why `fetch-depth: 0`?**
The `git-revision-date-localized` plugin reads each file's git history to display "Last updated" and "Created" timestamps in the page footer. A shallow clone (`fetch-depth: 1`, the default) would cause all pages to show the same build date instead of their actual last-modified date.

**Why daily cron?**
Even without code changes, the daily rebuild ensures the "timeago" timestamps (e.g. "3 days ago") stay fresh and the site stays up if GitHub Pages has transient issues.

---

### 2. Ingest New URLs (`ingest-new-urls.yml`)

Automatically extracts newly added URLs whenever markdown files change.

| Setting | Value |
|---------|-------|
| **Triggers** | Push to `main` (only when `**.md` files change), manual `workflow_dispatch` |
| **Runner** | `ubuntu-latest` |
| **Python** | 3.12 |
| **Output** | JSON artifact, 90-day retention |

**Workflow steps:**

1. **Checkout** with `fetch-depth: 2` (need parent commit for diff)
2. **Set up Python 3.12**
3. **Resolve base ref** -- handles both normal pushes and first commits
4. **Run `scripts/extract_urls.py`** -- diffs markdown files, extracts and classifies URLs
5. **Upload artifact** -- JSON file named `new-urls-<sha>` with 90-day retention
6. **Job summary** -- writes a formatted summary to the GitHub Actions run page

**URL classification categories:**
`arxiv`, `github`, `huggingface`, `paper`, `youtube`, `docs`, `blog`, `other`

**Example output (`queue/urls-*.json`):**
```json
{
  "extracted_at": "2026-04-13T17:00:00+00:00",
  "commit": "abc1234...",
  "url_count": 5,
  "urls": [
    {
      "url": "https://github.com/example/repo",
      "category": "github",
      "link_text": "Example Repo",
      "section": "Frameworks and Platforms",
      "source_file": "README.md"
    }
  ]
}
```

---

## MkDocs Configuration (`mkdocs.yml`)

### Theme

- **Theme:** [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) with a white/minimalist palette
- **Font:** Inter (text), Roboto Mono (code)
- **Custom CSS:** `docs/stylesheets/custom.css` -- white header, clean tables, responsive breakpoints at 768px and 480px

### Plugins

| Plugin | Purpose |
|--------|---------|
| `search` | Full-text search with English language support and custom word separators |
| `blog` | Blog section at `/blog/` with date-formatted posts |
| `git-revision-date-localized` | Adds "Last updated" and "Created" timestamps to every page footer, read from git history |
| `social` | Auto-generates Open Graph social card images (1200x630 PNG) for every page |
| `meta` | Reads YAML front matter for per-page meta descriptions and keywords |
| `tags` | Enables content tagging (for future use) |

### Navigation Features

- **Sticky tabs** -- top-level navigation tabs remain visible on scroll
- **Instant navigation** -- SPA-like page transitions without full reloads
- **Progress bar** -- loading indicator during navigation
- **Back to top** -- floating button on long pages
- **Integrated TOC** -- table of contents in the left sidebar
- **Search suggestions** -- autocomplete search with match highlighting

### Markdown Extensions

| Extension | Purpose |
|-----------|---------|
| `tables` | Standard markdown tables |
| `admonition` | Note/warning/info callout boxes |
| `pymdownx.details` | Collapsible `??? info "title"` sections (used for comparison table) |
| `pymdownx.superfences` | Fenced code blocks with syntax highlighting |
| `attr_list` | Add HTML attributes to markdown elements |
| `md_in_html` | Process markdown inside HTML blocks |
| `meta` | YAML front matter support |
| `toc` | Table of contents with permalink anchors, depth 3 |

---

## SEO Setup

Every page includes the following SEO features, injected via `overrides/main.html`:

### Meta Tags
- **Open Graph** (`og:title`, `og:description`, `og:url`, `og:site_name`, `og:locale`) -- for Facebook, LinkedIn, Discord previews
- **Twitter Cards** (`twitter:card`, `twitter:title`, `twitter:description`) -- for Twitter/X previews
- **Standard meta** (`description`, `keywords`, `author`, `robots`) -- for Google/Bing crawlers

### Per-Page Descriptions
Each `.md` file has YAML front matter with a unique `description` and `keywords`:

```yaml
---
description: "Page-specific description for search engines (150-160 chars)"
keywords: "keyword1, keyword2, keyword3"
---
# Page Title
```

### Structured Data (JSON-LD)
- **WebPage schema** on every page (name, description, URL, publisher)
- **BreadcrumbList schema** on nested pages for Google rich results

### Social Cards
The `social` plugin auto-generates Open Graph share images (1200x630 PNG) per page. These are used when sharing links on social media. Requires `pillow` and `cairosvg` (plus `libcairo2-dev` system dependency in CI).

### Sitemap & Robots
- **`sitemap.xml`** -- auto-generated by MkDocs with all page URLs
- **`robots.txt`** -- allows all crawlers, points to the sitemap

---

## Last Updated Timestamps

Every page footer displays two timestamps:

- **Last update** -- when the page's source file was last modified (from git history)
- **Created** -- when the file was first committed

These are powered by the `git-revision-date-localized` plugin with `type: timeago`, which shows relative times like "3 days ago" with the full date available on hover.

**Important for CI:** The deploy workflow uses `fetch-depth: 0` (full clone) so the plugin can read the complete git history. Without this, all pages would show the build date instead of their actual last-modified date.

If building locally without full git history, the plugin falls back to the build date (`fallback_to_build_date: true`).

---

## Local Development

### Prerequisites

- Python 3.10+
- `libcairo2-dev` and `libffi-dev` (for social card generation)

### Setup

```bash
# Clone the repository
git clone https://github.com/nellaivijay/Awesome-AGI-and-ASI.git
cd Awesome-AGI-and-ASI

# Install system dependencies (Ubuntu/Debian)
sudo apt-get install -y libcairo2-dev libffi-dev

# Install Python dependencies
pip install -r requirements.txt
```

### Common Commands

```bash
# Live preview with hot-reload (http://localhost:8000)
mkdocs serve

# Build the site to ./site/
mkdocs build

# Build and deploy to gh-pages (usually done by CI)
mkdocs gh-deploy --force
```

### Adding a New Page

1. Create the markdown file under `docs/` (e.g. `docs/build/new-topic.md`)
2. Add YAML front matter with SEO meta:
   ```yaml
   ---
   description: "Short description for search engines"
   keywords: "relevant, keywords, here"
   ---
   # Page Title
   ```
3. Add the page to the `nav:` section in `mkdocs.yml`
4. Run `mkdocs serve` to preview locally

### Adding a Blog Post

1. Create a markdown file under `docs/blog/posts/` with front matter:
   ```yaml
   ---
   date: 2026-04-13
   categories:
     - Announcement
   description: "Blog post description"
   ---
   # Post Title
   ```
2. The blog plugin auto-indexes it at `/blog/`

---

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `mkdocs-material` | >= 9.5 | MkDocs Material theme |
| `mkdocs-blog-plugin` | >= 0.25 | Blog section support |
| `mkdocs-git-revision-date-localized-plugin` | >= 1.2 | Last-updated timestamps from git |
| `pillow` | >= 10.0 | Image processing for social cards |
| `cairosvg` | >= 2.7 | SVG-to-PNG rendering for social cards |

**System dependencies (CI):** `libcairo2-dev`, `libffi-dev`

---

## Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| All pages show same "Last updated" date | Shallow git clone in CI | Ensure `fetch-depth: 0` in checkout step |
| Social card images missing | Missing `libcairo2-dev` | Install: `sudo apt-get install libcairo2-dev libffi-dev` |
| Tables render as raw text in collapsibles | Using raw `<details>` HTML | Use `??? info "title"` admonition syntax instead |
| Blog posts not appearing | Missing `date` in front matter | Add `date: YYYY-MM-DD` to post front matter |
| Search not finding content | Plugin misconfigured | Check `search` plugin has `lang: en` in `mkdocs.yml` |
