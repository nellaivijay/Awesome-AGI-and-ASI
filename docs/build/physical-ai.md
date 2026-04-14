---
description: "AGI cannot exist only in text -- it must understand and act in the physical world. **Physical AI** bridges foundation models with embodiment: humanoid robots, manipulation, navigation, and physics simulation. Moravec's Paradox -- sensorimotor skills are harder than abstract reasoning -- remains one of the deepest unsolved AGI challenges."
keywords: "physical AI, embodied intelligence, robotics, VLA models, humanoid robots, simulation, Isaac Sim"
---
# Physical AI & Embodied Intelligence

> AGI cannot exist only in text -- it must understand and act in the physical world. **Physical AI** bridges foundation models with embodiment: humanoid robots, manipulation, navigation, and physics simulation. Moravec's Paradox -- sensorimotor skills are harder than abstract reasoning -- remains one of the deepest unsolved AGI challenges.

![Robotics](https://img.shields.io/badge/Robotics-Humanoid-red?style=flat-square) ![VLA](https://img.shields.io/badge/VLA-Vision--Language--Action-blue?style=flat-square) ![Simulation](https://img.shields.io/badge/Simulation-Isaac_MuJoCo-green?style=flat-square) ![Embodied](https://img.shields.io/badge/Embodied_AI-Physical_Intelligence-purple?style=flat-square)

### Humanoid Robotics & AGI Hardware

> The race to build general-purpose humanoid robots capable of operating in unstructured human environments. These platforms are the physical embodiment layer for AGI.

| Company | Description | Links |
|---------|-------------|-------|
| **Figure AI** | Humanoid robots with advanced AI. Partnered with OpenAI and Microsoft for embodied AI. Figure 02 demonstrates autonomous manipulation, language-guided task execution, and learning from human feedback. Raised $2.6B+. | [figure.ai](https://www.figure.ai/) |
| **Tesla Optimus** | General-purpose humanoid robot leveraging Tesla's massive autonomous driving AI stack (FSD neural nets, Dojo supercomputer). Targeting manufacturing and consumer deployment at scale. | [tesla.com](https://www.tesla.com/) |
| **Boston Dynamics** | Pioneers of advanced locomotion. Atlas (humanoid) and Spot (quadruped) set the standard for physical capability, agility, and dexterity. Now Hyundai-owned, pivoting to AI-first control. | [bostondynamics.com](https://www.bostondynamics.com/) |
| **1X Technologies** | NEO humanoid robot with human-like form factor. Backed by OpenAI. Focused on safe, embodied AI for real-world deployment in homes and workplaces. | [1x.tech](https://www.1x.tech/) |
| **Unitree Robotics** | Democratizing humanoid robotics with affordable platforms (G1, H1 series). Enables broad research access to embodied AI experimentation. | [unitree.com](https://www.unitree.com/) |
| **Sanctuary AI** | Phoenix humanoid robot powered by "Carbon" -- a proprietary AI system designed for general-purpose task learning and autonomous execution. | [sanctuary.ai](https://www.sanctuary.ai/) |
| **Agility Robotics** | Digit bipedal robot designed for logistics and warehouse automation. Real-world deployment partner with Amazon. | [agilityrobotics.com](https://www.agilityrobotics.com/) |
| **Apptronik** | Apollo full-size humanoid robot for industrial applications. Emphasis on safe human-robot collaboration. Mercedes-Benz partnership. | [apptronik.com](https://www.apptronik.com/) |

### Robot Foundation Models (Vision-Language-Action)

> The frontier of embodied AI research: models that take visual observations and language commands as input and directly output robot motor actions. VLA models represent the convergence of foundation models and physical intelligence.

| Model | Org | Year | Description | Links |
|-------|-----|------|-------------|-------|
| **Gemini Robotics 1.5** | Google DeepMind | 2025 | Agentic VLA model that turns visual information and language instructions into motor commands. Generality across novel situations, dexterity (origami, food prep), agentic tool-use, and thinking before acting. Supports multiple embodiments (ALOHA, Franka, Apptronik Apollo). Dual approach with Robotics-ER 1.5 for embodied reasoning. | [Site](https://deepmind.google/models/gemini-robotics/), [Report](https://deepmind.google/models/gemini-robotics/gemini-robotics/) |
| **pi0** | Physical Intelligence | 2024 | VLA flow model for general robot control. Novel flow matching architecture on top of pre-trained VLM. Trained on diverse dexterous tasks (laundry folding, table cleaning, box assembly) across single-arm, dual-arm, and mobile manipulators. Open-sourced weights. | [Paper](https://arxiv.org/abs/2410.24164), [Site](https://www.physicalintelligence.company/) |
| **RT-2** | Google DeepMind | 2023 | Vision-Language-Action model that transfers web-scale knowledge to robotic control. Expresses actions as text tokens, enabling emergent reasoning (pick up the "improvised hammer" -> picks rock). 6k evaluation trials. | [Paper](https://arxiv.org/abs/2307.15818) |
| **PaLM-E** | Google | 2023 | 562B-parameter embodied multimodal language model. Directly incorporates continuous sensor modalities into LLMs. Positive transfer across internet-scale language, vision, and robotics domains. | [Paper](https://arxiv.org/abs/2303.03378) |
| **Open X-Embodiment / RT-X** | 21 Institutions | 2023 | Largest robotics dataset: 22 robots, 527 skills, 160k+ tasks from 21 institutions. RT-X model shows positive transfer across robot morphologies. The "ImageNet moment" for robotics. | [Paper](https://arxiv.org/abs/2310.08864) |
| **OpenVLA** | Stanford / UC Berkeley | 2024 | Open-source 7B-parameter VLA. Democratizes embodied AI research -- matches proprietary models on manipulation benchmarks. Fine-tunable for new robots and tasks. | [GitHub](https://github.com/openvla/openvla) |
| **NVIDIA GR00T** | NVIDIA | 2024 | Foundation model for humanoid robots. Multimodal inputs (text, video, demonstration) to robot actions. Part of NVIDIA's Physical AI platform alongside Isaac and Cosmos. | [nvidia.com](https://developer.nvidia.com/isaac) |

### Simulation & Infrastructure for Physical AI

> Training embodied AI requires massive simulation before real-world deployment. These platforms enable sim-to-real transfer, digital twins, and scalable robot learning.

| Platform | Description | Links |
|----------|-------------|-------|
| **NVIDIA Isaac Sim / Isaac Lab** | Production-grade robotics simulation platform with photorealistic rendering, physics accuracy, and domain randomization. Isaac Lab provides GPU-accelerated RL environments for robot learning at scale. | [Developer](https://developer.nvidia.com/isaac/), [GitHub](https://github.com/isaac-sim/) |
| **NVIDIA Omniverse** | Collaborative 3D simulation platform for building digital twins and physics-based robotics simulation. Foundation for NVIDIA's Physical AI ecosystem. | [nvidia.com/omniverse](https://www.nvidia.com/en-us/omniverse/) |
| **MuJoCo** | Google DeepMind's open-source physics engine optimized for robotics and biomechanics. Fast, accurate contact dynamics. The standard tool for embodied AI research and RL benchmarking. | [mujoco.org](https://mujoco.org/), [GitHub](https://github.com/google-deepmind/mujoco) |
| **Genesis** | Next-generation open-source physics engine for embodied AI. Differentiable simulation enabling gradient-based learning for physical systems. | [GitHub](https://github.com/Genesis-Embodied-AI/Genesis) |
