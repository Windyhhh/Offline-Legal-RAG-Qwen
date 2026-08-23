# -*- coding: utf-8 -*-
"""
工具函数
"""

import os
import sys
from typing import Optional

def check_environment() -> dict:
    """检查运行环境"""
    info = {
        'python_version': sys.version,
        'cuda_available': False,
        'gpu_memory': 0,
        'transformers_available': False,
        'torch_available': False
    }
    
    try:
        import torch
        info['torch_available'] = True
        info['cuda_available'] = torch.cuda.is_available()
        if info['cuda_available']:
            info['gpu_memory'] = torch.cuda.get_device_properties(0).total_memory / (1024**3)
    except ImportError:
        pass
    
    try:
        import transformers
        info['transformers_available'] = True
    except ImportError:
        pass
    
    return info

def print_system_info():
    """打印系统信息"""
    info = check_environment()
    
    print("=== 系统环境检查 ===")
    print(f"Python版本: {info['python_version']}")
    print(f"PyTorch: {'✓' if info['torch_available'] else '✗'}")
    print(f"Transformers: {'✓' if info['transformers_available'] else '✗'}")
    print(f"CUDA: {'✓' if info['cuda_available'] else '✗'}")
    
    if info['cuda_available']:
        print(f"GPU显存: {info['gpu_memory']:.2f} GB")
    
    print("====================")

def validate_model_paths(base_model_root: str) -> dict:
    """验证模型路径"""
    results = {
        'llm_found': False,
        'emb_found': False,
        'llm_path': None,
        'emb_path': None
    }
    
    llm_candidates = [
        "Qwen-7B-Chat-int4", "qwen-7b-chat-int4",
        "Qwen-7B-Chat", "qwen-7b-chat"
    ]
    
    emb_candidates = [
        "qwen-0.6b-embedding", "qwen-embedding-0.6b",
        "qwen-embedding", "qwen-0.6b-embed"
    ]
    
    for candidate in llm_candidates:
        path = os.path.join(base_model_root, candidate)
        if os.path.exists(path):
            results['llm_found'] = True
            results['llm_path'] = path
            break
    
    for candidate in emb_candidates:
        path = os.path.join(base_model_root, candidate)
        if os.path.exists(path):
            results['emb_found'] = True
            results['emb_path'] = path
            break
    
    return results