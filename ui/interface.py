# -*- coding: utf-8 -*-
"""
用户界面
"""

from typing import List, Optional
from core.rag_app import LegalRAGApp

class LegalRAGUI:
    """法律RAG系统UI"""
    
    def __init__(self, app: LegalRAGApp):
        self.app = app
    
    def create_interface(self):
        """创建Gradio界面"""
        try:
            import gradio as gr
        except ImportError:
            raise ImportError("请安装gradio: pip install gradio")
        
        with gr.Blocks(title="离线智能法律咨询") as interface:
            # 标题和说明
            gr.Markdown(
                "# 离线智能法律咨询系统\n"
                "- 模型: Qwen-7B-Chat (4bit)  |  "
                "嵌入: Qwen-0.6b-embedding |  "
                "向量库: Chroma\n"
                "- 将法律文本放入 ./legal_docs/ 并重启以更新索引"
            )
            
            # 聊天界面
            chat_interface = gr.ChatInterface(
                fn=self._chat_handler,
                retry_btn=None,
                undo_btn=None,
                clear_btn="清空会话",
                textbox=gr.Textbox(
                    placeholder="请输入法律问题…",
                    lines=3
                )
            )
        
        return interface
    
    def _chat_handler(self, message: str, history: List[List[str]]) -> str:
        """聊天处理器"""
        return self.app.chat(message, history)
    
    def launch(self, server_name: str = '0.0.0.0', server_port: int = 7860, share: bool = False):
        """启动界面"""
        interface = self.create_interface()
        interface.launch(
            server_name=server_name,
            server_port=server_port,
            share=share
        )