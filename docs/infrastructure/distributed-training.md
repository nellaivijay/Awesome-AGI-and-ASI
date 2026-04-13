---
description: "Frameworks for training frontier models across thousands of GPUs with data, tensor, and pipeline parallelism plus memory optimization techniques."
keywords: "distributed training, DeepSpeed, Megatron-LM, ColossalAI, GPU parallelism, model training, FSDP"
---
# Distributed Training Frameworks

> Training frontier models requires distributing computation across thousands of GPUs. These frameworks handle the parallelism, memory optimization, and communication needed to train models with billions (or trillions) of parameters.

![DeepSpeed](https://img.shields.io/badge/DeepSpeed-Microsoft-blue?style=flat-square) ![Megatron](https://img.shields.io/badge/Megatron-NVIDIA-76B900?style=flat-square) ![Distributed](https://img.shields.io/badge/Distributed-Multi--GPU-purple?style=flat-square)

| Name | Description | Links |
|------|-------------|-------|
| [ColossalAI](https://github.com/hpcaitech/ColossalAI) | Making large AI models cheaper, faster, and more accessible with efficient parallelism techniques. | [colossalai.org](https://colossalai.org/) |
| [DeepSpeed](https://github.com/microsoft/DeepSpeed) | Microsoft's deep learning optimization library for distributed training and inference. | [deepspeed.ai](https://www.deepspeed.ai/) |
| [Megatron-LM](https://github.com/NVIDIA/Megatron-LM) | NVIDIA's research framework for training large-scale Transformer models with model and data parallelism. | - |

> **Looking for AI hardware, quantization, and compute infrastructure?** See [Compute, Hardware & Quantization](compute-hardware.md).

### Additional Training Frameworks & Libraries

| Name | Description | Links |
|------|-------------|-------|
| [PyTorch FSDP](https://pytorch.org/docs/stable/fsdp.html) | Fully Sharded Data Parallelism built into PyTorch. Shards model parameters, gradients, and optimizer states across GPUs. Native PyTorch solution for large model training. | [Docs](https://pytorch.org/docs/stable/fsdp.html) |
| [Hugging Face Accelerate](https://github.com/huggingface/accelerate) | Simple library to run PyTorch training across any distributed configuration (multi-GPU, TPU, FSDP, DeepSpeed) with minimal code changes. 8k+ stars. | [Docs](https://huggingface.co/docs/accelerate) |
| [Determined AI](https://github.com/determined-ai/determined) | Open-source deep learning training platform with distributed training, hyperparameter search, and resource management. | [determined.ai](https://www.determined.ai/) |
| [Composer](https://github.com/mosaicml/composer) | MosaicML's training library with speed-up algorithms (FlashAttention, streaming datasets, mixed precision) for efficient large model training. | [GitHub](https://github.com/mosaicml/composer) |

---

