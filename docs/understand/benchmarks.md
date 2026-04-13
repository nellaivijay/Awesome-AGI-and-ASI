---
description: "Post-Turing AGI benchmarks and evaluation frameworks tracking the path from narrow AI to general intelligence -- ARC-AGI, SWE-bench, GAIA, GPQA, and more."
keywords: "AGI benchmarks, ARC-AGI, SWE-bench, GAIA, GPQA, Humanity's Last Exam, FrontierMath, AI evaluation, post-Turing tests"
---
# AGI Benchmarks & Evals

> Standard benchmarks (MMLU, GSM8K) are saturated. The path to AGI is now measured by post-Turing tests that evaluate fluid reasoning, real-world problem solving, and capabilities no narrow system can fake.

![Reasoning](https://img.shields.io/badge/Reasoning-blue?style=flat-square) ![Coding](https://img.shields.io/badge/Coding-green?style=flat-square) ![Science](https://img.shields.io/badge/Science-purple?style=flat-square) ![Multi-Modal](https://img.shields.io/badge/Multi--Modal-orange?style=flat-square) ![Open Source](https://img.shields.io/badge/Open_Source-brightgreen?style=flat-square)

### Post-Turing AGI Benchmarks

|| Benchmark | Creator | What It Tests | Best Score (2026) | Human Baseline | Links |
||-----------|---------|---------------|-------------------|----------------|-------|
|| **ARC-AGI** (Abstraction and Reasoning Corpus) | François Chollet / ARC Prize Foundation | Fluid intelligence, novel pattern recognition, abstract reasoning -- tasks trivial for humans but unsolved by AI | Best AI: ~55-65% | ~85% | [arcprize.org](https://arcprize.org/), [GitHub](https://github.com/fchollet/ARC-AGI) |
|| **SWE-bench / SWE-bench Verified** | Princeton NLP | Real GitHub issue resolution, end-to-end software engineering across real-world codebases | Best: ~50% (Verified) | Human SWE: varies | [swebench.com](https://www.swebench.com/), [Paper](https://arxiv.org/abs/2310.06770) |
|| **GAIA** (General AI Assistants) | Meta / HuggingFace | Multi-step reasoning with real-world tool use (web browsing, code execution, file manipulation) | Best: ~75% L1, ~50% L3 | 92% | [Paper](https://arxiv.org/abs/2311.12983), [HuggingFace](https://huggingface.co/gaia-benchmark) |
|| **GPQA** (Graduate-Level Google-Proof QA) | NYU | PhD-level science questions in physics, chemistry, and biology that cannot be answered via search | Best: ~75% | Expert PhD: ~65%, Non-expert: ~34% | [Paper](https://arxiv.org/abs/2311.12022) |
|| **Humanity's Last Exam (HLE)** | Scale AI / CAIS | 3,000+ expert-crafted questions across dozens of domains designed to be the hardest test for AI | Best: ~18-58% (model dependent) | Human expert: varies by domain | [Paper](https://arxiv.org/abs/2501.14249), [GitHub](https://github.com/centerforaisafety/hle) |
|| **FrontierMath** | Epoch AI | Extremely hard, unpublished math problems crafted by professional mathematicians -- problems that take hours or days to solve | Best: <5% | Fields Medalists: varies | [epochai.org/frontiermath](https://epochai.org/frontiermath), [Paper](https://arxiv.org/abs/2411.04872) |
|| **MathArena / AIME 2025** | AIME / MathArena | American math competition problems testing creative problem-solving under time pressure | Best: o3/Gemini solve 85-90% | Human top competitors: 100% | [matharena.ai](https://matharena.ai/) |
|| **ARC-AGI-2** | ARC Prize Foundation (2025) | Harder version of ARC-AGI with reduced pattern memorization and increased abstraction requirements | Best AI: ~30% | ~85% | [arcprize.org](https://arcprize.org/) |

### Saturated Benchmarks (Historical / Foundational)

> These benchmarks are still important for tracking progress and establishing baselines, but they no longer differentiate frontier models. When a benchmark is "saturated," most top models score 90%+ and improvements are marginal. The field has moved to harder evaluations above.

|| Benchmark | What It Tests | Status | Links |
||-----------|---------------|--------|-------|
|| **MMLU** (Massive Multitask Language Understanding) | 57-subject knowledge test spanning STEM, humanities, social sciences, and more | 90%+ saturated | [Paper](https://arxiv.org/abs/2009.03300) |
|| **MMLU-Pro** | Harder version of MMLU with 10 answer choices and more reasoning-heavy questions | ~80% by top models | [Paper](https://arxiv.org/abs/2406.01574) |
|| **GSM8K** (Grade School Math) | Grade school math word problems requiring multi-step arithmetic reasoning | 95%+ saturated | [Paper](https://arxiv.org/abs/2110.14168) |
|| **HumanEval** | Python code generation from docstrings -- functional correctness of synthesized programs | 95%+ saturated | [Paper](https://arxiv.org/abs/2107.03374) |
|| **HellaSwag** | Commonsense natural language inference -- predicting plausible continuations of everyday scenarios | 95%+ saturated | [Paper](https://arxiv.org/abs/1905.07830) |
|| **BIG-Bench Hard** | Challenging subset of BIG-Bench tasks that prior language models failed at | 85%+ by frontier models | [Paper](https://arxiv.org/abs/2210.09261) |

### Agent & Embodied Benchmarks

|| Benchmark | What It Tests | Best Score (2026) | Links |
||-----------|---------------|-------------------|-------|
|| **WebArena** | Real web task completion across functional websites (shopping, forums, maps, GitLab) | ~35% (human: 78%) | [Paper](https://arxiv.org/abs/2307.13854) |
|| **OSWorld** | Real operating system GUI tasks -- file management, app usage, multi-app workflows | ~22% (human: 72%) | [Paper](https://arxiv.org/abs/2404.07972) |
|| **SWE-bench Multimodal** | GUI-based coding tasks requiring visual understanding alongside code generation | Emerging | [swebench.com](https://www.swebench.com/) |
|| **MINT** (Multi-turn Interactive) | Multi-turn tool use requiring sustained reasoning across sequential interactions | Emerging | [Paper](https://arxiv.org/abs/2309.10691) |
|| **AgentBench** | Diverse agent environments -- OS interaction, database ops, web browsing, lateral thinking games | Varies by environment | [Paper](https://arxiv.org/abs/2308.03688), [GitHub](https://github.com/THUDM/AgentBench) |

### How to Read These Benchmarks

Benchmark scores alone don't define AGI. A model that tops one benchmark while failing another is still narrow AI. True AGI requires **generality** (performing well across *all* benchmarks, not just one), **robustness** (performing well on novel variations and out-of-distribution inputs, not just memorized patterns), and **efficiency** (not requiring task-specific training data or fine-tuning for each new domain). The best way to gauge progress toward AGI is to track performance *across* the full suite of post-Turing benchmarks above, not any single score in isolation.

> **See also:** [ARC Prize -- the $1M+ challenge for AGI](https://arcprize.org/) | [DeepMind Levels of AGI Framework](../understand/ai-agi-asi.md#google-deepminds-levels-of-agi-framework-2023)

---
