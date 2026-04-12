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

> *"The development of full artificial intelligence could spell the end of the human race... or it could be the best thing ever to happen to humanity."* -- Stephen Hawking

The most comprehensive, curated collection of resources on the journey from **AI** to **AGI** to **ASI** -- covering frameworks, agents, research papers, safety & alignment, books, benchmarks, conferences, and tools for builders and researchers shaping the future of intelligence.

---

## Understanding AI, AGI, and ASI

### What is AI (Artificial Intelligence)?

**Artificial Intelligence (AI)** is the broad field of creating machines and software that can perform tasks typically requiring human intelligence. Today's AI systems -- often called **Artificial Narrow Intelligence (ANI)** -- are specialists: they excel at one specific task (playing chess, recognizing faces, translating languages, generating text) but cannot transfer that skill to unrelated domains. Every AI system you use today, from Siri to GPT-4 to self-driving cars, is narrow AI. It is powerful within its domain but fundamentally limited -- a chess engine cannot write poetry, and a language model cannot physically navigate a room.

### What is AGI (Artificial General Intelligence)?

**Artificial General Intelligence (AGI)** refers to AI systems that match or exceed human-level cognitive abilities **across virtually all intellectual tasks** -- learning, reasoning, problem-solving, perception, creativity, and social understanding. Unlike narrow AI, an AGI system could teach itself a new discipline, transfer knowledge between domains, handle novel situations it was never trained on, and understand context the way humans do. AGI does not yet exist, but its pursuit drives the most ambitious research programs in history (OpenAI, DeepMind, Anthropic, xAI, Meta, SSI). Estimated arrival: **2027--2035** according to leading researchers, though timelines remain highly uncertain.

### What is ASI (Artificial Superintelligence)?

**Artificial Superintelligence (ASI)**, also called **Super AI**, is a hypothetical system whose intelligence surpasses the most gifted human minds in **every domain** -- scientific creativity, social skills, strategic reasoning, and general wisdom. Philosopher Nick Bostrom defines it as *"any intellect that greatly exceeds the cognitive performance of humans in virtually all domains of interest."* ASI could emerge from recursive self-improvement cycles (an **"intelligence explosion"**), where an AI that can improve its own design rapidly surpasses human-level capabilities. Key concerns include the **control problem** (keeping ASI aligned with human values), **goal misalignment** (unintended optimization targets), and the potential for a **technological singularity** -- a point beyond which human civilization is fundamentally and unpredictably transformed.

### AI vs AGI vs ASI -- The Complete Comparison

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
| **GPT-4, Claude 3.5, Gemini 2.0** score expert-level on many benchmarks | Frontier models approach human performance in narrow domains, but still fail on novel reasoning |
| **o1, o3, DeepSeek-R1** use chain-of-thought reasoning | Test-time compute scaling is a new paradigm -- models that "think longer" perform better |
| **ARC-AGI scores remain <65%** (humans score ~85%) | Core fluid reasoning and abstraction remain unsolved -- the gap to AGI is real |
| **Autonomous coding agents** (OpenHands, Devin, SWE-agent) resolve real GitHub issues | Agents are achieving narrow AGI-like performance in software engineering |
| **Safe Superintelligence Inc.** raised $30B+ in 2024 | Ilya Sutskever (ex-OpenAI chief scientist) is betting everything on the ASI path |
| **AI Safety Summits** held at Bletchley Park, Seoul, Paris | Governments worldwide are treating AGI/ASI risk as a top-tier policy issue |
| **Scaling debate** intensifies | Some argue scaling alone leads to AGI; others say fundamental breakthroughs are needed |

### Google DeepMind's Levels of AGI Framework (2023)

