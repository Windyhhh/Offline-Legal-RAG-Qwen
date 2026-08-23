# -*- coding: utf-8 -*-
"""
RAG应用主类
"""

import os
import torch
from typing import List, Optional, Tuple
from config.settings import SystemConfig
from config.environment import setup_environment, should_load_llm, should_use_tiny_embedding
from models.embeddings import EmbeddingFactory
from models.llm import Qwen7BModel
from data.loaders import DocumentLoader
from data.processors import TextProcessor
from data.vectorstore import VectorStoreManager
from core.retriever import Retriever

class LegalRAGApp:
    """法律RAG应用"""
    
    def __init__(
        self, 
        base_model_root: Optional[str] = None,
        load_llm: Optional[bool] = None
    ):
        # 环境设置
        setup_environment()
        
        # 配置
        self.config = SystemConfig()
        self.config.BASE_MODEL_ROOT = base_model_root or self.config.BASE_MODEL_ROOT
        
        # LLM加载控制
        if load_llm is None:
            load_llm = should_load_llm()
        self.load_llm = load_llm
        
        # 设备检查
        self._device_check()
        
        # 目录设置
        self._setup_dirs()
        
        # 初始化组件
        self._init_components()
    
    def _device_check(self):
        """设备检查"""
        if torch.cuda.is_available():
            mem = torch.cuda.get_device_properties(0).total_memory / (1024**3)
            print(f"GPU 显存: {mem:.2f} GB (建议>=8GB, 已启用4-bit)")
        else:
            print("⚠ CUDA不可用，将使用CPU模式")
    
    def _setup_dirs(self):
        """设置目录"""
        os.makedirs(self.config.DATA_DIR, exist_ok=True)
        os.makedirs(self.config.DB_DIR, exist_ok=True)
    
    def _init_components(self):
        """初始化组件"""
        # 检测模型路径
        self.llm_path = self.config.get_llm_path()
        self.emb_path = self.config.get_emb_path()
        
        if not self.llm_path:
            print("❌ 未找到 Qwen-7B-Chat，本地路径无效")
        if not self.emb_path:
            print("⚠ 未找到嵌入模型，将使用退化方案")
        
        # 初始化嵌入模型
        use_tiny = should_use_tiny_embedding()
        self.embedding = EmbeddingFactory.create_embedding(
            use_tiny=use_tiny,
            model_path=self.emb_path,
            use_langchain=True
        )
        
        # 初始化向量库
        self.vectorstore_manager = VectorStoreManager(
            embedding_function=self.embedding,
            db_dir=self.config.DB_DIR,
            collection_name=self.config.COLLECTION_NAME
        )
        
        # 初始化文档加载器和处理器
        self.document_loader = DocumentLoader(self.config.DATA_DIR)
        self.text_processor = TextProcessor(
            chunk_size=self.config.CHUNK_SIZE,
            chunk_overlap=self.config.CHUNK_OVERLAP,
            separators=self.config.SEPARATORS
        )
        
        # 构建向量库
        self._build_vectorstore()
        
        # 初始化检索器
        self.retriever = Retriever(
            vectorstore=self.vectorstore,
            search_k=self.config.DEFAULT_SEARCH_K
        )
        
        # 初始化LLM
        if self.load_llm:
            self._init_llm()
    
    def _build_vectorstore(self):
        """构建向量库"""
        documents = self.document_loader.load_documents()
        if documents:
            documents = self.text_processor.split_documents(documents)
        
        self.vectorstore = self.vectorstore_manager.get_or_create(documents)
        
        if not documents:
            print("⚠ 未发现法律文本(.txt/.md)，请放入 legal_docs/ 目录后重启。将创建空索引。")
    
    def _init_llm(self):
        """初始化LLM"""
        if not self.llm_path:
            print("⚠ 未找到LLM模型路径，跳过LLM初始化")
            self.llm_model = None
            return
        
        self.llm_model = Qwen7BModel(self.llm_path)
        self.tokenizer, self.llm = self.llm_model.load()
    
    def chat(self, query: str, history: List[List[str]] = None) -> str:
        """聊天接口"""
        if history is None:
            history = []
        
        # 检索上下文
        contexts = self.retriever.retrieve(query) if query.strip() else []
        
        # 干跑模式
        if self.llm is None:
            preview = "\n\n".join(contexts[:2]) if contexts else "无检索结果（请放入 legal_docs/ 文本）"
            return (
                f"[DRY_RUN] 已完成检索与管线检查。\n\n"
                f"问题：{query}\n\n"
                f"检索预览：\n{preview}\n\n"
                f"提示：已跳过大模型生成（NO_LLM/DRY_RUN 生效）。"
            )
        
        # 生成回复
        prompt = self.retriever.format_prompt(query, contexts)
        return self.llm_model.generate(
            tokenizer=self.tokenizer,
            model=self.llm,
            prompt=prompt,
            max_new_tokens=self.config.MAX_NEW_TOKENS,
            temperature=self.config.TEMPERATURE,
            top_p=self.config.TOP_P
        )