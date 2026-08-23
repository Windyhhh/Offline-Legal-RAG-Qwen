# -*- coding: utf-8 -*-
"""
向量数据库管理
"""

import os
from typing import List, Optional
from langchain_community.vectorstores import Chroma
from chromadb.config import Settings

class VectorStoreManager:
    """向量数据库管理器"""
    
    def __init__(
        self, 
        embedding_function, 
        db_dir: str,
        collection_name: str = "legal_kb"
    ):
        self.embedding_function = embedding_function
        self.db_dir = db_dir
        self.collection_name = collection_name
        self.client_settings = Settings(
            anonymized_telemetry=False,
            is_persistent=True
        )
        
        # 确保目录存在
        os.makedirs(db_dir, exist_ok=True)
    
    def create_from_documents(self, documents: List, metadata: dict = None) -> Chroma:
        """从文档创建向量库"""
        if not documents:
            print("⚠ 无文档需要索引")
            return self.load_existing()
        
        metadata = metadata or {"hnsw:space": "cosine"}
        
        print(f"构建向量库，文档段落数: {len(documents)}")
        
        vs = Chroma.from_documents(
            documents=documents,
            embedding_function=self.embedding_function,
            persist_directory=self.db_dir,
            collection_name=self.collection_name,
            client_settings=self.client_settings,
            collection_metadata=metadata
        )
        vs.persist()
        return vs
    
    def load_existing(self) -> Chroma:
        """加载已存在的向量库"""
        return Chroma(
            persist_directory=self.db_dir,
            embedding_function=self.embedding_function,
            collection_name=self.collection_name,
            client_settings=self.client_settings,
            collection_metadata={"hnsw:space": "cosine"}
        )
    
    def get_or_create(self, documents: List = None) -> Chroma:
        """获取或创建向量库"""
        # 如果有新的文档或数据库为空，重新构建
        if documents or not os.listdir(self.db_dir):
            print("✓ 构建新的向量库")
            return self.create_from_documents(documents)
        else:
            print("✓ 载入已存在的向量库")
            return self.load_existing()