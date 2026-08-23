# -*- coding: utf-8 -*-
"""
文本处理器
"""

from typing import List
from langchain_text_splitters import RecursiveCharacterTextSplitter

class TextProcessor:
    """文本处理器"""
    
    def __init__(
        self, 
        chunk_size: int = 1000, 
        chunk_overlap: int = 150,
        separators: List[str] = None
    ):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.separators = separators or [
            "\n\n", "\n", "。", "！", "？", ".", " "
        ]
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=self.separators
        )
    
    def split_documents(self, documents) -> List:
        """分割文档"""
        return self.splitter.split_documents(documents)
    
    def split_text(self, text: str) -> List[str]:
        """分割文本"""
        return self.splitter.split_text(text)