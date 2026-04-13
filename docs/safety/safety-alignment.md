---
description: "Critical research on AI safety, alignment with human values, red teaming, interpretability, and governance to keep AI under meaningful human control."
keywords: "AI safety, alignment, RLHF, interpretability, red teaming, AI governance, existential risk, control problem"
---
# Safety, Alignment and Governance

> The most critical section. Ensuring AI remains safe, aligned with human values, and under meaningful control is the defining challenge as systems grow more capable.

![Alignment](https://img.shields.io/badge/Alignment-RLHF_DPO-red?style=flat-square) ![Safety](https://img.shields.io/badge/Safety-Red_Teaming-orange?style=flat-square) ![Governance](https://img.shields.io/badge/Governance-Policy_&_Ethics-blue?style=flat-square) ![Interpretability](https://img.shields.io/badge/Interpretability-Mechanistic-purple?style=flat-square) ![Detection](https://img.shields.io/badge/Detection-AI_Text-green?style=flat-square)

### Safety and Alignment

| Topic | Description | Links |
|-------|-------------|-------|
| LLM Hallucination Survey | Survey on detecting, explaining, and mitigating hallucinations in LLMs. | [Paper](https://arxiv.org/abs/2309.06794v1), [Code](https://github.com/hongbinye/Cognitive-Mirage-Hallucinations-in-LLMs) |
| Hallucination Detection | Survey covering hallucination detection methods and mitigation strategies. | [Paper](https://www.zhuanzhi.ai/paper/61ebe9c5007cf1373b900452ad52f0ae), [Code](https://github.com/HillZhang1999/llm-hallucination-survey) |
| LLM Attacks | Universal adversarial attacks on aligned language models (CMU). | [Paper](https://arxiv.org/abs/2307.15043), [Code](https://github.com/llm-attacks/llm-attacks) |
| RLHF | Reinforcement Learning from Human Feedback -- key technique behind ChatGPT alignment. | [Code Example](https://github.com/HarderThenHarder/transformers_tasks/tree/main/RLHF) |
| DPO | Direct Preference Optimization -- trains LM directly as reward model, alternative to RLHF. | [Paper](https://arxiv.org/abs/2305.18290), [Code](https://github.com/eric-mitchell/direct-preference-optimization) |

### Scalable Oversight & Automated Alignment

> As AI systems approach and exceed human-level capability, humans can no longer directly evaluate their outputs. These techniques aim to maintain meaningful oversight over superhuman systems -- the defining technical challenge of the ASI transition.

| Approach | Description | Links |
|----------|-------------|-------|
| **Weak-to-Strong Generalization** | Weak supervisors eliciting capabilities from stronger models. GPT-2 supervising GPT-4 as alignment proxy. | [Paper](https://arxiv.org/abs/2312.09390) |
| **Constitutional AI (CAI)** | AI-generated feedback from principles, reducing dependence on human labelers. | [Paper](https://arxiv.org/abs/2212.08073) |
| **Debate** | Two AIs argue opposing sides; human judge evaluates. Decomposes claims into verifiable steps. | [Paper](https://arxiv.org/abs/1805.00899) |
| **Recursive Reward Modeling** | AI assists with evaluation, then assists training the next model. Bootstrapping oversight. | [Paper](https://arxiv.org/abs/1811.07871) |
| **AI Control** | Redwood Research's framework for safety against models actively trying to subvert controls. | [Paper](https://arxiv.org/abs/2312.06942) |
| **Cooperative AI** | DeepMind research on AI cooperating with humans and other AI systems. | [Paper](https://arxiv.org/abs/2012.08630) |

### Superalignment

> The defining challenge of the ASI transition: how do you align a system that is smarter than you? These research programs aim to solve alignment for superhuman AI systems before they arrive.

| Program | Description | Links |
|---------|-------------|-------|
| **OpenAI Superalignment** | 20% of OpenAI compute for superintelligence alignment. Key output: Weak-to-Strong Generalization. | [Blog](https://openai.com/index/introducing-superalignment/) |
| **Anthropic RSP (Responsible Scaling Policy)** | Evaluate dangerous capabilities at each scaling threshold; pause if safety insufficient. | [Paper](https://www.anthropic.com/index/anthropics-responsible-scaling-policy) |
| **DeepMind Scalable Alignment** | Research on reward modeling, debate, and recursive oversight for superhuman systems. | [deepmind.google](https://deepmind.google/) |
| **Eliciting Latent Knowledge (ELK)** | ARC's framework for extracting truthful beliefs from AI, even when models may deceive. | [Paper](https://docs.google.com/document/d/1WwsnJQstPq91_Yh-Ch2XRL8H_EpsnjrC1dwZXR37PC8/) |

### Mechanistic Interpretability

> Understanding *how* neural networks actually compute internally. If we can reverse-engineer the algorithms learned by frontier models, we can detect dangerous capabilities, verify alignment, and build safer systems. This is arguably the most important field for AGI safety -- and the key to **superalignment**: aligning systems smarter than us.

| Resource | Description | Links |
|----------|-------------|-------|
| **Towards Monosemanticity** (Anthropic, 2023) | Sparse autoencoders decompose polysemantic neurons into interpretable features in Claude. | [Blog](https://transformer-circuits.pub/2023/monosemantic-features/) |
| **Scaling Monosemanticity** (Anthropic, 2024) | 34M interpretable features from Claude 3 Sonnet, including safety-relevant concepts. | [Blog](https://transformer-circuits.pub/2024/scaling-monosemanticity/) |
| **Representation Engineering** (Zou et al., 2023) | Identifies and steers high-level concepts (honesty, power-seeking) in neural representations. | [Paper](https://arxiv.org/abs/2310.01405) |
| **TransformerLens** | Neel Nanda's open-source library for mechanistic interpretability on GPT-2 style models. | [GitHub](https://github.com/TransformerLensOrg/TransformerLens) |
| **SAE Bench** | Standardized benchmark for evaluating sparse autoencoder quality. | [GitHub](https://github.com/adamkarvonen/SAEBench) |
| **Steering Vectors / Activation Engineering** | Modify model behavior by adding direction vectors to activations at inference. No retraining needed. | [Paper](https://arxiv.org/abs/2308.10248), [Blog](https://www.lesswrong.com/posts/5spBue2z2tw4JuDCx/steering-vectors) |
| **Goodfire** | Commercial platform for visualizing, searching, and steering neural network features. | [goodfire.ai](https://goodfire.ai/) |
| **Neuronpedia** | Open platform for neuron-level interpretability. Hosts SAE features from multiple models. | [neuronpedia.org](https://neuronpedia.org/) |
| **Circuits Updates (Anthropic, 2025)** | Anthropic's circuit-level analysis of multi-step reasoning and safety-relevant features in Claude. | [Blog](https://transformer-circuits.pub/) |
| **Transformer Circuits Thread** (Anthropic) | Anthropic's research on transformer internals: induction heads, superposition, circuits. | [Blog](https://transformer-circuits.pub/) |

### AI-Generated Text Detection

| Tool/Method | Description | Links |
|-------------|-------------|-------|
| DetectGPT | Stanford method using probability curvature to detect LLM-generated text. | [Paper](https://arxiv.org/abs/2301.11305), [Code](https://ericmitchell.ai/detectgpt/) |
| Detecting LLM-Generated-Text | Comprehensive survey on the science of LLM-generated text detection. | [Paper](https://github.com/datamllab/The-Science-of-LLM-generated-Text-Detection) |
| GPTZero | AI detection model designed specifically for educators. | [GPTZero](https://gptzero.me/) |

### AI Governance & Planetary-Scale Challenges

| Resource | Description | Links |
|----------|-------------|-------|
| **Climate Change AI** | Global non-profit at the intersection of climate change and ML. NeurIPS/ICLR workshops. | [climatechange.ai](https://www.climatechange.ai/) |
| **Global Algorithmic Institute** | Governance frameworks for algorithmic systems, AI accountability, international policy. | [globalalgorithmicinstitute.org](https://globalalgorithmicinstitute.org/) |
| **AI Leadership Institute** | Building responsible AI leadership across industries. Ethical deployment and trust. | [aileadershipinstitute.com](https://www.aileadershipinstitute.com/) |
| **EU AI Act** | First comprehensive AI regulation (2024-2026). Risk-based framework, sets global precedent. | [digital-strategy.ec.europa.eu](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) |
| **US Executive Order on AI Safety** | EO 14110 (Oct 2023). Safety testing for frontier models, red-teaming standards, watermarking. | [whitehouse.gov](https://www.whitehouse.gov/briefing-room/presidential-actions/2023/10/30/executive-order-on-the-safe-secure-and-trustworthy-development-and-use-of-artificial-intelligence/) |
| **Frontier Model Forum** | Industry consortium (OpenAI, Google, Microsoft, Anthropic) for responsible frontier AI. | [frontiermodelforum.org](https://www.frontiermodelforum.org/) |

---

