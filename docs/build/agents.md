---
description: "Autonomous AI systems that perceive, reason, and act in the world. These agents represent the closest things we have to AGI-like behavior in narrow domains -- writing code, conducting research, operating computers, and navigating virtual worlds."
keywords: "AI agents, coding agents, research agents, computer use agents, embodied AI, autonomous systems, Devin, SWE-agent"
---
# Agents

> Autonomous AI systems that perceive, reason, and act in the world. These agents represent the closest things we have to AGI-like behavior in narrow domains -- writing code, conducting research, operating computers, and navigating virtual worlds.

![Coding](https://img.shields.io/badge/Coding-green?style=flat-square) ![Research](https://img.shields.io/badge/Research-purple?style=flat-square) ![Computer Use](https://img.shields.io/badge/Computer_Use-blue?style=flat-square) ![Embodied](https://img.shields.io/badge/Embodied-red?style=flat-square) ![Autonomous](https://img.shields.io/badge/Autonomous-orange?style=flat-square)

### Coding & Software Engineering Agents

|Name|Github Stars|Introduction| Notes |
|-|-|-|-|
|[Aider](https://github.com/Aider-AI/aider)|![GitHub Repo stars](https://badgen.net/github/stars/Aider-AI/aider)|AI pair programming in your terminal. Edit code across your entire repo with LLMs. Tops SWE-bench Lite.|Best-in-class AI pair programmer. Works with GPT-4o, Claude, DeepSeek, local models.|
|[SWE-agent](https://github.com/princeton-nlp/SWE-agent)|![GitHub Repo stars](https://badgen.net/github/stars/princeton-nlp/SWE-agent)|Turns LLMs into software engineering agents that fix real GitHub issues. Pioneered the Agent-Computer Interface (ACI) concept.|[Paper](https://arxiv.org/abs/2405.15232). Princeton NLP. Key SWE-bench benchmark agent.|
|[goose](https://github.com/block/goose)|![GitHub Repo stars](https://badgen.net/github/stars/block/goose)|Open-source extensible AI agent that goes beyond code suggestions — install, execute, edit, and test with any LLM. Written in Rust.|Supports MCP and ACP protocols. By Block.|
|[Open Interpreter](https://github.com/OpenInterpreter/open-interpreter)|![GitHub Repo stars](https://badgen.net/github/stars/OpenInterpreter/open-interpreter)|A natural language interface for computers. Lets LLMs run code (Python, JS, shell) locally with no restrictions.|Full computer control via natural language. Like ChatGPT Code Interpreter but unrestricted.|
|Cursor Composer 2|N/A|Next-generation IDE incorporating Kimi K2.5 model. Beats Anthropic Opus 4.6 on major coding benchmarks at lower cost.|AI-native IDE with frontier model integration.
|Opencode|N/A|Open source AI coding agent using most models including free and local. Terminal, desktop, IDE, or extension. Privacy-sensitive environments.|Multi-model, privacy-first coding agent.
|Claude Review|N/A|Code review on every pull request that Claude Code makes. Research preview for Claude Teams and Enterprise.|Automated PR review for AI-generated code.

### Research & Knowledge Agents

|Name|Github Stars|Introduction| Notes |
|-|-|-|-|
|[STORM](https://github.com/stanford-oval/storm)|![GitHub Repo stars](https://badgen.net/github/stars/stanford-oval/storm)|Stanford: Synthesis of Topic Outlines through Retrieval and Multi-perspective Question Asking. Writes Wikipedia-quality long-form articles autonomously.|[Paper](https://arxiv.org/abs/2402.14207). Expert-level knowledge synthesis agent.|
|[AI Scientist](https://github.com/SakanaAI/AI-Scientist)|![GitHub Repo stars](https://badgen.net/github/stars/SakanaAI/AI-Scientist)|Fully autonomous scientific research pipeline: generates ideas, implements experiments, writes and reviews full academic papers.|[Paper](https://arxiv.org/abs/2408.06292). By Sakana AI. ASI-threshold capability.|
|[gpt-researcher](https://github.com/assafelovic/gpt-researcher)|![GitHub Repo stars](https://badgen.net/github/stars/assafelovic/gpt-researcher)|GPT-based autonomous agent for comprehensive online research on any topic. Searches, reads, and synthesizes long-form reports.|-|
|[mem0](https://github.com/mem0ai/mem0)|![GitHub Repo stars](https://badgen.net/github/stars/mem0ai/mem0)|Universal memory layer for AI agents. Persistent long-term, episodic, and semantic memory across agent sessions.|52k+ stars. Key missing component between current agents and AGI.|
|Autoresearch|N/A|Automates the scientific method with AI agents. Runs hundreds of ML experiments per night - experiment, results, modify code, repeat.|By Andrej Karpathy. ASI-threshold automation.
|Claude Code Channels|N/A|Experimental feature allowing communication with Claude using Telegram or Discord. Competes with OpenClaw.|Multi-platform Claude integration.
|Claude Cowork Dispatch|N/A|Control Claude Cowork from your phone. Claude runs on computer, assign tasks from anywhere, get text notification when done.|Remote Claude control via mobile.

### Computer-Use & Desktop Agents

|Name|Github Stars|Introduction| Notes |
|-|-|-|-|
|[everything-claude-code](https://github.com/anthropics/claude-code)|![GitHub Repo stars](https://badgen.net/github/stars/anthropics/claude-code)|Agent harness performance optimization system with skills, instincts, memory, and security for AI coding agents.|Cognitive scaffolding for agentic AI — directly relevant to persistent AGI.|
|[nanobot](https://github.com/HKUDS/nanobot)|![GitHub Repo stars](https://badgen.net/github/stars/HKUDS/nanobot)|Ultra-lightweight personal AI agent. Minimal footprint with full agent capabilities.|39k+ stars. Edge-AGI and ubiquitous deployment.|
|[Screenpipe](https://github.com/screenpipe/screenpipe)|![GitHub Repo stars](https://badgen.net/github/stars/screenpipe/screenpipe)|Run agents that work for you based on what you do. Continuously observes your screen, builds personal memory, and triggers AI actions.|Always-on environmental awareness — a prototype AGI assistant.|

### Local Agent Stacks

> Local-first agent orchestration stacks that replace cloud-based model dependence with on-device deployment.

| Name | Introduction | Notes |
|------|--------------|-------|
| Qwen-3-coder | Local agent stack for coding that can replace cloud-based orchestration tools. | Local-first coding agent infrastructure. |
| Ollama | Run Llama, Mistral, and other models locally. Simple CLI for local model deployment and inference. | Local model serving for agents. |
| goose | Already listed in coding agents - local agent framework supporting MCP and ACP protocols. | Local agent framework (see Coding & Software Engineering Agents). |

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
