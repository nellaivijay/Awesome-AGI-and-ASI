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
| [vLLM](https://github.com/vllm-project/vllm) | High-throughput LLM inference with PagedAttention. | [Docs](https://docs.vllm.ai/) |
| [TGI (Text Generation Inference)](https://github.com/huggingface/text-generation-inference) | HuggingFace's production inference server for LLMs. | [Docs](https://huggingface.co/docs/text-generation-inference/) |
| [BentoML](https://github.com/bentoml/BentoML) | Framework for building scalable AI applications with model serving. | [bentoml.com](https://bentoml.com/) |
| [LMDeploy](https://github.com/InternLM/lmdeploy) | Toolkit for compressing, deploying, and serving LLMs. | - |
| [MLC LLM](https://github.com/mlc-ai/mlc-llm) | ML Compilation for LLMs; native deployment on diverse hardware. | [mlc.ai](https://mlc.ai/) |
| [LightLLM](https://github.com/ModelTC/lightllm) | Lightweight, high-performance LLM inference framework. | - |
| [FastLLM](https://github.com/ztxz16/fastllm) | Efficient LLM inference library for CPU/GPU. | - |
| [DeepSpeed-MII](https://github.com/microsoft/DeepSpeed-MII) | Low-latency, low-cost inference by DeepSpeed. | - |
| [CTranslate2](https://github.com/OpenNMT/CTranslate2) | Fast Transformer inference with quantization and pruning. | - |
| [OpenLLM](https://github.com/bentoml/OpenLLM) | Fine-tune, serve, deploy, and monitor LLMs in production. | - |

### Production AI Orchestration & Cloud Platforms

> Training a frontier model is only half the battle -- orchestrating it in production is the other. These platforms handle the end-to-end lifecycle: model hosting, autoscaling, monitoring, A/B testing, and supporting massive context windows at enterprise scale.

| Name | Description | Links |
|------|-------------|-------|
| [Google Vertex AI](https://cloud.google.com/vertex-ai) | Google Cloud AI platform. Model Garden (100+ models incl. Gemini), pipelines, AutoML, 1M+ token context. | [Docs](https://cloud.google.com/vertex-ai/docs) |
| [Amazon Bedrock](https://aws.amazon.com/bedrock/) | Managed GenAI service. Access Claude, Llama, Titan via unified API. Guardrails, RAG, Agents. | [Docs](https://docs.aws.amazon.com/bedrock/) |
| [Amazon SageMaker](https://aws.amazon.com/sagemaker/) | ML platform for training and deploying at scale. HyperPod, JumpStart, inference endpoints. | [Docs](https://docs.aws.amazon.com/sagemaker/) |
| [Azure AI Studio](https://ai.azure.com/) | Microsoft's enterprise AI platform. Model catalog (OpenAI, Meta, Mistral), prompt flow, content safety. | [Docs](https://learn.microsoft.com/en-us/azure/ai-studio/) |
| [NVIDIA Triton Inference Server](https://github.com/triton-inference-server/server) | Production inference for any framework. Dynamic batching, multi-GPU, multi-node. Standard for GPU inference. | [Docs](https://docs.nvidia.com/deeplearning/triton-inference-server/), [GitHub](https://github.com/triton-inference-server/server) |
| [KServe](https://kserve.github.io/website/) | K8s-native model serving. Autoscaling (incl. scale-to-zero), canary deploys, GPU inference. CNCF-backed. | [Docs](https://kserve.github.io/website/), [GitHub](https://github.com/kserve/kserve) |

---