| Level | Name | Description | Current Status |
|-------|------|-------------|----------------|
| 0 | **No AI** | Narrow software with no AI capability | Calculator, basic scripts |
| 1 | **Emerging** | Equal to or somewhat better than an unskilled human | ChatGPT, Bard, Llama (most current LLMs) |
| 2 | **Competent** | At least 50th percentile of skilled adults | Frontier models on some tasks (coding, writing) |
| 3 | **Expert** | At least 90th percentile of skilled adults | Narrow domains only (AlphaFold, specialized coding) |
| 4 | **Virtuoso** | At least 99th percentile of skilled adults | Not yet achieved across general tasks |
| 5 | **Superhuman (ASI)** | Outperforms 100% of humans in all tasks | Theoretical -- the ASI threshold |

> **Source:** [Levels of AGI: Operationalizing Progress on the Path to AGI](https://arxiv.org/abs/2311.02462) -- Morris et al., Google DeepMind (2023)

## Table of Contents

### Understand
- [Understanding AI, AGI, and ASI](#understanding-ai-agi-and-asi) -- Definitions, comparison table, where we are now, DeepMind's AGI levels
- [ASI and Superintelligence Research](#asi-and-superintelligence-research) -- Key organizations, books (27 titles in 4 categories), seminal papers, benchmarks, roadmaps & timelines

### Build
- [Frameworks and Platforms](#frameworks-and-platforms) -- Next-gen, established, and specialized agent frameworks
- [Agents](#agents) -- Coding, research, computer-use, and embodied agents
- [LLM Application Frameworks](#llm-application-frameworks) -- Orchestration, platforms, structured output, observability
- [RAG and Vector Databases](#rag-and-vector-databases) -- Vector DBs, RAG engines, Graph RAG, document parsing, embeddings

### Train & Deploy
- [LLM Fine-Tuning Techniques](#llm-fine-tuning-techniques) -- LoRA variants, adapters, PEFT, DPO, instruction tuning
- [LLM Deployment and Serving](#llm-deployment-and-serving) -- vLLM, TGI, BentoML, and inference optimization
- [Distributed Training Frameworks](#distributed-training-frameworks) -- ColossalAI, DeepSpeed, Megatron-LM
- [Prompt Engineering](#prompt-engineering) -- CoT, ToT, GoT, and advanced prompting techniques

### Safety & Governance
- [Safety, Alignment and Governance](#safety-alignment-and-governance) -- RLHF, DPO, hallucination, AI detection, long context

### Research & Learn
- [Papers, Blogs, Courses and Lectures](#papers-blogs-courses-and-lectures) -- Frontier models, reasoning, agents, alignment, interpretability
- [Tutorials and Guides](#tutorials-and-guides) -- Courses, documentation, and hands-on learning resources
- [Top Conferences](#top-conferences) -- Academic, AGI-specific, safety, industry conferences, and MIT Imagination in Action 2026 highlights

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
|[Screenpipe](https://github.com/screenpipe/screenpipe)|![GitHub Repo stars](https://badgen.net/github/stars/screenpipe/screenpipe)|Run agents that work for you based on what you do. AI that observes your screen and acts accordingly.|18k+ stars. Context-aware desktop agent.|

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
|[gpt-researcher](https://github.com/assafelovic/gpt-researcher)|![GitHub Repo stars](https://badgen.net/github/stars/assafelovic/gpt-researcher)|GPT based autonomous agent that does online comprehensive research on any given topic.|-|
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

> Retrieval-Augmented Generation (RAG) grounds LLMs in real-world data, eliminating hallucinations and enabling knowledge-intensive applications. This section covers the full RAG stack: vector storage, retrieval engines, graph-based approaches, document parsing, and cutting-edge embedding models.

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

---

## Distributed Training Frameworks

> Training frontier models requires distributing computation across thousands of GPUs. These frameworks handle the parallelism, memory optimization, and communication needed to train models with billions (or trillions) of parameters.

![DeepSpeed](https://img.shields.io/badge/DeepSpeed-Microsoft-blue?style=flat-square) ![Megatron](https://img.shields.io/badge/Megatron-NVIDIA-76B900?style=flat-square) ![Distributed](https://img.shields.io/badge/Distributed-Multi--GPU-purple?style=flat-square)

| Name | Description | Links |
|------|-------------|-------|
| [ColossalAI](https://github.com/hpcaitech/ColossalAI) | Making large AI models cheaper, faster, and more accessible with efficient parallelism techniques. | [colossalai.org](https://colossalai.org/) |
| [DeepSpeed](https://github.com/microsoft/DeepSpeed) | Microsoft's deep learning optimization library for distributed training and inference. | [deepspeed.ai](https://www.deepspeed.ai/) |
| [Megatron-LM](https://github.com/NVIDIA/Megatron-LM) | NVIDIA's research framework for training large-scale Transformer models with model and data parallelism. | - |

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

---

## Safety, Alignment and Governance

> The most important section in this entire repository. As AI systems grow more capable, ensuring they remain safe, aligned with human values, and under meaningful control becomes the defining challenge of our era. This covers technical alignment research, adversarial attacks, governance frameworks, and the tools to detect and mitigate AI harms.

![Alignment](https://img.shields.io/badge/Alignment-RLHF_DPO-red?style=flat-square) ![Safety](https://img.shields.io/badge/Safety-Red_Teaming-orange?style=flat-square) ![Governance](https://img.shields.io/badge/Governance-Policy_&_Ethics-blue?style=flat-square) ![Interpretability](https://img.shields.io/badge/Interpretability-Mechanistic-purple?style=flat-square) ![Detection](https://img.shields.io/badge/Detection-AI_Text-green?style=flat-square)

### Safety and Alignment

| Topic | Description | Links |
|-------|-------------|-------|
| LLM Hallucination Survey | Comprehensive survey on detecting, explaining, and mitigating hallucinations in LLMs. | [Paper](https://arxiv.org/abs/2309.06794v1), [Code](https://github.com/hongbinye/Cognitive-Mirage-Hallucinations-in-LLMs) |
| Hallucination Detection | Survey on hallucination in LLMs covering detection methods and mitigation strategies. | [Paper](https://www.zhuanzhi.ai/paper/61ebe9c5007cf1373b900452ad52f0ae), [Code](https://github.com/HillZhang1999/llm-hallucination-survey) |
| LLM Attacks | Universal and transferable adversarial attacks on aligned language models (CMU research). | [Paper](https://arxiv.org/abs/2307.15043), [Code](https://github.com/llm-attacks/llm-attacks) |
| RLHF | Reinforcement Learning from Human Feedback - the key technique behind ChatGPT's alignment. | [Code Example](https://github.com/HarderThenHarder/transformers_tasks/tree/main/RLHF) |
| DPO | Direct Preference Optimization - an alternative to RLHF that trains the LM directly as a reward model. | [Paper](https://arxiv.org/abs/2305.18290), [Code](https://github.com/eric-mitchell/direct-preference-optimization) |

### AI-Generated Text Detection

| Tool/Method | Description | Links |
|-------------|-------------|-------|
| DetectGPT | Stanford method using probability curvature to detect LLM-generated text. | [Paper](https://arxiv.org/abs/2301.11305), [Code](https://ericmitchell.ai/detectgpt/) |
| Detecting LLM-Generated-Text | Comprehensive survey on the science of LLM-generated text detection. | [Paper](https://github.com/datamllab/The-Science-of-LLM-generated-Text-Detection) |
| GPTZero | AI detection model designed specifically for educators. | [GPTZero](https://gptzero.me/) |

### Long Context and Positional Encoding

| Method | Description | Links |
|--------|-------------|-------|
| RoPE (Rotary Position Embedding) | Rotary position encoding widely used in modern LLMs for handling positional information. | - |
| LongRoPE | Extends LLM context windows beyond 2 million tokens. | [Paper](https://arxiv.org/pdf/2402.13753.pdf) |
| RecurrentGPT | Interactive ultra-long text generation using recurrent prompting mechanisms. | [Paper](https://arxiv.org/abs/2305.13304), [Code](https://github.com/aiwaves-cn/RecurrentGPT) |
| MEGALODON | Efficient LLM pretraining and inference with unlimited context length. | [Paper](https://arxiv.org/pdf/2404.08801.pdf), [Code](https://github.com/XuezheMax/megalodon) |
| CLongEval | Chinese benchmark for evaluating long-context LLMs. | [Paper](https://arxiv.org/pdf/2403.03514), [Code](https://github.com/zexuanqiu/CLongEval) |

---

## ASI and Superintelligence Research

> The long game. This section tracks the organizations racing toward AGI/ASI, the books that frame the debate, the seminal papers that define the field, the benchmarks that measure progress, and the roadmaps that predict when -- and how -- we get there.

![Organizations](https://img.shields.io/badge/Organizations-OpenAI_Anthropic_DeepMind_SSI-blue?style=flat-square) ![Books](https://img.shields.io/badge/Books-27_Titles-green?style=flat-square) ![Benchmarks](https://img.shields.io/badge/Benchmarks-ARC--AGI_SWE--bench-orange?style=flat-square) ![Existential Risk](https://img.shields.io/badge/Existential_Risk-Control_Problem-red?style=flat-square)

### Key Organizations Pursuing or Studying AGI/ASI

| Organization | Focus | Links |
|-------------|-------|-------|
| **Safe Superintelligence Inc. (SSI)** | Founded by Ilya Sutskever (ex-OpenAI) in 2024. Focused solely on building safe superintelligence, avoiding distraction by product cycles. Valued at $30B+ (2025). | [ssi.inc](https://ssi.inc/) |
| **OpenAI** | Building AGI that benefits all of humanity. Created GPT-4, o1, o3 and pursues the path toward superintelligence with safety research (Superalignment team). | [openai.com](https://openai.com/) |
| **Anthropic** | AI safety company building reliable, interpretable, and steerable AI (Claude). Founded by ex-OpenAI researchers focused on Constitutional AI and alignment. | [anthropic.com](https://www.anthropic.com/) |
| **DeepMind (Google)** | Pioneered AlphaGo, AlphaFold, Gemini. Researches AGI with focus on neuroscience-inspired approaches and safety. | [deepmind.google](https://deepmind.google/) |
| **Meta Superintelligence Labs** | New Meta AI division (2025) led by Alexandr Wang, focused on building superintelligent AI systems. | [ai.meta.com](https://ai.meta.com/) |
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
| **AI Impacts** | Research organization analyzing evidence on AI timelines, risks, and impacts. | [aiimpacts.org](https://aiimpacts.org/) |
| **LessWrong / Alignment Forum** | Community discussion hub for AI alignment research, ASI forecasting, and safety strategies. | [lesswrong.com](https://www.lesswrong.com/), [alignmentforum.org](https://www.alignmentforum.org/) |
| **The Pause Letter (Future of Life Institute, 2023)** | Open letter calling for a 6-month pause on training AI systems more powerful than GPT-4. Signed by 33,000+. | [futureoflife.org](https://futureoflife.org/open-letter/pause-giant-ai-experiments/) |
| **Statement on AI Risk (CAIS, 2023)** | One-sentence statement: "Mitigating the risk of extinction from AI should be a global priority." Signed by Hinton, Bengio, and hundreds of researchers. | [safe.ai](https://www.safe.ai/work/statement-on-ai-risk) |

---

## Papers, Blogs, Courses and Lectures

> The research frontier. These papers represent the cutting edge of AI capabilities, reasoning, agent design, alignment, and interpretability -- the ideas that will define the path from today's LLMs to tomorrow's AGI.

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

### Reasoning, Scaling & Architecture Papers

| Paper | Authors | Year | Description | Links |
|-------|---------|------|-------------|-------|
| Chain-of-Thought Prompting Elicits Reasoning in LLMs | Wei et al. (Google) | 2022 | Foundational paper: intermediate reasoning steps dramatically improve LLM performance. | [Paper](https://arxiv.org/abs/2201.11903) |
| Tree of Thoughts: Deliberate Problem Solving with LLMs | Yao et al. (Princeton/Google) | 2023 | Tree-structured reasoning enabling backtracking and lookahead. | [Paper](https://arxiv.org/abs/2305.10601) |
| Let's Verify Step by Step | Lightman et al. (OpenAI) | 2023 | Process reward models (PRMs) scoring each reasoning step — the mechanism behind o1-style training. | [Paper](https://arxiv.org/abs/2305.20050) |
| Scaling LLM Test-Time Compute Optimally | Snell et al. (Berkeley) | 2024 | More compute at inference can equal more training compute on hard tasks. | [Paper](https://arxiv.org/abs/2408.03314) |
| Training Compute-Optimal LLMs (Chinchilla) | Hoffmann et al. (DeepMind) | 2022 | Optimal LLM training scales data and parameters equally. | [Paper](https://arxiv.org/abs/2203.15556) |
| Scaling Laws for Neural Language Models | Kaplan et al. (OpenAI) | 2020 | Power-law relationships between model scale and performance, underpinning AGI scaling hypotheses. | [Paper](https://arxiv.org/abs/2001.08361) |
| Video Generation Models as World Simulators (Sora) | OpenAI | 2024 | Sora: text-to-video diffusion transformer that models physics and long-horizon consistency. | [Blog](https://openai.com/research/video-generation-models-as-world-simulators) |
| Genie: Generative Interactive Environments | Bruce et al. (DeepMind) | 2024 | Learns playable 2D world models from unlabeled internet video. | [Paper](https://arxiv.org/abs/2402.15391) |
| LongRoPE: Extending LLM Context Beyond 2M Tokens | Ding et al. (Microsoft) | 2024 | Extends RoPE to 2M tokens via non-uniform interpolation. | [Paper](https://arxiv.org/abs/2402.13753) |
| Infini-Attention | Munkhdalai et al. (Google) | 2024 | Compressive memory in standard attention for infinite-length inputs with bounded memory. | [Paper](https://arxiv.org/abs/2404.07143) |

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
| **Imagination in Action @ MIT** | Imagination in Action + MIT CSAIL | Apr, Annual | [imaginationinaction.co](https://imaginationinaction.co) | MIT-hosted summit on AGI, agentic AI, world models, and AI governance. Speakers from OpenAI, DeepMind, Amazon AGI, LiquidAI, Salesforce, Stanford HAI. 3 stages, 40+ sessions. |

### MIT Imagination in Action Summit -- AGI/ASI Highlights (April 2026)

> The Imagination in Action summit at MIT brought together frontier AI researchers, industry leaders, and policymakers across three stages (Futurist Forum, Tech Talks, Builder's Lab) for a full-day deep dive into the path toward general intelligence. Below are the sessions most relevant to AGI and ASI.

| Session | Stage | Speakers | AGI/ASI Relevance |
|---------|-------|----------|-------------------|
| **The Road to General Intelligence** | Tech Talks | Rohit Prasad (Amazon, Former SVP & Head Scientist of AGI), Steve Frey (AGI, Inc. Co-Founder), Christopher O'Donnell (Day AI) | Where AGI research stands today -- from frontier labs to AI-native products putting general capabilities into users' hands. |
| **The Architecture of Intelligence** | Forum | Peter Danenberg (Google DeepMind), Alexander Amini (LiquidAI, Co-Founder & CSO) | Deep dive into frontier AI system design -- model architecture, reasoning, scaling laws, and the path toward more general intelligence. |
| **World Models and the Inflection Point of Intelligence** | Forum | Aleksander Madry (OpenAI), Daniela Rus (MIT CSAIL Director) | Frontier AI research on world models and the inflection point where machine intelligence reshapes scientific discovery. |
| **A Pro Human Future** | Forum (Keynote) | Max Tegmark (MIT, Professor of Physics & AI), Ramesh Raskar (MIT Media Lab) | Keynote on ensuring AI amplifies human agency, creativity, and flourishing -- not replaces it. Tegmark is author of *Life 3.0*. |
| **Intelligence at Scale: Building the Next Era of AI** | Forum | Rohit Prasad (Amazon AGI), Daniela Rus (MIT CSAIL) | How AI is moving from breakthrough models to systems that shape how we work, communicate, and make decisions. |
| **The Neuroscience of Intelligence** | Tech Talks | Manolis Kellis (MIT & Broad Institute), Simran Chana (Cambridge, Frontier Technologies Lab), David Rock (NeuroLeadership Institute) | What neuroscience reveals about how intelligence works -- and how those insights inform next-generation AI architectures. |
| **Embodied Intelligence: How Machines Learn, Move, and Decide** | Forum | Daniela Rus, Russ Tedrake, Leslie Pack Kaelbling (all MIT CSAIL) | Latest from MIT robotics on how machines learn to move, manipulate, and decide in the physical world. |
| **Building the Agentic Enterprise** | Forum (Fireside) | Wade Foster (Zapier, Co-Founder & CEO) | Building agentic systems at enterprise scale -- how AI agents and the future of work converge inside real organizations. |
| **Governance in the Age of AI** | Tech Talks | Hamid Rashid (Global Algorithmic Institute), Suneel Ratan (Precognitive), Moinul Khan (Aurascape AI) | The governance gap: are institutions and frameworks keeping pace as AI capabilities accelerate? |
| **Human-centered AI** | Tech Talks | Rumman Chowdhury (Humane Intelligence CEO), Stephen Casper (MIT), Keyun Ruan (Harvard AI & Flourishing) | Designing AI systems that serve human needs first -- frameworks and trade-offs for human-centered AGI. |
| **Trust in the Intelligent World** | Forum | Rumman Chowdhury (Humane Intelligence), Noelle Russell (AI Leadership Institute), Ashley Reichheld (Deloitte Digital) | Building trust at institutional scale -- responsible deployment and what defines ethical AI. |
| **Building the Backbone: Energy, Compute, and the Future of Infrastructure** | Forum | Jeremy Kepner (MIT Lincoln Lab, Head of Supercomputing), Chase Lochmiller (Crusoe CEO), Libby Wayman (Breakthrough Energy Ventures) | The physical bottleneck behind AI's exponential growth -- power plants, data centers, and the compute fabric the frontier depends on. |
| **AI, Power, and the Global Chessboard** | Forum (Fireside) | Mark Machin (Intrepid Growth Partners), Alvin Graylin (Stanford HAI), Sean Batir (AWS, Global Head of Mission Innovation) | How AI is reshaping global competition -- cloud infrastructure, defense, capital flows, and the shifting balance of power. |
| **Leading at the Frontier** | Forum (Fireside) | Marc Benioff (Salesforce, Chair & CEO) | Leading an AI-first enterprise -- transformation at scale, trust, and what comes next. |
| **Biotech Meets AI** | Builder's Lab | Alexander Wissner-Gross, Fridolin Haugg (Harvard Medical School), Disleve Kanku (OncoSys AI) | Convergence of computational biology and AI -- drug discovery, clinical trial optimization, and molecular intelligence. |
| **Planetary Intelligence** | Builder's Lab | Priya Donti (Climate Change AI, MIT EECS), Libby Wayman (Breakthrough Energy Ventures) | Deploying AI for climate, sustainability, and Earth systems -- planetary-scale problems meet planetary-scale intelligence. |

---

## Contributing

We're building the most comprehensive AGI/ASI resource on the internet -- and we need your help. Contributions are welcome!

**How to contribute:**

1. **Fork** this repository
2. **Add** your resource following the format below
3. **Open a Pull Request** with your additions

**Format:**
- **Title** - Author(s) (Year). [Link](URL) - One-line description

### Guidelines
- Use official links (DOI, arXiv, publisher, GitHub)
- Ensure title, author(s), year are correct
- Keep descriptions short (1 line)
- Avoid duplicates -- search the README first
- Include GitHub star counts for repositories when available
- Open a Pull Request with your additions

---

## License

[Apache-2.0](LICENSE)

---

> **If you find this resource useful, please give it a star!** It helps others discover it and motivates us to keep it updated as the field evolves at breakneck speed.
