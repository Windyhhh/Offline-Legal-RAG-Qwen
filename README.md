# ⚖️ Offline Legal RAG (Qwen) | 离线智能法律咨询系统

> **High-performance offline RAG (Retrieval-Augmented Generation) legal consultation system based on Qwen-7B-Chat. Chroma vector store, modular architecture, CI/CD pipeline, and complete documentation. Runs fully offline without external API calls.**
>
> 基于 Qwen-7B-Chat 的高性能离线 RAG（检索增强生成）法律咨询系统。Chroma 向量存储，模块化架构，CI/CD 流水线，完整文档。完全离线运行，无需外部 API 调用。

---

## 🌟 Why This Project? | 项目亮点

Legal consultation requires accurate, context-aware responses grounded in reliable legal knowledge. Online LLM APIs raise concerns about **data privacy, cost, and availability**. This project implements a **fully offline RAG system** using **Qwen-7B-Chat** as the language model and **Chroma** as the vector database — enabling private, cost-free legal consultation with retrieval-augmented generation. The modular architecture separates concerns into core RAG logic, data processing, model wrappers, configuration, and UI, with a complete CI/CD pipeline.

法律咨询需要基于可靠法律知识的准确、上下文感知的回答。在线 LLM API 带来**数据隐私、成本和可用性**的担忧。本项目实现了一个**完全离线的 RAG 系统**，使用 **Qwen-7B-Chat** 作为语言模型，**Chroma** 作为向量数据库——实现私密、免费的法律咨询与检索增强生成。模块化架构将关注点分离为核心 RAG 逻辑、数据处理、模型封装、配置和 UI，并配有完整的 CI/CD 流水线。

| Feature | Details |
|---------|---------|
| **LLM** | Qwen-7B-Chat (offline, local inference) |
| **Vector Store** | Chroma (embedded SQLite, no external server) |
| **Embeddings** | Sentence-Transformers / HuggingFace embeddings |
| **Architecture** | Modular: core / data / models / config / ui |
| **RAG Pipeline** | Query → Retrieve → Augment → Generate |
| **Offline** | Fully offline, no external API calls |
| **CI/CD** | GitHub Actions workflow (ci-cd.yml) |
| **UI** | Command-line interface (interface.py) |
| **Data Pipeline** | Loaders → Processors → VectorStore |
| **Config** | Environment-based (.env.example) + Python settings |

---

## 🏗️ Architecture | 架构设计

```
┌─────────────────────────────────────────────────────────────┐
│                      User Query (Legal Question)              │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                   Core RAG Application                         │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │  core/rag_app.py                                          │  │
│  │  • Orchestrates full RAG pipeline                         │  │
│  │  • Query processing → retrieval → generation → response   │  │
│  │  • Context assembly from retrieved chunks                  │  │
│  └─────────────────────────────────────────────────────────┘  │
└──────────────┬───────────────────────────────┬───────────────┘
               │                               │
               ▼                               ▼
┌──────────────────────────┐     ┌──────────────────────────┐
│    Retriever (core)       │     │    LLM (models)          │
│  core/retriever.py        │     │  models/llm.py           │
│                           │     │                           │
│  • Query embedding        │     │  • Qwen-7B-Chat loader   │
│  • Vector similarity      │     │  • Prompt construction    │
│    search (Chroma)        │     │  • Inference (offline)   │
│  • Top-k chunk retrieval  │     │  • Response generation    │
│  • Relevance scoring      │     │                           │
└──────────────┬───────────┘     └──────────────┬────────────┘
               │                                  │
               ▼                                  ▼
┌──────────────────────────┐     ┌──────────────────────────┐
│    Vector Store (data)    │     │    Embeddings (models)   │
│  data/vectorstore.py      │     │  models/embeddings.py    │
│                           │     │                           │
│  • Chroma client          │     │  • Sentence-Transformers │
│  • Collection management  │     │  • HuggingFace embeddings│
│  • Document ingestion     │     │  • Batch embedding       │
│  • Similarity search      │     │  • Dimension config      │
└──────────────┬───────────┘     └──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────────┐
│                   Data Processing Layer                        │
│  ┌─────────────────────┐  ┌─────────────────────┐           │
│  │  Loaders (data)     │  │  Processors (data)  │           │
│  │  data/loaders.py    │  │  data/processors.py │           │
│  │                     │  │                     │           │
│  │  • PDF loading      │  │  • Text chunking    │           │
│  │  • Text file load   │  │  • Cleaning         │           │
│  │  • Directory scan   │  │  • Normalization    │           │
│  │  • Metadata extract │  │  • Overlap windows  │           │
│  └─────────────────────┘  └─────────────────────┘           │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│              Legal Knowledge Base (Documents)                  │
│         Laws, regulations, case law, legal articles            │
└─────────────────────────────────────────────────────────────┘
```

