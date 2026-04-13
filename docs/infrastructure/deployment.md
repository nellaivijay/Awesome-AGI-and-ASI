---
description: "High-performance inference engines and optimization tools for fast, cost-efficient LLM serving at production scale with vLLM, TGI, and more."
keywords: "LLM deployment, model serving, vLLM, TGI, inference optimization, Triton, Vertex AI, Bedrock, production AI"
---
# LLM Deployment and Serving

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

