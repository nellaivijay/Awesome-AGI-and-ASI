---
description: "The most comprehensive curated collection of AGI, ASI, and Collective Intelligence resources updated April 2026 -- frameworks, agents, multi-agent systems, GPT 5.4, Gemini 3.1 Flash Live, Claude Opus 4.6, JEPA models, frontier AI, LLMs, RAG, fine-tuning, safety, alignment, research papers, development tools, and emerging security threats for AI builders."
keywords: "AGI, ASI, Collective Intelligence, artificial general intelligence, artificial superintelligence, multi-agent systems, swarm intelligence, AI resources, GPT 5.4, Gemini 3.1 Flash Live, Claude Opus 4.6, JEPA, frontier models, AI agents, LLM, machine learning, AI safety, alignment, AI development tools, 2026 AI trends, AI security threats, software development AI impact"
---

<div class="hero-section">
  <h1>🤖 Awesome AGI, ASI & Collective Intelligence</h1>
  <p>The frontier of artificial intelligence research — from AI to AGI to ASI and beyond. Curated resources for builders and researchers shaping the future of intelligence.</p>
</div>

<!-- Bento Box Hero Section -->
<div class="bento-grid">
  <div class="bento-card bento-large" onclick="scrollToSection('understand')">
    <div class="bento-icon">🧠</div>
    <div class="bento-content">
      <h3>Understand</h3>
      <p>AI, AGI, ASI & Collective Intelligence fundamentals</p>
      <span class="bento-badge">4 sections</span>
    </div>
  </div>

  <div class="bento-card bento-medium" onclick="scrollToSection('build')">
    <div class="bento-icon">⚙️</div>
    <div class="bento-content">
      <h3>Build</h3>
      <p>Frameworks, Agents & Physical AI</p>
      <span class="bento-badge">4 sections</span>
    </div>
  </div>

  <div class="bento-card bento-medium" onclick="scrollToSection('infrastructure')">
    <div class="bento-icon">🏗️</div>
    <div class="bento-content">
      <h3>Infrastructure</h3>
      <p>LLM Frameworks, RAG & Deployment</p>
      <span class="bento-badge">8 sections</span>
    </div>
  </div>

  <div class="bento-card bento-small" onclick="scrollToSection('safety')">
    <div class="bento-icon">🛡️</div>
    <div class="bento-content">
      <h3>Safety</h3>
      <p>Alignment & Governance</p>
    </div>
  </div>

  <div class="bento-card bento-small" onclick="scrollToSection('research')">
    <div class="bento-icon">📚</div>
    <div class="bento-content">
      <h3>Research</h3>
      <p>Papers & Learning</p>
    </div>
  </div>

  <div class="bento-card bento-wide" onclick="window.open('https://github.com/nellaivijay/Awesome-AGI-and-ASI/issues/new?template=resource-suggestion.yml', '_blank')">
    <div class="bento-icon">📚</div>
    <div class="bento-content">
      <h3>Suggest a Resource</h3>
      <p>Contribute to the collection</p>
      <span class="bento-badge bento-action">→</span>
    </div>
  </div>
</div>

<script>
function scrollToSection(section) {
  const element = document.getElementById(section);
  if (element) {
    element.scrollIntoView({ behavior: 'smooth' });
  }
}
</script>

<style>
.bento-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: repeat(2, 180px);
  gap: 16px;
  margin: 2rem 0;
  max-width: 1200px;
  margin-left: auto;
  margin-right: auto;
}

.bento-card {
  background: var(--cyber-bg-secondary);
  border: 1px solid var(--cyber-border);
  border-radius: 16px;
  padding: 24px;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
  display: flex;
  align-items: center;
  gap: 16px;
}

.bento-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, var(--cyber-accent-blue), var(--cyber-accent-purple));
  opacity: 0;
  transition: opacity 0.3s ease;
  z-index: 0;
}

.bento-card:hover::before {
  opacity: 0.1;
}

.bento-card:hover {
  transform: translateY(-4px);
  border-color: var(--cyber-accent-blue);
  box-shadow: 0 8px 25px rgba(88, 166, 255, 0.3);
}

.bento-icon {
  font-size: 2.5rem;
  z-index: 1;
  min-width: 60px;
}

.bento-content {
  z-index: 1;
  flex: 1;
}

.bento-content h3 {
  margin: 0 0 8px 0;
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--cyber-text-primary);
}

.bento-content p {
  margin: 0 0 8px 0;
  font-size: 0.875rem;
  color: var(--cyber-text-secondary);
}

