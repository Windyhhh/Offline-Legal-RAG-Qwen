# -*- coding: utf-8 -*-
"""
检索逻辑
"""

from typing import List
from langchain.schema import Document

class Retriever:
    """检索器"""
    
    def __init__(self, vectorstore, search_k: int = 4):
        self.vectorstore = vectorstore
        self.search_k = search_k
        self._setup_retriever()
    
    def _setup_retriever(self):
        """设置检索器"""
        self.retriever = self.vectorstore.as_retriever(
            search_type='mmr',
            search_kwargs={
                "k": self.search_k,
                "fetch_k": max(8, self.search_k * 2),
                "lambda_mult": 0.5
            }
        )
    
    def retrieve(self, query: str) -> List[str]:
        """检索相关文档"""
        docs = self.retriever.get_relevant_documents(query)
        return [
            f"[来源:{d.metadata.get('source','')}]\n{d.page_content}" 
            for d in docs
        ]
    
    def format_contexts(self, contexts: List[str]) -> str:
        """格式化上下文"""
        return "\n\n".join([
            f"【检索片段{i+1}】\n{c}" 
            for i, c in enumerate(contexts)
        ])
    
    def format_prompt(self, query: str, contexts: List[str]) -> str:
        """格式化提示词"""
        ctx = self.format_contexts(contexts)
        return (
            "你是离线法律助手，请基于给定片段谨慎作答，明确列出引用片段编号；"
            "如无法从片段得出结论，请说明'依据不足'。\n"
            f"用户问题：{query}\n\n"
            f"参考片段：\n{ctx}\n\n"
            "请给出：\n1) 简明结论；2) 依据与条文引用；3) 风险提示。"
        )