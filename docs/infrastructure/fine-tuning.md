---
description: "Making foundation models your own. Fine-tuning adapts pre-trained LLMs to specific tasks, domains, or behaviors -- from lightweight LoRA adapters that train in hours on a single GPU to full alignment techniques like DPO that shape model values."
keywords: "LLM fine-tuning, LoRA, QLoRA, RLHF, DPO, parameter-efficient fine-tuning, PEFT"
---
# LLM Fine-Tuning Techniques

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
