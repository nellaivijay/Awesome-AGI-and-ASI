# RAG and Vector Databases

> RAG grounds LLMs in real-world data, eliminating hallucinations and enabling knowledge-intensive applications. Full RAG stack: vector storage, retrieval engines, graph RAG, document parsing, and embedding models.

![Vector DB](https://img.shields.io/badge/Vector_DB-Milvus_Qdrant_Chroma-blue?style=flat-square) ![Graph RAG](https://img.shields.io/badge/Graph_RAG-Knowledge_Graphs-purple?style=flat-square) ![Embeddings](https://img.shields.io/badge/Embeddings-OpenAI_Cohere_NVIDIA-green?style=flat-square) ![Document Parsing](https://img.shields.io/badge/Document_Parsing-PDF_OCR-orange?style=flat-square)

### Vector Databases

| Name | Description | Links |
|------|-------------|-------|
| [Milvus](https://github.com/milvus-io/milvus) | Cloud-native, distributed vector database for billion-scale similarity search. Most scalable open-source vector DB. 44k+ stars. | [milvus.io](https://milvus.io/) |
| [Qdrant](https://github.com/qdrant/qdrant) | High-performance vector search engine in Rust. Dense + sparse vectors, hybrid search, payload filtering, quantization. 30k+ stars. | [qdrant.tech](https://qdrant.tech/) |
| [Weaviate](https://github.com/weaviate/weaviate) | AI-native vector database with GraphQL API, built-in vectorization, hybrid search, and generative search modules. 16k+ stars. | [weaviate.io](https://weaviate.io/) |
| [Chroma](https://github.com/chroma-core/chroma) | AI-native open-source embedding database. Extremely easy to start, built-in embedding functions. 16k+ stars. | [trychroma.com](https://trychroma.com/) |
| [pgvector](https://github.com/pgvector/pgvector) | PostgreSQL extension for vector similarity search. HNSW + IVFFlat indexes. Game-changer for Postgres users. 14k+ stars. | [GitHub](https://github.com/pgvector/pgvector) |
| [LanceDB](https://github.com/lancedb/lancedb) | Serverless vector database built on Lance columnar format. Embedded, multimodal, full-text + vector hybrid search. | [lancedb.com](https://lancedb.com/) |
| [Meilisearch](https://github.com/meilisearch/meilisearch) | Lightning-fast search engine API with AI-powered hybrid search (full-text + vector). 57k+ stars. | [meilisearch.com](https://www.meilisearch.com/) |
| [Vespa](https://github.com/vespa-engine/vespa) | Yahoo's battle-tested big data serving engine. ANN + lexical hybrid, tensor expressions, complex ML ranking. | [vespa.ai](https://vespa.ai/) |
| [Pinecone](https://www.pinecone.io/) | Managed vector database for high-performance vector search at scale. | [Docs](https://docs.pinecone.io/) |
| [Zilliz](https://zilliz.com/) | Cloud-native vector database service (managed Milvus). | [zilliz.com](https://zilliz.com/) |
| [Turbopuffer](https://turbopuffer.com/) | Serverless vector database using object storage (S3) for cost-efficient large-scale search. | [Docs](https://turbopuffer.com/docs) |

### RAG Engines & Platforms

| Name | Description | Links |
|------|-------------|-------|
| [RAGFlow](https://github.com/infiniflow/ragflow) | Leading open-source RAG engine with vision-based document parsing (tables, figures, layouts). Multi-recall: vector + full-text + knowledge graph. 78k+ stars. | [ragflow.io](https://ragflow.io/) |
| [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm) | All-in-one AI app with RAG, agents, MCP support. Use any LLM, any document, any vector database. Privacy-first. 58k+ stars. | [useanything.com](https://useanything.com/) |
| [Kotaemon](https://github.com/Cinnamon/kotaemon) | Open-source RAG document QA tool with chat UI, graph RAG, multi-modal support, and citation highlighting. 22k+ stars. | [GitHub](https://github.com/Cinnamon/kotaemon) |
| [Pathway LLM App](https://github.com/pathwaycom/llm-app) | Ready-to-run cloud templates for RAG and AI pipelines with live data sync (Sharepoint, S3, Kafka, Postgres). 60k+ stars. | [pathway.com](https://pathway.com/) |
| [Cognee](https://github.com/topoteretes/cognee) | Memory management for AI agents and apps. Builds knowledge graphs from documents for reasoning-based RAG. 15k+ stars. | [cognee.ai](https://www.cognee.ai/) |
| [R2R (SciPhi)](https://github.com/SciPhi-AI/R2R) | Production RAG engine with hybrid search, knowledge graph building (Neo4j), ingestion pipelines, and REST API. | [Docs](https://r2r-docs.sciphi.ai/) |

### Graph RAG

| Name | Description | Links |
|------|-------------|-------|
| [Microsoft GraphRAG](https://github.com/microsoft/graphrag) | Landmark Graph-based RAG: extracts knowledge graphs from documents, performs global queries via community summaries. 32k+ stars. | [Paper](https://arxiv.org/abs/2404.16130), [Docs](https://microsoft.github.io/graphrag/) |
| [LightRAG](https://github.com/HKUDS/LightRAG) | Faster, simpler alternative to GraphRAG. Dual-level retrieval (entity + thematic) with incremental knowledge graph updates. 15k+ stars. | [GitHub](https://github.com/HKUDS/LightRAG) |
| [PageIndex](https://github.com/VectifyAI/PageIndex) | Document index for vectorless, reasoning-based RAG. Bypasses traditional embedding for reasoning-first retrieval. 25k+ stars. | [GitHub](https://github.com/VectifyAI/PageIndex) |
| [Neo4j GraphRAG](https://github.com/neo4j/neo4j-graphrag-python) | Official Neo4j library for GraphRAG pipelines. KG construction, hybrid retrieval (vector + Cypher). | [Docs](https://neo4j.com/docs/neo4j-graphrag-python/current/) |

### Document Parsing for RAG

| Name | Description | Links |
|------|-------------|-------|
| [Docling](https://github.com/DS4SD/docling) | IBM's fast document conversion: PDFs with layout understanding, table recognition (TableFormer), figure extraction. 20k+ stars. | [Docs](https://ds4sd.github.io/docling/) |
| [Unstructured](https://github.com/Unstructured-IO/unstructured) | Document parsing ETL for RAG. Extracts from PDFs, DOCX, HTML, images, and 30+ formats. 10k+ stars. | [unstructured.io](https://unstructured.io/) |
| [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | Turn any PDF or image into structured data for AI. Supports 100+ languages. 75k+ stars. | [GitHub](https://github.com/PaddlePaddle/PaddleOCR) |

### Advanced RAG Techniques

| Technique | Description | Links |
|-----------|-------------|-------|
| Self-RAG | LLMs that reflect on retrieval decisions using special tokens. Adaptive retrieval — only retrieve when needed. | [Paper](https://arxiv.org/abs/2310.11511), [Code](https://github.com/AkariAsai/self-rag) |
| CRAG (Corrective RAG) | Adds retrieval evaluator + correction mechanism. Falls back to web search if retrieved docs are irrelevant. | [Paper](https://arxiv.org/abs/2401.15884) |
| ColPali (Visual RAG) | Revolutionary: indexes documents as images using vision-language models, eliminating OCR failures entirely. | [Paper](https://arxiv.org/abs/2407.01449), [Code](https://github.com/illuin-tech/colpali) |
| HippoRAG | Neurobiologically-inspired RAG using knowledge graphs mimicking hippocampal memory for multi-hop reasoning. | [Code](https://github.com/OSU-NLP-Group/HippoRAG) |
| RAG Techniques Guide | Comprehensive tutorial repository showcasing 20+ advanced RAG techniques with notebooks. 27k+ stars. | [GitHub](https://github.com/NirDiamant/RAG_Techniques) |

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

