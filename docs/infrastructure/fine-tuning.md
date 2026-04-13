---
description: "Adapt pre-trained LLMs to specific tasks and domains using LoRA, QLoRA, DPO, RLHF, and other parameter-efficient fine-tuning techniques."
keywords: "LLM fine-tuning, LoRA, QLoRA, RLHF, DPO, PEFT, instruction tuning, alignment, adapter methods"
---
# LLM Fine-Tuning Techniques

> Making foundation models your own. Fine-tuning adapts pre-trained LLMs to specific tasks, domains, or behaviors -- from lightweight LoRA adapters that train in hours on a single GPU to full alignment techniques like DPO that shape model values.

![LoRA](https://img.shields.io/badge/LoRA-Low--Rank_Adaptation-blue?style=flat-square) ![QLoRA](https://img.shields.io/badge/QLoRA-4--bit_Quantized-green?style=flat-square) ![PEFT](https://img.shields.io/badge/PEFT-Parameter_Efficient-purple?style=flat-square) ![DPO](https://img.shields.io/badge/DPO-Preference_Optimization-orange?style=flat-square) ![RLHF](https://img.shields.io/badge/RLHF-Human_Feedback-red?style=flat-square)

### LoRA and Variants

| Method | Description | Paper | Code |
|--------|-------------|-------|------|
| LoRA | Low-Rank Adaptation: trainable low-rank matrices in attention layers, frozen pretrained weights. Rank 4-16 typical. | [Paper](https://arxiv.org/pdf/2106.09685.pdf) | [Code](https://github.com/microsoft/LoRA) |
| LoRA+ | Different learning rates for A and B matrices (B gets 16x higher LR). ~2% accuracy gain, 2x faster. | [Paper](https://arxiv.org/abs/2402.12354) | - |
| AdaLoRA | Adaptive budget allocation via SVD-based importance scoring for LoRA parameters. | [Paper](https://arxiv.org/abs/2303.10512) | [Code](https://github.com/QingruZhang/AdaLoRA) |
| QLoRA | 4-bit quantized model + trainable LoRA adapters. NormalFloat, double quantization, paged optimizers. | [Paper](https://arxiv.org/abs/2305.14314) | [Code](https://github.com/artidoro/qlora) |
| DoRA | Weight-Decomposed LoRA: separate magnitude and direction fine-tuning. By NVIDIA. | [Paper](https://arxiv.org/pdf/2402.09353.pdf) | [Code](https://github.com/catid/dora) |
| PiSSA | SVD-based LoRA initialization for significantly better fine-tuning. | [Paper](https://arxiv.org/abs/2404.02948) | [Code](https://github.com/GraphPKU/PiSSA) |
| MOELoRA | Combines MoE with LoRA for multi-task PEFT, especially medical applications. | [Paper](https://arxiv.org/abs/2310.18339) | [Code](https://github.com/liuqidong07/MOELoRA-peft) |
| LoRA-FA | Freezes matrix A after init; trains only B. Halves param count, comparable performance. | [Paper](https://arxiv.org/abs/2308.03303) | - |
| LoRA-drop | Determines which layers need LoRA fine-tuning based on output evaluation. | [Paper](https://arxiv.org/abs/2402.07721) | - |
| Delta-LoRA | Updates base W using gradient of AB difference, controlled by lambda hyperparameter. | [Paper](https://arxiv.org/abs/2309.02411) | - |

### Other Fine-Tuning Methods

| Method | Description | Paper | Code |
|--------|-------------|-------|------|
| [PEFT](https://github.com/huggingface/peft) | HuggingFace library for multiple parameter-efficient fine-tuning methods. | - | [Code](https://github.com/huggingface/peft) |
| Instruction Tuning | Fine-tuning on (instruction, output) pairs for better controllability. | [Paper](https://arxiv.org/abs/2308.10792) | [Code](https://github.com/xiaoya-li/Instruction-Tuning-Survey) |
| Prefix Tuning | Trainable continuous prefixes at each layer; LM stays frozen. | [Paper](https://arxiv.org/abs/2101.00190) | [Code](https://github.com/huggingface/peft) |
| Prompt Tuning | Soft prompt tokens at input layer only. Simplified Prefix Tuning. | [Paper](https://arxiv.org/abs/2104.08691) | [Code](https://github.com/huggingface/peft) |
| P-Tuning | Learnable prompt embeddings via MLP+LSTM. GPT surpassed BERT on SuperGLUE. | [Paper](https://arxiv.org/abs/2103.10385) | [Code](https://github.com/huggingface/peft) |
| P-Tuning v2 | Prompt tokens at every layer, not just input. Task-specific prompt lengths. | [Paper](https://arxiv.org/abs/2110.07602) | [Code](https://github.com/THUDM/P-tuning-v2) |
| Adapter Tuning | Small adapter modules in each Transformer layer. ~3.6% added params. | [Paper](https://arxiv.org/abs/1902.00751) | [Code](https://github.com/google-research/adapter-bert) |
| BitFit | Sparse fine-tuning: only updates bias parameters. | [Paper](https://arxiv.org/abs/2106.10199) | [Code](https://github.com/benzakenelad/BitFit) |
| DPO | Direct Preference Optimization: trains LM directly as reward model, no separate RM needed. | [Paper](https://arxiv.org/abs/2305.18290) | [Code](https://github.com/eric-mitchell/direct-preference-optimization) |

---

