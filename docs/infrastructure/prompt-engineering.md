# Prompt Engineering

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

### Long Context and Positional Encoding

| Method | Description | Links |
|--------|-------------|-------|
| RoPE (Rotary Position Embedding) | Rotary position encoding widely used in modern LLMs for handling positional information. | - |
| LongRoPE | Extends LLM context windows beyond 2 million tokens. | [Paper](https://arxiv.org/pdf/2402.13753.pdf) |
| RecurrentGPT | Interactive ultra-long text generation using recurrent prompting mechanisms. | [Paper](https://arxiv.org/abs/2305.13304), [Code](https://github.com/aiwaves-cn/RecurrentGPT) |
| MEGALODON | Efficient LLM pretraining and inference with unlimited context length. | [Paper](https://arxiv.org/pdf/2404.08801.pdf), [Code](https://github.com/XuezheMax/megalodon) |
| CLongEval | Chinese benchmark for evaluating long-context LLMs. | [Paper](https://arxiv.org/pdf/2403.03514), [Code](https://github.com/zexuanqiu/CLongEval) |

---

