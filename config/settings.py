# -*- coding: utf-8 -*-
"""
系统配置
"""

import os
from typing import Optional

class SystemConfig:
    """系统配置类"""
    
    # 模型配置
    BASE_MODEL_ROOT: str = os.environ.get('MODEL_ROOT', r"E:\\PythonProject\\model")
    LLM_CANDIDATES = [
        "Qwen-7B-Chat-int4", "qwen-7b-chat-int4", 
        "Qwen-7B-Chat", "qwen-7b-chat"
    ]
    EMB_CANDIDATES = [
        "qwen-0.6b-embedding", "qwen-embedding-0.6b", 
        "qwen-embedding", "qwen-0.6b-embed"
    ]
    
    # 数据配置
    DATA_DIR: str = 'legal_docs'
    DB_DIR: str = 'chroma_db'
    
    # 文本分割配置
    CHUNK_SIZE: int = 1000
    CHUNK_OVERLAP: int = 150
    SEPARATORS = ["\n\n", "\n", "。", "！", "？", ".", " "]
    
    # 检索配置
    DEFAULT_SEARCH_K: int = 4
    FETCH_K_MULTIPLIER: int = 2
    LAMBDA_MULT: float = 0.5
    
    # 生成配置
    MAX_NEW_TOKENS: int = 512
    TEMPERATURE: float = 0.2
    TOP_P: float = 0.9
    
    # 向量配置
    COLLECTION_NAME: str = "legal_kb"
    HNSW_SPACE: str = "cosine"
    
    @classmethod
    def get_llm_path(cls) -> Optional[str]:
        """检测LLM模型路径"""
        for candidate in cls.LLM_CANDIDATES:
            path = os.path.join(cls.BASE_MODEL_ROOT, candidate)
            if os.path.exists(path):
                return path
        return None
    
    @classmethod
    def get_emb_path(cls) -> Optional[str]:
        """检测嵌入模型路径"""
        for candidate in cls.EMB_CANDIDATES:
            path = os.path.join(cls.BASE_MODEL_ROOT, candidate)
            if os.path.exists(path):
                return path
        return None