---
description: "Complete RAG stack with vector databases, retrieval engines, Graph RAG, document parsing, and embedding models to ground LLMs in real-world data."
keywords: "RAG, vector database, retrieval augmented generation, embeddings, Pinecone, Weaviate, ChromaDB, Graph RAG"
---
# RAG and Vector Databases

> RAG grounds LLMs in real-world data, eliminating hallucinations and enabling knowledge-intensive applications. Full RAG stack: vector storage, retrieval engines, graph RAG, document parsing, and embedding models.

![Vector DB](https://img.shields.io/badge/Vector_DB-Milvus_Qdrant_Chroma-blue?style=flat-square) ![Graph RAG](https://img.shields.io/badge/Graph_RAG-Knowledge_Graphs-purple?style=flat-square) ![Embeddings](https://img.shields.io/badge/Embeddings-OpenAI_Cohere_NVIDIA-green?style=flat-square) ![Document Parsing](https://img.shields.io/badge/Document_Parsing-PDF_OCR-orange?style=flat-square)

### Vector Databases

| Name | Description | Links |
|------|-------------|-------|
| [Milvus](https://github.com/milvus-io/milvus) | Cloud-native distributed vector DB for billion-scale search. 44k+ stars. | [milvus.io](https://milvus.io/) |
| [Qdrant](https://github.com/qdrant/qdrant) | Rust-based vector search. Dense + sparse, hybrid search, quantization. 30k+ stars. | [qdrant.tech](https://qdrant.tech/) |
| [Weaviate](https://github.com/weaviate/weaviate) | AI-native vector DB with GraphQL, built-in vectorization, hybrid search. 16k+ stars. | [weaviate.io](https://weaviate.io/) |
| [Chroma](https://github.com/chroma-core/chroma) | AI-native open-source embedding DB. Easy to start, built-in embeddings. 16k+ stars. | [trychroma.com](https://trychroma.com/) |
| [pgvector](https://github.com/pgvector/pgvector) | PostgreSQL extension for vector search. HNSW + IVFFlat indexes. 14k+ stars. | [GitHub](https://github.com/pgvector/pgvector) |
| [LanceDB](https://github.com/lancedb/lancedb) | Serverless vector DB on Lance format. Embedded, multimodal, hybrid search. | [lancedb.com](https://lancedb.com/) |
| [Meilisearch](https://github.com/meilisearch/meilisearch) | Fast search API with AI hybrid search (full-text + vector). 57k+ stars. | [meilisearch.com](https://www.meilisearch.com/) |
| [Vespa](https://github.com/vespa-engine/vespa) | Yahoo's big data serving engine. ANN + lexical hybrid, tensor ranking. | [vespa.ai](https://vespa.ai/) |
| [Pinecone](https://www.pinecone.io/) | Managed vector database for high-performance search at scale. | [Docs](https://docs.pinecone.io/) |
| [Zilliz](https://zilliz.com/) | Cloud-native vector DB service (managed Milvus). | [zilliz.com](https://zilliz.com/) |
| [Turbopuffer](https://turbopuffer.com/) | Serverless vector DB on object storage (S3) for cost-efficient search. | [Docs](https://turbopuffer.com/docs) |

### RAG Engines & Platforms

| Name | Description | Links |
|------|-------------|-------|
| [RAGFlow](https://github.com/infiniflow/ragflow) | Open-source RAG engine with vision-based doc parsing. Vector + full-text + KG retrieval. 78k+ stars. | [ragflow.io](https://ragflow.io/) |
| [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm) | All-in-one RAG + agents + MCP. Any LLM, any document, any vector DB. 58k+ stars. | [useanything.com](https://useanything.com/) |
| [Kotaemon](https://github.com/Cinnamon/kotaemon) | Open-source RAG doc QA with chat UI, graph RAG, and citation highlighting. 22k+ stars. | [GitHub](https://github.com/Cinnamon/kotaemon) |
| [Pathway LLM App](https://github.com/pathwaycom/llm-app) | Cloud templates for RAG pipelines with live data sync (S3, Kafka, Postgres). 60k+ stars. | [pathway.com](https://pathway.com/) |
| [Cognee](https://github.com/topoteretes/cognee) | Memory management for AI agents. Builds knowledge graphs for reasoning-based RAG. 15k+ stars. | [cognee.ai](https://www.cognee.ai/) |
| [R2R (SciPhi)](https://github.com/SciPhi-AI/R2R) | Production RAG with hybrid search, KG building (Neo4j), and REST API. | [Docs](https://r2r-docs.sciphi.ai/) |

### Graph RAG

| Name | Description | Links |
|------|-------------|-------|
| [Microsoft GraphRAG](https://github.com/microsoft/graphrag) | Graph-based RAG: extracts KGs from docs, global queries via community summaries. 32k+ stars. | [Paper](https://arxiv.org/abs/2404.16130), [Docs](https://microsoft.github.io/graphrag/) |
| [LightRAG](https://github.com/HKUDS/LightRAG) | Faster GraphRAG alternative. Dual-level retrieval with incremental KG updates. 15k+ stars. | [GitHub](https://github.com/HKUDS/LightRAG) |
| [PageIndex](https://github.com/VectifyAI/PageIndex) | Vectorless, reasoning-based RAG document index. 25k+ stars. | [GitHub](https://github.com/VectifyAI/PageIndex) |
| [Neo4j GraphRAG](https://github.com/neo4j/neo4j-graphrag-python) | Official Neo4j GraphRAG library. KG construction, vector + Cypher retrieval. | [Docs](https://neo4j.com/docs/neo4j-graphrag-python/current/) |

### Document Parsing for RAG

| Name | Description | Links |
|------|-------------|-------|
| [Docling](https://github.com/DS4SD/docling) | IBM's PDF conversion with layout understanding and table recognition. 20k+ stars. | [Docs](https://ds4sd.github.io/docling/) |
| [Unstructured](https://github.com/Unstructured-IO/unstructured) | Document parsing ETL for RAG. Extracts from PDFs, DOCX, HTML, images, 30+ formats. 10k+ stars. | [unstructured.io](https://unstructured.io/) |
| [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | OCR for PDFs/images into structured data. 100+ languages. 75k+ stars. | [GitHub](https://github.com/PaddlePaddle/PaddleOCR) |

### Advanced RAG Techniques

| Technique | Description | Links |
|-----------|-------------|-------|
| Self-RAG | LLMs that reflect on retrieval decisions. Adaptive: only retrieve when needed. | [Paper](https://arxiv.org/abs/2310.11511), [Code](https://github.com/AkariAsai/self-rag) |
| CRAG (Corrective RAG) | Retrieval evaluator + correction. Falls back to web search if docs are irrelevant. | [Paper](https://arxiv.org/abs/2401.15884) |
| ColPali (Visual RAG) | Indexes documents as images via VLMs, eliminating OCR failures. | [Paper](https://arxiv.org/abs/2407.01449), [Code](https://github.com/illuin-tech/colpali) |
| HippoRAG | Neuro-inspired RAG using KGs mimicking hippocampal memory for multi-hop reasoning. | [Code](https://github.com/OSU-NLP-Group/HippoRAG) |
| RAG Techniques Guide | Tutorial repo with 20+ advanced RAG techniques and notebooks. 27k+ stars. | [GitHub](https://github.com/NirDiamant/RAG_Techniques) |

### Embedding Models (2025-2026)

| Model | Provider | Key Notes | Links |
|-------|----------|-----------|-------|
| text-embedding-3-large | OpenAI | 3072 dims (Matryoshka), strong general performance. | [Docs](https://platform.openai.com/docs/guides/embeddings) |
| embed-v4.0 | Cohere | Multimodal (text+image), 128K context, 100+ languages. | [Docs](https://docs.cohere.com/docs/cohere-embed) |
| voyage-3 | Voyage AI | Top MTEB scores (esp. code/finance/law), 32K context. Anthropic-backed. | [Docs](https://docs.voyageai.com/) |
| NV-Embed-v2 | NVIDIA | #1 MTEB overall at release. Decoder-only LLM architecture. 4096 dims. | [HuggingFace](https://huggingface.co/nvidia/NV-Embed-v2) |
| nomic-embed-text-v1.5 | Nomic AI | Fully open (weights + data + code). Matryoshka dimensions. 8K context. | [HuggingFace](https://huggingface.co/nomic-ai/nomic-embed-text-v1.5) |
| jina-embeddings-v3 | Jina AI | Task-specific LoRA adapters, Matryoshka, multilingual. | [HuggingFace](https://huggingface.co/jinaai/jina-embeddings-v3) |
| bge-m3 | BAAI | Multilingual (100 langs), multi-functionality: dense + sparse + ColBERT. | [HuggingFace](https://huggingface.co/BAAI/bge-m3) |
| gte-Qwen2-7B-instruct | Alibaba | LLM-based embedding, top MTEB, instruction-tuned, 32K context. | [HuggingFace](https://huggingface.co/Alibaba-NLP/gte-Qwen2-7B-instruct) |

---

