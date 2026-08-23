# 示例配置文件

## 1. 环境变量配置示例

将以下内容保存为 `.env` 文件，放在项目根目录下：

```bash
# 模型根目录
MODEL_ROOT="/path/to/models"

# 跳过LLM加载（用于健康检查）
# NO_LLM="1"

# 干跑模式
# DRY_RUN="1"

# 跳过嵌入模型加载
# NO_EMB="1"
```

## 2. 自定义配置示例

创建 `custom_config.py` 文件，用于覆盖默认配置：

```python
from config.settings import SystemConfig

# 修改文本分块配置
SystemConfig.CHUNK_SIZE = 1500      # 增大分块大小
SystemConfig.CHUNK_OVERLAP = 200    # 增大重叠大小

# 修改检索配置
SystemConfig.DEFAULT_SEARCH_K = 6   # 增加检索数量
SystemConfig.LAMBDA_MULT = 0.6      # 调整MMR参数

# 修改生成配置
SystemConfig.MAX_NEW_TOKENS = 1024  # 增加最大生成tokens
SystemConfig.TEMPERATURE = 0.3      # 调整温度参数

# 修改向量库配置
SystemConfig.COLLECTION_NAME = "custom_legal_kb"  # 自定义集合名称
```

## 3. 命令行启动示例

### 3.1 基本启动

```bash
python main.py
```

### 3.2 自定义模型路径

```bash
# Linux/macOS
MODEL_ROOT="/path/to/models" python main.py

# Windows CMD
set MODEL_ROOT=D:\models && python main.py

# Windows PowerShell
$env:MODEL_ROOT="D:\models" ; python main.py
```

### 3.3 健康检查模式

```bash
# Linux/macOS
DRY_RUN=1 python main.py

# Windows
set DRY_RUN=1 && python main.py
```

### 3.4 跳过LLM加载

```bash
# Linux/macOS
NO_LLM=1 python main.py

# Windows
set NO_LLM=1 && python main.py
```

## 4. Docker配置示例

创建 `Dockerfile`：

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 7860

CMD ["python", "main.py"]
```

创建 `docker-compose.yml`：

```yaml
version: '3.8'

services:
  legal-rag:
    build: .
    ports:
      - "7860:7860"
    volumes:
      - ./legal_docs:/app/legal_docs
      - ./chroma_db:/app/chroma_db
      - /path/to/models:/app/models
    environment:
      - MODEL_ROOT=/app/models
      - PYTHONUNBUFFERED=1
    restart: unless-stopped
```

## 5. 模型配置示例

### 5.1 LLM模型配置

确保LLM模型目录结构如下：

```
Qwen-7B-Chat-int4/
├── config.json
├── generation_config.json
├── model-00001-of-00003.safetensors
├── model-00002-of-00003.safetensors
├── model-00003-of-00003.safetensors
├── model.safetensors.index.json
├── tokenizer.json
└── tokenizer_config.json
```

### 5.2 嵌入模型配置

确保嵌入模型目录结构如下：

```
qwen-0.6b-embedding/
├── config.json
├── model.safetensors
├── README.md
├── sentence_bert_config.json
├── tokenizer.json
└── tokenizer_config.json
```

## 6. 文档目录结构示例

```
legal_docs/
├── 民法典/
│   ├── 总则编.txt
│   ├── 物权编.txt
│   └── 合同编.txt
├── 劳动合同法.txt
└── 知识产权法/
    ├── 著作权法.txt
    └── 专利法.txt
```

## 7. 开发配置示例

### 7.1 PyCharm配置

1. 打开项目
2. 设置Python解释器
3. 配置运行参数：
   - Script path: `main.py`
   - Environment variables: `MODEL_ROOT=/path/to/models`

### 7.2 VSCode配置

创建 `.vscode/launch.json`：

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Run Legal RAG",
            "type": "python",
            "request": "launch",
            "program": "main.py",
            "console": "integratedTerminal",
            "env": {
                "MODEL_ROOT": "/path/to/models"
            }
        },
        {
            "name": "Dry Run",
            "type": "python",
            "request": "launch",
            "program": "main.py",
            "console": "integratedTerminal",
            "env": {
                "DRY_RUN": "1"
            }
        }
    ]
}
```

## 8. 性能优化配置

### 8.1 GPU优化

```python
# 在config/settings.py中添加
USE_4BIT_QUANTIZATION = True
QUANTIZATION_DTYPE = "bfloat16"
USE_DOUBLE_QUANT = True
QUANT_TYPE = "nf4"
```

### 8.2 内存优化

```python
# 在config/settings.py中添加
MAX_BATCH_SIZE = 8
USE_CPU_OFFLOAD = False
USE_FLASH_ATTENTION = True
```

## 9. 安全配置

### 9.1 模型安全

```bash
# 设置模型文件权限
chmod 600 /path/to/models/*

# 限制模型访问
chown -R user:group /path/to/models
```

### 9.2 数据安全

```bash
# 设置向量数据库权限
chmod 600 ./chroma_db/*

# 定期备份向量数据库
cp -r ./chroma_db ./chroma_db_backup_$(date +%Y%m%d)
```

---

**注意**: 配置文件中包含敏感信息，请勿提交到版本控制系统。
