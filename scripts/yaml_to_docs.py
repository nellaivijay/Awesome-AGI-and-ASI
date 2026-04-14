#!/usr/bin/env python3
"""Generate MkDocs documentation pages from YAML data files.

Reads:
  - data/*.yaml     (structured resource data)

Writes:
  - docs/<path>.md  (MkDocs-compatible pages with frontmatter)

Each YAML file maps to a docs path based on YAML_TO_DOCS.
"""

import sys
from pathlib import Path

import yaml

# Reuse rendering functions from yaml_to_readme
from yaml_to_readme import (
    shield_badge,
    render_links,
    render_cell,
    render_name_cell,
    render_table,
    COMPACT_TYPES,
)


# ---------------------------------------------------------------------------
# YAML file -> docs path mapping (matches mkdocs.yml nav)
# ---------------------------------------------------------------------------

YAML_TO_DOCS = {
    "asi-research.yaml": "understand/asi-research.md",
    "frameworks.yaml": "build/frameworks.md",
    "agents.yaml": "build/agents.md",
    "physical-ai.yaml": "build/physical-ai.md",
    "paper-to-code.yaml": "build/paper-to-code.md",
    "llm-frameworks.yaml": "infrastructure/llm-frameworks.md",
    "rag-vector-db.yaml": "infrastructure/rag-vector-db.md",
    "data-infra.yaml": "infrastructure/data-infra.md",
    "fine-tuning.yaml": "infrastructure/fine-tuning.md",
    "deployment.yaml": "infrastructure/deployment.md",
    "distributed-training.yaml": "infrastructure/distributed-training.md",
    "prompt-engineering.yaml": "infrastructure/prompt-engineering.md",
    "safety-alignment.yaml": "safety/safety-alignment.md",
    "papers-blogs.yaml": "research/papers-blogs.md",
    "tutorials.yaml": "research/tutorials.md",
    "conferences.yaml": "research/conferences.md",
}

# SEO keywords per section (auto-generated from section content)
YAML_KEYWORDS = {
    "asi-research.yaml": "ASI research, superintelligence, AGI timeline, OpenAI, Anthropic, DeepMind, SSI, AGI benchmarks, intelligence explosion",
    "frameworks.yaml": "AI frameworks, ML platforms, PyTorch, TensorFlow, JAX, Hugging Face, machine learning tools",
    "agents.yaml": "AI agents, coding agents, research agents, computer use agents, embodied AI, autonomous systems, Devin, SWE-agent",
    "physical-ai.yaml": "physical AI, embodied intelligence, robotics, VLA models, humanoid robots, simulation, Isaac Sim",
    "paper-to-code.yaml": "paper to code, research automation, ML implementation, code generation, Research2Repo",
    "llm-frameworks.yaml": "LLM frameworks, LangChain, LlamaIndex, AI application development, agent frameworks",
    "rag-vector-db.yaml": "RAG, vector database, retrieval augmented generation, embeddings, Pinecone, Weaviate, ChromaDB, Graph RAG",
    "data-infra.yaml": "data infrastructure, AI data pipelines, feature stores, data labeling, data quality",
    "fine-tuning.yaml": "LLM fine-tuning, LoRA, QLoRA, RLHF, DPO, parameter-efficient fine-tuning, PEFT",
    "deployment.yaml": "LLM deployment, model serving, inference optimization, vLLM, TGI, ONNX, quantization",
    "distributed-training.yaml": "distributed training, DeepSpeed, FSDP, Megatron-LM, multi-GPU, AI compute",
    "prompt-engineering.yaml": "prompt engineering, chain-of-thought, few-shot learning, prompt optimization, CoT, ToT",
    "safety-alignment.yaml": "AI safety, alignment, governance, RLHF, red teaming, interpretability, AI ethics",
    "papers-blogs.yaml": "AI papers, research blogs, courses, lectures, scaling laws, reasoning, multimodal AI",
    "tutorials.yaml": "AI tutorials, guides, LLM tutorial, RAG tutorial, fine-tuning guide",
    "conferences.yaml": "AI conferences, NeurIPS, ICML, ICLR, AAAI, AI safety summit, GTC, AGI conference",
}


# ---------------------------------------------------------------------------
# Page rendering
# ---------------------------------------------------------------------------

def render_docs_page(yaml_filename: str, data: dict) -> str:
    """Render a complete MkDocs documentation page from YAML data."""
    lines = []

    section = data.get("section", {})
    title = section.get("title", "")
    desc = section.get("description", "")
    badges = section.get("badges", [])

    # YAML frontmatter
    keywords = YAML_KEYWORDS.get(yaml_filename, "")
    # Use first line of description for SEO
    seo_desc = desc.split("\n")[0] if desc else title
    # Escape quotes in description
    seo_desc = seo_desc.replace('"', '\\"')

    lines.append("---")
    lines.append(f'description: "{seo_desc}"')
    lines.append(f'keywords: "{keywords}"')
    lines.append("---")

    # H1 heading (docs uses H1, not H2 like README)
    lines.append(f"# {title}")
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
        else:
            lines.append(f"### {sub_title}")
            last_parent = None
            heading_emitted = True

        if heading_emitted:
            lines.append("")

        # Subsection description as blockquote
        if sub_desc:
            for desc_line in sub_desc.split("\n"):
                lines.append(f"> {desc_line}")
            lines.append("")

        # Pre-table text
        pre_text = sub.get("pre_table_text", "")
        if pre_text:
            lines.append(pre_text)
            lines.append("")

        # Render table
        lines.append(render_table(sub))
        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    repo_root = Path(__file__).resolve().parent.parent
    data_dir = repo_root / "data"
    docs_dir = repo_root / "docs"

    generated = 0
    for yaml_file, docs_path in YAML_TO_DOCS.items():
        filepath = data_dir / yaml_file
        if not filepath.exists():
            print(f"  [skip] {yaml_file} not found", file=sys.stderr)
            continue

        with open(filepath) as f:
            data = yaml.safe_load(f)

        page_md = render_docs_page(yaml_file, data)

        output_path = docs_dir / docs_path
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(page_md)

        generated += 1
        print(f"  -> {output_path}")

    print(f"\nGenerated {generated} docs pages.")


if __name__ == "__main__":
    main()
