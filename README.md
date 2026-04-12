# Awesome AGI and ASI Resources [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

![AGI](https://img.shields.io/badge/AGI-Artificial_General_Intelligence-blue)
![ASI](https://img.shields.io/badge/ASI-Artificial_Superintelligence-red)
![Super AI](https://img.shields.io/badge/Super_AI-Beyond_Human_Intelligence-purple)
![AI Safety](https://img.shields.io/badge/AI_Safety-Alignment_&_Control-green)
![LLM](https://img.shields.io/badge/LLM-Large_Language_Models-orange)
![Agents](https://img.shields.io/badge/Agents-Autonomous_AI-yellow)

A comprehensive, curated collection of resources on **Artificial General Intelligence (AGI)**, **Artificial Superintelligence (ASI)**, and **Super AI** -- covering frameworks, agents, research papers, safety & alignment, books, benchmarks, and tools.

Related Resources:  [LangGPT](https://github.com/yzfly/LangGPT) | [ML Papers Explained](https://github.com/dair-ai/ML-Papers-Explained) | [Awesome AGI & ASI by shajibghosh](https://github.com/shajibghosh/Awesome-AGI-and-ASI)

---

## What is AGI?
> **Artificial General Intelligence (AGI)** refers to advanced AI systems that exhibit human-like cognitive abilities across various tasks and domains. Unlike narrow AI, which excels in specific tasks, AGI aims to encompass learning, reasoning, problem-solving, perception, and natural language understanding. Although AGI remains an ambitious goal, its pursuit has led to numerous AI advancements. The development of AGI holds the potential to revolutionize industries such as healthcare, finance, transportation, and education, while also raising ethical, safety, and societal concerns that must be carefully addressed.

## What is ASI (Artificial Superintelligence)?
> **Artificial Superintelligence (ASI)**, also referred to as **Super AI**, is a hypothetical AI agent that possesses intelligence surpassing the most gifted human minds in virtually all domains -- including scientific creativity, social skills, and general wisdom. Philosopher Nick Bostrom defines it as "any intellect that greatly exceeds the cognitive performance of humans in virtually all domains of interest." ASI could emerge from recursive self-improvement cycles (an "intelligence explosion"), where an AI capable of improving its own design rapidly exceeds human-level capabilities. Key concerns include the **control problem** (ensuring ASI remains aligned with human values), **goal misalignment** (unintended optimization targets), and the potential for an **intelligence explosion** leading to a technological singularity.

### Levels of AI Intelligence
| Level | Type | Description |
|-------|------|-------------|
| 1 | **ANI** (Artificial Narrow Intelligence) | AI excelling at a single specific task (e.g., chess, image recognition, language translation). |
| 2 | **AGI** (Artificial General Intelligence) | AI with human-level cognitive abilities across all intellectual tasks. |
| 3 | **ASI** (Artificial Superintelligence) | AI that vastly surpasses the best human minds in every domain, including creativity, problem-solving, and social intelligence. |

## Table of Contents

- [Awesome AGI and ASI Resources](#awesome-agi-and-asi-resources-)
  - [What is AGI?](#what-is-agi)
  - [What is ASI?](#what-is-asi-artificial-superintelligence)
  - [Frameworks and Platforms](#frameworks-and-platforms)
    - [Next-Generation Agent Frameworks (2024-2026)](#next-generation-agent-frameworks-2024-2026)
    - [Established Agent Frameworks](#established-agent-frameworks)
    - [Specialized & Utility Frameworks](#specialized--utility-frameworks)
  - [Agents](#agents)
  - [LLM Application Frameworks](#llm-application-frameworks)
  - [RAG and Vector Databases](#rag-and-vector-databases)
  - [LLM Fine-Tuning Techniques](#llm-fine-tuning-techniques)
  - [LLM Deployment and Serving](#llm-deployment-and-serving)
  - [Prompt Engineering](#prompt-engineering)
  - [Safety, Alignment and Governance](#safety-alignment-and-governance)
  - [ASI and Superintelligence Research](#asi-and-superintelligence-research)
    - [Key Organizations](#key-organizations-pursuing-or-studying-agisi)
    - [Books on AGI and ASI](#books-on-agi-asi-and-superintelligence)
    - [Seminal Papers on ASI](#seminal-papers-on-asi-and-superintelligence)
    - [AGI/ASI Benchmarks and Evaluation](#agiasi-benchmarks-and-evaluation)
    - [Roadmaps and Perspectives](#roadmaps-perspectives-and-timelines)
  - [Papers, Blogs, Courses and Lectures](#papers-blogs-courses-and-lectures)
    - [Papers](#papers)
    - [Blogs and News](#blogs-and-news)
  - [Tutorials and Guides](#tutorials-and-guides)

---

## Frameworks and Platforms

### Next-Generation Agent Frameworks (2024-2026)

|Name|Github Stars|Introduction| Notes |
|-|-|-|-|
|[:fire: OpenHands](https://github.com/All-Hands-AI/OpenHands)|![GitHub Repo stars](https://badgen.net/github/stars/All-Hands-AI/OpenHands)|AI-powered software development agent platform (formerly OpenDevin). Autonomous coding agent that can write, test, and debug code end-to-end.|71k+ stars. #1 on SWE-bench. Sandboxed execution environment.|
|[:fire: browser-use](https://github.com/browser-use/browser-use)|![GitHub Repo stars](https://badgen.net/github/stars/browser-use/browser-use)|Make websites accessible for AI agents. Automate tasks online with ease using Playwright-based browser automation.|87k+ stars. AI agents that browse the web autonomously.|
|[:fire: DeerFlow](https://github.com/bytedance/deer-flow)|![GitHub Repo stars](https://badgen.net/github/stars/bytedance/deer-flow)|ByteDance's open-source long-horizon SuperAgent harness that researches, codes, and creates. Multi-agent with sandboxes, memories, tools, and skills.|60k+ stars. Built on LangGraph.|
|[:fire: Firecrawl](https://github.com/firecrawl/firecrawl)|![GitHub Repo stars](https://badgen.net/github/stars/firecrawl/firecrawl)|The Web Data API for AI - Power AI agents with clean web data. Scrapes and converts websites to LLM-ready markdown.|108k+ stars. Used by major AI agent frameworks.|
|[:fire: crewAI](https://github.com/joaomdmoura/crewAI)|![GitHub Repo stars](https://badgen.net/github/stars/joaomdmoura/crewAI)|Framework for orchestrating role-playing, autonomous AI agents. Craft collaborative AI crews for complex tasks.|Production-grade multi-agent orchestration.|
|[:fire: agenticSeek](https://github.com/Fosowl/agenticSeek)|![GitHub Repo stars](https://badgen.net/github/stars/Fosowl/agenticSeek)|Fully local autonomous agent - No APIs, no monthly bills. Thinks, browses the web, and codes using only local LLMs.|26k+ stars. Fully local, privacy-first.|
|[Gemini CLI](https://github.com/google-gemini/gemini-cli)|![GitHub Repo stars](https://badgen.net/github/stars/google-gemini/gemini-cli)|Google's open-source AI agent that brings Gemini directly into your terminal. MCP support built-in.|101k+ stars. Official Google agent.|
|[Hermes Agent](https://github.com/NousResearch/hermes-agent)|![GitHub Repo stars](https://badgen.net/github/stars/NousResearch/hermes-agent)|The agent that grows with you. By Nous Research - multi-model AI agent with Claude, GPT, and open-source model support.|66k+ stars. From Nous Research.|
|[Daytona](https://github.com/daytonaio/daytona)|![GitHub Repo stars](https://badgen.net/github/stars/daytonaio/daytona)|Secure and elastic infrastructure for running AI-generated code. Sandboxed execution environment for AI agents.|72k+ stars. Secure code execution.|
|[Composio](https://github.com/ComposioHQ/composio)|![GitHub Repo stars](https://badgen.net/github/stars/ComposioHQ/composio)|Production-ready toolset for AI agents. 250+ tools, frameworks, and integrations for building agentic AI applications.|[composio.dev](https://composio.dev/)|
|[PentAGI](https://github.com/vxcontrol/pentagi)|![GitHub Repo stars](https://badgen.net/github/stars/vxcontrol/pentagi)|Fully autonomous AI agent system for complex penetration testing tasks. Multi-agent security automation.|15k+ stars. Autonomous security testing.|
|[Screenpipe](https://github.com/screenpipe/screenpipe)|![GitHub Repo stars](https://badgen.net/github/stars/screenpipe/screenpipe)|Run agents that work for you based on what you do. AI that observes your screen and acts accordingly.|18k+ stars. Context-aware desktop agent.|

### Established Agent Frameworks

|Name|Github Stars|Introduction| Notes |
|-|-|-|-|
|[:fire: Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT)|![GitHub Repo stars](https://badgen.net/github/stars/Significant-Gravitas/Auto-GPT)|The original autonomous AI agent. Now evolved into a full platform for building and deploying autonomous agents.|183k+ stars. The project that started the autonomous agent movement.|
|[:fire: MetaGPT](https://github.com/geekan/MetaGPT)|![GitHub Repo stars](https://badgen.net/github/stars/geekan/MetaGPT)|The Multi-Agent Framework: Given one line Requirement, return PRD, Design, Tasks, Repo.|Mimics a software company with PM, architect, and engineer agent roles.|
|[:fire: AgentGPT](https://github.com/reworkd/AgentGPT)|![GitHub Repo stars](https://badgen.net/github/stars/reworkd/AgentGPT)|Assemble, configure, and deploy autonomous AI Agents in your browser.|36k+ stars. Browser-based agent deployment.|
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

|Name|Github Stars|Introduction| Notes |
|-|-|-|-|
|[:fire: generative_agents](https://github.com/joonspk-research/generative_agents)|![GitHub Repo stars](https://badgen.net/github/stars/joonspk-research/generative_agents)|Generative Agents: Interactive Simulacra of Human Behavior.| Stanford & Google research: 25 AI agents living in a simulated town with unique identities, memories, and behaviors. [Paper](https://arxiv.org/abs/2304.03442)|
|[:fire: ai-town](https://github.com/a16z-infra/ai-town)|![GitHub Repo stars](https://badgen.net/github/stars/a16z-infra/ai-town)|A MIT-licensed, deployable starter kit for building and customizing your own version of AI town - a virtual town where AI characters live, chat and socialize.|-|
|[:fire: gpt-engineer](https://github.com/AntonOsika/gpt-engineer)|![GitHub Repo stars](https://badgen.net/github/stars/AntonOsika/gpt-engineer)|Specify what you want it to build, the AI asks for clarification, and then builds it.|-|
|[:fire: MetaGPT](https://github.com/geekan/MetaGPT) |![GitHub Repo stars](https://badgen.net/github/stars/geekan/MetaGPT)|The Multi-Agent Framework: Given one line Requirement, return PRD, Design, Tasks, Repo.|-|
|[gpt-researcher](https://github.com/assafelovic/gpt-researcher)|![GitHub Repo stars](https://badgen.net/github/stars/assafelovic/gpt-researcher)|GPT based autonomous agent that does online comprehensive research on any given topic.|-|
|[llama-hub, shopify agent](https://github.com/emptycrown/llama-hub/blob/main/llama_hub/tools/notebooks/shopify.ipynb)|![GitHub Repo stars](https://badgen.net/github/stars/emptycrown/llama-hub)|A customer support agent that can interface with Shopify's ENTIRE GraphQL API Spec (>50k lines!).|-|
|[FastGPT](https://github.com/labring/FastGPT)|![GitHub Repo stars](https://badgen.net/github/stars/labring/FastGPT)|FastGPT is a knowledge-based question answering system built on LLMs. Offers out-of-the-box data processing, model invocation capabilities, and workflow orchestration through Flow visualization.|-|
|[AutoGen](https://github.com/microsoft/autogen)|![GitHub Repo stars](https://badgen.net/github/stars/microsoft/autogen)|AutoGen is a framework that enables development of LLM applications using multiple agents that can converse with each other to solve tasks. Developed by Microsoft, supports multi-agent communication, human feedback, and tool integration.|-|
|[Agents](https://github.com/aiwaves-cn/agents)|![GitHub Repo stars](https://badgen.net/github/stars/aiwaves-cn/agents)|An Open-source Framework for Autonomous Language Agents.|[Paper](https://arxiv.org/pdf/2309.07870.pdf), [aiwaves-agents.com](http://www.aiwaves-agents.com/)|
|[HuggingGPT](https://github.com/microsoft/JARVIS)|![GitHub Repo stars](https://badgen.net/github/stars/microsoft/JARVIS)|Uses ChatGPT as a controller to manage AI models on HuggingFace for solving complex AI tasks across language, vision, and speech.|[HuggingGPT Demo](https://huggingface.co/spaces/microsoft/HuggingGPT)|
|[RestGPT](https://github.com/Yifan-Song793/RestGPT)|![GitHub Repo stars](https://badgen.net/github/stars/Yifan-Song793/RestGPT)|Connecting Large Language Models with Real-World RESTful APIs for autonomous API interaction.|[Paper](https://arxiv.org/abs/2306.06624)|
|[RoboGen](https://github.com/Genesis-Embodied-AI)|![GitHub Repo stars](https://badgen.net/github/stars/Genesis-Embodied-AI/RoboGen)|Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation.|[Paper](https://arxiv.org/abs/2311.01455), [Project Page](https://robogen-ai.github.io/)|
|[Toolformer](https://arxiv.org/pdf/2302.04761.pdf)|-|Language Models Can Teach Themselves to Use Tools. Meta AI research on LLMs learning when and how to call external APIs.|[Paper](https://arxiv.org/pdf/2302.04761.pdf)|
|[FixAgent](https://arxiv.org/abs/2404.17153)|-|A multi-agent system for automated debugging that improves model debug capability by ~20%.|[Paper](https://arxiv.org/abs/2404.17153)|
|[NexusGPT](https://nexus.snikpic.io/)|-|A marketplace and platform for building AI agents with no-code tools.|[NexusGPT](https://nexus.snikpic.io/)|
|[Godmode](https://godmode.space/)|-|Web-based autonomous AI agent interface for exploring the capabilities of autoGPT.|[Godmode](https://godmode.space/)|
|[Do Anything Machine](https://www.doanythingmachine.com/)|-|A web-based AI agent that attempts to accomplish any task you describe.|[Demo](https://www.doanythingmachine.com/)|

---

## LLM Application Frameworks

| Name | Description | Links |
|------|-------------|-------|
| [LangChain](https://github.com/langchain-ai/langchain) | Framework for developing applications powered by language models. Enables chaining of LLM calls with tools, memory, and retrieval. | [Docs](https://python.langchain.com/docs/) |
| [LlamaIndex](https://github.com/run-llama/llama_index) | Data framework for LLM applications. Connect custom data sources to LLMs with indexing, retrieval, and query interfaces. | [Docs](https://docs.llamaindex.ai/) |
| [LangSmith](https://www.langchain.com/langsmith) | Platform by LangChain for debugging, testing, evaluating, and monitoring LLM chains and agents. | [Docs](https://python.langchain.com/docs/langsmith/walkthrough) |
| [LangFuse](https://langfuse.com/) | Open-source LLM engineering platform. Traces, evals, prompt management and metrics for LLM apps. | [GitHub](https://github.com/langfuse) |
| [Opik](https://github.com/comet-ml/opik) | Open-source LLM observability and evaluation platform. Supports tracing, evaluation, and prompt optimization. | [Docs](https://www.comet.com/docs/opik/) |
| [TaskingAI](https://github.com/TaskingAI/TaskingAI) | BaaS (Backend as a Service) platform for LLM-based agent development with integrated tools and retrieval. | [Docs](https://docs.tasking.ai/) |

---

## RAG and Vector Databases

### Vector Databases

| Name | Description | Links |
|------|-------------|-------|
| [Chroma](https://github.com/chroma-core/chroma) | Open-source embedding database for building AI apps with embeddings and LLMs. | [Docs](https://docs.trychroma.com/) |
| [Milvus](https://github.com/milvus-io/milvus) | Open-source vector database for scalable similarity search and AI applications. | [milvus.io](https://milvus.io/) |
| [Pinecone](https://www.pinecone.io/) | Managed vector database for high-performance vector search at scale. | [Docs](https://docs.pinecone.io/) |
| [Weaviate](https://github.com/weaviate/weaviate) | Open-source vector search engine with built-in vectorization and hybrid search. | [weaviate.io](https://weaviate.io/) |
| [Qdrant](https://github.com/qdrant/qdrant) | High-performance vector similarity search engine with filtering support. | [qdrant.tech](https://qdrant.tech/) |
| [LanceDB](https://github.com/lancedb/lancedb) | Serverless vector database for AI applications, built on Lance columnar format. | [lancedb.com](https://lancedb.com/) |
| [Zilliz](https://zilliz.com/) | Cloud-native vector database service (managed Milvus). | [zilliz.com](https://zilliz.com/) |
| [DingoDB](https://github.com/dingodb/dingo) | Distributed multi-modal vector database for real-time data analysis. | [dingodb.com](https://www.dingodb.com/) |

### RAG Tools and Platforms

| Name | Description | Links |
|------|-------------|-------|
| [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm) | All-in-one AI application that can use any LLM, any document, and any vector database. | [useanything.com](https://useanything.com/) |
| [QAnything](https://github.com/netease-youdao/QAnything) | Question answering system based on anything (files, URLs, databases) by NetEase Youdao. | - |

---

## LLM Fine-Tuning Techniques

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

| Name | Description | Links |
|------|-------------|-------|
| [ColossalAI](https://github.com/hpcaitech/ColossalAI) | Making large AI models cheaper, faster, and more accessible with efficient parallelism techniques. | [colossalai.org](https://colossalai.org/) |
| [DeepSpeed](https://github.com/microsoft/DeepSpeed) | Microsoft's deep learning optimization library for distributed training and inference. | [deepspeed.ai](https://www.deepspeed.ai/) |
| [Megatron-LM](https://github.com/NVIDIA/Megatron-LM) | NVIDIA's research framework for training large-scale Transformer models with model and data parallelism. | - |

---

## Prompt Engineering

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

### Books on AGI, ASI, and Superintelligence

| Book | Author(s) | Year | Description |
|------|-----------|------|-------------|
| **Superintelligence: Paths, Dangers, Strategies** | Nick Bostrom | 2014 | The foundational book on ASI risks. Examines paths to superintelligence and strategies for ensuring it remains beneficial. |
| **Life 3.0: Being Human in the Age of Artificial Intelligence** | Max Tegmark | 2017 | Explores how AGI/ASI could transform every aspect of life, from warfare to work, and what we can do to ensure a good outcome. |
| **Human Compatible: Artificial Intelligence and the Problem of Control** | Stuart Russell | 2019 | Proposes a new framework for AI development based on uncertainty about human preferences to solve the control problem. |
| **The Alignment Problem: Machine Learning and Human Values** | Brian Christian | 2020 | Explores the technical and societal challenges of aligning AI systems with human values. |
| **AI 2041: Ten Visions for Our Future** | Kai-Fu Lee, Chen Qiufan | 2021 | Ten stories imagining how AI will transform the world over the next two decades, blending fiction with AI expertise. |
| **Power and Prediction: The Disruptive Economics of Artificial Intelligence** | Ajay Agrawal, Joshua Gans, Avi Goldfarb | 2022 | How AI shifts decision-making economics and creates system-level disruption. |
| **The Coming Wave: Technology, Power, and the 21st Century's Greatest Dilemma** | Mustafa Suleyman | 2023 | DeepMind co-founder on the unstoppable wave of AI and synthetic biology, and the containment problem. |
| **Co-Intelligence: Living and Working with AI** | Ethan Mollick | 2024 | Practical guide on how humans and AI can work together, based on extensive hands-on research with frontier models. |
| **Situational Awareness: The Decade Ahead** | Leopold Aschenbrenner | 2024 | Former OpenAI researcher's detailed analysis of the path from GPT-4 to AGI/ASI within this decade. |
| **Our Final Invention: Artificial Intelligence and the End of the Human Era** | James Barrat | 2013 | Investigative account of the race toward AGI and the existential risks of superintelligence. |
| **The Singularity Is Near** | Ray Kurzweil | 2005 | Foundational forecast of the technological singularity driven by exponential growth in AI, genetics, and nanotech. |
| **The Singularity Is Nearer** | Ray Kurzweil | 2024 | Updated vision with two decades of new evidence, arguing the singularity arrives by 2045. |

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

### Papers

| Paper | Description | Links |
|-------|-------------|-------|
| Generative Agents: Interactive Simulacra of Human Behavior | Stanford/Google research on AI agents simulating human behavior in a virtual town. | [Paper](https://arxiv.org/abs/2304.03442) |
| HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face | System using ChatGPT to orchestrate specialized AI models. | [Paper](https://arxiv.org/abs/2303.17580) |
| Toolformer: Language Models Can Teach Themselves to Use Tools | Meta AI research on LLMs learning API tool use. | [Paper](https://arxiv.org/pdf/2302.04761.pdf) |
| Chain-of-Thought Prompting Elicits Reasoning in LLMs | Foundational paper on CoT prompting by Google. | [Paper](https://arxiv.org/abs/2201.11903) |
| Tree of Thoughts: Deliberate Problem Solving with LLMs | Tree-structured reasoning for complex problems. | [Paper](https://arxiv.org/abs/2305.10601) |
| LoRA: Low-Rank Adaptation of Large Language Models | Parameter-efficient fine-tuning through low-rank decomposition. | [Paper](https://arxiv.org/pdf/2106.09685.pdf) |
| QLoRA: Efficient Finetuning of Quantized LLMs | 4-bit quantized fine-tuning enabling LLM training on consumer GPUs. | [Paper](https://arxiv.org/abs/2305.14314) |
| Instruction Tuning for LLMs: A Survey | Comprehensive survey on instruction tuning techniques. | [Paper](https://arxiv.org/abs/2308.10792) |
| Agents: An Open-source Framework for Autonomous Language Agents | Framework for building autonomous language agents. | [Paper](https://arxiv.org/pdf/2309.07870.pdf) |
| RestGPT: Connecting LLMs with Real-World RESTful APIs | Enabling LLMs to autonomously interact with REST APIs. | [Paper](https://arxiv.org/abs/2306.06624) |
| RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning | Generative simulation for robot learning. | [Paper](https://arxiv.org/abs/2311.01455) |

### Blogs and News

| Resource | Description |
|----------|-------------|
| [OpenAI Blog](https://openai.com/blog) | Official blog from OpenAI with research updates and announcements. |
| [Google AI Blog](https://ai.googleblog.com/) | Google's AI research blog. |
| [HuggingFace Blog](https://huggingface.co/blog) | Latest in open-source ML and NLP. |
| [LangChain Blog](https://blog.langchain.dev/) | Updates on LangChain framework and LLM applications. |
| [The Gradient](https://thegradient.pub/) | Perspectives on AI research and its implications. |
| [Lilian Weng's Blog](https://lilianweng.github.io/) | In-depth technical posts on LLMs, agents, and AI research. |

---

## Tutorials and Guides

| Resource | Description | Links |
|----------|-------------|-------|
| [awesome-agi-cocosci](https://github.com/YuzheSHI/awesome-agi-cocosci) | Collection of resources on AGI from the perspective of cognitive science. | [GitHub](https://github.com/YuzheSHI/awesome-agi-cocosci) |
| [Prompt Engineering Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) | Comprehensive guide to prompt engineering techniques, papers, and tools. | [promptingguide.ai](https://www.promptingguide.ai/) |
| [LLM Course](https://github.com/mlabonne/llm-course) | Course to get into Large Language Models with roadmaps and Colab notebooks. | [GitHub](https://github.com/mlabonne/llm-course) |
| [LangChain Documentation](https://python.langchain.com/docs/) | Official documentation and tutorials for the LangChain framework. | [Docs](https://python.langchain.com/docs/) |
| [LlamaIndex Documentation](https://docs.llamaindex.ai/) | Official docs for LlamaIndex data framework. | [Docs](https://docs.llamaindex.ai/) |
| [PEFT Documentation](https://huggingface.co/docs/peft/) | HuggingFace's guide to parameter-efficient fine-tuning methods. | [Docs](https://huggingface.co/docs/peft/) |

---

## Contributing

Contributions are welcome! Please follow this format when adding resources:

- **Title** - Author(s) (Year). [Link](URL) - One-line description

### Guidelines
- Use official links (DOI, arXiv, publisher, GitHub)
- Ensure title, author(s), year are correct
- Keep descriptions short (1 line)
- Avoid duplicates
- Open a Pull Request with your additions

---

## License

[Apache-2.0](LICENSE)
