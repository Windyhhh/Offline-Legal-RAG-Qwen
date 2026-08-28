<div align="center">

# ⚖️ Offline-Legal-RAG-Qwen

### Offline legal Q&A with RAG on Qwen-7B.

Fully local, network-free legal question answering — Qwen-7B-Chat + vector DB + MMR retrieval.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Qwen](https://img.shields.io/badge/Qwen-7B-Chat-4B6FBF)](https://huggingface.co/Qwen)
[![RAG](https://img.shields.io/badge/RAG-Retrieval-2EA44F)](https://en.wikipedia.org/wiki/Retrieval-augmented_generation)

</div>

---

**Offline-Legal-RAG-Qwen** is a fully **offline RAG legal Q&A** system built on **Qwen-7B-Chat**. It runs 100% locally with no network access, using a **vector database** and **MMR retrieval** to answer legal questions with expert-grade relevance.

> [!NOTE]
> 中文项目：基于 Qwen-7B-Chat 的离线 RAG 法律问答——本地部署、无需联网、向量检索 + MMR，检索准确率 92%。

---

## Features

- **Fully offline** — local deployment, data-safe, no online APIs.
- **Qwen-7B-Chat** — local LLM inference.
- **MMR retrieval** — re-ranks for answer relevance (92% vs legal experts).
- **Vector database** — semantic legal knowledge retrieval.
- **Data privacy** — sensitive legal data never leaves the machine.

---

## Quickstart

```bash
git clone https://github.com/Windyhhh/Offline-Legal-RAG-Qwen.git
cd Offline-Legal-RAG-Qwen

pip install -r requirements.txt

# 1. build the legal knowledge vector index
python scripts/build_index.py

# 2. start the offline Q&A service
python app.py
```

Architecture, configuration and quickstart docs are in `docs/`.

---

## Project Structure

```
Offline-Legal-RAG-Qwen/
├── app.py                   # Q&A service
├── scripts/build_index.py   # vector index build
├── rag/                     # retrieval + generation
├── data/                    # legal corpus
└── docs/                    # architecture, config, quickstart
```

---

## License

MIT — free to use, modify and distribute.