---

## 📁 Project Structure | 项目结构

```
Offline-Legal-RAG-Qwen/
├── main.py                         # Application entry point
├── requirements.txt                # Python dependencies
├── .env.example                    # Environment variable template
├── .gitignore
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
├── README.md
├── 爆款博客.md                      # Technical blog (40KB)
├── .github/
│   └── workflows/
│       └── ci-cd.yml               # GitHub Actions CI/CD pipeline
├── chroma_db/                      # Chroma vector database
│   └── chroma.sqlite3              # Embedded SQLite vector store
├── config/                         # Configuration
│   ├── __init__.py
│   ├── settings.py                 # Application settings
│   └── environment.py              # Environment variable handling
├── core/                           # Core RAG logic
│   ├── __init__.py
│   ├── rag_app.py                  # Main RAG application orchestrator
│   ├── retriever.py                # Document retriever
│   └── utils.py                    # Utility functions
├── data/                           # Data processing
│   ├── __init__.py
│   ├── loaders.py                  # Document loaders (PDF, text, etc.)
│   ├── processors.py               # Text processors (chunking, cleaning)
│   └── vectorstore.py              # Chroma vector store wrapper
├── models/                         # Model wrappers
│   ├── __init__.py
│   ├── llm.py                      # Qwen-7B-Chat LLM wrapper
│   └── embeddings.py               # Embedding model wrapper
├── ui/                             # User interface
│   ├── __init__.py
│   └── interface.py                # CLI interface
├── scripts/                        # Helper scripts
│   ├── setup.ps1                   # Windows setup script
│   └── run_dry.ps1                 # Dry-run test script
└── docs/                           # Documentation
    ├── architecture.md             # Architecture design document
    ├── configuration.md            # Configuration guide
    └── quickstart.md               # Quick start guide
```

---

## 🚀 Quick Start | 快速开始

### 1. Prerequisites | 前置条件

- Python 3.9+
- PyTorch (for Qwen-7B-Chat inference)
- At least 16GB RAM (32GB recommended for 7B model)
- (Optional) GPU with CUDA for faster inference

### 2. Installation | 安装

```bash
# Clone the repository
git clone https://github.com/Windyhhh/Offline-Legal-RAG-Qwen.git
cd Offline-Legal-RAG-Qwen

# Install dependencies
pip install -r requirements.txt

# (Windows) Run setup script
powershell -ExecutionPolicy Bypass -File scripts/setup.ps1
```

### 3. Configuration | 配置

```bash
# Copy environment template
cp .env.example .env

# Edit .env with your settings:
# MODEL_PATH=./models/Qwen-7B-Chat
# EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
# CHROMA_PERSIST_DIR=./chroma_db
# TOP_K=5
```

### 4. Ingest Legal Documents | 导入法律文档

