# ⚖️ 离线法律 RAG 问答系统 | Offline Legal RAG with Qwen

> **本地部署的法律智能问答——基于 Qwen 大模型 + RAG 检索增强，数据不出本地，隐私安全有保障。**
>
> *Locally-deployed legal Q&A — Qwen LLM + RAG retrieval augmentation, data stays local, privacy guaranteed.*

---

## ⭐ 核心卖点 | Why Star This

| 卖点 | Feature | 一句话 |
|------|---------|--------|
| 🔒 **完全离线** | Fully Offline | 模型和数据都在本地，法律数据不出门 |
| 🤖 **Qwen 大模型** | Qwen LLM | 通义千问开源模型，中文法律理解能力强 |
| 🔍 **RAG 检索增强** | Retrieval-Augmented | 从法律库中精准检索相关法条，减少幻觉 |
| 📚 **法律知识库** | Legal Knowledge Base | 支持法律法规、案例、合同模板的知识库构建 |
| ⚡ **快速部署** | Quick Deploy | 一键启动，无需复杂配置 |

---

## 🏆 技术栈 | Tech Stack

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red?logo=pytorch)
![LangChain](https://img.shields.io/badge/LangChain-0.1+-green?logo=langchain)
![FAISS](https://img.shields.io/badge/FAISS-1.7+-orange?logo=facebook)

---

## 📊 方案对比 | Solution Comparison

| 方案 | 数据隐私 | 中文法律能力 | 可定制性 | 部署成本 |
|------|---------|-------------|---------|---------|
| 在线 API (GPT/Claude) | ❌ 数据上传 | 🟡 中 | ❌ 低 | 🔴 高 |
| 通用搜索引擎 | ❌ 公开数据 | 🟡 中 | ❌ 低 | 🟢 低 |
| **离线 RAG (本项目)** | ✅ 本地 | ✅ 强 | ✅ 高 | 🟡 中 |

---

## 🚀 快速开始 | Quick Start

```bash
git clone https://github.com/Windyhhh/Offline-Legal-RAG-Qwen.git
cd Offline-Legal-RAG-Qwen
pip install -r requirements.txt

# 构建法律知识库
python build_kb.py --docs ./legal_docs

# 启动问答服务
python app.py --model Qwen-7B --kb ./faiss_index
```

---

## 📂 项目结构 | Project Structure

```
Offline-Legal-RAG-Qwen/
├── app.py                     # 问答服务入口
├── build_kb.py                # 知识库构建
├── requirements.txt           # 依赖
├── models/
│   └── qwen_wrapper.py        # Qwen 模型封装
├── retrieval/
│   ├── embedder.py            # 向量化编码
│   └── faiss_store.py         # FAISS 向量库
├── legal_docs/                # 法律文档
│   ├── laws/                  # 法律法规
│   ├── cases/                 # 案例
│   └── contracts/             # 合同模板
├── prompts/                   # Prompt 模板
└── web/                       # Web 界面
```

---

## 🔬 核心架构 | Core Architecture

### RAG 流程 | RAG Pipeline

```
用户问题
  ↓
Query 向量化 (Embedding)
  ↓
FAISS 相似度检索 Top-K 相关法条/案例
  ↓
检索结果 + 用户问题 → Prompt 组装
  ↓
Qwen 大模型生成回答
  ↓
返回答案 + 引用来源
```

### 法律知识库 | Legal Knowledge Base

| 文档类型 | 示例 | 用途 |
|---------|------|------|
| 法律法规 | 民法典、刑法、公司法 | 法条引用 |
| 司法案例 | 最高法指导案例 | 类案参考 |
| 合同模板 | 劳动合同、租赁合同 | 合同审查 |
| 法律文书 | 起诉状、答辩状 | 文书生成 |

---

## 🎯 应用场景 | Use Cases

- ⚖️ **律师助手**：快速检索法条和案例，提高工作效率
- 🏢 **企业法务**：合同审查、法律风险评估
- 🎓 **法学教育**：学生学习法律知识的智能助手
- 👤 **公众咨询**：普通用户的基础法律问题解答
- 🏛️ **法律援助**：为弱势群体提供基础法律帮助

---

## ⚠️ 免责声明 | Disclaimer

本项目仅供学习和研究使用，生成的回答不构成法律意见。具体法律问题请咨询专业律师。

---

## 📄 License

MIT License — 自由使用、修改和分发。

---

> 💡 **法律 + AI 的隐私优先方案，Star ⭐ 支持开源！**
