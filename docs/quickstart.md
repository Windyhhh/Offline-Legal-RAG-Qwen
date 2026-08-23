# 快速入门指南

本指南将帮助您快速部署和使用离线智能法律咨询系统。

## 1. 环境要求

- **Python**: 3.8+  
- **操作系统**: Windows 10+, macOS 10.15+, Linux  
- **GPU**: NVIDIA GPU (推荐8GB+显存)  
- **硬盘**: 20GB+可用空间  

## 2. 安装步骤

### 2.1 克隆仓库

```bash
git clone https://github.com/username/legal-rag-system.git
cd legal-rag-system
```

### 2.2 安装依赖

```bash
pip install -r requirements.txt
```

### 2.3 准备模型文件

将模型文件下载并放置在指定目录：

```
# 默认模型目录
E:\PythonProject\model\
├── Qwen-7B-Chat-int4/      # LLM模型
└── qwen-0.6b-embedding/     # 嵌入模型
```

## 3. 配置说明

### 3.1 环境变量

| 变量名 | 说明 | 默认值 |
|--------|------|--------|
| `MODEL_ROOT` | 模型根目录 | `E:\PythonProject\model` |
| `NO_LLM` | 跳过LLM加载 | `False` |
| `DRY_RUN` | 干跑模式 | `False` |
| `NO_EMB` | 跳过嵌入模型 | `False` |

### 3.2 配置文件

主要配置位于 `config/settings.py`：

```python
# 文本分割配置
CHUNK_SIZE = 1000         # 分块大小
CHUNK_OVERLAP = 150       # 重叠大小

# 检索配置
DEFAULT_SEARCH_K = 4      # 检索数量

# 生成配置
MAX_NEW_TOKENS = 512      # 最大生成 tokens
TEMPERATURE = 0.2         # 温度参数
TOP_P = 0.9               # Top-p 参数
```

## 4. 启动系统

### 4.1 基本启动

```bash
python main.py
```

### 4.2 干跑模式

```bash
# 仅测试系统组件，不加载模型
DRY_RUN=1 python main.py
```

### 4.3 自定义模型路径

```bash
# 指定自定义模型路径
MODEL_ROOT="/path/to/models" python main.py
```

## 5. 使用说明

### 5.1 上传法律文档

将法律文本文件（.txt, .md）放入 `legal_docs/` 目录，系统会自动索引。

### 5.2 访问界面

系统启动后，在浏览器中访问：

```
http://localhost:7860
```

### 5.3 示例查询

```
- 什么是民法典中的离婚冷静期？
- 劳动合同解除的条件有哪些？
- 著作权的保护期限是多久？
```

## 6. 常见问题

### 6.1 模型未找到

**问题**: 系统提示"未找到 Qwen-7B-Chat，本地路径无效"

**解决**: 
- 检查模型文件是否正确放置
- 确认 `MODEL_ROOT` 环境变量设置正确
- 检查模型文件夹名称是否匹配

### 6.2 显存不足

**问题**: 系统提示CUDA out of memory

**解决**:
- 使用4bit量化模式
- 减少批处理大小
- 关闭其他占用GPU的程序

### 6.3 文档未索引

**问题**: 系统提示"未发现法律文本(.txt/.md)"

**解决**:
- 确认 `legal_docs/` 目录下有文本文件
- 检查文件格式是否为 .txt 或 .md
- 重启系统

## 7. 高级用法

### 7.1 批量导入文档

将多个文档放入 `legal_docs/` 目录，系统会自动批量索引。

### 7.2 自定义检索策略

修改 `core/retriever.py` 中的检索配置：

```python
self.retriever = self.vectorstore.as_retriever(
    search_type='mmr',  # 或 'similarity'
    search_kwargs={
        "k": self.search_k,
        "fetch_k": max(8, self.search_k * 2),
        "lambda_mult": 0.5
    }
)
```

## 8. 停止系统

在终端中按 `Ctrl+C` 停止系统运行。

## 9. 下一步

- 阅读 [架构设计](architecture.md) 了解系统设计
- 查看 [API文档](api.md) 了解系统接口
- 参考 [开发指南](development.md) 参与开发

---

**提示**: 首次运行时，系统会初始化向量数据库，可能需要几分钟时间。
