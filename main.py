# -*- coding: utf-8 -*-
"""
法律RAG系统 - 主入口
"""

import sys
import os

# 添加项目根目录到路径
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

from core.rag_app import LegalRAGApp
from ui.interface import LegalRAGUI
from core.utils import print_system_info

def main():
    """主函数"""
    print_system_info()
    
    try:
        # 创建应用
        app = LegalRAGApp()
        
        # 创建界面
        ui = LegalRAGUI(app)
        
        # 启动应用
        ui.launch()
        
    except Exception as e:
        print(f"❌ 应用启动失败: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()