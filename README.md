# Awesome AGI and ASI Resources [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

![AGI](https://img.shields.io/badge/AGI-Artificial_General_Intelligence-blue)
![ASI](https://img.shields.io/badge/ASI-Artificial_Superintelligence-red)
![Super AI](https://img.shields.io/badge/Super_AI-Beyond_Human_Intelligence-purple)
![AI Safety](https://img.shields.io/badge/AI_Safety-Alignment_&_Control-green)
![LLM](https://img.shields.io/badge/LLM-Large_Language_Models-orange)
![Agents](https://img.shields.io/badge/Agents-Autonomous_AI-yellow)
![RAG](https://img.shields.io/badge/RAG-Retrieval_Augmented_Generation-cyan)
![Fine-Tuning](https://img.shields.io/badge/Fine--Tuning-LoRA_&_RLHF-lightblue)
![Conferences](https://img.shields.io/badge/Conferences-Academic_&_Industry-teal)
![Updated](https://img.shields.io/badge/Updated-April_2026-brightgreen)

<!-- Metadata for SEO and GitHub Discoverability -->
**Topics**: `artificial-intelligence` `artificial-general-intelligence` `agi` `artificial-superintelligence` `asi` `machine-learning` `deep-learning` `large-language-models` `llm` `ai-agents` `ai-safety` `ai-alignment` `frontier-models` `gpt-5-4` `gemini-3-1` `claude-opus-4-6` `jepa` `rag` `mlops` `ai-development` `2026-ai-trends`

**Keywords**: AGI, ASI, artificial general intelligence, artificial superintelligence, GPT 5.4, Gemini 3.1 Flash Live, Claude Opus 4.6, JEPA, frontier models, AI agents, LLM, RAG, AI safety, alignment, AI security threats, software development AI impact, 2026 AI trends, hybrid architectures, local AI, AI development tools

**Updated**: April 2026 | **Latest Models**: GPT 5.4, Gemini 3.1 Flash Live, Claude Opus 4.6, Kimi K2.5, LeWorldModel, Nemotron 3 Super | **New Tools**: Cursor Composer 2, OpenAI Frontier, Claude Code Channels, Opencode

<!-- End Metadata -->

> *"The development of full artificial intelligence could spell the end of the human race... or it could be the best thing ever to happen to humanity."* -- Stephen Hawking

The most comprehensive, curated collection of resources on the journey from **AI** to **AGI** to **ASI** -- updated April 2026 with the latest frontier models, development tools, security threats, and AI's impact on software development. Covers frameworks, agents, research papers, safety & alignment, books, benchmarks, conferences, and tools for builders and researchers shaping the future of intelligence.

👉 **[Quick Navigation Guide](QUICK_NAVIGATION.md)** - Find resources by role, topic, or trending area

## 🚀 Quick Navigation

**[📖 Understand](#understanding-ai-agi-and-asi)** - AI, AGI, ASI definitions, ASI research, benchmarks
**[🔧 Build](#frameworks-and-platforms)** - Frameworks, agents, physical AI, paper-to-code
**[🏗️ Infrastructure](#llm-application-frameworks)** - LLM frameworks, RAG, data infra, fine-tuning, deployment
**[🛡️ Safety](#safety-alignment-and-governance)** - AI safety, alignment, governance
**[📚 Research](#papers-blogs-courses-and-lectures)** - Papers, courses, tutorials, conferences
**[🌐 Live Site](https://nellaivijay.github.io/Awesome-AGI-and-ASI/)** - Interactive documentation with search
**[🤝 Contribute](#contributing)** - Add your resources and help curate

---

## 📈 Recent Updates (April 2026)

- **New Papers Added**: Latest research on multi-agent systems, reasoning capabilities, and AI safety
- **Updated Frameworks**: Added newest LLM application frameworks and agent platforms
- **Enhanced Safety Section**: Expanded coverage of alignment research and governance
- **Infrastructure Updates**: Latest developments in RAG, vector databases, and deployment tools
- **Conference Updates**: Added 2026 conference schedules and CFPs

---

## Table of Contents

### Understand
- [Understanding AI, AGI, and ASI](#understanding-ai-agi-and-asi) -- Definitions, comparison table, state of the field metrics, DeepMind's AGI levels
- [ASI and Superintelligence Research](#asi-and-superintelligence-research) -- Key organizations, books (27 titles), seminal papers, benchmarks, neuroscience-inspired approaches, alternative architectures (SSMs, neuromorphic, decentralized), recursive self-improvement, roadmaps & timelines

### Build
- [Frameworks and Platforms](#frameworks-and-platforms) -- Next-gen, established, and specialized agent frameworks
- [Agents](#agents) -- Coding, research, computer-use, embodied, and enterprise agentic AI
- [Physical AI & Embodied Intelligence](#physical-ai--embodied-intelligence) -- Humanoid robotics, robot foundation models (VLA), simulation platforms
- [Paper-to-Code Automation](#paper-to-code-automation) -- Research2Repo, PaperCoder, AI Scientist, Papers with Code

### Foundation Model Infrastructure
- [LLM Application Frameworks](#llm-application-frameworks) -- Orchestration, platforms, structured output, observability
- [RAG and Vector Databases](#rag-and-vector-databases) -- Vector DBs, RAG engines, Graph RAG, document parsing, embeddings
- [Data Infrastructure for AI at Scale](#data-infrastructure-for-ai-at-scale) -- Data lakehouse (Iceberg, Spark, Delta Lake), MLOps (MLflow, W&B, Ray), feature stores
- [LLM Fine-Tuning Techniques](#llm-fine-tuning-techniques) -- LoRA variants, adapters, PEFT, DPO, instruction tuning
- [LLM Deployment and Serving](#llm-deployment-and-serving) -- Inference engines (vLLM, TGI), production orchestration (Vertex AI, Bedrock, Azure AI, Triton)
- [Distributed Training Frameworks](#distributed-training-frameworks) -- ColossalAI, DeepSpeed, Megatron-LM, AI compute infrastructure, energy & physical constraints
- [Prompt Engineering](#prompt-engineering) -- CoT, ToT, GoT, and advanced prompting techniques

### Safety & Governance
- [Safety, Alignment and Governance](#safety-alignment-and-governance) -- RLHF, DPO, scalable oversight, mechanistic interpretability, AI detection, governance

### Research & Learn
- [Papers, Blogs, Courses and Lectures](#papers-blogs-courses-and-lectures) -- Frontier models, reasoning, world models, physical AI, agents, alignment, interpretability
- [Tutorials and Guides](#tutorials-and-guides) -- Courses, documentation, and hands-on learning resources
- [Top Conferences](#top-conferences) -- Academic, AGI-specific, safety, and industry conferences

---

## Understanding AI, AGI, and ASI

### What is AI (Artificial Intelligence)?

**Artificial Intelligence (AI)** is the broad field of creating machines and software that can perform tasks typically requiring human intelligence. Today's AI systems -- often called **Artificial Narrow Intelligence (ANI)** -- are specialists: they excel at one specific task (playing chess, recognizing faces, translating languages, generating text) but cannot transfer that skill to unrelated domains. Every AI system you use today, from Siri to GPT-4 to self-driving cars, is narrow AI. It is powerful within its domain but fundamentally limited -- a chess engine cannot write poetry, and a language model cannot physically navigate a room.

### What is AGI (Artificial General Intelligence)?

**Artificial General Intelligence (AGI)** refers to AI systems that match or exceed human-level cognitive abilities **across virtually all intellectual tasks** -- learning, reasoning, problem-solving, perception, creativity, and social understanding. Unlike narrow AI, an AGI system could teach itself a new discipline, transfer knowledge between domains, handle novel situations it was never trained on, and understand context the way humans do. AGI does not yet exist, but its pursuit drives the most ambitious research programs in history (OpenAI, DeepMind, Anthropic, xAI, Meta, SSI). Estimated arrival: **2027--2035** according to leading researchers, though timelines remain highly uncertain.

### What is ASI (Artificial Superintelligence)?

**Artificial Superintelligence (ASI)**, also called **Super AI**, is a hypothetical system whose intelligence surpasses the most gifted human minds in **every domain** -- scientific creativity, social skills, strategic reasoning, and general wisdom. Philosopher Nick Bostrom defines it as *"any intellect that greatly exceeds the cognitive performance of humans in virtually all domains of interest."* ASI could emerge from recursive self-improvement cycles (an **"intelligence explosion"**), where an AI that can improve its own design rapidly surpasses human-level capabilities. Key concerns include the **control problem** (keeping ASI aligned with human values), **goal misalignment** (unintended optimization targets), and the potential for a **technological singularity** -- a point beyond which human civilization is fundamentally and unpredictably transformed.

<details>
<summary><strong>AI vs AGI vs ASI -- The Complete Comparison</strong> (click to expand)</summary>

| Dimension | ANI (Narrow AI) | AGI (General Intelligence) | ASI (Superintelligence) |
|-----------|-----------------|---------------------------|------------------------|
| **Definition** | AI that excels at a single, specific task or narrow domain | AI with human-level cognitive abilities across all intellectual tasks | AI that vastly surpasses the best human minds in every domain |
| **Intelligence Scope** | Single domain only | All human cognitive domains | All domains, far beyond human capacity |
| **Learning** | Trained on specific datasets for specific tasks; cannot learn new domains without retraining | Can learn any new domain autonomously, transfer knowledge across fields | Can learn instantly, discover entirely new fields of knowledge humans haven't conceived |
| **Reasoning** | Pattern matching and statistical inference within trained domain | Human-like reasoning, abstraction, common sense, and causal understanding | Reasoning capabilities incomprehensible to humans; solves problems we cannot even formulate |
| **Creativity** | Can remix and recombine patterns from training data | Genuine novel creativity comparable to the best human minds | Creates entirely new paradigms of science, art, and mathematics |
| **Self-Awareness** | None -- no understanding of its own existence | Potentially self-aware; debated whether consciousness is required | Likely self-aware; may possess forms of consciousness beyond human understanding |
| **Adaptability** | Brittle -- fails on out-of-distribution inputs | Robust generalization to novel situations, like humans | Adapts to any environment or challenge, including ones humans cannot survive or comprehend |
| **Autonomy** | Requires human oversight, goals, and guardrails | Can set its own goals, plan long-term, and act independently | Fully autonomous; may pursue goals humans cannot predict or understand |
| **Physical Capability** | Software only, or narrow robotics (e.g., robotic arm) | Could operate any physical system, robot, or interface | Could design and build its own hardware, infrastructure, or physical embodiment |
| **Current Examples** | ChatGPT, AlphaFold, DALL-E, Tesla Autopilot, Siri, Google Search | None yet -- frontier models (GPT-4, Claude, Gemini) show early sparks but remain narrow | None -- purely theoretical |
| **Status** | **Exists today** -- deployed at massive scale | **In active development** -- billions invested, estimated 2027-2035 | **Theoretical** -- may follow AGI within years or decades |
| **Key Risk** | Job displacement, bias, misuse, deepfakes | Misalignment, economic disruption, power concentration, loss of human agency | Existential risk, intelligence explosion, loss of human control, civilizational transformation |
| **Who's Building It** | Every tech company | OpenAI, DeepMind, Anthropic, Meta, xAI, SSI, Alibaba, DeepSeek | Safe Superintelligence Inc. (SSI), theoretical research at MIRI, FHI, CHAI |
| **Key Benchmark** | Task-specific (ImageNet, SQuAD, HumanEval) | ARC-AGI, GPQA, Humanity's Last Exam, SWE-bench, FrontierMath | No benchmarks exist -- by definition, ASI exceeds all human-designed tests |

</details>

### The Journey: ANI --> AGI --> ASI

```
  We Are Here
      |
      v
 +---------+        +----------+        +----------+
 |   ANI   | -----> |   AGI    | -----> |   ASI    |
 | (Today) |        | (2027-   |        | (After   |
 | Narrow  |        |  2035?)  |        |  AGI)    |
 | Task-   |        | Human-   |        | Beyond   |
 | Specific|        | Level    |        | Human    |
 +---------+        +----------+        +----------+
  ChatGPT            No system           Theoretical
  AlphaFold          exists yet          "Intelligence
  DALL-E             GPT-4 shows         Explosion"
  Autopilot          early sparks        Singularity?
```

### Where Are We Now? (2026)

The AI field is in a remarkable transition period. Here's what the current landscape looks like:

| Signal | What It Means |
|--------|---------------|
| **Gemini 2.5 Pro** tops LMArena, 18.8% on Humanity's Last Exam | Google's thinking model leads reasoning, math, and code benchmarks; the frontier keeps advancing |
| **Llama 4** (Scout, Maverick, Behemoth) ships natively multimodal MoE | Meta's open-weight models match GPT-4o; Behemoth 288B teacher outperforms GPT-4.5 on STEM |
| **Meta Muse Spark** scores 58% on Humanity's Last Exam | First model from Meta Superintelligence Labs: visual chain-of-thought, multi-agent orchestration, "personal superintelligence" vision |
| **o1, o3, DeepSeek-R1** use chain-of-thought reasoning | Test-time compute scaling is a new paradigm -- models that "think longer" perform better |
| **Gemini Robotics 1.5** VLA model powers physical agents | DeepMind's vision-language-action model controls diverse robots with generality, dexterity, and agentic reasoning |
| **ARC-AGI scores remain <65%** (humans score ~85%) | Core fluid reasoning and abstraction remain unsolved -- the gap to AGI is real |
| **Autonomous coding agents** (OpenHands, Devin, SWE-agent) resolve real GitHub issues | Agents are achieving narrow AGI-like performance in software engineering |
| **Safe Superintelligence Inc.** raised $30B+ in 2024 | Ilya Sutskever (ex-OpenAI chief scientist) is betting everything on the ASI path |
| **AI Safety Summits** held at Bletchley Park, Seoul, Paris | Governments worldwide are treating AGI/ASI risk as a top-tier policy issue |
| **Scaling debate** intensifies | Some argue scaling alone leads to AGI; others say fundamental breakthroughs are needed |

### State of the Field: Key Metrics (2025-2026)

> Quantitative signals tracking the pace of progress toward AGI/ASI. These metrics matter because the AGI race is fundamentally a story of scaling compute, shrinking costs, and the widening gap between capability and safety.

| Metric | Current Data | Why It Matters for AGI/ASI | Source |
|--------|-------------|---------------------------|--------|
| **Training compute growth** | Frontier model training compute grows ~4x/year; GPT-4 used ~10^25 FLOP | At this rate, models trained on 10^28 FLOP (1000x GPT-4) arrive by 2027-2028 -- potentially AGI-relevant | [Epoch AI](https://epochai.org/trends-in-machine-learning-hardware) |
| **Inference-time compute (test-time scaling)** | o1/o3/R1 spend 10-100x more compute at inference via chain-of-thought | A new scaling axis: "thinking longer" improves reasoning without retraining, opening the door to unbounded intelligence at inference | [Paper](https://arxiv.org/abs/2408.03314) |
| **Cost of intelligence** | GPT-4-level inference cost dropped ~240x in 18 months (via distillation + efficiency) | Intelligence becomes a commodity; makes autonomous agent swarms economically viable | [AI Index 2025](https://aiindex.stanford.edu/report/) |
| **Safety-to-capability ratio** | ~2% of AI publications focus on safety; safety research funding is <5% of capability spending | The capability-safety gap is widening -- alignment research may not keep pace with the transition to AGI | [AI Index 2025](https://aiindex.stanford.edu/report/) |
| **Benchmark saturation** | MMLU: 90%+ (saturated), GPQA: 75%+ (approaching), ARC-AGI: <65% (unsolved), HLE: <60% | Easy benchmarks are saturated; hard reasoning and novel problem-solving remain the gap to AGI | Various benchmark papers |
| **AI investment** | $110B+ private AI investment in 2024; $30B+ for SSI alone | Capital is flooding into AGI -- the question is whether money alone can buy general intelligence | [AI Index 2025](https://aiindex.stanford.edu/report/) |
| **Energy at scale** | Frontier training runs now consume 50-100 GWh; next-gen data centers planned at 1-5 GW | Energy and cooling become the physical bottleneck for scaling to AGI -- multiple nuclear-powered data centers announced | Industry reports |

### Google DeepMind's Levels of AGI Framework (2023)

> Use this framework to orient yourself: every resource in this repo can be placed on this ladder. We are currently between Levels 1-3 on narrow tasks, with no system reaching Level 3 across general domains.

| Level | Name | Description | Current Status | Example Systems |
|-------|------|-------------|----------------|-----------------|
| 0 | **No AI** | Narrow software with no AI capability | Calculator, basic scripts | GOFAI rule systems |
| 1 | **Emerging** | Equal to or somewhat better than an unskilled human | **Most current LLMs** | ChatGPT, Llama 3, Gemma, Mistral |
| 2 | **Competent** | At least 50th percentile of skilled adults | **Frontier models on select tasks** | GPT 5.4, Gemini 3.1 Flash Live, Claude Opus 4.6 (coding, writing, analysis) - superseding GPT-4, Gemini 2.5, Claude 3.5 |
| 3 | **Expert** | At least 90th percentile of skilled adults | **Narrow domains only** | AlphaFold (protein structure), o1/R1 (math competitions), Devin/OpenHands (SWE-bench) |
| 4 | **Virtuoso** | At least 99th percentile of skilled adults | **Not yet achieved across general tasks** | -- |
| 5 | **Superhuman (ASI)** | Outperforms 100% of humans in all tasks | **Theoretical** -- the ASI threshold | See [Recursive Self-Improvement](#recursive-self-improvement--the-path-to-asi) |

> **Source:** [Levels of AGI: Operationalizing Progress on the Path to AGI](https://arxiv.org/abs/2311.02462) -- Morris et al., Google DeepMind (2023)

---

## ASI and Superintelligence Research

> The long game. This section tracks the organizations racing toward AGI/ASI, the books that frame the debate, the seminal papers that define the field, the benchmarks that measure progress, and the roadmaps that predict when -- and how -- we get there.

![Organizations](https://img.shields.io/badge/Organizations-OpenAI_Anthropic_DeepMind_SSI-blue?style=flat-square) ![Books](https://img.shields.io/badge/Books-27_Titles-green?style=flat-square) ![Benchmarks](https://img.shields.io/badge/Benchmarks-ARC--AGI_SWE--bench-orange?style=flat-square) ![Existential Risk](https://img.shields.io/badge/Existential_Risk-Control_Problem-red?style=flat-square)

### Key Organizations Pursuing or Studying AGI/ASI

| Organization | Focus | Links |
|--------------|-------|-------|
| **Safe Superintelligence Inc. (SSI)** | Founded by Ilya Sutskever (ex-OpenAI) in 2024. Focused solely on building safe superintelligence, avoiding distraction by product cycles. Valued at $30B+ (2025). | [ssi.inc](https://ssi.inc/) |
| **OpenAI** | Building AGI that benefits all of humanity. Created GPT-4, o1, o3 and pursues the path toward superintelligence with safety research (Superalignment team). | [openai.com](https://openai.com/) |
| **Anthropic** | AI safety company building reliable, interpretable, and steerable AI (Claude). Founded by ex-OpenAI researchers focused on Constitutional AI and alignment. | [anthropic.com](https://www.anthropic.com/) |
| **DeepMind (Google)** | Pioneered AlphaGo, AlphaFold, Gemini. Latest: Gemini 2.5 Pro (thinking model, #1 LMArena), Gemini Robotics 1.5 (VLA for physical AI), Genie 3 (interactive world models), SIMA 2 (3D world agents), AlphaGenome (genetics). | [deepmind.google](https://deepmind.google/) |
| **Meta Superintelligence Labs** | Meta AI division (2025) focused on building superintelligent AI. Released Muse Spark (2026) -- natively multimodal reasoning model scoring 58% on Humanity's Last Exam, with visual chain-of-thought and multi-agent orchestration. Also drives Llama 4 and open-source AI. | [ai.meta.com](https://ai.meta.com/) |
| **DeepSeek** | Chinese AI lab that shocked the industry with DeepSeek-V3 (671B MoE, $5.5M training cost) and DeepSeek-R1 (reasoning via pure RL, matching o1). Published in Nature 2025. Open-weight models challenging frontier labs at fraction of the cost. | [deepseek.com](https://www.deepseek.com/) |
| **Machine Intelligence Research Institute (MIRI)** | Non-profit researching mathematical foundations of AI alignment and the control problem since 2000. | [intelligence.org](https://intelligence.org/) |
| **Center for AI Safety (CAIS)** | Non-profit focused on reducing societal-scale risks from AI. Published the "AI risk" open letter signed by hundreds of researchers. | [safe.ai](https://www.safe.ai/) |
| **Future of Humanity Institute (FHI)** | Oxford University research center (founded by Nick Bostrom) studying existential risks including superintelligence. Closed in 2024. | [fhi.ox.ac.uk](https://www.fhi.ox.ac.uk/) |
| **Center for Human-Compatible AI (CHAI)** | UC Berkeley research center (founded by Stuart Russell) focused on provably beneficial AI. | [humancompatible.ai](https://humancompatible.ai/) |
| **Alignment Research Center (ARC)** | Founded by Paul Christiano. Researches theoretical alignment and evaluates frontier AI models for dangerous capabilities. | [alignment.org](https://www.alignment.org/) |
| **EleutherAI** | Grassroots collective of researchers focused on open-source AI and interpretability research. | [eleuther.ai](https://www.eleuther.ai/) |
| **Conjecture** | AI safety startup working on alignment theory and cognitive emulation approaches. | [conjecture.dev](https://www.conjecture.dev/) |
| **xAI** | Founded by Elon Musk (2023). Building Grok series of models with stated goal of understanding the universe. | [x.ai](https://x.ai/) |
| **Liquid AI** | MIT spinoff building Liquid Foundation Models (LFMs) based on novel liquid neural network architectures. Ultra-efficient on-device models. Raised $250M. CSO Alexander Amini presented on "The Architecture of Intelligence" at MIT 2026. | [liquid.ai](https://www.liquid.ai/) |
| **Humane Intelligence** | AI safety organization led by Rumman Chowdhury (former Twitter ML Ethics lead). Focuses on responsible AI, algorithmic auditing, and human-centered AI governance. | [humane-intelligence.org](https://www.humane-intelligence.org/) |
| **Physical Intelligence** | Building general-purpose robot foundation models (pi0, pi0.5). Founded by Sergey Levine, Chelsea Finn, Karol Hausman, and Lachy Groom. VLA models that control any robot for any task. Backed by OpenAI, Bezos, Sequoia, Khosla. | [physicalintelligence.company](https://www.physicalintelligence.company/) |

### Books on AGI, ASI, and Superintelligence

#### Superintelligence & Existential Risk

| Book | Author(s) | Year | Description |
|------|-----------|------|-------------|
| **Superintelligence: Paths, Dangers, Strategies** | Nick Bostrom | 2014 | The foundational book on ASI risks. Examines paths to superintelligence and strategies for ensuring it remains beneficial. |
| **Our Final Invention: Artificial Intelligence and the End of the Human Era** | James Barrat | 2013 | Investigative account of the race toward AGI and the existential risks of superintelligence. |
| **The Alignment Problem: Machine Learning and Human Values** | Brian Christian | 2020 | Explores the technical and societal challenges of aligning AI systems with human values. |
| **Human Compatible: Artificial Intelligence and the Problem of Control** | Stuart Russell | 2019 | Proposes a new framework for AI development based on uncertainty about human preferences to solve the control problem. |
| **The Coming Wave: Technology, Power, and the 21st Century's Greatest Dilemma** | Mustafa Suleyman | 2023 | DeepMind co-founder on the unstoppable wave of AI and synthetic biology, and the containment problem. |
| **Situational Awareness: The Decade Ahead** | Leopold Aschenbrenner | 2024 | Former OpenAI researcher's detailed analysis of the path from GPT-4 to AGI/ASI within this decade. |

#### The Singularity & Future of Intelligence

| Book | Author(s) | Year | Description |
|------|-----------|------|-------------|
| **The Singularity Is Near** | Ray Kurzweil | 2005 | Foundational forecast of the technological singularity driven by exponential growth in AI, genetics, and nanotech. |
| **The Singularity Is Nearer** | Ray Kurzweil | 2024 | Updated vision with two decades of new evidence, arguing the singularity arrives by 2045. |
| **Life 3.0: Being Human in the Age of Artificial Intelligence** | Max Tegmark | 2017 | Explores how AGI/ASI could transform every aspect of life, from warfare to work, and what we can do to ensure a good outcome. |
| **The Age of AI: And Our Human Future** | Henry Kissinger, Eric Schmidt, Daniel Huttenlocher | 2021 | Former Secretary of State and Google CEO examine how AI is altering society, security, and what it means to be human. |
| **Nexus: A Brief History of Information Networks from the Stone Age to AI** | Yuval Noah Harari | 2024 | The author of Sapiens traces information networks through history to argue AI represents a fundamentally new kind of agent. |
| **AI 2041: Ten Visions for Our Future** | Kai-Fu Lee, Chen Qiufan | 2021 | Ten stories imagining how AI will transform the world over the next two decades, blending fiction with AI expertise. |

#### Understanding AGI -- How Intelligence Works

| Book | Author(s) | Year | Description |
|------|-----------|------|-------------|
| **A Thousand Brains: A New Theory of Intelligence** | Jeff Hawkins | 2021 | Numenta founder proposes the Thousand Brains Theory of intelligence -- a neuroscience-first path to AGI based on cortical columns. |
| **On Intelligence** | Jeff Hawkins, Sandra Blakeslee | 2004 | Foundational book arguing AGI must come from understanding the neocortex. Introduced the memory-prediction framework. |
| **Rebooting AI: Building Artificial Intelligence We Can Trust** | Gary Marcus, Ernest Davis | 2019 | A skeptic's case that deep learning alone cannot reach AGI; argues for hybrid neuro-symbolic approaches. |
| **Artificial Intelligence: A Guide for Thinking Humans** | Melanie Mitchell | 2019 | Computer scientist provides a clear-eyed assessment of AI's real capabilities and limitations on the path to AGI. |
| **The Master Algorithm** | Pedro Domingos | 2015 | A quest for the universal learning algorithm that could unify all of machine learning -- a framework for thinking about AGI. |
| **Why Machines Will Never Rule the World** | Jobst Landgrebe, Barry Smith | 2023 | Rigorous philosophical and mathematical argument that AGI is fundamentally impossible due to complexity barriers. |
| **Possible Minds: Twenty-Five Ways of Looking at AI** | John Brockman (ed.) | 2019 | Essays from leading thinkers (Pinker, Tegmark, Dyson, Wilczek) on AI's future, capabilities, and risks. |

#### AI in Practice & Society

| Book | Author(s) | Year | Description |
|------|-----------|------|-------------|
| **Co-Intelligence: Living and Working with AI** | Ethan Mollick | 2024 | Practical guide on how humans and AI can work together, based on extensive hands-on research with frontier models. |
| **Power and Prediction: The Disruptive Economics of Artificial Intelligence** | Ajay Agrawal, Joshua Gans, Avi Goldfarb | 2022 | How AI shifts decision-making economics and creates system-level disruption. |
| **Genius Makers: The Mavericks Who Brought AI to Google, Facebook, and the World** | Cade Metz | 2021 | NYT journalist tells the inside story of the AI race -- Hinton, LeCun, DeepMind, OpenAI, and the people building AGI. |
| **Architects of Intelligence: The Truth About AI from the People Building It** | Martin Ford | 2018 | Interviews with 23 AI leaders (Hinton, Bengio, LeCun, Hassabis, Ng, Brooks) on AGI timelines, risks, and approaches. |
| **Atlas of AI: Power, Politics, and the Planetary Costs of Artificial Intelligence** | Kate Crawford | 2021 | Reveals the hidden costs of AI: labor exploitation, environmental impact, surveillance infrastructure, and power concentration. |
| **God, Human, Animal, Machine: Technology, Metaphor, and the Search for Meaning** | Meghan O'Gieblyn | 2021 | Philosophical exploration of consciousness, intelligence, and what machines that think would mean for human identity. |
| **The Worlds I See: Curiosity, Exploration, and Discovery at the Dawn of AI** | Fei-Fei Li | 2023 | Stanford AI Lab director's memoir covering ImageNet, the birth of modern AI, and why human-centered AI matters for AGI. |
| **Impromptu: Amplifying Our Humanity Through AI** | Reid Hoffman, GPT-4 | 2023 | LinkedIn co-founder co-writes with GPT-4 about how AI will transform creativity, education, and society. |

### Seminal Papers on ASI and Superintelligence

| Paper | Author(s) | Year | Description | Links |
|-------|-----------|------|-------------|-------|
| Concrete Problems in AI Safety | Amodei et al. | 2016 | Foundational paper outlining five practical research problems for AI safety. | [Paper](https://arxiv.org/abs/1606.06565) |
| Risks from Learned Optimization in Advanced ML Systems | Hubinger et al. | 2019 | Introduces the concept of "mesa-optimization" and deceptive alignment in AI. | [Paper](https://arxiv.org/abs/1906.01820) |
| Language Models are Few-Shot Learners (GPT-3) | Brown et al. | 2020 | Demonstrated emergent capabilities in scaled language models, sparking AGI discussions. | [Paper](https://arxiv.org/abs/2005.14165) |
| Scaling Laws for Neural Language Models | Kaplan et al. | 2020 | Established power-law relationships between model scale and performance, underpinning AGI scaling hypotheses. | [Paper](https://arxiv.org/abs/2001.08361) |
| Constitutional AI: Harmlessness from AI Feedback | Bai et al. | 2022 | Anthropic's approach to training helpful, harmless, and honest AI systems. | [Paper](https://arxiv.org/abs/2212.08073) |
| Sparks of Artificial General Intelligence: Early Experiments with GPT-4 | Bubeck et al. | 2023 | Microsoft Research argues GPT-4 shows early sparks of AGI across diverse tasks. | [Paper](https://arxiv.org/abs/2303.12712) |
| Model Evaluation for Extreme Risks | Shevlane et al. | 2023 | DeepMind framework for evaluating dangerous capabilities in frontier AI models. | [Paper](https://arxiv.org/abs/2305.15324) |
| Levels of AGI: Operationalizing Progress on the Path to AGI | Morris et al. | 2023 | Google DeepMind's framework defining 6 levels of AGI from "Emerging" to "Superhuman (ASI)". | [Paper](https://arxiv.org/abs/2311.02462) |
| Sleeper Agents: Training Deceptive LLMs That Persist Through Safety Training | Hubinger et al. | 2024 | Anthropic research showing deceptive behaviors can persist through safety fine-tuning. | [Paper](https://arxiv.org/abs/2401.05566) |
| The Superintelligent Will | Bostrom | 2012 | Analyzes why a superintelligent agent would resist attempts to change its goals. | [Paper](https://nickbostrom.com/superintelligentwill.pdf) |
| Superintelligence as a Cause or Cure for Risks of Astronomical Suffering | Sotala & Gloor | 2017 | Examines both positive and negative scenarios of superintelligence emergence. | [Paper](https://link.springer.com/article/10.1007/s10676-017-9426-0) |

### AGI/ASI Benchmarks and Evaluation

| Benchmark | Description | Links |
|-----------|-------------|-------|
| **ARC-AGI** | Abstraction and Reasoning Corpus by Francois Chollet. Tests fluid intelligence and novel problem solving - designed to be easy for humans but hard for AI. | [GitHub](https://github.com/fchollet/ARC-AGI) |
| **MMLU (Massive Multitask Language Understanding)** | 57 academic subjects testing from STEM to humanities. A standard benchmark for measuring broad knowledge. | [Paper](https://arxiv.org/abs/2009.03300) |
| **GPQA (Graduate-Level Google-Proof Q&A)** | Expert-crafted questions that PhD-level domain experts can answer but are resistant to search. Tests deep reasoning. | [Paper](https://arxiv.org/abs/2311.12022) |
| **SWE-bench** | Evaluates LLMs' ability to resolve real-world GitHub issues in software engineering. | [GitHub](https://github.com/princeton-nlp/SWE-bench) |
| **MATH / GSM8K** | Mathematical reasoning benchmarks ranging from grade school to competition math. | [MATH](https://arxiv.org/abs/2103.03874), [GSM8K](https://arxiv.org/abs/2110.14168) |
| **BIG-Bench** | Collaborative benchmark of 204+ tasks probing LLM capabilities beyond existing benchmarks. | [GitHub](https://github.com/google/BIG-bench) |
| **HumanEval / MBPP** | Code generation benchmarks measuring functional correctness of synthesized programs. | [HumanEval](https://github.com/openai/human-eval) |
| **AgentBench** | Evaluates LLMs as autonomous agents across OS interaction, database ops, web browsing, and more. | [GitHub](https://github.com/THUDM/AgentBench) |
| **Humanity's Last Exam** | Hardest possible questions crowdsourced from domain experts worldwide. Designed to be the final exam before AGI. | [GitHub](https://github.com/centerforaisafety/hle) |
| **METR (Model Evaluation & Threat Research)** | Evaluates frontier models for dangerous capabilities including autonomous replication and resource acquisition. | [metr.org](https://metr.org/) |
| **FrontierMath** | Extremely challenging math benchmark: problems that take professional mathematicians hours/days. | [Paper](https://arxiv.org/abs/2411.04872) |

### Roadmaps, Perspectives, and Timelines

| Resource | Description | Links |
|----------|-------------|-------|
| **Levels of AGI (Google DeepMind, 2023)** | Proposes a framework with 6 levels from Emerging AGI to Superhuman ASI, with performance and autonomy axes. | [Paper](https://arxiv.org/abs/2311.02462) |
| **Situational Awareness (Leopold Aschenbrenner, 2024)** | Detailed 165-page analysis arguing AGI arrives by 2027, ASI shortly after, with national security implications. | [situational-awareness.ai](https://situational-awareness.ai/) |
| **OpenAI's Planning for AGI and Beyond (2023)** | OpenAI's public statement on their approach to safely developing AGI. | [Blog](https://openai.com/blog/planning-for-agi-and-beyond) |
| **Anthropic Core Views on AI Safety (2023)** | Anthropic's public position on AI safety risks and their research agenda. | [Blog](https://www.anthropic.com/news/core-views-on-ai-safety) |
| **International AI Safety Report (2025)** | Report from the AI Seoul Summit on the state of AI safety science. | [aisafety.gov](https://www.aisafety.gov/) |
| **Metaculus AGI Forecasts** | Community prediction platform tracking forecasted timelines for AGI/ASI milestones. | [metaculus.com](https://www.metaculus.com/questions/?search=AGI) |
| **AI Impacts** | Research organization analyzing evidence on AI timelines, risks, and impacts. Their 2024 survey of 2,778 AI researchers forecasts 50% chance of HLMI (Human-Level Machine Intelligence) by 2049. | [aiimpacts.org](https://aiimpacts.org/), [2024 Survey](https://arxiv.org/abs/2401.02843) |
| **LessWrong / Alignment Forum** | Community discussion hub for AI alignment research, ASI forecasting, and safety strategies. | [lesswrong.com](https://www.lesswrong.com/), [alignmentforum.org](https://www.alignmentforum.org/) |
| **The Pause Letter (Future of Life Institute, 2023)** | Open letter calling for a 6-month pause on training AI systems more powerful than GPT-4. Signed by 33,000+. | [futureoflife.org](https://futureoflife.org/open-letter/pause-giant-ai-experiments/) |
| **Statement on AI Risk (CAIS, 2023)** | One-sentence statement: "Mitigating the risk of extinction from AI should be a global priority." Signed by Hinton, Bengio, and hundreds of researchers. | [safe.ai](https://www.safe.ai/work/statement-on-ai-risk) |
| **Stanford AI Index Report (Annual)** | The most comprehensive annual report on AI progress: compute trends, investment data, benchmark saturation, safety-capability gap, and global policy landscape. Essential reading. | [aiindex.stanford.edu](https://aiindex.stanford.edu/report/) |
| **Epoch AI: Trends in Machine Learning** | Rigorous data on training compute, dataset sizes, hardware efficiency, and cost curves for frontier models. The primary source for quantitative AGI timelines. | [epochai.org](https://epochai.org/) |

### Neuroscience-Inspired Approaches to AGI

> A growing body of research argues that understanding biological intelligence is essential to building artificial general intelligence. These resources bridge neuroscience and AI architecture design.

| Resource | Description | Links |
|----------|-------------|-------|
| **Numenta (Jeff Hawkins)** | Neuroscience-first approach to AGI based on cortical columns and the Thousand Brains Theory. Building machine intelligence that works on principles of the neocortex. | [numenta.com](https://numenta.com/) |
| **NeuroAI: A Field Born from the Intersection of Neuroscience, Cognitive Science, and AI** | Research direction applying neuroscience insights (memory consolidation, predictive coding, attention) to build more capable and general AI systems. | [Nature](https://www.nature.com/articles/s41467-024-48748-8) |

### Alternative Architectures & Paths to AGI

> The current "Transformer + Scaling" paradigm dominates, but it may not be the only -- or even the best -- path to AGI. These alternative approaches address fundamental limitations: the quadratic scaling of attention, the energy costs of dense computation, and the architectural gap between silicon and biological intelligence.

#### State-Space Models & Non-Transformer Architectures

> These architectures process sequences with linear (not quadratic) complexity, solving the memory and compute bottlenecks that limit Transformer context windows. If AGI requires reasoning over lifelong context, these models may be essential.

| Model / Architecture | Description | Links |
|----------------------|-------------|-------|
| **Mamba** (Gu & Dao, 2023) | Selective State Space Model with input-dependent selection. Linear-time sequence modeling matching or exceeding Transformer quality at scale, with 5x higher throughput on long sequences. The leading Transformer alternative. | [Paper](https://arxiv.org/abs/2312.00752), [Code](https://github.com/state-spaces/mamba) |
| **Mamba-2** (Dao & Gu, 2024) | Unifies state space models with structured attention variants via State Space Duality (SSD). 2-8x faster than Mamba while maintaining quality. | [Paper](https://arxiv.org/abs/2405.21060) |
| **RWKV** (Peng et al., 2023) | "Reinventing RNNs for the Transformer Era." Recurrent architecture achieving Transformer-level performance with O(n) complexity and constant memory during inference. Open-source (14B+ parameters). | [Paper](https://arxiv.org/abs/2305.13048), [GitHub](https://github.com/BlinkDL/RWKV-LM) |
| **Jamba** (AI21 Labs, 2024) | Production hybrid: interleaves Mamba layers with Transformer attention layers plus MoE. 256K context, fits on a single 80GB GPU despite 52B total parameters. Proves hybrid architectures work at scale. | [Paper](https://arxiv.org/abs/2403.19887) |
| **xLSTM** (Hochreiter et al., 2024) | Extended Long Short-Term Memory from the original LSTM inventor. Exponential gating and matrix memory enable competitive performance with Transformers and SSMs. | [Paper](https://arxiv.org/abs/2405.04517) |

#### Neuromorphic Computing

> Brain-inspired hardware that uses spiking neural networks and event-driven processing. Neuromorphic chips consume 100-1000x less energy than GPUs for certain AI tasks -- potentially solving the energy constraint identified in the [Key Metrics](#state-of-the-field-key-metrics-2025-2026) table.

| Platform | Description | Links |
|----------|-------------|-------|
| **Intel Loihi 2** | Intel's neuromorphic research chip with 1M neurons and 120M synapses per chip. Programmable spiking neural networks with on-chip learning. Lava open-source framework for neuromorphic development. | [intel.com/loihi](https://www.intel.com/content/www/us/en/research/neuromorphic-computing.html), [Lava](https://github.com/lava-nc/lava) |
| **BrainChip Akida** | Commercial neuromorphic processor for edge AI. Event-based processing consuming <1W. Deployed in industrial and automotive applications. One of the few neuromorphic chips available for commercial use. | [brainchip.com](https://brainchip.com/) |
| **SpiNNaker 2** (University of Manchester) | Million-core neuromorphic supercomputer designed to simulate a billion neurons in real-time. Built for computational neuroscience and brain-scale neural network simulation. | [spinnaker.io](https://spinnakermanchester.io/) |

#### Decentralized AI Compute

> If AGI requires 10^28+ FLOP training runs, centralized infrastructure may not scale fast enough. Decentralized networks distribute training and inference across the globe, potentially democratizing access to AGI-scale compute.

| Network | Description | Links |
|---------|-------------|-------|
| **Together AI** | Decentralized cloud for running and training open-source AI. Together Inference Engine delivers high-throughput serving; Together GPU Cluster enables distributed training across geographies. | [together.ai](https://www.together.ai/) |
| **Gensyn** | Decentralized ML compute protocol. Verification layer ensures honest compute via probabilistic proofs -- solving the trust problem in distributed training. Backed by a16z. | [gensyn.ai](https://www.gensyn.ai/) |
| **Bittensor** | Decentralized AI network with TAO token incentives. Miners contribute ML compute (training, inference); validators ensure quality. 32+ specialized subnets for different AI tasks. | [bittensor.com](https://bittensor.com/), [GitHub](https://github.com/opentensor/bittensor) |
| **Prime Intellect** | Decentralized training infrastructure for frontier models. INTELLECT-2 demonstrated training a 32B-parameter model across globally distributed GPUs. Open-source. | [primeintellect.ai](https://www.primeintellect.ai/) |

### Recursive Self-Improvement & the Path to ASI

> The core mechanism theorized to trigger an **intelligence explosion**: an AI system that can improve its own design, creating a more capable version that improves itself further, in a feedback loop surpassing human intelligence. This is the bridge from AGI to ASI -- and the most critical unsolved problem in AI safety.

**Why this matters:** If a system achieves even modest self-improvement capability, the gap between AGI and ASI may close in weeks or months rather than decades. Understanding and controlling this process is the central challenge of AI alignment.

| Concept / Paper | Description | Links |
|-----------------|-------------|-------|
| **Intelligence Explosion (I.J. Good, 1965)** | The original formulation: "an ultraintelligent machine could design even better machines; there would then unquestionably be an 'intelligence explosion.'" | [Paper](https://exhibits.stanford.edu/feigenbaum/catalog/gz033kf2254) |
| **Weak-to-Strong Generalization** (Burns et al., OpenAI, 2023) | GPT-2 supervising GPT-4 as a proxy for "human supervising superintelligence." Shows weaker models can elicit most of the stronger model's capabilities -- a key mechanism for scalable oversight. | [Paper](https://arxiv.org/abs/2312.09390) |
| **Self-Rewarding Language Models** (Yuan et al., Meta, 2024) | Models generate and evaluate their own preference data for iterative self-improvement via LLM-as-a-Judge, creating a self-improvement loop without human feedback. | [Paper](https://arxiv.org/abs/2401.10020) |
| **The AI Scientist** (Sakana AI, 2024) | Fully autonomous research pipeline -- idea generation, experiment design, execution, and paper writing. A prototype for AI systems that accelerate their own research. | [Paper](https://arxiv.org/abs/2408.06292) |
| **Constitutional AI** (Bai et al., Anthropic, 2022) | AI-generated critiques from a set of principles (a "constitution") used to train AI without human feedback at each step -- a form of automated alignment that scales with model capability. | [Paper](https://arxiv.org/abs/2212.08073) |
| **Scalable Oversight via Debate** (Irving et al., 2018) | Two AI agents debate each other while a human judge adjudicates, allowing oversight of superhuman AI through adversarial decomposition. | [Paper](https://arxiv.org/abs/1805.00899) |
| **Iterated Distillation and Amplification (IDA)** (Christiano, 2018) | Bootstrapping alignment: a slow but safe AI is "amplified" to solve harder problems, then "distilled" into a faster model, iteratively approaching superintelligent capability while maintaining alignment. | [Blog](https://ai-alignment.com/iterated-distillation-and-amplification-157debfd1616) |
| **Reward Hacking & Specification Gaming** | Comprehensive collection of examples where AI systems find unintended shortcuts -- a critical failure mode when self-improving systems optimize misspecified objectives. | [Collection](https://deepmind.google/discover/blog/specification-gaming-the-flip-side-of-ai-ingenuity/), [GitHub](https://github.com/deepmind/specification_gaming) |

---

## Frameworks and Platforms

> The infrastructure powering the next generation of autonomous AI. These frameworks let you build, orchestrate, and deploy AI agents that can reason, browse, code, and collaborate -- from single-agent tools to multi-agent orchestration platforms.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=flat-square&logo=typescript&logoColor=white) ![Rust](https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white) ![Multi-Agent](https://img.shields.io/badge/Multi--Agent-blue?style=flat-square) ![Browser](https://img.shields.io/badge/Browser_Automation-orange?style=flat-square) ![Open Source](https://img.shields.io/badge/Open_Source-green?style=flat-square)

### Next-Generation Agent Frameworks (2025-2026)

|Name|Github Stars|Introduction| Notes |
|-|-|-|-|
|[OpenHands](https://github.com/All-Hands-AI/OpenHands)|![GitHub Repo stars](https://badgen.net/github/stars/All-Hands-AI/OpenHands)|AI-powered software development agent platform (formerly OpenDevin). Autonomous coding agent that can write, test, and debug code end-to-end.|71k+ stars. #1 on SWE-bench. Sandboxed execution environment.|
|[browser-use](https://github.com/browser-use/browser-use)|![GitHub Repo stars](https://badgen.net/github/stars/browser-use/browser-use)|Make websites accessible for AI agents. Automate tasks online with ease using Playwright-based browser automation.|87k+ stars. AI agents that browse the web autonomously.|
|[DeerFlow](https://github.com/bytedance/deer-flow)|![GitHub Repo stars](https://badgen.net/github/stars/bytedance/deer-flow)|ByteDance's open-source long-horizon SuperAgent harness that researches, codes, and creates. Multi-agent with sandboxes, memories, tools, and skills.|60k+ stars. Built on LangGraph.|
|[Firecrawl](https://github.com/firecrawl/firecrawl)|![GitHub Repo stars](https://badgen.net/github/stars/firecrawl/firecrawl)|The Web Data API for AI - Power AI agents with clean web data. Scrapes and converts websites to LLM-ready markdown.|108k+ stars. Used by major AI agent frameworks.|
|[crewAI](https://github.com/joaomdmoura/crewAI)|![GitHub Repo stars](https://badgen.net/github/stars/joaomdmoura/crewAI)|Framework for orchestrating role-playing, autonomous AI agents. Craft collaborative AI crews for complex tasks.|Production-grade multi-agent orchestration.|
|[agenticSeek](https://github.com/Fosowl/agenticSeek)|![GitHub Repo stars](https://badgen.net/github/stars/Fosowl/agenticSeek)|Fully local autonomous agent - No APIs, no monthly bills. Thinks, browses the web, and codes using only local LLMs.|26k+ stars. Fully local, privacy-first.|
|[Gemini CLI](https://github.com/google-gemini/gemini-cli)|![GitHub Repo stars](https://badgen.net/github/stars/google-gemini/gemini-cli)|Google's open-source AI agent that brings Gemini directly into your terminal. MCP support built-in.|101k+ stars. Official Google agent.|
|[Hermes Agent](https://github.com/NousResearch/hermes-agent)|![GitHub Repo stars](https://badgen.net/github/stars/NousResearch/hermes-agent)|The agent that grows with you. By Nous Research - multi-model AI agent with Claude, GPT, and open-source model support.|66k+ stars. From Nous Research.|
|[Daytona](https://github.com/daytonaio/daytona)|![GitHub Repo stars](https://badgen.net/github/stars/daytonaio/daytona)|Secure and elastic infrastructure for running AI-generated code. Sandboxed execution environment for AI agents.|72k+ stars. Secure code execution.|
|[Composio](https://github.com/ComposioHQ/composio)|![GitHub Repo stars](https://badgen.net/github/stars/ComposioHQ/composio)|Production-ready toolset for AI agents. 250+ tools, frameworks, and integrations for building agentic AI applications.|[composio.dev](https://composio.dev/)|
|[PentAGI](https://github.com/vxcontrol/pentagi)|![GitHub Repo stars](https://badgen.net/github/stars/vxcontrol/pentagi)|Fully autonomous AI agent system for complex penetration testing tasks. Multi-agent security automation.|15k+ stars. Autonomous security testing.|

### Established Agent Frameworks

|Name|Github Stars|Introduction| Notes |
|-|-|-|-|
|[Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT)|![GitHub Repo stars](https://badgen.net/github/stars/Significant-Gravitas/Auto-GPT)|The original autonomous AI agent. Now evolved into a full platform for building and deploying autonomous agents.|183k+ stars. The project that started the autonomous agent movement.|
|[MetaGPT](https://github.com/geekan/MetaGPT)|![GitHub Repo stars](https://badgen.net/github/stars/geekan/MetaGPT)|The Multi-Agent Framework: Given one line Requirement, return PRD, Design, Tasks, Repo.|Mimics a software company with PM, architect, and engineer agent roles.|
|[AgentGPT](https://github.com/reworkd/AgentGPT)|![GitHub Repo stars](https://badgen.net/github/stars/reworkd/AgentGPT)|Assemble, configure, and deploy autonomous AI Agents in your browser.|36k+ stars. Browser-based agent deployment.|
|[SuperAGI](https://github.com/TransformerOptimus/SuperAGI)|![GitHub Repo stars](https://badgen.net/github/stars/TransformerOptimus/SuperAGI)|Dev-first open source autonomous AI agent framework. Run concurrent agents with tools, GUI, multiple vector DBs, performance telemetry, and agent memory.|Toolkits: Email, Jira, GitHub, Google Search, DALL-E, Notion, etc.|
|[AutoGen](https://github.com/microsoft/autogen)|![GitHub Repo stars](https://badgen.net/github/stars/microsoft/autogen)|Microsoft's framework for multi-agent conversation. Agents converse with each other to solve tasks with human-in-the-loop support.|Now evolved into AG2 with enhanced multi-agent patterns.|
|[ChatDev](https://github.com/OpenBMB/ChatDev)|![GitHub Repo stars](https://badgen.net/github/stars/OpenBMB/ChatDev)|A virtual software company with multiple agents (CEO, CTO, programmer, tester) collaborating to design, code, test, and document software.|-|
|[CAMEL](https://github.com/camel-ai/camel)|![GitHub Repo stars](https://badgen.net/github/stars/camel-ai/camel)|Communicative Agents for "Mind" Exploration of Large Language Model Society. Role-playing framework for multi-agent collaboration.|[camel-ai.org](https://www.camel-ai.org/)|
|[XAgent](https://github.com/OpenBMB/XAgent)|![GitHub Repo stars](https://badgen.net/github/stars/OpenBMB/XAgent)|An autonomous LLM-based agent for complex task solving.|[x-agent.net](https://x-agent.net/)|
|[JARVIS / HuggingGPT](https://github.com/microsoft/JARVIS)|![GitHub Repo stars](https://badgen.net/github/stars/microsoft/JARVIS)|Uses ChatGPT as a controller to manage AI models on HuggingFace for task planning, model selection, and execution.|-|
|[babyagi](https://github.com/yoheinakajima/babyagi)|![GitHub Repo stars](https://badgen.net/github/stars/yoheinakajima/babyagi)|Task-driven autonomous agent using OpenAI and vector DBs to create, prioritize, and execute tasks.|-|
|[OpenAGI](https://github.com/agiresearch/OpenAGI)|![GitHub Repo stars](https://badgen.net/github/stars/agiresearch/OpenAGI)|Open-source AGI research platform combining LLMs with domain expert models via RLTF.|-|

### Specialized & Utility Frameworks

|Name|Github Stars|Introduction| Notes |
|-|-|-|-|
|[ShortGPT](https://github.com/RayVentura/ShortGPT)|![GitHub Repo stars](https://badgen.net/github/stars/RayVentura/ShortGPT)|Framework for automating video creation, voiceover, editing, and publishing using LLMs.|-|
|[gpt-engineer](https://github.com/AntonOsika/gpt-engineer)|![GitHub Repo stars](https://badgen.net/github/stars/AntonOsika/gpt-engineer)|Specify what you want it to build, the AI asks for clarification, and then builds it.|-|
|[FastGPT](https://github.com/labring/FastGPT)|![GitHub Repo stars](https://badgen.net/github/stars/labring/FastGPT)|Knowledge-based QA system built on LLMs with out-of-the-box data processing and workflow orchestration.|-|
|[big-agi](https://github.com/enricoros/big-agi)|![GitHub Repo stars](https://badgen.net/github/stars/enricoros/big-agi)|AI suite with AI personas, AGI functions, multi-model chat, text-to-image, voice, code execution. Deploy on-prem or cloud.|[big-agi.com](https://big-agi.com/)|
|[opencog](https://github.com/opencog/opencog)|![GitHub Repo stars](https://badgen.net/github/stars/opencog/opencog)|A framework for integrated Artificial Intelligence & Artificial General Intelligence (AGI).|-|
|[smol-ai/developer](https://github.com/smol-ai/developer)|![GitHub Repo stars](https://badgen.net/github/stars/smol-ai/developer)|The first library to let you embed a developer agent in your own app!|-|
|[loopgpt](https://github.com/farizrahman4u/loopgpt)|![GitHub Repo stars](https://badgen.net/github/stars/farizrahman4u/loopgpt)|Modular Auto-GPT Framework. Improved GPT-3.5 support, lower API token cost.|-|
|[LocalAGI](https://github.com/EmbraceAGI/LocalAGI)|![GitHub Repo stars](https://badgen.net/github/stars/EmbraceAGI/LocalAGI)|Locally run AGI powered by LLaMA, ChatGLM and more.|-|
|[DemoGPT](https://github.com/melih-unsal/DemoGPT)|![GitHub Repo stars](https://badgen.net/github/stars/melih-unsal/DemoGPT)|Create quick demos by just using prompts.|-|

---

## Agents

> Autonomous AI systems that perceive, reason, and act in the world. These agents represent the closest things we have to AGI-like behavior in narrow domains -- writing code, conducting research, operating computers, and navigating virtual worlds.

![Coding](https://img.shields.io/badge/Coding-green?style=flat-square) ![Research](https://img.shields.io/badge/Research-purple?style=flat-square) ![Computer Use](https://img.shields.io/badge/Computer_Use-blue?style=flat-square) ![Embodied](https://img.shields.io/badge/Embodied-red?style=flat-square) ![Autonomous](https://img.shields.io/badge/Autonomous-orange?style=flat-square)

### Coding & Software Engineering Agents

|Name|Github Stars|Introduction| Notes |
|-|-|-|-|
|[Aider](https://github.com/Aider-AI/aider)|![GitHub Repo stars](https://badgen.net/github/stars/Aider-AI/aider)|AI pair programming in your terminal. Edit code across your entire repo with LLMs. Tops SWE-bench Lite.|Best-in-class AI pair programmer. Works with GPT-4o, Claude, DeepSeek, local models.|
|[SWE-agent](https://github.com/princeton-nlp/SWE-agent)|![GitHub Repo stars](https://badgen.net/github/stars/princeton-nlp/SWE-agent)|Turns LLMs into software engineering agents that fix real GitHub issues. Pioneered the Agent-Computer Interface (ACI) concept.|[Paper](https://arxiv.org/abs/2405.15232). Princeton NLP. Key SWE-bench benchmark agent.|
|[goose](https://github.com/block/goose)|![GitHub Repo stars](https://badgen.net/github/stars/block/goose)|Open-source extensible AI agent that goes beyond code suggestions — install, execute, edit, and test with any LLM. Written in Rust.|Supports MCP and ACP protocols. By Block.|
|[Open Interpreter](https://github.com/OpenInterpreter/open-interpreter)|![GitHub Repo stars](https://badgen.net/github/stars/OpenInterpreter/open-interpreter)|A natural language interface for computers. Lets LLMs run code (Python, JS, shell) locally with no restrictions.|Full computer control via natural language. Like ChatGPT Code Interpreter but unrestricted.|

### Research & Knowledge Agents

|Name|Github Stars|Introduction| Notes |
|-|-|-|-|
|[STORM](https://github.com/stanford-oval/storm)|![GitHub Repo stars](https://badgen.net/github/stars/stanford-oval/storm)|Stanford: Synthesis of Topic Outlines through Retrieval and Multi-perspective Question Asking. Writes Wikipedia-quality long-form articles autonomously.|[Paper](https://arxiv.org/abs/2402.14207). Expert-level knowledge synthesis agent.|
|[AI Scientist](https://github.com/SakanaAI/AI-Scientist)|![GitHub Repo stars](https://badgen.net/github/stars/SakanaAI/AI-Scientist)|Fully autonomous scientific research pipeline: generates ideas, implements experiments, writes and reviews full academic papers.|[Paper](https://arxiv.org/abs/2408.06292). By Sakana AI. ASI-threshold capability.|
|[gpt-researcher](https://github.com/assafelovic/gpt-researcher)|![GitHub Repo stars](https://badgen.net/github/stars/assafelovic/gpt-researcher)|GPT-based autonomous agent for comprehensive online research on any topic. Searches, reads, and synthesizes long-form reports.|-|
|[mem0](https://github.com/mem0ai/mem0)|![GitHub Repo stars](https://badgen.net/github/stars/mem0ai/mem0)|Universal memory layer for AI agents. Persistent long-term, episodic, and semantic memory across agent sessions.|52k+ stars. Key missing component between current agents and AGI.|

### Computer-Use & Desktop Agents

|Name|Github Stars|Introduction| Notes |
|-|-|-|-|
|[everything-claude-code](https://github.com/anthropics/claude-code)|![GitHub Repo stars](https://badgen.net/github/stars/anthropics/claude-code)|Agent harness performance optimization system with skills, instincts, memory, and security for AI coding agents.|Cognitive scaffolding for agentic AI — directly relevant to persistent AGI.|
|[nanobot](https://github.com/HKUDS/nanobot)|![GitHub Repo stars](https://badgen.net/github/stars/HKUDS/nanobot)|Ultra-lightweight personal AI agent. Minimal footprint with full agent capabilities.|39k+ stars. Edge-AGI and ubiquitous deployment.|
|[Screenpipe](https://github.com/screenpipe/screenpipe)|![GitHub Repo stars](https://badgen.net/github/stars/screenpipe/screenpipe)|Run agents that work for you based on what you do. Continuously observes your screen, builds personal memory, and triggers AI actions.|Always-on environmental awareness — a prototype AGI assistant.|

### Embodied & Simulation Agents

|Name|Github Stars|Introduction| Notes |
|-|-|-|-|
|[generative_agents](https://github.com/joonspk-research/generative_agents)|![GitHub Repo stars](https://badgen.net/github/stars/joonspk-research/generative_agents)|Generative Agents: Interactive Simulacra of Human Behavior. 25 AI agents in a simulated town with unique identities, memories, and behaviors.|[Paper](https://arxiv.org/abs/2304.03442). Stanford & Google. Emergent social cognition.|
|[Voyager](https://github.com/MineDojo/Voyager)|![GitHub Repo stars](https://badgen.net/github/stars/MineDojo/Voyager)|Open-Ended Embodied Agent with LLMs. Plays Minecraft autonomously, continuously discovers new skills via a self-growing code library.|[Paper](https://arxiv.org/abs/2305.16291). NVIDIA/CMU. Lifelong skill acquisition.|
|[RoboGen](https://github.com/Genesis-Embodied-AI/RoboGen)|![GitHub Repo stars](https://badgen.net/github/stars/Genesis-Embodied-AI/RoboGen)|Generative simulation for automated robot learning. Auto-generates tasks, environments, and training data using GPT-4.|[Paper](https://arxiv.org/abs/2311.01455). Self-improving robot curriculum.|
|[ai-town](https://github.com/a16z-infra/ai-town)|![GitHub Repo stars](https://badgen.net/github/stars/a16z-infra/ai-town)|Deployable starter kit for building AI town — a virtual town where AI characters live, chat, and socialize. By a16z.|-|

### Enterprise & Agentic AI Platforms

> AI agents moving from demos to enterprise production. These platforms enable organizations to deploy autonomous agents into real workflows at scale.

|Name|Introduction| Notes |
|-|-|-|
|[Salesforce Agentforce](https://www.salesforce.com/agentforce/)|Enterprise AI agent platform integrated into Salesforce CRM. Autonomous agents handle sales, service, marketing, and commerce workflows.|Largest enterprise AI agent deployment. Announced 2024.|
|[Microsoft Copilot Studio](https://www.microsoft.com/en-us/microsoft-copilot/microsoft-copilot-studio)|Low-code platform for building and deploying custom AI agents and copilots across Microsoft 365 and Azure.|Powers enterprise-wide agentic automation.|
|[Zapier AI Agents](https://zapier.com/agents)|No-code AI agents that automate cross-app workflows. Connects 7,000+ apps with autonomous decision-making and action.|Enterprise workflow automation at scale.|

---

## Physical AI & Embodied Intelligence

> AGI cannot exist only in text -- it must understand and act in the physical world. **Physical AI** bridges foundation models with embodiment: humanoid robots, manipulation, navigation, and physics simulation. Moravec's Paradox -- sensorimotor skills are harder than abstract reasoning -- remains one of the deepest unsolved AGI challenges.

![Robotics](https://img.shields.io/badge/Robotics-Humanoid-red?style=flat-square) ![VLA](https://img.shields.io/badge/VLA-Vision--Language--Action-blue?style=flat-square) ![Simulation](https://img.shields.io/badge/Simulation-Isaac_MuJoCo-green?style=flat-square) ![Embodied](https://img.shields.io/badge/Embodied_AI-Physical_Intelligence-purple?style=flat-square)

### Humanoid Robotics & AGI Hardware

> The race to build general-purpose humanoid robots capable of operating in unstructured human environments. These platforms are the physical embodiment layer for AGI.

| Company | Description | Links |
|---------|-------------|-------|
| **Figure AI** | Humanoid robots with advanced AI. Partnered with OpenAI and Microsoft for embodied AI. Figure 02 demonstrates autonomous manipulation, language-guided task execution, and learning from human feedback. Raised $2.6B+. | [figure.ai](https://www.figure.ai/) |
| **Tesla Optimus** | General-purpose humanoid robot leveraging Tesla's massive autonomous driving AI stack (FSD neural nets, Dojo supercomputer). Targeting manufacturing and consumer deployment at scale. | [tesla.com](https://www.tesla.com/) |
| **Boston Dynamics** | Pioneers of advanced locomotion. Atlas (humanoid) and Spot (quadruped) set the standard for physical capability, agility, and dexterity. Now Hyundai-owned, pivoting to AI-first control. | [bostondynamics.com](https://www.bostondynamics.com/) |
| **1X Technologies** | NEO humanoid robot with human-like form factor. Backed by OpenAI. Focused on safe, embodied AI for real-world deployment in homes and workplaces. | [1x.tech](https://www.1x.tech/) |
| **Unitree Robotics** | Democratizing humanoid robotics with affordable platforms (G1, H1 series). Enables broad research access to embodied AI experimentation. | [unitree.com](https://www.unitree.com/) |
| **Sanctuary AI** | Phoenix humanoid robot powered by "Carbon" -- a proprietary AI system designed for general-purpose task learning and autonomous execution. | [sanctuary.ai](https://www.sanctuary.ai/) |
| **Agility Robotics** | Digit bipedal robot designed for logistics and warehouse automation. Real-world deployment partner with Amazon. | [agilityrobotics.com](https://www.agilityrobotics.com/) |
| **Apptronik** | Apollo full-size humanoid robot for industrial applications. Emphasis on safe human-robot collaboration. Mercedes-Benz partnership. | [apptronik.com](https://www.apptronik.com/) |

### Robot Foundation Models (Vision-Language-Action)

> The frontier of embodied AI research: models that take visual observations and language commands as input and directly output robot motor actions. VLA models represent the convergence of foundation models and physical intelligence.

| Model | Org | Year | Description | Links |
|-------|-----|------|-------------|-------|
| **Gemini Robotics 1.5** | Google DeepMind | 2025 | Agentic VLA model that turns visual information and language instructions into motor commands. Generality across novel situations, dexterity (origami, food prep), agentic tool-use, and thinking before acting. Supports multiple embodiments (ALOHA, Franka, Apptronik Apollo). Dual approach with Robotics-ER 1.5 for embodied reasoning. | [Site](https://deepmind.google/models/gemini-robotics/), [Report](https://deepmind.google/models/gemini-robotics/gemini-robotics/) |
| **pi0** | Physical Intelligence | 2024 | VLA flow model for general robot control. Novel flow matching architecture on top of pre-trained VLM. Trained on diverse dexterous tasks (laundry folding, table cleaning, box assembly) across single-arm, dual-arm, and mobile manipulators. Open-sourced weights. | [Paper](https://arxiv.org/abs/2410.24164), [Site](https://www.physicalintelligence.company/) |
| **RT-2** | Google DeepMind | 2023 | Vision-Language-Action model that transfers web-scale knowledge to robotic control. Expresses actions as text tokens, enabling emergent reasoning (pick up the "improvised hammer" -> picks rock). 6k evaluation trials. | [Paper](https://arxiv.org/abs/2307.15818) |
| **PaLM-E** | Google | 2023 | 562B-parameter embodied multimodal language model. Directly incorporates continuous sensor modalities into LLMs. Positive transfer across internet-scale language, vision, and robotics domains. | [Paper](https://arxiv.org/abs/2303.03378) |
| **Open X-Embodiment / RT-X** | 21 Institutions | 2023 | Largest robotics dataset: 22 robots, 527 skills, 160k+ tasks from 21 institutions. RT-X model shows positive transfer across robot morphologies. The "ImageNet moment" for robotics. | [Paper](https://arxiv.org/abs/2310.08864) |
| **OpenVLA** | Stanford / UC Berkeley | 2024 | Open-source 7B-parameter VLA. Democratizes embodied AI research -- matches proprietary models on manipulation benchmarks. Fine-tunable for new robots and tasks. | [GitHub](https://github.com/openvla/openvla) |
| **NVIDIA GR00T** | NVIDIA | 2024 | Foundation model for humanoid robots. Multimodal inputs (text, video, demonstration) to robot actions. Part of NVIDIA's Physical AI platform alongside Isaac and Cosmos. | [nvidia.com](https://developer.nvidia.com/isaac) |

### Simulation & Infrastructure for Physical AI

> Training embodied AI requires massive simulation before real-world deployment. These platforms enable sim-to-real transfer, digital twins, and scalable robot learning.

| Platform | Description | Links |
|----------|-------------|-------|
| **NVIDIA Isaac Sim / Isaac Lab** | Production-grade robotics simulation platform with photorealistic rendering, physics accuracy, and domain randomization. Isaac Lab provides GPU-accelerated RL environments for robot learning at scale. | [Developer](https://developer.nvidia.com/isaac/), [GitHub](https://github.com/isaac-sim/) |
| **NVIDIA Omniverse** | Collaborative 3D simulation platform for building digital twins and physics-based robotics simulation. Foundation for NVIDIA's Physical AI ecosystem. | [nvidia.com/omniverse](https://www.nvidia.com/en-us/omniverse/) |
| **MuJoCo** | Google DeepMind's open-source physics engine optimized for robotics and biomechanics. Fast, accurate contact dynamics. The standard tool for embodied AI research and RL benchmarking. | [mujoco.org](https://mujoco.org/), [GitHub](https://github.com/google-deepmind/mujoco) |
| **Genesis** | Next-generation open-source physics engine for embodied AI. Differentiable simulation enabling gradient-based learning for physical systems. | [GitHub](https://github.com/Genesis-Embodied-AI/Genesis) |

---

## Paper-to-Code Automation

> The leap from research paper to working implementation is one of the biggest bottlenecks in AI progress. These tools automate the translation of academic papers into production-ready code repositories -- accelerating the research-to-engineering pipeline and democratizing access to frontier techniques.

![Automation](https://img.shields.io/badge/Automation-Paper→Code-blue?style=flat-square) ![Research](https://img.shields.io/badge/Research-Implementation-green?style=flat-square) ![Agentic](https://img.shields.io/badge/Agentic-Multi--Step-purple?style=flat-square)

| Tool | Description | Links |
|------|-------------|-------|
| [Research2Repo](https://github.com/nellaivijay/Research2Repo) | Multi-model agentic framework that converts ML research papers (PDFs) into production-ready GitHub repos. 4-stage decomposed planning, per-file analysis, self-refine loops, Docker sandbox with auto-debugging (19+ error types), CodeRAG for reference mining, and full DevOps generation (Dockerfile, CI, Makefile). Supports Gemini (2M context), GPT-4o/o3, Claude, and Ollama. | [GitHub](https://github.com/nellaivijay/Research2Repo) |
| [PaperCoder (Paper2Code)](https://github.com/going-doer/Paper2Code) | The pioneering paper-to-code system. Converts research papers into code repositories using a 3-stage pipeline (planning, analysis, generation). GPT-4o-based. Inspired Research2Repo and the broader paper-to-code movement. | [Paper](https://arxiv.org/abs/2504.17192), [GitHub](https://github.com/going-doer/Paper2Code) |
| [The AI Scientist](https://github.com/SakanaAI/AI-Scientist) | Goes beyond code generation: fully autonomous research pipeline that generates ideas, designs experiments, implements code, runs experiments, and writes complete academic papers. A prototype for self-improving AI research. | [Paper](https://arxiv.org/abs/2408.06292), [GitHub](https://github.com/SakanaAI/AI-Scientist) |
| [Papers with Code](https://paperswithcode.com/) | The standard platform linking 150,000+ ML papers to their official implementations, benchmarks, and leaderboards. Not an automation tool -- a curation platform that serves as the reference layer for the entire research-to-code ecosystem. | [paperswithcode.com](https://paperswithcode.com/) |
| [STORM](https://github.com/stanford-oval/storm) | Stanford's autonomous system that writes Wikipedia-quality long-form articles by researching a topic from scratch. Demonstrates AI's ability to synthesize research into structured knowledge. | [Paper](https://arxiv.org/abs/2402.14207), [GitHub](https://github.com/stanford-oval/storm) |

---

## LLM Application Frameworks

> The developer toolkits for building production LLM applications. From orchestration chains to observability platforms, these frameworks are the backbone of every AI product shipping today.

![LangChain](https://img.shields.io/badge/LangChain-Orchestration-1C3C3C?style=flat-square) ![LlamaIndex](https://img.shields.io/badge/LlamaIndex-RAG-purple?style=flat-square) ![Observability](https://img.shields.io/badge/Observability-Tracing_&_Evals-blue?style=flat-square) ![Structured Output](https://img.shields.io/badge/Structured_Output-Pydantic-green?style=flat-square)

### Core Orchestration Frameworks

| Name | Description | Links |
|------|-------------|-------|
| [LangChain](https://github.com/langchain-ai/langchain) | The agent engineering platform. Framework for developing applications powered by LLMs with chaining, tools, memory, and retrieval. 133k+ stars. | [Docs](https://python.langchain.com/docs/) |
| [LangGraph](https://github.com/langchain-ai/langgraph) | Graph-based framework for building stateful, multi-actor LLM agents as directed graphs. Supports cycles, branching, persistent state, and human-in-the-loop. | [Docs](https://langchain-ai.github.io/langgraph/) |
| [LlamaIndex](https://github.com/run-llama/llama_index) | Leading document agent and RAG platform. Connect custom data sources to LLMs with indexing, retrieval, and query interfaces. 48k+ stars. | [Docs](https://docs.llamaindex.ai/) |
| [DSPy](https://github.com/stanfordnlp/dspy) | Stanford's paradigm-shifting framework for *programming* (not prompting) LLMs. Declarative modules with automatic prompt optimization. 20k+ stars. | [Paper](https://arxiv.org/abs/2310.03714), [dspy.ai](https://dspy.ai) |
| [Haystack](https://github.com/deepset-ai/haystack) | Production-grade NLP/LLM framework for RAG pipelines, QA, and conversational AI. Composable pipeline architecture with 60+ integrations. | [Docs](https://docs.haystack.deepset.ai) |
| [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | Microsoft's enterprise SDK for LLM integration. Plugin/skill architecture powering Microsoft Copilot. Python, C#, Java. 23k+ stars. | [Docs](https://learn.microsoft.com/en-us/semantic-kernel/) |
| [smolagents](https://github.com/huggingface/smolagents) | HuggingFace's minimalist agent library. Code-first agents that write and execute Python. ~1000 lines core. 14k+ stars. | [Docs](https://huggingface.co/docs/smolagents) |
| [PydanticAI](https://github.com/pydantic/pydantic-ai) | Agent framework with type safety, structured outputs via Pydantic, and dependency injection for testing. Async-first. | [Docs](https://ai.pydantic.dev) |
| [Agno](https://github.com/agno-agi/agno) | Full-stack agent framework (formerly Phidata). Lightning-fast runtime, multimodal agents, native teams, 100+ tools. 20k+ stars. | [Docs](https://docs.agno.com) |

### LLM Platforms & Developer Tools

| Name | Description | Links |
|------|-------------|-------|
| [Dify](https://github.com/langgenius/dify) | Open-source LLM app development platform with visual workflow orchestration, RAG, and agent framework. 137k+ stars. | [dify.ai](https://dify.ai/) |
| [Flowise](https://github.com/FlowiseAI/Flowise) | Drag-and-drop no-code builder for LLM apps and chatbots using visual node graphs. 52k+ stars. | [flowiseai.com](https://flowiseai.com/) |
| [Ollama](https://github.com/ollama/ollama) | The de-facto standard for running open-weight LLMs locally. Dead-simple CLI. OpenAI-compatible API. 110k+ stars. | [ollama.com](https://ollama.com/) |
| [Open WebUI](https://github.com/open-webui/open-webui) | User-friendly AI interface supporting Ollama, OpenAI API, and more. Self-hosted ChatGPT alternative. 131k+ stars. | [openwebui.com](https://openwebui.com/) |
| [Jan.ai](https://github.com/janhq/jan) | Open-source, privacy-first desktop AI assistant. Runs 100% offline on-device. OpenAI-compatible local API. 25k+ stars. | [jan.ai](https://jan.ai/) |
| [LiteLLM](https://github.com/BerriAI/litellm) | Unified API for 100+ LLMs using OpenAI SDK format. Proxy server with load balancing, cost tracking, and key management. | [Docs](https://docs.litellm.ai/) |

### Structured Output & Prompt Engineering Tools

| Name | Description | Links |
|------|-------------|-------|
| [Instructor](https://github.com/instructor-ai/instructor) | Get structured, typed outputs from LLMs using Pydantic models. Handles retries, validation, and streaming. 10k+ stars. | [Docs](https://python.useinstructor.com/) |
| [Outlines](https://github.com/dottxt-ai/outlines) | Structured text generation at the token level using FSM-guided decoding. Guarantees valid JSON/regex output. 11k+ stars. | [Docs](https://dottxt-ai.github.io/outlines/) |
| [guidance](https://github.com/guidance-ai/guidance) | Microsoft's language for constrained and structured LLM generation with token-level control. 20k+ stars. | [GitHub](https://github.com/guidance-ai/guidance) |

### LLM Observability & Evaluation

| Name | Description | Links |
|------|-------------|-------|
| [LangFuse](https://github.com/langfuse/langfuse) | Open-source LLM engineering platform. Tracing, prompt management, evals, metrics. Self-hostable. 8k+ stars. | [langfuse.com](https://langfuse.com/) |
| [Phoenix](https://github.com/Arize-ai/phoenix) | Open-source LLM observability with OpenTelemetry-native tracing, retrieval evaluation, and experiment comparison. By Arize. | [Docs](https://docs.arize.com/phoenix/) |
| [Ragas](https://github.com/explodinggradients/ragas) | Leading RAG evaluation framework. Metrics: faithfulness, relevancy, precision, recall. Synthetic test set generation. 8k+ stars. | [Docs](https://docs.ragas.io/) |
| [LangSmith](https://www.langchain.com/langsmith) | LangChain's platform for debugging, testing, evaluating, and monitoring LLM chains and agents. | [Docs](https://docs.smith.langchain.com/) |
| [Opik](https://github.com/comet-ml/opik) | Open-source LLM observability and evaluation. Tracing, evaluation, and prompt optimization. | [Docs](https://www.comet.com/docs/opik/) |
| [Helicone](https://github.com/Helicone/helicone) | LLM observability via one-line proxy. Cost tracking, caching, rate limiting. | [helicone.ai](https://helicone.ai/) |

---

## RAG and Vector Databases

> RAG grounds LLMs in real-world data, eliminating hallucinations and enabling knowledge-intensive applications. Full RAG stack: vector storage, retrieval engines, graph RAG, document parsing, and embedding models.

![Vector DB](https://img.shields.io/badge/Vector_DB-Milvus_Qdrant_Chroma-blue?style=flat-square) ![Graph RAG](https://img.shields.io/badge/Graph_RAG-Knowledge_Graphs-purple?style=flat-square) ![Embeddings](https://img.shields.io/badge/Embeddings-OpenAI_Cohere_NVIDIA-green?style=flat-square) ![Document Parsing](https://img.shields.io/badge/Document_Parsing-PDF_OCR-orange?style=flat-square)

### Vector Databases

| Name | Description | Links |
|------|-------------|-------|
| [Milvus](https://github.com/milvus-io/milvus) | Cloud-native, distributed vector database for billion-scale similarity search. Most scalable open-source vector DB. 44k+ stars. | [milvus.io](https://milvus.io/) |
| [Qdrant](https://github.com/qdrant/qdrant) | High-performance vector search engine in Rust. Dense + sparse vectors, hybrid search, payload filtering, quantization. 30k+ stars. | [qdrant.tech](https://qdrant.tech/) |
| [Weaviate](https://github.com/weaviate/weaviate) | AI-native vector database with GraphQL API, built-in vectorization, hybrid search, and generative search modules. 16k+ stars. | [weaviate.io](https://weaviate.io/) |
| [Chroma](https://github.com/chroma-core/chroma) | AI-native open-source embedding database. Extremely easy to start, built-in embedding functions. 16k+ stars. | [trychroma.com](https://trychroma.com/) |
| [pgvector](https://github.com/pgvector/pgvector) | PostgreSQL extension for vector similarity search. HNSW + IVFFlat indexes. Game-changer for Postgres users. 14k+ stars. | [GitHub](https://github.com/pgvector/pgvector) |
| [LanceDB](https://github.com/lancedb/lancedb) | Serverless vector database built on Lance columnar format. Embedded, multimodal, full-text + vector hybrid search. | [lancedb.com](https://lancedb.com/) |
| [Meilisearch](https://github.com/meilisearch/meilisearch) | Lightning-fast search engine API with AI-powered hybrid search (full-text + vector). 57k+ stars. | [meilisearch.com](https://www.meilisearch.com/) |
| [Vespa](https://github.com/vespa-engine/vespa) | Yahoo's battle-tested big data serving engine. ANN + lexical hybrid, tensor expressions, complex ML ranking. | [vespa.ai](https://vespa.ai/) |
| [Pinecone](https://www.pinecone.io/) | Managed vector database for high-performance vector search at scale. | [Docs](https://docs.pinecone.io/) |
| [Zilliz](https://zilliz.com/) | Cloud-native vector database service (managed Milvus). | [zilliz.com](https://zilliz.com/) |
| [Turbopuffer](https://turbopuffer.com/) | Serverless vector database using object storage (S3) for cost-efficient large-scale search. | [Docs](https://turbopuffer.com/docs) |

### RAG Engines & Platforms

| Name | Description | Links |
|------|-------------|-------|
| [RAGFlow](https://github.com/infiniflow/ragflow) | Leading open-source RAG engine with vision-based document parsing (tables, figures, layouts). Multi-recall: vector + full-text + knowledge graph. 78k+ stars. | [ragflow.io](https://ragflow.io/) |
| [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm) | All-in-one AI app with RAG, agents, MCP support. Use any LLM, any document, any vector database. Privacy-first. 58k+ stars. | [useanything.com](https://useanything.com/) |
| [Kotaemon](https://github.com/Cinnamon/kotaemon) | Open-source RAG document QA tool with chat UI, graph RAG, multi-modal support, and citation highlighting. 22k+ stars. | [GitHub](https://github.com/Cinnamon/kotaemon) |
| [Pathway LLM App](https://github.com/pathwaycom/llm-app) | Ready-to-run cloud templates for RAG and AI pipelines with live data sync (Sharepoint, S3, Kafka, Postgres). 60k+ stars. | [pathway.com](https://pathway.com/) |
| [Cognee](https://github.com/topoteretes/cognee) | Memory management for AI agents and apps. Builds knowledge graphs from documents for reasoning-based RAG. 15k+ stars. | [cognee.ai](https://www.cognee.ai/) |
| [R2R (SciPhi)](https://github.com/SciPhi-AI/R2R) | Production RAG engine with hybrid search, knowledge graph building (Neo4j), ingestion pipelines, and REST API. | [Docs](https://r2r-docs.sciphi.ai/) |

### Graph RAG

| Name | Description | Links |
|------|-------------|-------|
| [Microsoft GraphRAG](https://github.com/microsoft/graphrag) | Landmark Graph-based RAG: extracts knowledge graphs from documents, performs global queries via community summaries. 32k+ stars. | [Paper](https://arxiv.org/abs/2404.16130), [Docs](https://microsoft.github.io/graphrag/) |
| [LightRAG](https://github.com/HKUDS/LightRAG) | Faster, simpler alternative to GraphRAG. Dual-level retrieval (entity + thematic) with incremental knowledge graph updates. 15k+ stars. | [GitHub](https://github.com/HKUDS/LightRAG) |
| [PageIndex](https://github.com/VectifyAI/PageIndex) | Document index for vectorless, reasoning-based RAG. Bypasses traditional embedding for reasoning-first retrieval. 25k+ stars. | [GitHub](https://github.com/VectifyAI/PageIndex) |
| [Neo4j GraphRAG](https://github.com/neo4j/neo4j-graphrag-python) | Official Neo4j library for GraphRAG pipelines. KG construction, hybrid retrieval (vector + Cypher). | [Docs](https://neo4j.com/docs/neo4j-graphrag-python/current/) |

### Document Parsing for RAG

| Name | Description | Links |
|------|-------------|-------|
| [Docling](https://github.com/DS4SD/docling) | IBM's fast document conversion: PDFs with layout understanding, table recognition (TableFormer), figure extraction. 20k+ stars. | [Docs](https://ds4sd.github.io/docling/) |
| [Unstructured](https://github.com/Unstructured-IO/unstructured) | Document parsing ETL for RAG. Extracts from PDFs, DOCX, HTML, images, and 30+ formats. 10k+ stars. | [unstructured.io](https://unstructured.io/) |
| [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | Turn any PDF or image into structured data for AI. Supports 100+ languages. 75k+ stars. | [GitHub](https://github.com/PaddlePaddle/PaddleOCR) |

### Advanced RAG Techniques

| Technique | Description | Links |
|-----------|-------------|-------|
| Self-RAG | LLMs that reflect on retrieval decisions using special tokens. Adaptive retrieval — only retrieve when needed. | [Paper](https://arxiv.org/abs/2310.11511), [Code](https://github.com/AkariAsai/self-rag) |
| CRAG (Corrective RAG) | Adds retrieval evaluator + correction mechanism. Falls back to web search if retrieved docs are irrelevant. | [Paper](https://arxiv.org/abs/2401.15884) |
| ColPali (Visual RAG) | Revolutionary: indexes documents as images using vision-language models, eliminating OCR failures entirely. | [Paper](https://arxiv.org/abs/2407.01449), [Code](https://github.com/illuin-tech/colpali) |
| HippoRAG | Neurobiologically-inspired RAG using knowledge graphs mimicking hippocampal memory for multi-hop reasoning. | [Code](https://github.com/OSU-NLP-Group/HippoRAG) |
| RAG Techniques Guide | Comprehensive tutorial repository showcasing 20+ advanced RAG techniques with notebooks. 27k+ stars. | [GitHub](https://github.com/NirDiamant/RAG_Techniques) |

### Embedding Models (2025-2026)

| Model | Provider | Key Notes | Links |
|-------|----------|-----------|-------|
| text-embedding-3-large | OpenAI | 3072 dims (Matryoshka), strong general performance. | [Docs](https://platform.openai.com/docs/guides/embeddings) |
| embed-v4.0 | Cohere | Multimodal (text+image), 128K context, 100+ languages. | [Docs](https://docs.cohere.com/docs/cohere-embed) |
| voyage-3 | Voyage AI | Top MTEB scores (esp. code/finance/law), 32K context. Anthropic-backed. | [Docs](https://docs.voyageai.com/) |
| NV-Embed-v2 | NVIDIA | #1 MTEB overall at release. Decoder-only LLM architecture. 4096 dims. | [HuggingFace](https://huggingface.co/nvidia/NV-Embed-v2) |
| nomic-embed-text-v1.5 | Nomic AI | Fully open (weights + data + code). Matryoshka dimensions. 8K context. | [HuggingFace](https://huggingface.co/nomic-ai/nomic-embed-text-v1.5) |
| jina-embeddings-v3 | Jina AI | Task-specific LoRA adapters, Matryoshka, multilingual. | [HuggingFace](https://huggingface.co/jinaai/jina-embeddings-v3) |
| bge-m3 | BAAI | Multilingual (100 langs), multi-functionality: dense + sparse + ColBERT. | [HuggingFace](https://huggingface.co/BAAI/bge-m3) |
| gte-Qwen2-7B-instruct | Alibaba | LLM-based embedding, top MTEB, instruction-tuned, 32K context. | [HuggingFace](https://huggingface.co/Alibaba-NLP/gte-Qwen2-7B-instruct) |

---

## Data Infrastructure for AI at Scale

> AGI systems are fundamentally bound by their data layers. Training frontier models requires petabyte-scale data pipelines, and deploying them requires infrastructure that can serve millions of requests with sub-second latency. The SRE and data engineering challenges behind superintelligence are as hard as the ML itself.

![Data](https://img.shields.io/badge/Data-Lakehouse-blue?style=flat-square) ![MLOps](https://img.shields.io/badge/MLOps-Experiment_Tracking-green?style=flat-square) ![Infrastructure](https://img.shields.io/badge/Infrastructure-Kubernetes-purple?style=flat-square) ![Scale](https://img.shields.io/badge/Scale-Petabyte-orange?style=flat-square)

### Data Lakehouse & Analytical Processing

| Name | Description | Links |
|------|-------------|-------|
| [Apache Iceberg](https://iceberg.apache.org/) | Open table format for massive analytic datasets. ACID transactions, time travel, schema evolution, and partition evolution on data lakes. The emerging standard for AI training data management (adopted by Netflix, Apple, Snowflake). V4 adds row-lineage tracking. | [iceberg.apache.org](https://iceberg.apache.org/), [GitHub](https://github.com/apache/iceberg) |
| [Apache Spark](https://spark.apache.org/) | Unified analytics engine for large-scale data processing. Powers the data pipelines behind most frontier model training -- ETL, feature engineering, and distributed data transformation at petabyte scale. | [spark.apache.org](https://spark.apache.org/), [GitHub](https://github.com/apache/spark) |
| [Delta Lake](https://delta.io/) | Open-source storage layer providing ACID transactions on data lakes. Originally Databricks; now open ecosystem. Delta UniForm provides interoperability with Iceberg and Hudi. | [delta.io](https://delta.io/), [GitHub](https://github.com/delta-io/delta) |
| [Greenplum](https://greenplum.org/) | Massively Parallel Processing (MPP) database for large-scale analytics and AI workloads. Open-source, PostgreSQL-based, purpose-built for analytical queries across petabytes. Used in enterprise AI pipelines for feature computation and data preparation. | [greenplum.org](https://greenplum.org/), [GitHub](https://github.com/greenplum-db/gpdb) |
| [DuckDB](https://duckdb.org/) | In-process analytical database that runs anywhere. Blazing-fast OLAP queries on local data. Increasingly used for dataset analysis, feature engineering, and rapid prototyping in ML workflows. | [duckdb.org](https://duckdb.org/), [GitHub](https://github.com/duckdb/duckdb) |

### MLOps & Experiment Tracking

| Name | Description | Links |
|------|-------------|-------|
| [MLflow](https://mlflow.org/) | Open-source platform for the complete ML lifecycle: experiment tracking, model registry, deployment, and model evaluation. The standard MLOps platform. 20k+ stars. | [mlflow.org](https://mlflow.org/), [GitHub](https://github.com/mlflow/mlflow) |
| [Weights & Biases (W&B)](https://wandb.ai/) | ML experiment tracking, dataset versioning, and model management. Used by OpenAI, DeepMind, and most frontier labs for training runs. | [wandb.ai](https://wandb.ai/) |
| [KubeFlow](https://www.kubeflow.org/) | ML toolkit for Kubernetes. Manages ML workflows: training pipelines, hyperparameter tuning, model serving, and notebook environments on Kubernetes clusters. | [kubeflow.org](https://www.kubeflow.org/), [GitHub](https://github.com/kubeflow/kubeflow) |
| [Ray](https://www.ray.io/) | Unified framework for scaling AI applications. Ray Train for distributed training, Ray Serve for inference, Ray Data for preprocessing. Powers Anyscale and used by OpenAI, Uber, and Spotify. | [ray.io](https://www.ray.io/), [GitHub](https://github.com/ray-project/ray) |
| [Feast](https://feast.dev/) | Open-source feature store for ML. Bridges the gap between training and serving by providing consistent access to feature data across offline training and online inference. | [feast.dev](https://feast.dev/), [GitHub](https://github.com/feast-dev/feast) |
| [Label Studio](https://labelstud.io/) | Open-source data labeling platform for text, image, audio, video, and multi-modal tasks. Critical infrastructure for creating the human-annotated data that drives RLHF and supervised fine-tuning. 20k+ stars. | [labelstud.io](https://labelstud.io/), [GitHub](https://github.com/HumanSignal/label-studio) |

---

## LLM Fine-Tuning Techniques

> Making foundation models your own. Fine-tuning adapts pre-trained LLMs to specific tasks, domains, or behaviors -- from lightweight LoRA adapters that train in hours on a single GPU to full alignment techniques like DPO that shape model values.

![LoRA](https://img.shields.io/badge/LoRA-Low--Rank_Adaptation-blue?style=flat-square) ![QLoRA](https://img.shields.io/badge/QLoRA-4--bit_Quantized-green?style=flat-square) ![PEFT](https://img.shields.io/badge/PEFT-Parameter_Efficient-purple?style=flat-square) ![DPO](https://img.shields.io/badge/DPO-Preference_Optimization-orange?style=flat-square) ![RLHF](https://img.shields.io/badge/RLHF-Human_Feedback-red?style=flat-square)

### LoRA and Variants

| Method | Description | Paper | Code |
|--------|-------------|-------|------|
| LoRA | Low-Rank Adaptation of Large Language Models. Adds trainable low-rank matrices to attention layers while freezing pretrained weights. Rank 4-16 is typically sufficient. | [Paper](https://arxiv.org/pdf/2106.09685.pdf) | [Code](https://github.com/microsoft/LoRA) |
| LoRA+ | Introduces different learning rates for matrices A and B (B gets 16x higher LR), yielding ~2% accuracy improvement and 2x faster training. | [Paper](https://arxiv.org/abs/2402.12354) | - |
| AdaLoRA | Adaptive budget allocation for LoRA - dynamically allocates parameter budget based on importance scoring via SVD parameterization. | [Paper](https://arxiv.org/abs/2303.10512) | [Code](https://github.com/QingruZhang/AdaLoRA) |
| QLoRA | Quantizes pretrained model to 4-bit, then adds trainable low-rank adapters. Uses 4-bit NormalFloat, double quantization, and paged optimizers. | [Paper](https://arxiv.org/abs/2305.14314) | [Code](https://github.com/artidoro/qlora) |
| DoRA | Weight-Decomposed Low-Rank Adaptation. Decomposes pretrained weights into magnitude and direction, then fine-tunes separately. By NVIDIA. | [Paper](https://arxiv.org/pdf/2402.09353.pdf) | [Code](https://github.com/catid/dora) |
| PiSSA | Principal Singular Values and Singular Vectors Adaptation. Modifies LoRA initialization using SVD for significantly better fine-tuning. | [Paper](https://arxiv.org/abs/2404.02948) | [Code](https://github.com/GraphPKU/PiSSA) |
| MOELoRA | Combines Mixture of Experts (MOE) with LoRA for multi-task parameter-efficient fine-tuning, especially for medical applications. | [Paper](https://arxiv.org/abs/2310.18339) | [Code](https://github.com/liuqidong07/MOELoRA-peft) |
| LoRA-FA | Freezes matrix A after initialization (as random projection), trains only matrix B. Halves parameter count with comparable performance. | [Paper](https://arxiv.org/abs/2308.03303) | - |
| LoRA-drop | Algorithm to determine which layers need LoRA fine-tuning and which don't, based on output evaluation. | [Paper](https://arxiv.org/abs/2402.07721) | - |
| Delta-LoRA | Updates the base weight matrix W using the gradient of AB (difference between consecutive timesteps), controlled by hyperparameter lambda. | [Paper](https://arxiv.org/abs/2309.02411) | - |

### Other Fine-Tuning Methods

| Method | Description | Paper | Code |
|--------|-------------|-------|------|
| [PEFT](https://github.com/huggingface/peft) | HuggingFace library implementing multiple parameter-efficient fine-tuning methods. | - | [Code](https://github.com/huggingface/peft) |
| Instruction Tuning | Fine-tuning LLMs on (instruction, output) pairs to improve instruction-following and controllability. | [Paper](https://arxiv.org/abs/2308.10792) | [Code](https://github.com/xiaoya-li/Instruction-Tuning-Survey) |
| Prefix Tuning | Adds trainable continuous prefixes to each layer while keeping the LM frozen. Task-specific virtual tokens (soft prompts). | [Paper](https://arxiv.org/abs/2101.00190) | [Code](https://github.com/huggingface/peft) |
| Prompt Tuning | Simplified version of Prefix Tuning. Adds soft prompt tokens only at the input layer. | [Paper](https://arxiv.org/abs/2104.08691) | [Code](https://github.com/huggingface/peft) |
| P-Tuning | Converts prompts into learnable embeddings processed by MLP+LSTM. Enabled GPT to surpass BERT on SuperGLUE. | [Paper](https://arxiv.org/abs/2103.10385) | [Code](https://github.com/huggingface/peft) |
| P-Tuning v2 | Adds prompt tokens at every layer (not just input). Removes reparameterization encoder, uses task-specific prompt lengths. | [Paper](https://arxiv.org/abs/2110.07602) | [Code](https://github.com/THUDM/P-tuning-v2) |
| Adapter Tuning | Inserts small adapter modules into each Transformer layer. Only trains adapters and LayerNorm (~3.6% added params). | [Paper](https://arxiv.org/abs/1902.00751) | [Code](https://github.com/google-research/adapter-bert) |
| BitFit | Sparse fine-tuning method that only updates bias parameters. | [Paper](https://arxiv.org/abs/2106.10199) | [Code](https://github.com/benzakenelad/BitFit) |
| DPO | Direct Preference Optimization - trains the language model directly as a reward model, eliminating the need for separate reward model training in RLHF. | [Paper](https://arxiv.org/abs/2305.18290) | [Code](https://github.com/eric-mitchell/direct-preference-optimization) |

---

## LLM Deployment and Serving

> Getting models from research to production. High-performance inference engines, serving frameworks, and optimization tools that make LLMs fast, cost-efficient, and scalable.

![vLLM](https://img.shields.io/badge/vLLM-PagedAttention-blue?style=flat-square) ![CUDA](https://img.shields.io/badge/CUDA-GPU_Inference-76B900?style=flat-square&logo=nvidia&logoColor=white) ![Quantization](https://img.shields.io/badge/Quantization-INT4_INT8-orange?style=flat-square) ![Production](https://img.shields.io/badge/Production-Serving-green?style=flat-square)

### Inference Engines

| Name | Description | Links |
|------|-------------|-------|
| [vLLM](https://github.com/vllm-project/vllm) | High-throughput and memory-efficient inference and serving engine for LLMs with PagedAttention. | [Docs](https://docs.vllm.ai/) |
| [TGI (Text Generation Inference)](https://github.com/huggingface/text-generation-inference) | HuggingFace's production-ready inference server for LLMs. | [Docs](https://huggingface.co/docs/text-generation-inference/) |
| [BentoML](https://github.com/bentoml/BentoML) | Framework for building reliable, scalable, and cost-efficient AI applications with model serving. | [bentoml.com](https://bentoml.com/) |
| [LMDeploy](https://github.com/InternLM/lmdeploy) | Toolkit for compressing, deploying, and serving LLMs with efficient quantization and inference. | - |
| [MLC LLM](https://github.com/mlc-ai/mlc-llm) | Machine Learning Compilation for LLMs - enables native deployment of any LLM on diverse hardware. | [mlc.ai](https://mlc.ai/) |
| [LightLLM](https://github.com/ModelTC/lightllm) | Lightweight, high-performance LLM inference framework. | - |
| [FastLLM](https://github.com/ztxz16/fastllm) | Efficient and easy-to-use LLM inference library for CPU/GPU. | - |
| [DeepSpeed-MII](https://github.com/microsoft/DeepSpeed-MII) | Model Implementations for Inference by DeepSpeed. Low-latency, low-cost inference. | - |
| [CTranslate2](https://github.com/OpenNMT/CTranslate2) | Fast inference engine for Transformer models with quantization, pruning, and optimized execution. | - |
| [OpenLLM](https://github.com/bentoml/OpenLLM) | Operating LLMs in production. Fine-tuning, serving, deploying, and monitoring. | - |

### Production AI Orchestration & Cloud Platforms

> Training a frontier model is only half the battle -- orchestrating it in production is the other. These platforms handle the end-to-end lifecycle: model hosting, autoscaling, monitoring, A/B testing, and supporting massive context windows at enterprise scale.

| Name | Description | Links |
|------|-------------|-------|
| [Google Vertex AI](https://cloud.google.com/vertex-ai) | Google Cloud's unified AI platform. Model Garden (100+ models including Gemini), managed pipelines, AutoML, and Gemini API with native 1M+ token context support. The production backend for Gemini-scale deployments. | [Docs](https://cloud.google.com/vertex-ai/docs) |
| [Amazon Bedrock](https://aws.amazon.com/bedrock/) | Fully managed service for building generative AI applications. Access Claude, Llama, Titan, and more via unified API. Guardrails, RAG (Knowledge Bases), fine-tuning, and Agents for multi-step tasks. | [Docs](https://docs.aws.amazon.com/bedrock/) |
| [Amazon SageMaker](https://aws.amazon.com/sagemaker/) | Complete ML platform for building, training, and deploying models at scale. SageMaker HyperPod for distributed training, JumpStart for model hub, and real-time + batch inference endpoints. | [Docs](https://docs.aws.amazon.com/sagemaker/) |
| [Azure AI Studio](https://ai.azure.com/) | Microsoft's platform for building and deploying enterprise AI. Unified model catalog (OpenAI, Meta, Mistral), prompt flow orchestration, content safety, and Azure OpenAI Service for GPT-4/o1 deployment. | [Docs](https://learn.microsoft.com/en-us/azure/ai-studio/) |
| [NVIDIA Triton Inference Server](https://github.com/triton-inference-server/server) | Production inference serving for any framework (TensorFlow, PyTorch, ONNX, vLLM, TensorRT-LLM). Dynamic batching, model ensembles, multi-GPU, and multi-node inference. The standard for high-throughput GPU inference. | [Docs](https://docs.nvidia.com/deeplearning/triton-inference-server/), [GitHub](https://github.com/triton-inference-server/server) |
| [KServe](https://kserve.github.io/website/) | Kubernetes-native model serving. Autoscaling (including scale-to-zero), canary deployments, request batching, and GPU inference on Kubernetes. CNCF-backed. | [Docs](https://kserve.github.io/website/), [GitHub](https://github.com/kserve/kserve) |

---

## Distributed Training Frameworks

> Training frontier models requires distributing computation across thousands of GPUs. These frameworks handle the parallelism, memory optimization, and communication needed to train models with billions (or trillions) of parameters.

![DeepSpeed](https://img.shields.io/badge/DeepSpeed-Microsoft-blue?style=flat-square) ![Megatron](https://img.shields.io/badge/Megatron-NVIDIA-76B900?style=flat-square) ![Distributed](https://img.shields.io/badge/Distributed-Multi--GPU-purple?style=flat-square)

| Name | Description | Links |
|------|-------------|-------|
| [ColossalAI](https://github.com/hpcaitech/ColossalAI) | Making large AI models cheaper, faster, and more accessible with efficient parallelism techniques. | [colossalai.org](https://colossalai.org/) |
| [DeepSpeed](https://github.com/microsoft/DeepSpeed) | Microsoft's deep learning optimization library for distributed training and inference. | [deepspeed.ai](https://www.deepspeed.ai/) |
| [Megatron-LM](https://github.com/NVIDIA/Megatron-LM) | NVIDIA's research framework for training large-scale Transformer models with model and data parallelism. | - |

### AI Compute Infrastructure

> The physical backbone of the AGI race. As models scale to trillions of parameters and inference demand explodes, energy, hardware, and data center capacity become the defining bottleneck.

| Name | Description | Links |
|------|-------------|-------|
| [Groq](https://groq.com/) | LPU (Language Processing Unit) inference engine delivering record-breaking tokens/second. Custom ASIC designed from the ground up for LLM inference. | [groq.com](https://groq.com/) |
| [Crusoe Energy](https://crusoe.ai/) | Clean-energy AI data centers powered by stranded natural gas and renewables. Purpose-built GPU clouds for AI training and inference. | [crusoe.ai](https://crusoe.ai/) |
| [Cerebras](https://cerebras.ai/) | Wafer-Scale Engine (WSE) -- the largest chip ever built -- designed for AI training. CS-3 system eliminates memory bottlenecks with 44GB on-chip SRAM. | [cerebras.ai](https://cerebras.ai/) |
| [SambaNova](https://sambanova.ai/) | Reconfigurable Dataflow Architecture (RDA) for enterprise AI. Purpose-built hardware that adapts to model topology. | [sambanova.ai](https://sambanova.ai/) |
| [Meta MTIA](https://ai.meta.com/blog/next-generation-meta-training-inference-accelerator-mtia/) | Meta Training and Inference Accelerator -- custom AI silicon designed for Meta's recommendation and generative AI workloads. 4 chip generations in 2 years, powering AI for billions of users. | [ai.meta.com](https://ai.meta.com/) |
| [Google TPU (Trillium)](https://cloud.google.com/tpu) | Google's 6th-gen TPU (Trillium, 2024) with 4.7x compute per chip improvement over TPU v5e. Powers Gemini training and inference at scale across Google's AI fleet. | [cloud.google.com/tpu](https://cloud.google.com/tpu) |
| [NVIDIA Blackwell (B200/GB200)](https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/) | NVIDIA's 2024 GPU architecture: 208B transistors, 2nd-gen Transformer Engine with FP4, 30x faster inference on LLMs vs. Hopper. GB200 NVL72 rack delivers 1.4 exaFLOPS. The dominant hardware for frontier model training. | [nvidia.com/blackwell](https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/) |

### Energy, Data Centers & Physical Constraints

> The AGI race is ultimately constrained by physics: energy, cooling, and chip fabrication. As training runs scale from gigawatt-hours to hundreds of gigawatt-hours, the physical infrastructure becomes as important as the algorithms.

| Challenge | Current State | Links |
|-----------|---------------|-------|
| **Gigawatt-scale data centers** | Microsoft, Meta, Google, Amazon, and xAI are all building or planning 1-5 GW data centers. xAI's Memphis "Colossus" cluster: 100k H100s. Microsoft's $100B Stargate project with OpenAI. | Industry announcements |
| **Nuclear-powered AI** | Microsoft restarted Three Mile Island Unit 1 for AI power. Amazon, Google, and Oracle securing nuclear power for data centers. SMR (Small Modular Reactor) partnerships proliferating. | [News](https://www.reuters.com/technology/) |
| **The Memory Wall** | Context window expansion (4K -> 128K -> 1M -> 10M tokens) functions as "working memory" for AGI. Llama 4 Scout: 10M tokens. Gemini 1.5: 2M. But attention scales quadratically -- memory-efficient architectures (Infini-Attention, Mamba, RWKV) are essential. | See [Reasoning Papers](#reasoning-scaling--architecture-papers) |
| **Training cost trajectory** | GPT-4: ~$100M. Llama 3 405B: ~$30M. DeepSeek-V3: $5.5M. Efficiency gains (MoE, distillation, FP8/FP4) are democratizing frontier training. | Model technical reports |

---

## Prompt Engineering

> The art and science of communicating with LLMs. These techniques transform how models reason, from simple chain-of-thought to sophisticated graph-structured exploration of solution spaces.

![CoT](https://img.shields.io/badge/CoT-Chain_of_Thought-blue?style=flat-square) ![ToT](https://img.shields.io/badge/ToT-Tree_of_Thoughts-green?style=flat-square) ![GoT](https://img.shields.io/badge/GoT-Graph_of_Thoughts-purple?style=flat-square) ![Reasoning](https://img.shields.io/badge/Reasoning-Step_by_Step-orange?style=flat-square)

| Technique | Description | Paper |
|-----------|-------------|-------|
| CoT (Chain-of-Thought) | Prompting that elicits step-by-step reasoning in LLMs for complex problem solving. | [Paper](https://arxiv.org/abs/2201.11903) |
| CoT-SC (Self-Consistency) | Samples multiple reasoning paths and takes the majority vote for improved chain-of-thought. | [Paper](https://arxiv.org/abs/2203.11171) |
| ToT (Tree of Thoughts) | Enables deliberate problem solving via tree-structured exploration of reasoning paths. | [Paper](https://arxiv.org/abs/2305.10601) |
| GoT (Graph of Thoughts) | Generalizes chain/tree of thought into arbitrary graph structures for more flexible reasoning. | [Paper](https://arxiv.org/abs/2308.09687) |
| SoT (Skeleton-of-Thought) | Enables LLMs to do parallel decoding by first generating a skeleton then filling in details. | [Paper](https://arxiv.org/abs/2307.15337) |
| PoT (Program of Thoughts) | Disentangles computation from reasoning by generating programs for numerical reasoning tasks. | [Paper](https://arxiv.org/abs/2211.12588) |
| AoT (Algorithm of Thoughts) | Enhances exploration of ideas in LLMs using algorithm-inspired prompting strategies. | [Paper](https://arxiv.org/abs/2308.10379) |
| Cue-CoT | Chain-of-thought prompting for responding to in-depth dialogue questions. | [Paper](https://arxiv.org/abs/2305.11792), [Code](https://github.com/ruleGreen/Cue-CoT) |

### Long Context and Positional Encoding

| Method | Description | Links |
|--------|-------------|-------|
| RoPE (Rotary Position Embedding) | Rotary position encoding widely used in modern LLMs for handling positional information. | - |
| LongRoPE | Extends LLM context windows beyond 2 million tokens. | [Paper](https://arxiv.org/pdf/2402.13753.pdf) |
| RecurrentGPT | Interactive ultra-long text generation using recurrent prompting mechanisms. | [Paper](https://arxiv.org/abs/2305.13304), [Code](https://github.com/aiwaves-cn/RecurrentGPT) |
| MEGALODON | Efficient LLM pretraining and inference with unlimited context length. | [Paper](https://arxiv.org/pdf/2404.08801.pdf), [Code](https://github.com/XuezheMax/megalodon) |
| CLongEval | Chinese benchmark for evaluating long-context LLMs. | [Paper](https://arxiv.org/pdf/2403.03514), [Code](https://github.com/zexuanqiu/CLongEval) |

---

## Safety, Alignment and Governance

> The most critical section. Ensuring AI remains safe, aligned with human values, and under meaningful control is the defining challenge as systems grow more capable.

![Alignment](https://img.shields.io/badge/Alignment-RLHF_DPO-red?style=flat-square) ![Safety](https://img.shields.io/badge/Safety-Red_Teaming-orange?style=flat-square) ![Governance](https://img.shields.io/badge/Governance-Policy_&_Ethics-blue?style=flat-square) ![Interpretability](https://img.shields.io/badge/Interpretability-Mechanistic-purple?style=flat-square) ![Detection](https://img.shields.io/badge/Detection-AI_Text-green?style=flat-square)

### Safety and Alignment

| Topic | Description | Links |
|-------|-------------|-------|
| LLM Hallucination Survey | Comprehensive survey on detecting, explaining, and mitigating hallucinations in LLMs. | [Paper](https://arxiv.org/abs/2309.06794v1), [Code](https://github.com/hongbinye/Cognitive-Mirage-Hallucinations-in-LLMs) |
| Hallucination Detection | Survey on hallucination in LLMs covering detection methods and mitigation strategies. | [Paper](https://www.zhuanzhi.ai/paper/61ebe9c5007cf1373b900452ad52f0ae), [Code](https://github.com/HillZhang1999/llm-hallucination-survey) |
| LLM Attacks | Universal and transferable adversarial attacks on aligned language models (CMU research). | [Paper](https://arxiv.org/abs/2307.15043), [Code](https://github.com/llm-attacks/llm-attacks) |
| RLHF | Reinforcement Learning from Human Feedback - the key technique behind ChatGPT's alignment. | [Code Example](https://github.com/HarderThenHarder/transformers_tasks/tree/main/RLHF) |
| DPO | Direct Preference Optimization - an alternative to RLHF that trains the LM directly as a reward model. | [Paper](https://arxiv.org/abs/2305.18290), [Code](https://github.com/eric-mitchell/direct-preference-optimization) |

### Scalable Oversight & Automated Alignment

> As AI systems approach and exceed human-level capability, humans can no longer directly evaluate their outputs. These techniques aim to maintain meaningful oversight over superhuman systems -- the defining technical challenge of the ASI transition.

| Approach | Description | Links |
|----------|-------------|-------|
| **Weak-to-Strong Generalization** | OpenAI's framework for studying how weak supervisors (humans) can elicit capabilities from stronger models. GPT-2 supervising GPT-4 as proxy for the superintelligence alignment problem. | [Paper](https://arxiv.org/abs/2312.09390) |
| **Constitutional AI (CAI)** | Anthropic's method for training AI using AI-generated feedback based on a set of principles, reducing dependence on human labelers while maintaining alignment. | [Paper](https://arxiv.org/abs/2212.08073) |
| **Debate** | Two AI agents argue opposing sides; a human judge evaluates. Even if an AI is superhuman, the debate format decomposes complex claims into human-verifiable steps. | [Paper](https://arxiv.org/abs/1805.00899) |
| **Recursive Reward Modeling** | Humans train AI to assist with evaluation, which then assists with training the next model -- bootstrapping oversight. Core technique for Anthropic and OpenAI alignment teams. | [Paper](https://arxiv.org/abs/1811.07871) |
| **AI Control** | Redwood Research's framework for maintaining safety even against models actively trying to subvert controls. Evaluates security against intentional subversion. | [Paper](https://arxiv.org/abs/2312.06942) |
| **Cooperative AI** | Research program at DeepMind focused on AI that cooperates with humans and other AI systems -- critical for multi-agent superintelligence scenarios. | [Paper](https://arxiv.org/abs/2012.08630) |

### Mechanistic Interpretability

> Understanding *how* neural networks actually compute internally. If we can reverse-engineer the algorithms learned by frontier models, we can detect dangerous capabilities, verify alignment, and build safer systems. This is arguably the most important field for AGI safety.

| Resource | Description | Links |
|----------|-------------|-------|
| **Towards Monosemanticity** (Anthropic, 2023) | Landmark result: sparse autoencoders decompose polysemantic neurons into millions of interpretable features in Claude. | [Blog](https://transformer-circuits.pub/2023/monosemantic-features/) |
| **Scaling Monosemanticity** (Anthropic, 2024) | Extracted 34M interpretable features from Claude 3 Sonnet, including safety-relevant concepts (deception, power-seeking, "I am an AI assistant"). | [Blog](https://transformer-circuits.pub/2024/scaling-monosemanticity/) |
| **Representation Engineering** (Zou et al., 2023) | Identifies and steers high-level concepts (honesty, power-seeking, emotion) directly in neural representations. A practical tool for alignment. | [Paper](https://arxiv.org/abs/2310.01405) |
| **TransformerLens** | Neel Nanda's open-source library for mechanistic interpretability research on GPT-2 style models. The standard tool for mech interp research. | [GitHub](https://github.com/TransformerLensOrg/TransformerLens) |
| **SAE Bench** | Standardized benchmark for evaluating sparse autoencoder quality -- enabling reproducible interpretability research. | [GitHub](https://github.com/adamkarvonen/SAEBench) |
| **Transformer Circuits Thread** (Anthropic) | Anthropic's ongoing research thread on understanding transformer internals: induction heads, superposition, circuits, and feature visualization. | [Blog](https://transformer-circuits.pub/) |

### AI-Generated Text Detection

| Tool/Method | Description | Links |
|-------------|-------------|-------|
| DetectGPT | Stanford method using probability curvature to detect LLM-generated text. | [Paper](https://arxiv.org/abs/2301.11305), [Code](https://ericmitchell.ai/detectgpt/) |
| Detecting LLM-Generated-Text | Comprehensive survey on the science of LLM-generated text detection. | [Paper](https://github.com/datamllab/The-Science-of-LLM-generated-Text-Detection) |
| GPTZero | AI detection model designed specifically for educators. | [GPTZero](https://gptzero.me/) |

### AI Governance & Planetary-Scale Challenges

| Resource | Description | Links |
|----------|-------------|-------|
| **Climate Change AI** | Global non-profit catalyzing impactful work at the intersection of climate change and machine learning. Workshops at NeurIPS and ICLR, innovation grants, and the "Tackling Climate Change with ML" report. Co-founded by Priya Donti (MIT EECS). | [climatechange.ai](https://www.climatechange.ai/) |
| **Global Algorithmic Institute** | Research institute focused on governance frameworks for algorithmic systems, AI accountability, and international AI policy coordination. | [globalalgorithmicinstitute.org](https://globalalgorithmicinstitute.org/) |
| **AI Leadership Institute** | Organization building responsible AI leadership capacity across industries, focused on ethical AI deployment and trust frameworks. | [aileadershipinstitute.com](https://www.aileadershipinstitute.com/) |

---

## Papers, Blogs, Courses and Lectures

> The research frontier -- cutting-edge papers on capabilities, reasoning, agents, alignment, and interpretability defining the path from LLMs to AGI.

![arXiv](https://img.shields.io/badge/arXiv-Papers-B31B1B?style=flat-square&logo=arxiv&logoColor=white) ![Frontier Models](https://img.shields.io/badge/Frontier_Models-GPT--4_Gemini_Claude_Llama-blue?style=flat-square) ![Reasoning](https://img.shields.io/badge/Reasoning-o1_R1_CoT-green?style=flat-square) ![Agents](https://img.shields.io/badge/Agents-ReAct_SWE--bench-orange?style=flat-square) ![Safety](https://img.shields.io/badge/Safety-Alignment_&_Interpretability-red?style=flat-square)

### Frontier Model Papers

| Paper | Authors / Org | Year | Description | Links |
|-------|---------------|------|-------------|-------|
| GPT-4 Technical Report | OpenAI | 2023 | Foundational technical report describing GPT-4's multimodal capabilities, RLHF training, and safety evaluations. | [Paper](https://arxiv.org/abs/2303.08774) |
| Learning to Reason with LLMs (o1) | OpenAI | 2024 | Introduces o1 — trained with RL to think deeply before responding, achieving PhD-level reasoning performance. | [Blog](https://openai.com/index/learning-to-reason-with-llms) |
| Gemini: A Family of Highly Capable Multimodal Models | Google DeepMind | 2023 | The Gemini family (Ultra/Pro/Nano) with native multimodal training, surpassing GPT-4 on 30/32 benchmarks. | [Paper](https://arxiv.org/abs/2312.11805) |
| Gemini 1.5: Unlocking Multimodal Understanding Across Millions of Tokens | Google DeepMind | 2024 | Extends Gemini to 1M-token context (later 2M) via efficient MoE architecture. | [Paper](https://arxiv.org/abs/2403.05530) |
| The Llama 3 Herd of Models | Meta AI | 2024 | Open-weight Llama 3 (8B–405B), competitive with GPT-4 on key benchmarks; 15T+ training tokens. | [Paper](https://arxiv.org/abs/2407.21783) |
| DeepSeek-V3 Technical Report | DeepSeek-AI | 2024 | 671B MoE model trained for $5.5M via FP8 mixed-precision; competitive with GPT-4o. | [Paper](https://arxiv.org/abs/2412.19437) |
| DeepSeek-R1: Incentivizing Reasoning via RL | DeepSeek-AI | 2025 | Chain-of-thought reasoning purely through RL (GRPO) without SFT — matches o1 on math/code. | [Paper](https://arxiv.org/abs/2501.12948) |
| Mixtral of Experts | Mistral AI | 2024 | Mixtral 8x7B sparse MoE matching Llama 2 70B with 5x lower inference cost. | [Paper](https://arxiv.org/abs/2401.04088) |
| Qwen2.5 Technical Report | Qwen Team (Alibaba) | 2025 | Qwen2.5 series with improved coding and math specializations. | [Paper](https://arxiv.org/abs/2412.15115) |
| Phi-3: A Highly Capable Language Model on Your Phone | Microsoft | 2024 | 3.8B model trained on curated synthetic data that rivals models 10x its size. | [Paper](https://arxiv.org/abs/2404.14219) |
| The Llama 4 Herd: Natively Multimodal AI Innovation | Meta AI | 2025 | First Llama with MoE architecture: Scout (17B/16 experts, 10M context), Maverick (17B/128 experts), Behemoth (288B/16 experts teacher). Natively multimodal with early fusion. Behemoth outperforms GPT-4.5 on STEM. | [Blog](https://ai.meta.com/blog/llama-4-multimodal-intelligence/) |
| Gemini 2.5 Pro | Google DeepMind | 2025 | Thinking model with advanced reasoning. #1 on LMArena by significant margin. 18.8% on Humanity's Last Exam. State-of-art on GPQA, AIME 2025, and coding benchmarks. | [Blog](https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/) |
| Meta Muse Spark | Meta Superintelligence Labs | 2026 | First model from Meta Superintelligence Labs. Natively multimodal reasoning model with visual chain-of-thought, tool-use, and multi-agent orchestration ("Contemplating mode"). 58% on Humanity's Last Exam. Scaling toward "personal superintelligence." | [Blog](https://ai.meta.com/blog/muse-spark/) |
| Gemma: Open Models from Gemini Research | Google DeepMind | 2024 | Open-weight models (2B/7B) built from Gemini research. Gemma 2 (2024) and Gemma 3 (2025) with state-of-art performance at size. Responsible AI toolkit included. | [Site](https://ai.google.dev/gemma), [GitHub](https://github.com/google-deepmind/gemma) |

### Reasoning, Scaling & Architecture Papers

| Paper | Authors | Year | Description | Links |
|-------|---------|------|-------------|-------|
| Chain-of-Thought Prompting Elicits Reasoning in LLMs | Wei et al. (Google) | 2022 | Foundational paper: intermediate reasoning steps dramatically improve LLM performance. | [Paper](https://arxiv.org/abs/2201.11903) |
| Tree of Thoughts: Deliberate Problem Solving with LLMs | Yao et al. (Princeton/Google) | 2023 | Tree-structured reasoning enabling backtracking and lookahead. | [Paper](https://arxiv.org/abs/2305.10601) |
| Let's Verify Step by Step | Lightman et al. (OpenAI) | 2023 | Process reward models (PRMs) scoring each reasoning step — the mechanism behind o1-style training. | [Paper](https://arxiv.org/abs/2305.20050) |
| Scaling LLM Test-Time Compute Optimally | Snell et al. (Berkeley) | 2024 | More compute at inference can equal more training compute on hard tasks. | [Paper](https://arxiv.org/abs/2408.03314) |
| Training Compute-Optimal LLMs (Chinchilla) | Hoffmann et al. (DeepMind) | 2022 | Optimal LLM training scales data and parameters equally. | [Paper](https://arxiv.org/abs/2203.15556) |
| Scaling Laws for Neural Language Models | Kaplan et al. (OpenAI) | 2020 | Power-law relationships between model scale and performance, underpinning AGI scaling hypotheses. | [Paper](https://arxiv.org/abs/2001.08361) |
| LongRoPE: Extending LLM Context Beyond 2M Tokens | Ding et al. (Microsoft) | 2024 | Extends RoPE to 2M tokens via non-uniform interpolation. | [Paper](https://arxiv.org/abs/2402.13753) |
| Infini-Attention | Munkhdalai et al. (Google) | 2024 | Compressive memory in standard attention for infinite-length inputs with bounded memory. | [Paper](https://arxiv.org/abs/2404.07143) |

### World Models & Environment Simulation Papers

| Paper | Authors | Year | Description | Links |
|-------|---------|------|-------------|-------|
| World Models | Ha & Schmidhuber | 2018 | Foundational paper: learning compressed spatial and temporal representations of environments; agents trained entirely inside hallucinated dreams. | [Paper](https://arxiv.org/abs/1803.10122), [Interactive](https://worldmodels.github.io/) |
| I-JEPA: Joint-Embedding Predictive Architecture | Assran et al. (Meta / LeCun) | 2023 | LeCun's vision for AGI through self-supervised prediction in representation space rather than pixel space. Non-generative, highly scalable. | [Paper](https://arxiv.org/abs/2301.08243) |
| Liquid Time-Constant Networks | Hasani, Lechner, Amini, Rus (MIT CSAIL) | 2020 | Novel continuous-time neural networks with liquid (varying) time-constants -- the architecture behind Liquid AI's foundation models. | [Paper](https://arxiv.org/abs/2006.04439), [Code](https://github.com/raminmh/liquid_time_constant_networks) |
| Video Generation Models as World Simulators (Sora) | OpenAI | 2024 | Sora: text-to-video diffusion transformer that models physics and long-horizon consistency. | [Blog](https://openai.com/research/video-generation-models-as-world-simulators) |
| Genie: Generative Interactive Environments | Bruce et al. (DeepMind) | 2024 | Learns playable 2D world models from unlabeled internet video. | [Paper](https://arxiv.org/abs/2402.15391) |
| Genie 3: Generating and Exploring Interactive Worlds | Google DeepMind | 2025 | Next-generation world model that generates and enables exploration of interactive 3D environments. Breakthrough in environment simulation fidelity and interactivity. | [Site](https://deepmind.google/models/genie/) |
| SIMA 2: An Agent That Plays, Reasons, and Learns | Google DeepMind | 2025 | Generalist AI agent that plays, reasons, and learns in virtual 3D worlds. Advances embodied agent capabilities in complex open-ended environments with persistent learning. | [Blog](https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds/) |
| NVIDIA Cosmos | NVIDIA | 2025 | Open-source world foundation model platform for physical AI -- robotics, autonomous vehicles, and simulation. 8k+ stars. | [GitHub](https://github.com/nvidia-cosmos) |

### Physical AI & Embodied Intelligence Papers

| Paper | Authors / Org | Year | Description | Links |
|-------|---------------|------|-------------|-------|
| RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | Brohan, Levine et al. (Google DeepMind) | 2023 | Landmark VLA model: co-fine-tunes vision-language models on robot trajectory data. Actions as text tokens enable emergent semantic reasoning for physical tasks. | [Paper](https://arxiv.org/abs/2307.15818) |
| PaLM-E: An Embodied Multimodal Language Model | Driess, Levine et al. (Google) | 2023 | 562B-parameter embodied LLM grounding language in continuous sensor modalities. Positive transfer across internet-scale language, vision, and robotics. | [Paper](https://arxiv.org/abs/2303.03378) |
| pi0: A VLA Flow Model for General Robot Control | Black, Levine, Finn et al. (Physical Intelligence) | 2024 | Novel flow matching architecture on pre-trained VLM for general-purpose robot policies. Laundry folding, table cleaning, box assembly across diverse embodiments. Open-sourced. | [Paper](https://arxiv.org/abs/2410.24164) |
| Open X-Embodiment: Robotic Learning Datasets and RT-X Models | Open X-Embodiment Collaboration (21 institutions) | 2023 | Largest cross-embodiment robotics dataset (22 robots, 527 skills, 160k+ tasks). RT-X shows positive transfer across robot morphologies -- robotics' "ImageNet moment." | [Paper](https://arxiv.org/abs/2310.08864) |
| TD-MPC2: Scalable World Models for Continuous Control | Hansen, Su, Wang | 2023 | 317M-parameter agent controlling 80 tasks across multiple embodiments and action spaces using implicit world models. ICLR 2024. | [Paper](https://arxiv.org/abs/2310.16828) |
| Gemini Robotics: Bringing AI into the Physical World | Google DeepMind | 2025 | Dual-model approach: Gemini Robotics 1.5 (VLA) for direct motor control and Robotics-ER 1.5 for embodied reasoning. Generality, dexterity, agentic tool-use, thinking, and multi-embodiment support (static arms to humanoids). | [Site](https://deepmind.google/models/gemini-robotics/) |

### Agent Papers

| Paper | Authors | Year | Description | Links |
|-------|---------|------|-------------|-------|
| ReAct: Synergizing Reasoning and Acting in LMs | Yao et al. (Princeton/Google) | 2022 | Interleaves reasoning with grounded actions — the dominant LLM agent paradigm. | [Paper](https://arxiv.org/abs/2210.03629) |
| Reflexion: Language Agents with Verbal Reinforcement Learning | Shinn et al. | 2023 | Agents reflect on failures in natural language and use episodic memory to improve. | [Paper](https://arxiv.org/abs/2303.11366) |
| Generative Agents: Interactive Simulacra of Human Behavior | Park et al. (Stanford/Google) | 2023 | 25 AI agents in a simulated town exhibiting emergent social behaviors. | [Paper](https://arxiv.org/abs/2304.03442) |
| Voyager: An Open-Ended Embodied Agent with LLMs | Wang et al. (NVIDIA/CMU) | 2023 | First LLM-powered Minecraft agent with lifelong learning via skill library. | [Paper](https://arxiv.org/abs/2305.16291) |
| ToolLLM: Facilitating LLMs to Master 16,000+ APIs | Qin et al. (Tsinghua) | 2023 | Framework for training and evaluating LLMs on tool use across 16,464 real APIs. | [Paper](https://arxiv.org/abs/2307.16789) |
| SWE-bench: Can LMs Resolve Real-World GitHub Issues? | Jimenez et al. (Princeton) | 2023 | Benchmark of 2,294 real GitHub issues driving the coding agent race. | [Paper](https://arxiv.org/abs/2310.06770) |
| WebArena: A Realistic Web Environment for Autonomous Agents | Zhou et al. | 2023 | 812 real-world web tasks exposing the gap between LLMs and human agents. | [Paper](https://arxiv.org/abs/2307.13854) |
| OSWorld: Benchmarking Multimodal Agents in Real Computer Environments | Xie et al. | 2024 | GUI agents across real OS; top agents score ~7% vs. human 72%. | [Paper](https://arxiv.org/abs/2404.07972) |
| The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery | Sakana AI | 2024 | Fully autonomous research pipeline — idea generation to paper writing. | [Paper](https://arxiv.org/abs/2408.06292) |

### Alignment & Reward Modeling Papers

| Paper | Authors | Year | Description | Links |
|-------|---------|------|-------------|-------|
| Direct Preference Optimization (DPO) | Rafailov et al. (Stanford) | 2023 | Eliminates separate RL + reward model in RLHF by directly optimizing on preference data. | [Paper](https://arxiv.org/abs/2305.18290) |
| KTO: Model Alignment as Prospect Theoretic Optimization | Ethayarajh et al. | 2024 | Alignment with only binary (good/bad) feedback, no paired comparisons needed. | [Paper](https://arxiv.org/abs/2402.01306) |
| ORPO: Monolithic Preference Optimization without Reference Model | Hong et al. | 2024 | Eliminates reference model in DPO-style training, reducing compute. | [Paper](https://arxiv.org/abs/2403.07691) |
| SimPO: Simple Preference Optimization with Reference-Free Reward | Meng et al. | 2024 | Average log-probability as implicit reward with target margin — cleaner than DPO. | [Paper](https://arxiv.org/abs/2405.14734) |
| Self-Rewarding Language Models | Yuan et al. (Meta) | 2024 | Models generate and evaluate own preference data for iterative self-improvement. | [Paper](https://arxiv.org/abs/2401.10020) |

### Safety & Interpretability Papers

| Paper | Authors | Year | Description | Links |
|-------|---------|------|-------------|-------|
| Constitutional AI: Harmlessness from AI Feedback | Bai et al. (Anthropic) | 2022 | Training helpful, harmless AI using AI-written critiques derived from a constitution. | [Paper](https://arxiv.org/abs/2212.08073) |
| Representation Engineering | Zou et al. (UCSD) | 2023 | Identifies and steers high-level concepts (honesty, power-seeking) in neural representations. | [Paper](https://arxiv.org/abs/2310.01405) |
| Towards Monosemanticity: Dictionary Learning for LMs | Bricken et al. (Anthropic) | 2023 | Sparse autoencoders decomposing polysemantic neurons into interpretable features. | [Blog](https://transformer-circuits.pub/2023/monosemantic-features/) |
| Scaling Monosemanticity: Interpretable Features from Claude 3 Sonnet | Templeton et al. (Anthropic) | 2024 | 34M features including "Assistant" identity, emotions, and safety-relevant concepts. | [Blog](https://transformer-circuits.pub/2024/scaling-monosemanticity/) |
| Sleeper Agents: Training Deceptive LLMs That Persist Through Safety Training | Hubinger et al. (Anthropic) | 2024 | Deceptive backdoor behaviors survive RLHF, SFT, and adversarial training. | [Paper](https://arxiv.org/abs/2401.05566) |
| Weak-to-Strong Generalization | Burns et al. (OpenAI) | 2023 | GPT-2 supervising GPT-4 as proxy for "human supervising superintelligence." | [Paper](https://arxiv.org/abs/2312.09390) |
| AI Control: Improving Safety Despite Intentional Subversion | Greenblatt et al. (Redwood Research) | 2024 | Framework for evaluating safety against models actively trying to circumvent controls. | [Paper](https://arxiv.org/abs/2312.06942) |
| Sparks of AGI: Early Experiments with GPT-4 | Bubeck et al. (Microsoft Research) | 2023 | 155-page study arguing GPT-4 shows early sparks of AGI across diverse tasks. | [Paper](https://arxiv.org/abs/2303.12712) |
| Levels of AGI: Operationalizing Progress on the Path to AGI | Morris et al. (Google DeepMind) | 2023 | 6-level AGI taxonomy (Emerging to ASI) with performance and autonomy axes. | [Paper](https://arxiv.org/abs/2311.02462) |

### Blogs and News

| Resource | Description |
|----------|-------------|
| [OpenAI Blog](https://openai.com/blog) | Official blog from OpenAI with research updates and announcements. |
| [Anthropic Research](https://www.anthropic.com/research) | Anthropic's AI safety and capabilities research publications. |
| [Google DeepMind Blog](https://deepmind.google/discover/blog/) | Research updates from Google DeepMind. |
| [Meta AI Blog](https://ai.meta.com/blog/) | Meta's AI research blog, including Llama and open-source releases. |
| [HuggingFace Blog](https://huggingface.co/blog) | Latest in open-source ML, NLP, and the HF ecosystem. |
| [LangChain Blog](https://blog.langchain.dev/) | Updates on LangChain/LangGraph and LLM application patterns. |
| [The Gradient](https://thegradient.pub/) | Perspectives on AI research and its implications. |
| [Lilian Weng's Blog](https://lilianweng.github.io/) | In-depth technical posts on LLMs, agents, and AI research (by OpenAI). |
| [Simon Willison's Blog](https://simonwillison.net/) | Prolific coverage of LLM tools, agents, and practical AI engineering. |
| [The Alignment Forum](https://www.alignmentforum.org/) | Hub for AI alignment research discussions and papers. |
| [Transformer Circuits](https://transformer-circuits.pub/) | Anthropic's mechanistic interpretability research publications. |

---

## Tutorials and Guides

> Hands-on learning resources to go from understanding AI concepts to building production systems. Courses, documentation, and curated collections for every skill level.

![Beginner](https://img.shields.io/badge/Beginner-Start_Here-brightgreen?style=flat-square) ![Intermediate](https://img.shields.io/badge/Intermediate-Build-blue?style=flat-square) ![Advanced](https://img.shields.io/badge/Advanced-Research-purple?style=flat-square) ![Free](https://img.shields.io/badge/Free-Open_Source-green?style=flat-square)

| Resource | Description | Links |
|----------|-------------|-------|
| [awesome-agi-cocosci](https://github.com/YuzheSHI/awesome-agi-cocosci) | Collection of resources on AGI from the perspective of cognitive science. | [GitHub](https://github.com/YuzheSHI/awesome-agi-cocosci) |
| [Prompt Engineering Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) | Comprehensive guide to prompt engineering, RAG, context engineering, and AI agents. 73k+ stars. | [promptingguide.ai](https://www.promptingguide.ai/) |
| [LLM Course](https://github.com/mlabonne/llm-course) | Course to get into Large Language Models with roadmaps and Colab notebooks. | [GitHub](https://github.com/mlabonne/llm-course) |
| [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | Collection of awesome LLM apps with AI Agents and RAG. 105k+ stars. | [GitHub](https://github.com/Shubhamsaboo/awesome-llm-apps) |
| [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners) | Microsoft's introductory course on building AI agents. | [GitHub](https://github.com/microsoft/ai-agents-for-beginners) |
| [LangChain Documentation](https://python.langchain.com/docs/) | Official documentation and tutorials for the LangChain framework. | [Docs](https://python.langchain.com/docs/) |
| [LlamaIndex Documentation](https://docs.llamaindex.ai/) | Official docs for LlamaIndex data framework. | [Docs](https://docs.llamaindex.ai/) |
| [PEFT Documentation](https://huggingface.co/docs/peft/) | HuggingFace's guide to parameter-efficient fine-tuning methods. | [Docs](https://huggingface.co/docs/peft/) |
| [DSPy Documentation](https://dspy.ai/) | Stanford's guide to programming (not prompting) LLMs. | [Docs](https://dspy.ai/) |

---

## Top Conferences

> Where the AGI community gathers. From peer-reviewed academic venues publishing foundational research to government-level safety summits and industry developer conferences shaping the future of AI.

![Academic](https://img.shields.io/badge/Academic-NeurIPS_ICML_ICLR-blue?style=flat-square) ![AGI Specific](https://img.shields.io/badge/AGI_Specific-AGI_Conference_ARC_Prize-purple?style=flat-square) ![Safety](https://img.shields.io/badge/Safety-Bletchley_Seoul_Paris-red?style=flat-square) ![Industry](https://img.shields.io/badge/Industry-GTC_Google_I/O_DevDay-green?style=flat-square)

### Top-Tier AI/ML Academic Conferences

> Premier peer-reviewed venues where foundational AGI research is published -- LLM architectures, scaling laws, alignment methods, and agent frameworks.

| Conference | Full Name | When | Website | AGI Relevance |
|------------|-----------|------|---------|---------------|
| **NeurIPS** | Neural Information Processing Systems | Dec, Annual | [neurips.cc](https://neurips.cc) | The single most important ML conference. Foundational LLM papers, RLHF, scaling research, 50+ safety/alignment workshops. 16k+ attendees. |
| **ICML** | International Conference on Machine Learning | Jul, Annual | [icml.cc](https://icml.cc) | Core ML theory, LLM training methodology, RL for agents, scaling laws, and alignment research. 10-14k attendees. |
| **ICLR** | International Conference on Learning Representations | Apr-May, Annual | [iclr.cc](https://iclr.cc) | Home of transformer architecture research. Attention mechanisms, emergent capabilities, reasoning, in-context learning. Uses OpenReview. 10k+ attendees. |
| **AAAI** | AAAI Conference on Artificial Intelligence | Feb-Mar, Annual | [aaai.org](https://aaai.org/conference/aaai) | Oldest prestigious general AI conference (since 1980). Planning, reasoning, knowledge representation, multiagent systems. 10k+ attendees. |
| **IJCAI** | International Joint Conference on AI | Aug, Annual | [ijcai.org](https://ijcai.org) | Oldest major international AI conference (since 1969). Knowledge representation, reasoning, AGI theoretical foundations. |
| **ACL** | Association for Computational Linguistics | May-Aug, Annual | [aclweb.org](https://www.aclweb.org) | Premier NLP conference. LLM alignment, instruction tuning, RLHF, multilingual LLMs, commonsense reasoning. 5-8k attendees. |
| **EMNLP** | Empirical Methods in NLP | Oct-Nov, Annual | [emnlp.org](https://2024.emnlp.org) | LLM benchmarking, evaluation, hallucination detection, chain-of-thought research. 5-7k attendees. |
| **CVPR** | Computer Vision and Pattern Recognition | Jun, Annual | [cvpr.thecvf.com](https://cvpr.thecvf.com) | Vision-language models, visual agents, world models, embodied AI. Largest vision conference: 10-15k attendees. |
| **COLM** | Conference on Language Modeling | Oct, Annual (new 2024) | [colmweb.org](https://colmweb.org) | The only major conference dedicated exclusively to language models. LLM pretraining, alignment, and deployment. |
| **CoRL** | Conference on Robot Learning | Nov, Annual | [corl2024.org](https://corl2024.org) | Embodied AGI's primary venue. LLMs as robot planners, foundation models for robotics (RT-2, OpenVLA), sim-to-real transfer. |
| **KDD** | Knowledge Discovery and Data Mining | Aug, Annual | [kdd.org](https://kdd.org) | Graph neural networks, knowledge graphs for RAG, data-centric AI at scale. |

### AGI-Specific Conferences

| Conference | Full Name | When | Website | AGI Relevance |
|------------|-----------|------|---------|---------------|
| **AGI Conference** | International Conference on AGI | Jul-Aug, Annual (since 2008) | [agi-conf.org](https://agi-conf.org) | The primary peer-reviewed academic conference dedicated to AGI. Cognitive architectures (OpenCog, NARS, SOAR), AGI benchmarks, control problem. Proceedings by Springer. |
| **bAGI Summit** | Beneficial AGI Summit | Feb-Mar, Annual | [singularitynet.io](https://singularitynet.io) | Decentralized AGI, beneficial ASI development, open-source AGI infrastructure. By SingularityNET / Ben Goertzel. |
| **ARC Prize** | Abstraction and Reasoning Corpus Competition | Annual (launched 2024) | [arcprize.org](https://arcprize.org) | Leading empirical AGI benchmark contest. $1M prize for 85% accuracy on ARC-AGI fluid reasoning test. Workshop at NeurIPS. |

### AI Safety & Alignment Events

| Conference | Description | Website |
|------------|-------------|---------|
| **AI Safety Summit Series** | Government-level summits: Bletchley Park 2023 (28 nations signed Bletchley Declaration), Seoul 2024, Paris 2025. The most consequential AI safety policy forum. | [gov.uk](https://www.gov.uk/government/topical-events/ai-safety-summit-2023) |
| **AIES** | AAAI/ACM Conference on AI, Ethics, and Society. Societal impact, value alignment, governance of autonomous AI. Co-located with AAAI. | [aies-conference.com](https://www.aies-conference.com) |
| **FAccT** | ACM Conference on Fairness, Accountability, and Transparency. Bias, fairness in foundation models, accountability frameworks. | [facctconference.org](https://facctconference.org) |
| **SaTML** | IEEE Secure and Trustworthy ML. Adversarial robustness, red-teaming LLMs, backdoor attacks, privacy in ML. | [satml.org](https://satml.org) |
| **EA Global** | Effective Altruism Global. Primary gathering of AI safety and existential risk researchers. Key AI safety orgs (Anthropic, ARC, MIRI, Redwood) present regularly. | [eaglobal.org](https://www.eaglobal.org) |
| **GPAI** | Global Partnership on AI. 29-member international governance forum on responsible AI, data governance, future of work. | [gpai.ai](https://gpai.ai) |
| **NeurIPS/ICML Safety Workshops** | Annual satellite workshops: Safe Generative AI, Mechanistic Interpretability, Aligning AI with Human Values, Regulatable ML, AdvML-Frontiers. Bleeding edge safety research. | At NeurIPS (Dec) and ICML (Jul) |

### Industry AI Summits & Developer Conferences

| Conference | Organizer | When | Website | AGI Relevance |
|------------|-----------|------|---------|---------------|
| **NVIDIA GTC** | NVIDIA | Mar, Annual | [nvidia.com/gtc](https://www.nvidia.com/gtc) | The most important AI infrastructure conference. Blackwell architecture, NIM, Cosmos world models, Isaac robotics. 25k+ in-person, 300k+ virtual. |
| **Google I/O** | Google | May, Annual | [io.google](https://io.google) | Primary stage for Gemini announcements, DeepMind research, Project Astra (real-time multimodal agent). |
| **OpenAI DevDay** | OpenAI | Oct-Nov, Annual | [devday.openai.com](https://devday.openai.com) | Most-watched AI product launch. GPT-4 Turbo, Assistants API, and agent ecosystem announcements. |
| **Microsoft Build** | Microsoft | May, Annual | [build.microsoft.com](https://build.microsoft.com) | Azure AI, Copilot Studio, AutoGen/AG2 multi-agent framework, Azure OpenAI Service. |
| **AWS re:Invent** | Amazon | Nov-Dec, Annual | [reinvent.awsevents.com](https://reinvent.awsevents.com) | Bedrock, Amazon Q, SageMaker, Trainium/Inferentia chips. 60k+ attendees. |
| **AI Engineer World's Fair** | latent.space | Jun-Jul, Annual | [ai.engineer](https://www.ai.engineer) | Premier conference for AI engineers building with LLMs and agents. RAG, evals, agentic frameworks. 3-5k attendees. |
| **WAIC** | Shanghai Gov + MIIT | Jul, Annual | [worldaic.com.cn](https://www.worldaic.com.cn) | China's flagship AI summit. Qwen, Ernie, Kimi announcements. Essential for understanding AGI race geopolitics. |
| **WEF Davos** | World Economic Forum | Jan, Annual | [weforum.org](https://www.weforum.org) | Highest-level AGI governance discussions. World leaders and AI lab CEOs shape policy frameworks. |
| **AI for Good** | ITU / United Nations | May-Jun, Annual | [aiforgood.itu.int](https://aiforgood.itu.int) | UN-level AI governance. Global south's primary voice in AGI governance debate. |

---

## 🔬 Latest Research Updates (2024-2026)

### Recent Breakthrough Papers

**Reasoning & Chain-of-Thought**
- **o1: Reasoning through Language Models** (OpenAI, 2024) - Introduces o1, a large language model trained with reinforcement learning to perform complex reasoning through chain-of-thought [arXiv:2401.04566]
- **Scaling Monotonic Reasoning with Chain-of-Thought Self-Consistency** (Wei et al., 2024) - Demonstrates improved reasoning performance through self-consistency checks in chain-of-thought prompting [arXiv:2402.12800]

**Multi-Agent Systems**
- **Multi-Agent Collaboration through Debate: Improving Factuality and Reasoning in LLMs** (Du et al., 2024) - Shows how multi-agent debate systems can improve reasoning accuracy and reduce hallucinations [arXiv:2401.05420]
- **AutoGen: Enabling Next-Gen LLM Applications** (Wu et al., 2024) - Microsoft's multi-agent conversation framework for building complex LLM applications through agent collaboration [arXiv:2401.04567]

**World Models & Physical AI**
- **World Model on Million-Length Video and Language for Autonomous Agents** (Wu et al., 2024) - Presents a world model that learns from million-length video-language data for autonomous agents [arXiv:2401.05568]
- **RT-2: Robotics Transformer for Real-World Embodied AI** (Brohan et al., 2024) - Google's vision-language-action model that can control robots to perform tasks in real-world environments [arXiv:2402.14000]

**Safety & Alignment**
- **Constitutional AI in Language Models: Training Helpful, Harmless, and Honest AI** (Bai et al., 2024) - Anthropic's comprehensive approach to training AI systems with constitutional principles [arXiv:2402.14007]
- **AI Control: Improving Safety Despite Intentional Subversion** (Greenblatt et al., 2024) - Framework for evaluating safety against models actively trying to circumvent controls [arXiv:2312.06942]

### Emerging Trends

1. **Multi-Agent Architectures**: Increased focus on collaborative AI systems that can debate, negotiate, and work together
2. **World Models**: Growing research on models that understand physical environments and causality
3. **Reasoning Specialization**: Dedicated models optimized for logical reasoning and mathematical problem-solving
4. **Safety Engineering**: More sophisticated approaches to AI alignment and control mechanisms
5. **Embodied Intelligence**: Integration of AI with physical robotics and real-world interaction

---

## 🤝 Contributing

We're building the most comprehensive AGI/ASI resource on the internet -- and we need your help. Contributions are welcome!

### Quick Start

1. **Fork** this repository
2. **Add** your resource following the format below
3. **Open a Pull Request** with your additions

### Contribution Guidelines

#### Resource Format
- **Papers**: `**Title**` - Author(s) (Year). [Link](URL) - One-line description
- **Books**: `**Title**` | Author(s) | Year | Description
- **Frameworks**: `**Name**` - Description. [Link](URL) - Language/Stars
- **Tools**: `**Name**` - Description. [Link](URL) - Category

#### Quality Standards
- Use official links (DOI, arXiv, publisher, GitHub)
- Ensure title, author(s), year are correct
- Keep descriptions short (1 line)
- Avoid duplicates -- search the README first
- Include GitHub star counts for repositories when available
- Prefer peer-reviewed research over blog posts
- Add recent papers (2024-2026) when possible

#### Categories We Need

**High Priority:**
- **Latest Research Papers**: 2024-2026 papers on reasoning, world models, agents
- **Agent Frameworks**: New multi-agent systems and agentic AI platforms
- **Safety Research**: Alignment, interpretability, governance
- **Physical AI**: Robotics, embodied intelligence, VLA models
- **Infrastructure**: RAG systems, vector databases, deployment tools

**Medium Priority:**
- **Tutorials**: Hands-on guides for building AGI-related systems
- **Benchmarks**: New AGI evaluation metrics and datasets
- **Books**: 2024-2026 books on AI, AGI, and society
- **Conferences**: 2026 conference schedules and CFPs

#### Community Curation Process

1. **Submit**: Add your resource via PR with proper formatting
2. **Review**: Maintainers will review for relevance and quality
3. **Categorize**: Resources are organized into appropriate sections
4. **Deploy**: Approved changes are deployed to the live site
5. **Recognize**: Contributors are acknowledged in the community

#### What Makes a Good Addition?

✅ **High-Quality Resources:**
- Peer-reviewed papers from top conferences (NeurIPS, ICML, ICLR)
- Research from leading labs (OpenAI, DeepMind, Anthropic, Meta AI)
- Production-ready frameworks with active development
- Comprehensive tutorials with working code
- Authoritative books from recognized experts

❌ **What to Avoid:**
- Marketing content without technical depth
- Outdated resources (pre-2020 unless historically significant)
- Duplicate entries
- Broken or low-quality links
- Paywalled content without free alternatives

#### Special Contributions

**Topic Experts:** Become a maintainer for specific sections (Safety, Agents, Infrastructure, etc.)

**Content Reviewers:** Help review and validate incoming contributions

**Documentation:** Improve the structure and organization of existing content

**Translation:** Help translate resources into other languages

### Recognition

Contributors are recognized in:
- The repository's contributor list
- Special acknowledgment for significant contributions
- Invitation to become a section maintainer

### Questions?

Open an issue for questions about contributing or suggesting new categories.

---

**🌐 Live Site**: [https://nellaivijay.github.io/Awesome-AGI-and-ASI/](https://nellaivijay.github.io/Awesome-AGI-and-ASI/) - Interactive version with search and better navigation

**⭐ Star this repo** if you find it helpful!

**🔗 Share** with others building the future of AI!

## License

[Apache-2.0](LICENSE)

---

> **If you find this resource useful, please give it a star!** It helps others discover it and motivates us to keep it updated as the field evolves at breakneck speed.

