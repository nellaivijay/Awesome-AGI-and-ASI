# LLM Application Frameworks

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