.bento-badge {
  display: inline-block;
  padding: 4px 12px;
  background: rgba(88, 166, 255, 0.2);
  color: var(--cyber-accent-blue);
  border-radius: 12px;
  font-size: 0.75rem;
  font-weight: 600;
}

.bento-action {
  background: var(--cyber-accent-blue);
  color: white;
}

/* Bento card sizes */
.bento-large {
  grid-column: span 2;
  grid-row: span 2;
  flex-direction: column;
  text-align: left;
  justify-content: center;
}

.bento-medium {
  grid-column: span 1;
  grid-row: span 1;
}

.bento-small {
  grid-column: span 1;
  grid-row: span 1;
}

.bento-wide {
  grid-column: span 3;
  grid-row: span 1;
}

/* Large card specific styling */
.bento-large .bento-icon {
  font-size: 4rem;
  margin-bottom: 16px;
}

.bento-large .bento-content h3 {
  font-size: 2rem;
}

.bento-large .bento-content p {
  font-size: 1rem;
}

/* Mobile responsive */
@media (max-width: 768px) {
  .bento-grid {
    grid-template-columns: 1fr;
    grid-template-rows: auto;
  }

  .bento-card {
    grid-column: span 1 !important;
    grid-row: span 1 !important;
    min-height: 120px;
  }

  .bento-large {
    flex-direction: row;
    text-align: left;
  }

  .bento-large .bento-icon {
    font-size: 2.5rem;
    margin-bottom: 0;
  }

  .bento-large .bento-content h3 {
    font-size: 1.25rem;
  }

  .bento-wide {
    grid-column: span 1 !important;
  }
}
</style>

<!-- Interactive Mind Map -->
<div class="mindmap-section">
  <h2>🗺️ Knowledge Map</h2>
  <p>Visual overview of how AGI, ASI, and Collective Intelligence concepts connect</p>
  <div class="mindmap-container">
    <svg id="mindmap" style="width: 100%; height: 400px;"></svg>
  </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/d3@7"></script>
<script src="https://cdn.jsdelivr.net/npm/markmap-view@0.15.4"></script>
<script>
  const mindmapData = {
    name: "Awesome AGI, ASI & CI",
    children: [
      {
        name: "🧠 Understand",
        children: [
          { name: "AI, AGI, ASI" },
          { name: "Collective Intelligence" },
          { name: "AGI Benchmarks" },
          { name: "ASI Research" }
        ]
      },
      {
        name: "⚙️ Build",
        children: [
          { name: "Frameworks" },
          { name: "Agents" },
          { name: "Physical AI" },
          { name: "Paper-to-Code" }
        ]
      },
      {
        name: "🏗️ Infrastructure",
        children: [
          { name: "LLM Frameworks" },
          { name: "RAG & Vector DBs" },
          { name: "Data Infrastructure" },
          { name: "Fine-Tuning" },
          { name: "Deployment" },
          { name: "Distributed Training" },
          { name: "Compute & Hardware" },
          { name: "Prompt Engineering" }
        ]
      },
      {
        name: "🛡️ Safety",
        children: [
          { name: "Safety & Alignment" }
        ]
      },
      {
        name: "📚 Research",
        children: [
          { name: "Papers & Blogs" },
          { name: "Tutorials" },
          { name: "Conferences" }
        ]
      }
    ]
  };

  const { Markmap, loadCSS, loadJS } = window.markmap;
  
  Markmap.create('#mindmap', mindmapData, {
    autoFit: true,
    duration: 500,
    fitRatio: 0.95,
    pan: true,
    zoom: true,
    drawArrow: false,
    color: (node) => {
      const colors = ['#58a6ff', '#bc8cff', '#3fb950', '#f85149', '#d29922'];
      return colors[node.depth % colors.length];
    }
  });
</script>

<style>
.mindmap-section {
  margin: 3rem 0;
  padding: 2rem;
  background: var(--cyber-bg-secondary);
  border: 1px solid var(--cyber-border);
  border-radius: 16px;
  max-width: 1200px;
  margin-left: auto;
  margin-right: auto;
}

.mindmap-section h2 {
  margin-top: 0;
  color: var(--cyber-text-primary);
}

.mindmap-section p {
  color: var(--cyber-text-secondary);
  margin-bottom: 1.5rem;
}

.mindmap-container {
  background: var(--cyber-bg);
  border-radius: 12px;
  padding: 1rem;
  border: 1px solid var(--cyber-border);
}

@media (max-width: 768px) {
  .mindmap-section {
    padding: 1rem;
    margin: 2rem 1rem;
  }
  
  .mindmap-container svg {
    height: 300px !important;
  }
}
</style>

