---
description: "Humanoid robots, vision-language-action models, and physics simulation platforms bridging foundation models with physical embodiment and real-world interaction."
keywords: "physical AI, humanoid robots, embodied intelligence, VLA models, robotics, simulation, Moravec paradox"
---
# Physical AI & Embodied Intelligence

> AGI cannot exist only in text -- it must understand and act in the physical world. **Physical AI** bridges foundation models with embodiment: humanoid robots, manipulation, navigation, and physics simulation. Moravec's Paradox -- sensorimotor skills are harder than abstract reasoning -- remains one of the deepest unsolved AGI challenges.

![Robotics](https://img.shields.io/badge/Robotics-Humanoid-red?style=flat-square) ![VLA](https://img.shields.io/badge/VLA-Vision--Language--Action-blue?style=flat-square) ![Simulation](https://img.shields.io/badge/Simulation-Isaac_MuJoCo-green?style=flat-square) ![Embodied](https://img.shields.io/badge/Embodied_AI-Physical_Intelligence-purple?style=flat-square)

### Humanoid Robotics & AGI Hardware

> The race to build general-purpose humanoid robots capable of operating in unstructured human environments. These platforms are the physical embodiment layer for AGI.

| Company | Description | Links |
|---------|-------------|-------|
| **Figure AI** | Humanoid robots partnered with OpenAI/Microsoft. Figure 02: autonomous manipulation, language-guided tasks. Raised $2.6B+. | [figure.ai](https://www.figure.ai/) |
| **Tesla Optimus** | General-purpose humanoid leveraging Tesla FSD stack and Dojo. Targeting manufacturing at scale. | [tesla.com](https://www.tesla.com/) |
| **Boston Dynamics** | Pioneers of advanced locomotion. Atlas (humanoid), Spot (quadruped). Hyundai-owned, pivoting to AI-first. | [bostondynamics.com](https://www.bostondynamics.com/) |
| **1X Technologies** | NEO humanoid, backed by OpenAI. Safe embodied AI for homes and workplaces. | [1x.tech](https://www.1x.tech/) |
| **Unitree Robotics** | Affordable humanoid platforms (G1, H1). Democratizing embodied AI research. | [unitree.com](https://www.unitree.com/) |
| **Sanctuary AI** | Phoenix humanoid powered by Carbon AI for general-purpose task learning. | [sanctuary.ai](https://www.sanctuary.ai/) |
| **Agility Robotics** | Digit bipedal robot for logistics and warehouse automation. Amazon deployment partner. | [agilityrobotics.com](https://www.agilityrobotics.com/) |
| **Apptronik** | Apollo full-size humanoid for industrial use. Mercedes-Benz partnership. | [apptronik.com](https://www.apptronik.com/) |

### Robot Foundation Models (Vision-Language-Action)

> The frontier of embodied AI research: models that take visual observations and language commands as input and directly output robot motor actions. VLA models represent the convergence of foundation models and physical intelligence.

| Model | Org | Year | Description | Links |
|-------|-----|------|-------------|-------|
| **Gemini Robotics 1.5** | Google DeepMind | 2025 | Agentic VLA: vision + language → motor commands. Dexterous manipulation, tool-use, multi-embodiment (ALOHA, Franka, Apollo). | [Site](https://deepmind.google/models/gemini-robotics/), [Report](https://deepmind.google/models/gemini-robotics/gemini-robotics/) |
| **pi0** | Physical Intelligence | 2024 | VLA flow model for general robot control. Flow matching on pre-trained VLM. Diverse dexterous tasks. Open weights. | [Paper](https://arxiv.org/abs/2410.24164), [Site](https://www.physicalintelligence.company/) |
| **RT-2** | Google DeepMind | 2023 | VLA transferring web-scale knowledge to robotic control. Actions as text tokens, emergent reasoning. | [Paper](https://arxiv.org/abs/2307.15818) |
| **PaLM-E** | Google | 2023 | 562B embodied multimodal LM. Continuous sensor modalities directly in LLMs. Positive transfer across domains. | [Paper](https://arxiv.org/abs/2303.03378) |
| **Open X-Embodiment / RT-X** | 21 Institutions | 2023 | Largest robotics dataset: 22 robots, 527 skills, 160k+ tasks. Positive cross-embodiment transfer. | [Paper](https://arxiv.org/abs/2310.08864) |
| **OpenVLA** | Stanford / UC Berkeley | 2024 | Open-source 7B VLA matching proprietary models. Fine-tunable for new robots and tasks. | [GitHub](https://github.com/openvla/openvla) |
| **NVIDIA GR00T** | NVIDIA | 2024 | Foundation model for humanoids. Multimodal inputs to robot actions. Part of NVIDIA Physical AI platform. | [nvidia.com](https://developer.nvidia.com/isaac) |

### Simulation & Infrastructure for Physical AI

> Training embodied AI requires massive simulation before real-world deployment. These platforms enable sim-to-real transfer, digital twins, and scalable robot learning.

| Platform | Description | Links |
|----------|-------------|-------|
| **NVIDIA Isaac Sim / Isaac Lab** | Production-grade robotics sim with photorealistic rendering and domain randomization. GPU-accelerated RL. | [Developer](https://developer.nvidia.com/isaac/), [GitHub](https://github.com/isaac-sim/) |
| **NVIDIA Omniverse** | Collaborative 3D simulation for digital twins and physics-based robotics. | [nvidia.com/omniverse](https://www.nvidia.com/en-us/omniverse/) |
| **MuJoCo** | DeepMind's open-source physics engine for robotics and RL. Fast, accurate contact dynamics. | [mujoco.org](https://mujoco.org/), [GitHub](https://github.com/google-deepmind/mujoco) |
| **Genesis** | Next-gen open-source differentiable physics engine for gradient-based embodied AI learning. | [GitHub](https://github.com/Genesis-Embodied-AI/Genesis) |

### Reinforcement Learning Environments for Embodied AI

> Training embodied agents requires interactive environments where they can learn through trial and error. These platforms provide the virtual proving grounds for physical intelligence.

| Environment | Description | Links |
|-------------|-------------|-------|
| **Gymnasium (OpenAI Gym)** | Standard RL API by Farama Foundation. Hundreds of environments from classic control to robotics. | [gymnasium.farama.org](https://gymnasium.farama.org/), [GitHub](https://github.com/Farama-Foundation/Gymnasium) |
| **IsaacGym / Isaac Lab** | NVIDIA GPU-accelerated RL. Thousands of parallel envs on one GPU. State-of-art sim-to-real. | [GitHub](https://github.com/isaac-sim/IsaacLab) |
| **ManiSkill** | Large-scale robotics benchmark with GPU-parallelized sim. 20+ manipulation task families. | [GitHub](https://github.com/haosulab/ManiSkill) |
| **Habitat** | Meta's platform for embodied AI in photorealistic 3D. Navigation and rearrangement tasks. | [aihabitat.org](https://aihabitat.org/), [GitHub](https://github.com/facebookresearch/habitat-sim) |
| **MineDojo** | Open-ended agent benchmark on Minecraft. 1000s of tasks, programmatic generation. | [minedojo.org](https://minedojo.org/), [GitHub](https://github.com/MineDojo/MineDojo) |
| **RoboCasa** | Household robot simulation. 150+ object categories, diverse kitchens, procedural generation. | [GitHub](https://github.com/robocasa/robocasa) |
| **BEHAVIOR-1K** | 1,000 everyday activities across 50 scenes. Mobility, manipulation, and social tasks. | [behavior.stanford.edu](https://behavior.stanford.edu/) |

---

