# Awesome AGI Resources [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) 

A curated list of awesome AGI frameworks, software, and resources.

Related Resources:  [LangGPT](https://github.com/yzfly/LangGPT) | [ML Papers Explained](https://github.com/dair-ai/ML-Papers-Explained)

## What is AGI?
> Artificial General Intelligence (AGI) refers to advanced AI systems that exhibit human-like cognitive abilities across various tasks and domains. Unlike narrow AI, which excels in specific tasks, AGI aims to encompass learning, reasoning, problem-solving, perception, and natural language understanding. Although AGI remains an ambitious goal, its pursuit has led to numerous AI advancements. The development of AGI holds the potential to revolutionize industries such as healthcare, finance, transportation, and education, while also raising ethical, safety, and societal concerns that must be carefully addressed.

## Table of Contents

- [Awesome AGI Resources](#awesome-agi-resources-)
  - [What is AGI?](#what-is-agi)
  - [Frameworks and Platforms](#frameworks-and-platforms)
  - [Agents](#agents)
  - [LLM Application Frameworks](#llm-application-frameworks)
  - [RAG and Vector Databases](#rag-and-vector-databases)
  - [LLM Fine-Tuning Techniques](#llm-fine-tuning-techniques)
  - [LLM Deployment and Serving](#llm-deployment-and-serving)
  - [Prompt Engineering](#prompt-engineering)
  - [Safety, Alignment and Governance](#safety-alignment-and-governance)
  - [Papers, Blogs, Courses and Lectures](#papers-blogs-courses-and-lectures)
    - [Papers](#papers)
    - [Blogs and News](#blogs-and-news)
  - [Tutorials and Guides](#tutorials-and-guides)

---

## Frameworks and Platforms

|Name|Github Stars|Introduction| Notes |
|-|-|-|-|
|[:fire: Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT) |![GitHub Repo stars](https://badgen.net/github/stars/Significant-Gravitas/Auto-GPT)|An experimental open-source attempt to make GPT-4 fully autonomous.|-|
|[:fire: AgentGPT](https://github.com/reworkd/AgentGPT) |![GitHub Repo stars](https://badgen.net/github/stars/reworkd/AgentGPT)|Assemble, configure, and deploy autonomous AI Agents in your browser.|-|
|[:fire: MetaGPT](https://github.com/geekan/MetaGPT) |![GitHub Repo stars](https://badgen.net/github/stars/geekan/MetaGPT)|The Multi-Agent Framework: Given one line Requirement, return PRD, Design, Tasks, Repo.|Multi-agent framework that mimics a software company structure with PM, architect, and engineer roles.|
|[:fire: MiniGPT-4](https://github.com/Vision-CAIR/MiniGPT-4)|![GitHub Repo stars](https://badgen.net/github/stars/Vision-CAIR/MiniGPT-4)|MiniGPT-4: Enhancing Vision-language Understanding with Advanced Large Language Models.|-|
|[:fire: JARVIS](https://github.com/microsoft/JARVIS)|![GitHub Repo stars](https://badgen.net/github/stars/microsoft/JARVIS)|A system to connect LLMs with ML community. Uses ChatGPT as a controller to manage AI models on HuggingFace for task planning, model selection, and execution.|-|
|[:fire: babyagi](https://github.com/yoheinakajima/babyagi)|![GitHub Repo stars](https://badgen.net/github/stars/yoheinakajima/babyagi)|Use OpenAI and Pinecone APIs to create, prioritize, and execute tasks.| Task-driven autonomous agent using OpenAI and vector DBs.|
|[SuperAGI](https://github.com/TransformerOptimus/SuperAGI)|![GitHub Repo stars](https://badgen.net/github/stars/TransformerOptimus/SuperAGI)|A dev-first open source autonomous AI agent framework. Run concurrent agents seamlessly, extend agent capabilities with tools, GUI, action console, multiple vector DBs, performance telemetry, optimized token usage, and agent memory storage.|Toolkits: Twitter, Coding, Instagram, Email, Jira, File Manager, Google Search, DALL-E, GitHub, Web Interaction, DuckDuckGo, Google Calendar, Notion, Apollo.|
|[smol-ai/developer](https://github.com/smol-ai/developer)|![GitHub Repo stars](https://badgen.net/github/stars/smol-ai/developer)|The first library to let you embed a developer agent in your own app!|-|
|[Auto-GPT-Plugins](https://github.com/Significant-Gravitas/Auto-GPT-Plugins) |![GitHub Repo stars](https://badgen.net/github/stars/Significant-Gravitas/Auto-GPT-Plugins)|Plugins for Auto-GPT.|-|
|[AutoGPT.js](https://github.com/zabirauf/AutoGPT.js)|![GitHub Repo stars](https://badgen.net/github/stars/zabirauf/AutoGPT.js)|Auto-GPT on the browser.|-|
|[AutoGPT-GUI](https://github.com/thecookingsenpai/autogpt-gui)|![GitHub Repo stars](https://badgen.net/github/stars/thecookingsenpai/autogpt-gui)|A graphical user interface for AutoGPT.|-|
|[OpenAGI](https://github.com/agiresearch/OpenAGI) |![GitHub Repo stars](https://badgen.net/github/stars/agiresearch/OpenAGI)|When LLM (Large Language Models) Meets Domain Experts. An open-source AGI research platform combining expert models with RLTF.|Combines ChatGPT/LLaMA2 with specialized models, dynamically selecting tools based on task context.|
|[AI-legion](https://github.com/eumemic/ai-legion)|![GitHub Repo stars](https://badgen.net/github/stars/eumemic/ai-legion)|An LLM-powered autonomous agent platform.|-|
|[MicroGPT](https://github.com/muellerberndt/micro-gpt)|![GitHub Repo stars](https://badgen.net/github/stars/muellerberndt/micro-gpt)|A minimal generic autonomous agent based on GPT3.5/4. Can analyze stock prices, perform network security tests, create art, and order pizza.|-|
|[Agent-LLM](https://github.com/Josh-XT/Agent-LLM)|![GitHub Repo stars](https://badgen.net/github/stars/Josh-XT/Agent-LLM)|An Artificial Intelligence Automation Platform. AI Instruction management from various providers, has an adaptive memory, and a versatile plugin system with many commands including web browsing.|-|
|[loopgpt](https://github.com/farizrahman4u/loopgpt)|![GitHub Repo stars](https://badgen.net/github/stars/farizrahman4u/loopgpt)|Modular Auto-GPT Framework. Improved GPT-3.5 support, lower API token cost, can run with or without human in the loop.|-|
|[AutoGPT-Next-Web](https://github.com/ConnectAI-E/AutoGPT-Next-Web)|![GitHub Repo stars](https://badgen.net/github/stars/ConnectAI-E/AutoGPT-Next-Web)|Assemble, configure, and deploy autonomous AI Agents in your browser.|-|
|[Free-AUTO-GPT-with-NO-API](https://github.com/IntelligenzaArtificiale/Free-AUTO-GPT-with-NO-API)|![GitHub Repo stars](https://badgen.net/github/stars/IntelligenzaArtificiale/Free-AUTO-GPT-with-NO-API)|Free AUTOGPT with NO API - run AutoGPT/babyagi without any paid OpenAI API.|-|
|[opencog](https://github.com/opencog/opencog)|![GitHub Repo stars](https://badgen.net/github/stars/opencog/opencog)|A framework for integrated Artificial Intelligence & Artificial General Intelligence (AGI).|-|
|[mini-agi](https://github.com/muellerberndt/mini-agi)|![GitHub Repo stars](https://badgen.net/github/stars/muellerberndt/mini-agi)|MiniAGI is a minimal general-purpose autonomous agent based on GPT-3.5 / GPT-4.|-|
|[big-agi](https://github.com/enricoros/big-agi)|![GitHub Repo stars](https://badgen.net/github/stars/enricoros/big-agi)|Personal AI application powered by GPT-4 and beyond, with AI personas, AGI functions, text-to-image, voice, response streaming, code highlighting and execution, PDF import, presets for developers.|[big-agi.com](https://big-agi.com/)|
|[DemoGPT](https://github.com/melih-unsal/DemoGPT)|![GitHub Repo stars](https://badgen.net/github/stars/melih-unsal/DemoGPT)|DemoGPT enables you to create quick demos by just using prompts.|-|
|[LocalAGI](https://github.com/EmbraceAGI/LocalAGI)|![GitHub Repo stars](https://badgen.net/github/stars/EmbraceAGI/LocalAGI)|Locally run AGI powered by LLaMA, ChatGLM and more.|-|
|[ChatDev](https://github.com/OpenBMB/ChatDev)|![GitHub Repo stars](https://badgen.net/github/stars/OpenBMB/ChatDev)|A virtual software company with multiple agents (CEO, CTO, programmer, tester, etc.) collaborating to design, code, test, and document software.|Agents play different roles in a simulated dev organization.|
|[crewAI](https://github.com/joaomdmoura/crewAI)|![GitHub Repo stars](https://badgen.net/github/stars/joaomdmoura/crewAI)|Framework for orchestrating role-playing, autonomous AI agents. Craft collaborative AI crews for complex tasks.|-|
|[CAMEL](https://github.com/camel-ai/camel)|![GitHub Repo stars](https://badgen.net/github/stars/camel-ai/camel)|Communicative Agents for "Mind" Exploration of Large Language Model Society. Role-playing framework for multi-agent collaboration.|[camel-ai.org](https://www.camel-ai.org/)|
|[ShortGPT](https://github.com/RayVentura/ShortGPT)|![GitHub Repo stars](https://badgen.net/github/stars/RayVentura/ShortGPT)|Framework for automating video creation, voiceover, editing, and publishing using LLMs.|-|
|[XAgent](https://github.com/OpenBMB/XAgent)|![GitHub Repo stars](https://badgen.net/github/stars/OpenBMB/XAgent)|An autonomous LLM-based agent for complex task solving.|[x-agent.net](https://x-agent.net/)|

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
