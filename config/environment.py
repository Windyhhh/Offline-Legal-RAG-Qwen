# -*- coding: utf-8 -*-
"""
环境配置
"""

import os
import warnings
import types

def setup_environment():
    """设置环境变量"""
    # 离线模式配置
    os.environ['TRANSFORMERS_OFFLINE'] = '1'
    os.environ['HF_HUB_OFFLINE'] = '1'
    os.environ['TOKENIZERS_PARALLELISM'] = 'false'
    
    # 警告过滤
    warnings.filterwarnings("ignore")
    
    # 模块兼容性
    sys_modules = os.sys.modules
    if 'transformers_stream_generator' not in sys_modules:
        sys_modules['transformers_stream_generator'] = types.ModuleType('transformers_stream_generator')
        sys_modules['transformers_stream_generator'].__version__ = "0.0.0"

def should_load_llm() -> bool:
    """判断是否应该加载LLM"""
    env_no_llm = os.environ.get('NO_LLM', '').lower() in ('1', 'true', 'yes')
    env_dry = os.environ.get('DRY_RUN', '').lower() in ('1', 'true', 'yes')
    return not (env_no_llm or env_dry)

def should_use_tiny_embedding() -> bool:
    """判断是否使用极简嵌入"""
    env_no_llm = os.environ.get('NO_LLM', '').lower() in ('1', 'true', 'yes')
    env_dry = os.environ.get('DRY_RUN', '').lower() in ('1', 'true', 'yes')
    env_no_emb = os.environ.get('NO_EMB', '').lower() in ('1', 'true', 'yes')
    return env_no_llm or env_dry or env_no_emb