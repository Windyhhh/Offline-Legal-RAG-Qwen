# -*- coding: utf-8 -*-
"""
LLM模型管理
"""

import torch
from typing import Tuple, Optional
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

class Qwen7BModel:
    """Qwen-7B-Chat模型管理"""
    
    def __init__(self, model_path: str):
        self.model_path = model_path
        self.tokenizer = None
        self.model = None
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
    
    def load(self) -> Tuple[AutoTokenizer, AutoModelForCausalLM]:
        """加载模型和分词器"""
        if not self.model_path or not torch.cuda.is_available():
            raise ValueError("模型路径不存在或CUDA不可用")
        
        # 加载分词器
        self.tokenizer = AutoTokenizer.from_pretrained(
            self.model_path, 
            trust_remote_code=True, 
            use_fast=False
        )
        
        # 尝试4bit量化加载
        try:
            bnb_config = BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_compute_dtype=torch.bfloat16,
                bnb_4bit_use_double_quant=True,
                bnb_4bit_quant_type='nf4'
            )
            self.model = AutoModelForCausalLM.from_pretrained(
                self.model_path,
                trust_remote_code=True,
                quantization_config=bnb_config,
                device_map='auto'
            )
        except Exception as e:
            print(f"⚠ 4-bit量化加载失败，改为直接加载: {e}")
            self.model = AutoModelForCausalLM.from_pretrained(
                self.model_path,
                trust_remote_code=True,
                device_map='auto'
            )
        
        self.model.eval()
        return self.tokenizer, self.model
    
    def generate(
        self,
        tokenizer: AutoTokenizer,
        model: AutoModelForCausalLM,
        prompt: str,
        max_new_tokens: int = 512,
        temperature: float = 0.2,
        top_p: float = 0.9
    ) -> str:
        """生成回复"""
        try:
            messages = [
                {"role": "system", "content": "你是专业中文法律顾问"},
                {"role": "user", "content": prompt}
            ]
            text = tokenizer.apply_chat_template(
                messages, 
                tokenize=False, 
                add_generation_prompt=True
            )
        except Exception:
            text = prompt
        
        inputs = tokenizer(text, return_tensors='pt').to(model.device)
        
        with torch.no_grad():
            out = model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                temperature=temperature,
                top_p=top_p,
                do_sample=True,
                eos_token_id=tokenizer.eos_token_id
            )
        
        ans = tokenizer.decode(
            out[0][inputs['input_ids'].shape[-1]:], 
            skip_special_tokens=True
        )
        return ans