```python
from data.loaders import DocumentLoader
from data.processors import TextProcessor
from data.vectorstore import VectorStoreManager

# Load legal documents
loader = DocumentLoader()
documents = loader.load_directory("./legal_docs/")

# Process and chunk
processor = TextProcessor(chunk_size=512, chunk_overlap=50)
chunks = processor.process(documents)

# Store in Chroma
vs = VectorStoreManager()
vs.add_documents(chunks)
```

### 5. Run Consultation | 运行咨询

```bash
# Start the CLI interface
python main.py

# Or run dry-run test
powershell -ExecutionPolicy Bypass -File scripts/run_dry.ps1
```

### 6. Programmatic Usage | 编程式使用

```python
from core.rag_app import RAGApp

# Initialize RAG application
app = RAGApp(model_path="./models/Qwen-7B-Chat",
             chroma_dir="./chroma_db",
             top_k=5)

# Ask a legal question
question = "劳动合同到期不续签，公司需要支付经济补偿吗？"
response = app.query(question)

print(f"Question: {question}")
print(f"Answer: {response['answer']}")
print(f"Sources: {response['sources']}")
```

---

## 🔬 RAG Pipeline | RAG 流水线

### Step 1: Query Processing | 查询处理

```python
# Normalize and embed the user query
query_embedding = embedding_model.encode(query)
```

### Step 2: Retrieval | 检索

```python
# Search Chroma for top-k most similar document chunks
results = chroma_collection.query(
    query_embeddings=[query_embedding],
    n_results=top_k
)
retrieved_chunks = results['documents'][0]
```

### Step 3: Augmentation | 增强

```python
# Construct augmented prompt with retrieved context
context = "\n\n".join(retrieved_chunks)
prompt = f"""基于以下法律知识回答问题。如果知识中没有相关内容，请说明。

法律知识：
{context}

问题：{query}

回答："""
```

### Step 4: Generation | 生成

```python
# Generate response using Qwen-7B-Chat (offline)
response = qwen_model.generate(prompt, max_new_tokens=512, temperature=0.3)
```

---

## 📊 Configuration Options | 配置选项

| Parameter | Environment Variable | Default | Description |
|-----------|---------------------|---------|-------------|
| Model Path | `MODEL_PATH` | `./models/Qwen-7B-Chat` | Local Qwen model directory |
| Embedding Model | `EMBEDDING_MODEL` | `all-MiniLM-L6-v2` | Sentence transformer model |
| Chroma Dir | `CHROMA_PERSIST_DIR` | `./chroma_db` | Vector store persistence path |
| Top K | `TOP_K` | `5` | Number of retrieved chunks |
| Chunk Size | `CHUNK_SIZE` | `512` | Document chunk size (tokens) |
| Chunk Overlap | `CHUNK_OVERLAP` | `50` | Overlap between chunks |
| Max New Tokens | `MAX_NEW_TOKENS` | `512` | Max generation length |
| Temperature | `TEMPERATURE` | `0.3` | Generation temperature |
| Device | `DEVICE` | `auto` | CPU / CUDA / auto |

---

## 📚 References | 参考文献

1. **Lewis, P., et al.** (2020). *Retrieval-augmented generation for knowledge-intensive NLP tasks.* NeurIPS.
2. **Bai, J., et al.** (2023). *Qwen Technical Report.* arXiv:2309.16609.
3. **Chroma.** (2024). *Chroma: The AI-native open-source embedding database.*
4. **Reimers, N., & Gurevych, I.** (2019). *Sentence-BERT: Sentence embeddings using Siamese BERT-networks.* EMNLP.
5. **Gao, Y., et al.** (2023). *Retrieval augmentation for large language models: A survey.* arXiv:2312.10997.

---

## 📄 License | 许可证

MIT License — free to use, modify, and distribute.

---

<div align="center">

**Built with ⚖️ for offline legal AI**

[Report Bug](https://github.com/Windyhhh/Offline-Legal-RAG-Qwen/issues) · [Request Feature](https://github.com/Windyhhh/Offline-Legal-RAG-Qwen/issues)

</div>
