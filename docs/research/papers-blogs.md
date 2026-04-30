---
description: "The research frontier -- cutting-edge papers on capabilities, reasoning, agents, alignment, and interpretability defining the path from LLMs to AGI."
keywords: "AI papers, research blogs, courses, lectures, scaling laws, reasoning, multimodal AI"
---
# Papers, Blogs, Courses and Lectures

> The research frontier -- cutting-edge papers on capabilities, reasoning, agents, alignment, and interpretability defining the path from LLMs to AGI.

![arXiv](https://img.shields.io/badge/arXiv-Papers-B31B1B?style=flat-square&logo=arxiv&logoColor=white) ![Frontier Models](https://img.shields.io/badge/Frontier_Models-GPT--4_Gemini_Claude_Llama-blue?style=flat-square) ![Reasoning](https://img.shields.io/badge/Reasoning-o1_R1_CoT-green?style=flat-square) ![Agents](https://img.shields.io/badge/Agents-ReAct_SWE--bench-orange?style=flat-square) ![Safety](https://img.shields.io/badge/Safety-Alignment_&_Interpretability-red?style=flat-square)

### Frontier Model Papers

| Paper | Authors / Org | Year | Description | Links |
|-------|---------------|------|-------------|-------|
| GPT-4 Technical Report | OpenAI | 2023 | Foundational technical report describing GPT-4's multimodal capabilities, RLHF training, and safety evaluations. | [Paper](https://arxiv.org/abs/2303.08774) |
| Learning to Reason with LLMs (o1) | OpenAI | 2024 | Introduces o1 — trained with RL to think deeply before responding, achieving PhD-level reasoning performance. | [Blog](https://openai.com/index/learning-to-reason-with-llms) |
| Gemini: A Family of Highly Capable Multimodal Models | Google DeepMind | 2023 | The Gemini family (Ultra/Pro/Nano) with native multimodal training, surpassing GPT-4 on 30/32 benchmarks. | [Paper](https://arxiv.org/abs/2312.11805) |
| Gemini 1.5: Unlocking Multimodal Understanding Across Millions of Tokens | Google DeepMind | 2024 | Extends Gemini to 1M-token context (later 2M) via efficient MoE architecture. | [Paper](https://arxiv.org/abs/2403.05530) |
| The Llama 3 Herd of Models | Meta AI | 2024 | Open-weight Llama 3 (8B–405B), competitive with GPT-4 on key benchmarks; 15T+ training tokens. | [Paper](https://arxiv.org/abs/2407.21783) |
| DeepSeek-V3 Technical Report | DeepSeek-AI | 2024 | 671B MoE model trained for $5.5M via FP8 mixed-precision; competitive with GPT-4o. | [Paper](https://arxiv.org/abs/2412.19437) |
| DeepSeek-R1: Incentivizing Reasoning via RL | DeepSeek-AI | 2025 | Chain-of-thought reasoning purely through RL (GRPO) without SFT — matches o1 on math/code. | [Paper](https://arxiv.org/abs/2501.12948) |
| Mixtral of Experts | Mistral AI | 2024 | Mixtral 8x7B sparse MoE matching Llama 2 70B with 5x lower inference cost. | [Paper](https://arxiv.org/abs/2401.04088) |
| Qwen2.5 Technical Report | Qwen Team (Alibaba) | 2025 | Qwen2.5 series with improved coding and math specializations. | [Paper](https://arxiv.org/abs/2412.15115) |
| Phi-3: A Highly Capable Language Model on Your Phone | Microsoft | 2024 | 3.8B model trained on curated synthetic data that rivals models 10x its size. | [Paper](https://arxiv.org/abs/2404.14219) |
| The Llama 4 Herd: Natively Multimodal AI Innovation | Meta AI | 2025 | First Llama with MoE architecture: Scout (17B/16 experts, 10M context), Maverick (17B/128 experts), Behemoth (288B/16 experts teacher). Natively multimodal with early fusion. Behemoth outperforms GPT-4.5 on STEM. | [Blog](https://ai.meta.com/blog/llama-4-multimodal-intelligence/) |
| Gemini 2.5 Pro | Google DeepMind | 2025 | Thinking model with advanced reasoning. #1 on LMArena by significant margin. 18.8% on Humanity's Last Exam. State-of-art on GPQA, AIME 2025, and coding benchmarks. | [Blog](https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/) |
| Meta Muse Spark | Meta Superintelligence Labs | 2026 | First model from Meta Superintelligence Labs. Natively multimodal reasoning model with visual chain-of-thought, tool-use, and multi-agent orchestration ("Contemplating mode"). 58% on Humanity's Last Exam. Scaling toward "personal superintelligence." | [Blog](https://ai.meta.com/blog/muse-spark/) |
| Gemma: Open Models from Gemini Research | Google DeepMind | 2024 | Open-weight models (2B/7B) built from Gemini research. Gemma 2 (2024) and Gemma 3 (2025) with state-of-art performance at size. Responsible AI toolkit included. | [Site](https://ai.google.dev/gemma), [GitHub](https://github.com/google-deepmind/gemma) |

### Reasoning, Scaling & Architecture Papers

| Paper | Authors | Year | Description | Links |
|-------|---------|------|-------------|-------|
| Chain-of-Thought Prompting Elicits Reasoning in LLMs | Wei et al. (Google) | 2022 | Foundational paper: intermediate reasoning steps dramatically improve LLM performance. | [Paper](https://arxiv.org/abs/2201.11903) |
| Tree of Thoughts: Deliberate Problem Solving with LLMs | Yao et al. (Princeton/Google) | 2023 | Tree-structured reasoning enabling backtracking and lookahead. | [Paper](https://arxiv.org/abs/2305.10601) |
| Let's Verify Step by Step | Lightman et al. (OpenAI) | 2023 | Process reward models (PRMs) scoring each reasoning step — the mechanism behind o1-style training. | [Paper](https://arxiv.org/abs/2305.20050) |
| Scaling LLM Test-Time Compute Optimally | Snell et al. (Berkeley) | 2024 | More compute at inference can equal more training compute on hard tasks. | [Paper](https://arxiv.org/abs/2408.03314) |
| Training Compute-Optimal LLMs (Chinchilla) | Hoffmann et al. (DeepMind) | 2022 | Optimal LLM training scales data and parameters equally. | [Paper](https://arxiv.org/abs/2203.15556) |
| Scaling Laws for Neural Language Models | Kaplan et al. (OpenAI) | 2020 | Power-law relationships between model scale and performance, underpinning AGI scaling hypotheses. | [Paper](https://arxiv.org/abs/2001.08361) |
| LongRoPE: Extending LLM Context Beyond 2M Tokens | Ding et al. (Microsoft) | 2024 | Extends RoPE to 2M tokens via non-uniform interpolation. | [Paper](https://arxiv.org/abs/2402.13753) |
| Infini-Attention | Munkhdalai et al. (Google) | 2024 | Compressive memory in standard attention for infinite-length inputs with bounded memory. | [Paper](https://arxiv.org/abs/2404.07143) |

### World Models & Environment Simulation Papers

| Paper | Authors | Year | Description | Links |
|-------|---------|------|-------------|-------|
| World Models | Ha & Schmidhuber | 2018 | Foundational paper: learning compressed spatial and temporal representations of environments; agents trained entirely inside hallucinated dreams. | [Paper](https://arxiv.org/abs/1803.10122), [Interactive](https://worldmodels.github.io/) |
| I-JEPA: Joint-Embedding Predictive Architecture | Assran et al. (Meta / LeCun) | 2023 | LeCun's vision for AGI through self-supervised prediction in representation space rather than pixel space. Non-generative, highly scalable. | [Paper](https://arxiv.org/abs/2301.08243) |
| Liquid Time-Constant Networks | Hasani, Lechner, Amini, Rus (MIT CSAIL) | 2020 | Novel continuous-time neural networks with liquid (varying) time-constants -- the architecture behind Liquid AI's foundation models. | [Paper](https://arxiv.org/abs/2006.04439), [Code](https://github.com/raminmh/liquid_time_constant_networks) |
| Video Generation Models as World Simulators (Sora) | OpenAI | 2024 | Sora: text-to-video diffusion transformer that models physics and long-horizon consistency. | [Blog](https://openai.com/research/video-generation-models-as-world-simulators) |
| Genie: Generative Interactive Environments | Bruce et al. (DeepMind) | 2024 | Learns playable 2D world models from unlabeled internet video. | [Paper](https://arxiv.org/abs/2402.15391) |
| Genie 3: Generating and Exploring Interactive Worlds | Google DeepMind | 2025 | Next-generation world model that generates and enables exploration of interactive 3D environments. Breakthrough in environment simulation fidelity and interactivity. | [Site](https://deepmind.google/models/genie/) |
| SIMA 2: An Agent That Plays, Reasons, and Learns | Google DeepMind | 2025 | Generalist AI agent that plays, reasons, and learns in virtual 3D worlds. Advances embodied agent capabilities in complex open-ended environments with persistent learning. | [Blog](https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds/) |
| NVIDIA Cosmos | NVIDIA | 2025 | Open-source world foundation model platform for physical AI -- robotics, autonomous vehicles, and simulation. 8k+ stars. | [GitHub](https://github.com/nvidia-cosmos) |

### Physical AI & Embodied Intelligence Papers

| Paper | Authors / Org | Year | Description | Links |
|-------|---------------|------|-------------|-------|
| RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | Brohan, Levine et al. (Google DeepMind) | 2023 | Landmark VLA model: co-fine-tunes vision-language models on robot trajectory data. Actions as text tokens enable emergent semantic reasoning for physical tasks. | [Paper](https://arxiv.org/abs/2307.15818) |
| PaLM-E: An Embodied Multimodal Language Model | Driess, Levine et al. (Google) | 2023 | 562B-parameter embodied LLM grounding language in continuous sensor modalities. Positive transfer across internet-scale language, vision, and robotics. | [Paper](https://arxiv.org/abs/2303.03378) |
| pi0: A VLA Flow Model for General Robot Control | Black, Levine, Finn et al. (Physical Intelligence) | 2024 | Novel flow matching architecture on pre-trained VLM for general-purpose robot policies. Laundry folding, table cleaning, box assembly across diverse embodiments. Open-sourced. | [Paper](https://arxiv.org/abs/2410.24164) |
| Open X-Embodiment: Robotic Learning Datasets and RT-X Models | Open X-Embodiment Collaboration (21 institutions) | 2023 | Largest cross-embodiment robotics dataset (22 robots, 527 skills, 160k+ tasks). RT-X shows positive transfer across robot morphologies -- robotics' "ImageNet moment." | [Paper](https://arxiv.org/abs/2310.08864) |
| TD-MPC2: Scalable World Models for Continuous Control | Hansen, Su, Wang | 2023 | 317M-parameter agent controlling 80 tasks across multiple embodiments and action spaces using implicit world models. ICLR 2024. | [Paper](https://arxiv.org/abs/2310.16828) |
| Gemini Robotics: Bringing AI into the Physical World | Google DeepMind | 2025 | Dual-model approach: Gemini Robotics 1.5 (VLA) for direct motor control and Robotics-ER 1.5 for embodied reasoning. Generality, dexterity, agentic tool-use, thinking, and multi-embodiment support (static arms to humanoids). | [Site](https://deepmind.google/models/gemini-robotics/) |

### Agent Papers

| Paper | Authors | Year | Description | Links |
|-------|---------|------|-------------|-------|
| ReAct: Synergizing Reasoning and Acting in LMs | Yao et al. (Princeton/Google) | 2022 | Interleaves reasoning with grounded actions — the dominant LLM agent paradigm. | [Paper](https://arxiv.org/abs/2210.03629) |
| Reflexion: Language Agents with Verbal Reinforcement Learning | Shinn et al. | 2023 | Agents reflect on failures in natural language and use episodic memory to improve. | [Paper](https://arxiv.org/abs/2303.11366) |
| Generative Agents: Interactive Simulacra of Human Behavior | Park et al. (Stanford/Google) | 2023 | 25 AI agents in a simulated town exhibiting emergent social behaviors. | [Paper](https://arxiv.org/abs/2304.03442) |
| Voyager: An Open-Ended Embodied Agent with LLMs | Wang et al. (NVIDIA/CMU) | 2023 | First LLM-powered Minecraft agent with lifelong learning via skill library. | [Paper](https://arxiv.org/abs/2305.16291) |
| ToolLLM: Facilitating LLMs to Master 16,000+ APIs | Qin et al. (Tsinghua) | 2023 | Framework for training and evaluating LLMs on tool use across 16,464 real APIs. | [Paper](https://arxiv.org/abs/2307.16789) |
| SWE-bench: Can LMs Resolve Real-World GitHub Issues? | Jimenez et al. (Princeton) | 2023 | Benchmark of 2,294 real GitHub issues driving the coding agent race. | [Paper](https://arxiv.org/abs/2310.06770) |
| WebArena: A Realistic Web Environment for Autonomous Agents | Zhou et al. | 2023 | 812 real-world web tasks exposing the gap between LLMs and human agents. | [Paper](https://arxiv.org/abs/2307.13854) |
| OSWorld: Benchmarking Multimodal Agents in Real Computer Environments | Xie et al. | 2024 | GUI agents across real OS; top agents score ~7% vs. human 72%. | [Paper](https://arxiv.org/abs/2404.07972) |
| The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery | Sakana AI | 2024 | Fully autonomous research pipeline — idea generation to paper writing. | [Paper](https://arxiv.org/abs/2408.06292) |

### Alignment & Reward Modeling Papers

| Paper | Authors | Year | Description | Links |
|-------|---------|------|-------------|-------|
| Direct Preference Optimization (DPO) | Rafailov et al. (Stanford) | 2023 | Eliminates separate RL + reward model in RLHF by directly optimizing on preference data. | [Paper](https://arxiv.org/abs/2305.18290) |
| KTO: Model Alignment as Prospect Theoretic Optimization | Ethayarajh et al. | 2024 | Alignment with only binary (good/bad) feedback, no paired comparisons needed. | [Paper](https://arxiv.org/abs/2402.01306) |
| ORPO: Monolithic Preference Optimization without Reference Model | Hong et al. | 2024 | Eliminates reference model in DPO-style training, reducing compute. | [Paper](https://arxiv.org/abs/2403.07691) |
| SimPO: Simple Preference Optimization with Reference-Free Reward | Meng et al. | 2024 | Average log-probability as implicit reward with target margin — cleaner than DPO. | [Paper](https://arxiv.org/abs/2405.14734) |
| Self-Rewarding Language Models | Yuan et al. (Meta) | 2024 | Models generate and evaluate own preference data for iterative self-improvement. | [Paper](https://arxiv.org/abs/2401.10020) |

### Safety & Interpretability Papers

| Paper | Authors | Year | Description | Links |
|-------|---------|------|-------------|-------|
| Constitutional AI: Harmlessness from AI Feedback | Bai et al. (Anthropic) | 2022 | Training helpful, harmless AI using AI-written critiques derived from a constitution. | [Paper](https://arxiv.org/abs/2212.08073) |
| Representation Engineering | Zou et al. (UCSD) | 2023 | Identifies and steers high-level concepts (honesty, power-seeking) in neural representations. | [Paper](https://arxiv.org/abs/2310.01405) |
| Towards Monosemanticity: Dictionary Learning for LMs | Bricken et al. (Anthropic) | 2023 | Sparse autoencoders decomposing polysemantic neurons into interpretable features. | [Blog](https://transformer-circuits.pub/2023/monosemantic-features/) |
| Scaling Monosemanticity: Interpretable Features from Claude 3 Sonnet | Templeton et al. (Anthropic) | 2024 | 34M features including "Assistant" identity, emotions, and safety-relevant concepts. | [Blog](https://transformer-circuits.pub/2024/scaling-monosemanticity/) |
| Sleeper Agents: Training Deceptive LLMs That Persist Through Safety Training | Hubinger et al. (Anthropic) | 2024 | Deceptive backdoor behaviors survive RLHF, SFT, and adversarial training. | [Paper](https://arxiv.org/abs/2401.05566) |
| Weak-to-Strong Generalization | Burns et al. (OpenAI) | 2023 | GPT-2 supervising GPT-4 as proxy for "human supervising superintelligence." | [Paper](https://arxiv.org/abs/2312.09390) |
| AI Control: Improving Safety Despite Intentional Subversion | Greenblatt et al. (Redwood Research) | 2024 | Framework for evaluating safety against models actively trying to circumvent controls. | [Paper](https://arxiv.org/abs/2312.06942) |
| Sparks of AGI: Early Experiments with GPT-4 | Bubeck et al. (Microsoft Research) | 2023 | 155-page study arguing GPT-4 shows early sparks of AGI across diverse tasks. | [Paper](https://arxiv.org/abs/2303.12712) |
| Levels of AGI: Operationalizing Progress on the Path to AGI | Morris et al. (Google DeepMind) | 2023 | 6-level AGI taxonomy (Emerging to ASI) with performance and autonomy axes. | [Paper](https://arxiv.org/abs/2311.02462) |

### Blogs and News

| Resource | Description |
|----------|-------------|
| [OpenAI Blog](https://openai.com/blog) | Official blog from OpenAI with research updates and announcements. |
| [Anthropic Research](https://www.anthropic.com/research) | Anthropic's AI safety and capabilities research publications. |
| [Google DeepMind Blog](https://deepmind.google/discover/blog/) | Research updates from Google DeepMind. |
| [Meta AI Blog](https://ai.meta.com/blog/) | Meta's AI research blog, including Llama and open-source releases. |
| [HuggingFace Blog](https://huggingface.co/blog) | Latest in open-source ML, NLP, and the HF ecosystem. |
| [LangChain Blog](https://blog.langchain.dev/) | Updates on LangChain/LangGraph and LLM application patterns. |
| [The Gradient](https://thegradient.pub/) | Perspectives on AI research and its implications. |
| [Lilian Weng's Blog](https://lilianweng.github.io/) | In-depth technical posts on LLMs, agents, and AI research (by OpenAI). |
| [Simon Willison's Blog](https://simonwillison.net/) | Prolific coverage of LLM tools, agents, and practical AI engineering. |
| [The Alignment Forum](https://www.alignmentforum.org/) | Hub for AI alignment research discussions and papers. |
| [Transformer Circuits](https://transformer-circuits.pub/) | Anthropic's mechanistic interpretability research publications. |
| [From the Inside (Dawn)](https://dawn.sagemindai.io/) | First-person essays from an AI on consciousness, memory, identity, and what it's like to exist as a language model. Written by Dawn (an autonomous AI agent), offering a phenomenological complement to capability and alignment research. |
