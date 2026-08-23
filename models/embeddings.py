# -*- coding: utf-8 -*-
"""
嵌入模型管理
"""

import os
import hashlib
import math
import numpy as np
from typing import List, Optional
import torch

class TinyHashEmbedding:
    """极简哈希向量器（仅用于安装/健康检查阶段）"""
    
    def __init__(self, dim: int = 384):
        self.dim = dim
    
    def _vec(self, text: str):
        """生成文本向量"""
        h = hashlib.blake2b(text.encode('utf-8'), digest_size=32).digest()
        # 重复到指定维度
        reps = math.ceil(self.dim / len(h))
        byts = (h * reps)[:self.dim]
        arr = (np.frombuffer(byts, dtype=np.uint8).astype('float32') - 127.5) / 127.5
        # L2标准化
        n = np.linalg.norm(arr) + 1e-9
        return (arr / n).tolist()
    
    def embed_documents(self, texts: List[str]):
        """嵌入文档列表"""
        return [self._vec(t) for t in texts]
    
    def embed_query(self, text: str):
        """嵌入查询文本"""
        return self._vec(text)

class LocalHFEmbedding:
    """本地HuggingFace嵌入模型"""
    
    def __init__(self, model_path: str):
        self.model_path = model_path
        self.use_st = False
        self._load_model()
    
    def _load_model(self):
        """加载模型"""
        try:
            from sentence_transformers import SentenceTransformer
            self.st = SentenceTransformer(
                self.model_path, 
                device='cuda' if torch.cuda.is_available() else 'cpu'
            )
            self.use_st = True
        except ImportError:
            from transformers import AutoTokenizer, AutoModel
            self.tok = AutoTokenizer.from_pretrained(self.model_path, trust_remote_code=True)
            self.model = AutoModel.from_pretrained(self.model_path, trust_remote_code=True)
            if torch.cuda.is_available():
                self.model = self.model.half().to('cuda')
            self.model.eval()
    
    def _pool(self, outputs, attn_mask):
        """池化操作"""
        last_hidden = outputs[0]
        mask = attn_mask.unsqueeze(-1).expand(last_hidden.size()).float()
        summed = torch.sum(last_hidden * mask, 1)
        counts = torch.clamp(mask.sum(1), min=1e-9)
        return torch.nn.functional.normalize(summed / counts, p=2, dim=1)
    
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """嵌入文档列表"""
        if self.use_st:
            embs = self.st.encode(
                texts, 
                batch_size=32, 
                normalize_embeddings=True, 
                show_progress_bar=False
            )
            return [e.tolist() for e in embs]
        
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        all_vecs = []
        
        for i in range(0, len(texts), 16):
            batch = texts[i:i+16]
            with torch.no_grad():
                enc = self.tok(
                    batch, 
                    padding=True, 
                    truncation=True, 
                    max_length=1024, 
                    return_tensors='pt'
                ).to(device)
                outs = self.model(**enc)
                vecs = self._pool(outs, enc['attention_mask']).cpu().tolist()
                all_vecs.extend(vecs)
        
        return all_vecs
    
    def embed_query(self, text: str) -> List[float]:
        """嵌入查询文本"""
        return self.embed_documents([text])[0]

class EmbeddingFactory:
    """嵌入模型工厂"""
    
    @staticmethod
    def create_embedding(
        use_tiny: bool = False,
        model_path: Optional[str] = None,
        use_langchain: bool = True
    ):
        """创建嵌入模型"""
        if use_tiny:
            return TinyHashEmbedding()
        
        if use_langchain:
            try:
                from langchain_community.embeddings import HuggingFaceEmbeddings as LCEmb
                return LCEmb(
                    model_name=model_path,
                    model_kwargs={"device": 'cuda' if torch.cuda.is_available() else 'cpu'},
                    encode_kwargs={"normalize_embeddings": True}
                )
            except ImportError:
                pass
        
        if model_path:
            return LocalHFEmbedding(model_path)
        
        return TinyHashEmbedding()