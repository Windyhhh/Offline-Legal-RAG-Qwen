<div align="center">

# ⚖️ Offline-Legal-RAG-Qwen

### Fully offline legal RAG consultation.

Qwen-7B-Chat + Chroma vector store, modular architecture, CI/CD — completely offline legal Q&A.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Qwen](https://img.shields.io/badge/Qwen-7B--Chat-4B77BE)](https://qwenlm.github.io/)
[![Chroma](https://img.shields.io/badge/Chroma-VectorDB-FC60A8)](https://www.trychroma.com/)

</div>

---

**Offline-Legal-RAG-Qwen** is a fully offline **legal consultation** system built on **RAG** — **Qwen-7B-Chat** for generation and **Chroma** for retrieval — with a modular architecture and CI/CD, so legal Q&A runs entirely on your own machine.

> [!NOTE]
> 中文项目：离线 RAG 法律咨询系统——Qwen-7B-Chat + Chroma 向量库，模块化架构，CI/CD，完全离线。

---

## Quickstart

```bash
git clone https://github.com/Windyhhh/Offline-Legal-RAG-Qwen.git
cd Offline-Legal-RAG-Qwen

pip install -r requirements.txt
cp .env.example .env

# run the RAG app
python core/rag_app.py
```

See `core/retriever.py` and `data/` for retrieval and ingestion modules.

---

## Features

- **Fully offline** — no external API calls.
- **RAG pipeline** — Chroma retrieval + Qwen generation.
- **Modular + CI/CD** — clean layering with a GitHub Actions workflow.

---

## Project Structure

```
Offline-Legal-RAG-Qwen/
├── core/                 # rag_app, retriever, utils
├── config/               # settings, environment
├── data/                 # loaders, processors
├── chroma_db/            # vector store
├── .github/workflows/    # ci-cd.yml
└── .env.example
```

---

## License

MIT — free to use, modify and distribute.
