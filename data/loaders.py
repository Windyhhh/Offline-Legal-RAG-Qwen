# -*- coding: utf-8 -*-
"""
文档加载器
"""

import os
import hashlib
from typing import List, Iterator
from langchain_community.document_loaders import TextLoader

class DocumentLoader:
    """文档加载器"""
    
    def __init__(self, data_dir: str):
        self.data_dir = data_dir
    
    def iter_txt_files(self) -> Iterator[str]:
        """遍历文本文件"""
        if not os.path.exists(self.data_dir):
            return
        
        for root, _, files in os.walk(self.data_dir):
            for f in files:
                if f.lower().endswith(('.txt', '.md')):
                    yield os.path.join(root, f)
    
    def load_documents(self) -> List:
        """加载文档列表"""
        documents = []
        loader = None
        seen = set()
        
        for file_path in self.iter_txt_files():
            try:
                loader = TextLoader(file_path, autodetect_encoding=True)
                docs = loader.load()
                
                for doc in docs:
                    content = doc.page_content.strip()
                    if not content:
                        continue
                    
                    # 去重
                    content_hash = hashlib.md5(content.encode('utf-8')).hexdigest()
                    if content_hash in seen:
                        continue
                    seen.add(content_hash)
                    
                    documents.append(doc)
                    
            except Exception as e:
                print(f"跳过文件 {file_path}: {e}")
        
        return documents