# Awesome AGI, ASI, and Collective Intelligence Resources [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

![AGI](https://img.shields.io/badge/AGI-Artificial_General_Intelligence-blue)
![ASI](https://img.shields.io/badge/ASI-Artificial_Superintelligence-red)
![Collective](https://img.shields.io/badge/Collective_Intelligence-Multi_Agent_Systems-yellow)
![Super AI](https://img.shields.io/badge/Super_AI-Beyond_Human_Intelligence-purple)
![AI Safety](https://img.shields.io/badge/AI_Safety-Alignment_&_Control-green)
![LLM](https://img.shields.io/badge/LLM-Large_Language_Models-orange)
![Agents](https://img.shields.io/badge/Agents-Autonomous_AI-yellow)
![RAG](https://img.shields.io/badge/RAG-Retrieval_Augmented_Generation-cyan)
![Fine-Tuning](https://img.shields.io/badge/Fine--Tuning-LoRA_&_RLHF-lightblue)
![Conferences](https://img.shields.io/badge/Conferences-Academic_&_Industry-teal)
![Updated](https://img.shields.io/badge/Updated-April_2026-brightgreen)

> *"The development of full artificial intelligence could spell the end of the human race... or it could be the best thing ever to happen to humanity."* -- Stephen Hawking

The most comprehensive, curated collection of resources on the journey from **AI** to **AGI** to **ASI** and **Collective Intelligence** -- covering frameworks, agents, multi-agent systems, swarm intelligence, research papers, safety & alignment, books, benchmarks, conferences, and tools for builders and researchers shaping the future of intelligence.

---

## Explore

|| | Topic | What's Inside |
||---|---|---|
|| **Understand** <a id="understand"></a> | [AI, AGI, and ASI](understand/ai-agi-asi.md) | Definitions, comparison table, DeepMind's AGI levels, state of the field |
|| | [Collective Intelligence](understand/collective-intelligence.md) | Multi-agent systems, swarm intelligence, human-AI collaboration, distributed AI |
|| | [AGI Benchmarks & Evals](understand/benchmarks.md) | ARC-AGI, SWE-bench, GAIA, GPQA, FrontierMath, saturated benchmarks |
|| | [ASI Research](understand/asi-research.md) | Organizations, 27 books, seminal papers, benchmarks, roadmaps |
|| **Build** <a id="build"></a> | [Frameworks](build/frameworks.md) | LAMs, MCP/A2A protocols, 30+ agent frameworks |
|| | [Agents](build/agents.md) | Coding, research, computer-use, embodied, and enterprise agents |
|| | [Physical AI](build/physical-ai.md) | Humanoid robotics, VLA models, simulation, RL environments |
|| | [Paper-to-Code](build/paper-to-code.md) | Research2Repo, PaperCoder, AI Scientist |
|| **Infrastructure** <a id="infrastructure"></a> | [LLM Frameworks](infrastructure/llm-frameworks.md) | Orchestration, platforms, structured output, observability |
|| | [RAG & Vector DBs](infrastructure/rag-vector-db.md) | Vector databases, RAG engines, Graph RAG, embeddings |
|| | [Data Infra](infrastructure/data-infra.md) | Iceberg, Spark, Delta Lake, MLflow, Ray |
|| | [Fine-Tuning](infrastructure/fine-tuning.md) | LoRA variants, PEFT, DPO, instruction tuning |
|| | [Deployment](infrastructure/deployment.md) | vLLM, TGI, Vertex AI, Bedrock, Triton |
|| | [Distributed Training](infrastructure/distributed-training.md) | ColossalAI, DeepSpeed, Megatron-LM, FSDP, Accelerate |
|| | [Compute & Hardware](infrastructure/compute-hardware.md) | GPUs, TPUs, LPUs, quantization (GPTQ/AWQ), neuromorphic, decentralized |
|| | [Prompt Engineering](infrastructure/prompt-engineering.md) | CoT, ToT, GoT, advanced techniques |
|| **Safety** <a id="safety"></a> | [Safety & Alignment](safety/safety-alignment.md) | Superalignment, RLHF, DPO, interpretability, AI governance |
|| **Research** <a id="research"></a> | [Papers & Blogs](research/papers-blogs.md) | 60+ papers on frontier models, reasoning, agents |
|| | [Tutorials](research/tutorials.md) | Courses and hands-on learning resources |
|| | [Conferences](research/conferences.md) | 28 academic, AGI, safety, and industry events |
