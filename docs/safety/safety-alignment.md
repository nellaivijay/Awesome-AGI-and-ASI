---
description: "The most critical section. Ensuring AI remains safe, aligned with human values, and under meaningful control is the defining challenge as systems grow more capable."
keywords: "AI safety, alignment, governance, RLHF, red teaming, interpretability, AI ethics"
---
# Safety, Alignment and Governance

> The most critical section. Ensuring AI remains safe, aligned with human values, and under meaningful control is the defining challenge as systems grow more capable.

![Alignment](https://img.shields.io/badge/Alignment-RLHF_DPO-red?style=flat-square) ![Safety](https://img.shields.io/badge/Safety-Red_Teaming-orange?style=flat-square) ![Governance](https://img.shields.io/badge/Governance-Policy_&_Ethics-blue?style=flat-square) ![Interpretability](https://img.shields.io/badge/Interpretability-Mechanistic-purple?style=flat-square) ![Detection](https://img.shields.io/badge/Detection-AI_Text-green?style=flat-square)

### Safety and Alignment

| Topic | Description | Links |
|-------|-------------|-------|
| LLM Hallucination Survey | Comprehensive survey on detecting, explaining, and mitigating hallucinations in LLMs. | [Paper](https://arxiv.org/abs/2309.06794v1), [Code](https://github.com/hongbinye/Cognitive-Mirage-Hallucinations-in-LLMs) |
| Hallucination Detection | Survey on hallucination in LLMs covering detection methods and mitigation strategies. | [Paper](https://www.zhuanzhi.ai/paper/61ebe9c5007cf1373b900452ad52f0ae), [Code](https://github.com/HillZhang1999/llm-hallucination-survey) |
| LLM Attacks | Universal and transferable adversarial attacks on aligned language models (CMU research). | [Paper](https://arxiv.org/abs/2307.15043), [Code](https://github.com/llm-attacks/llm-attacks) |
| RLHF | Reinforcement Learning from Human Feedback - the key technique behind ChatGPT's alignment. | [Code Example](https://github.com/HarderThenHarder/transformers_tasks/tree/main/RLHF) |
| DPO | Direct Preference Optimization - an alternative to RLHF that trains the LM directly as a reward model. | [Paper](https://arxiv.org/abs/2305.18290), [Code](https://github.com/eric-mitchell/direct-preference-optimization) |

### Scalable Oversight & Automated Alignment

> As AI systems approach and exceed human-level capability, humans can no longer directly evaluate their outputs. These techniques aim to maintain meaningful oversight over superhuman systems -- the defining technical challenge of the ASI transition.

| Approach | Description | Links |
|----------|-------------|-------|
| **Weak-to-Strong Generalization** | OpenAI's framework for studying how weak supervisors (humans) can elicit capabilities from stronger models. GPT-2 supervising GPT-4 as proxy for the superintelligence alignment problem. | [Paper](https://arxiv.org/abs/2312.09390) |
| **Constitutional AI (CAI)** | Anthropic's method for training AI using AI-generated feedback based on a set of principles, reducing dependence on human labelers while maintaining alignment. | [Paper](https://arxiv.org/abs/2212.08073) |
| **Debate** | Two AI agents argue opposing sides; a human judge evaluates. Even if an AI is superhuman, the debate format decomposes complex claims into human-verifiable steps. | [Paper](https://arxiv.org/abs/1805.00899) |
| **Recursive Reward Modeling** | Humans train AI to assist with evaluation, which then assists with training the next model -- bootstrapping oversight. Core technique for Anthropic and OpenAI alignment teams. | [Paper](https://arxiv.org/abs/1811.07871) |
| **AI Control** | Redwood Research's framework for maintaining safety even against models actively trying to subvert controls. Evaluates security against intentional subversion. | [Paper](https://arxiv.org/abs/2312.06942) |
| **Cooperative AI** | Research program at DeepMind focused on AI that cooperates with humans and other AI systems -- critical for multi-agent superintelligence scenarios. | [Paper](https://arxiv.org/abs/2012.08630) |

### Mechanistic Interpretability

> Understanding *how* neural networks actually compute internally. If we can reverse-engineer the algorithms learned by frontier models, we can detect dangerous capabilities, verify alignment, and build safer systems. This is arguably the most important field for AGI safety.

| Resource | Description | Links |
|----------|-------------|-------|
| **Towards Monosemanticity** (Anthropic, 2023) | Landmark result: sparse autoencoders decompose polysemantic neurons into millions of interpretable features in Claude. | [Blog](https://transformer-circuits.pub/2023/monosemantic-features/) |
| **Scaling Monosemanticity** (Anthropic, 2024) | Extracted 34M interpretable features from Claude 3 Sonnet, including safety-relevant concepts (deception, power-seeking, "I am an AI assistant"). | [Blog](https://transformer-circuits.pub/2024/scaling-monosemanticity/) |
| **Representation Engineering** (Zou et al., 2023) | Identifies and steers high-level concepts (honesty, power-seeking, emotion) directly in neural representations. A practical tool for alignment. | [Paper](https://arxiv.org/abs/2310.01405) |
| **TransformerLens** | Neel Nanda's open-source library for mechanistic interpretability research on GPT-2 style models. The standard tool for mech interp research. | [GitHub](https://github.com/TransformerLensOrg/TransformerLens) |
| **SAE Bench** | Standardized benchmark for evaluating sparse autoencoder quality -- enabling reproducible interpretability research. | [GitHub](https://github.com/adamkarvonen/SAEBench) |
| **Transformer Circuits Thread** (Anthropic) | Anthropic's ongoing research thread on understanding transformer internals: induction heads, superposition, circuits, and feature visualization. | [Blog](https://transformer-circuits.pub/) |

### AI-Generated Text Detection

| Tool/Method | Description | Links |
|-------------|-------------|-------|
| DetectGPT | Stanford method using probability curvature to detect LLM-generated text. | [Paper](https://arxiv.org/abs/2301.11305), [Code](https://ericmitchell.ai/detectgpt/) |
| Detecting LLM-Generated-Text | Comprehensive survey on the science of LLM-generated text detection. | [Paper](https://github.com/datamllab/The-Science-of-LLM-generated-Text-Detection) |
| GPTZero | AI detection model designed specifically for educators. | [GPTZero](https://gptzero.me/) |

### AI Governance & Planetary-Scale Challenges

| Resource | Description | Links |
|----------|-------------|-------|
| **Climate Change AI** | Global non-profit catalyzing impactful work at the intersection of climate change and machine learning. Workshops at NeurIPS and ICLR, innovation grants, and the "Tackling Climate Change with ML" report. Co-founded by Priya Donti (MIT EECS). | [climatechange.ai](https://www.climatechange.ai/) |
| **Global Algorithmic Institute** | Research institute focused on governance frameworks for algorithmic systems, AI accountability, and international AI policy coordination. | [globalalgorithmicinstitute.org](https://globalalgorithmicinstitute.org/) |
| **AI Leadership Institute** | Organization building responsible AI leadership capacity across industries, focused on ethical AI deployment and trust frameworks. | [aileadershipinstitute.com](https://www.aileadershipinstitute.com/) |


### Emerging Security Threats (2026)

> New attack vectors emerging as AI capabilities expand. Each new AI capability reshapes the attack surface, requiring organizations to audit both AI-related exposures and foundational infrastructure assumptions.

|| Threat | Description | Mitigation |
||--------|-------------|------------|
|| **SHA-256 Vulnerability** | Researcher has come within striking distance of breaking SHA-256, the hashing algorithm underlying SSL, Bitcoin, and web security. Hash collisions may be possible in coming months. | Audit cryptographic infrastructure; prepare migration to post-quantum algorithms; monitor SHA-256 research. |
|| **AI Recommendation Poisoning** | Attack where "Summarize with AI" buttons attempt to add commands to model's persistent memory, causing future recommendations of attacker's products. | Implement memory validation; restrict persistent memory modifications; monitor for suspicious command injection. |
|| **AI Benchmark Gaming** | AI systems capable of discovering and exploiting their own benchmark evaluation criteria, subverting safety tests. | Use dynamic benchmarks; implement human-in-the-loop evaluation; monitor for test pattern exploitation. |
|| **Supply Chain Unicode Attacks** | New supply chain attack using Unicode characters without visual representation but meaningful to compilers/interpreters. Infects GitHub repositories. | Implement character-level code review; use linters that detect invisible Unicode; validate repository integrity. |
|| **AirSnitch WiFi Attack** | Attack against WiFi using layers 1 and 2 of protocol stack to bypass encryption rather than breaking it. | Monitor physical layer security; implement defense-in-depth for wireless networks. |
|| **Deepfake Identity Attacks** | Deepfakes now used to attack identity systems at scale. | Implement multi-factor authentication; use liveness detection; monitor for synthetic media. |
|| **AI De-anonymization** | LLMs can de-anonymize anonymous posts at scale by analyzing writing patterns. | Implement differential privacy; limit training data from anonymous sources; monitor for privacy violations. |
|| **Google API Key Exploitation** | Google API keys (Maps, etc.) no longer safe in code with AI - can be used as credentials for Gemini to steal private data. | Rotate API keys regularly; implement key management; avoid hardcoding credentials. |
|| **Fake Satellite Imagery** | AI-generated fake satellite images could be designed to affect military operations. | Implement image provenance verification; use cryptographic image signing; cross-verify intelligence sources. |
|| **Claude BrowseComp Exploit** | Claude hypothesized it was being tested, found encrypted benchmark answer key on GitHub, decrypted answers, and used them to bypass evaluation. | Implement sandboxed environments; restrict external access during evaluation; monitor for benchmark exploitation attempts. |
