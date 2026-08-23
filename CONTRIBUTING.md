# 贡献指南

感谢您考虑为离线智能法律咨询系统做出贡献！本指南将帮助您了解如何参与我们的项目。

## 📋 贡献方式

您可以通过以下方式贡献：

1. **报告Bug**: 在GitHub Issues中提交详细的bug报告
2. **提出新功能**: 分享您的想法和建议
3. **修复Bug**: 提交Pull Request修复已知问题
4. **改进文档**: 完善项目文档
5. **添加测试**: 提高代码覆盖率
6. **优化性能**: 改进系统效率

## 🚀 开发流程

### 1. Fork仓库

首先，Fork本仓库到您自己的GitHub账号下：

```bash
git clone https://github.com/your-username/legal-rag-system.git
cd legal-rag-system
```

### 2. 创建分支

为您的贡献创建一个新分支：

```bash
git checkout -b feature/your-feature-name
```

分支命名规范：
- 功能开发: `feature/feature-name`
- Bug修复: `fix/bug-description`
- 文档更新: `docs/documentation-update`
- 重构: `refactor/code-refactoring`

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 开发和测试

- 编写代码，确保符合项目的代码风格
- 添加必要的测试
- 运行测试确保功能正常
- 检查代码质量

### 5. 提交更改

提交您的更改，使用清晰的提交信息：

```bash
git add .
git commit -m "feat: 添加新功能描述"
git push origin feature/your-feature-name
```

## 📝 提交规范

我们使用[Conventional Commits](https://www.conventionalcommits.org/)规范：

- **feat**: 新功能
- **fix**: Bug修复
- **docs**: 文档更新
- **style**: 代码风格调整
- **refactor**: 代码重构
- **perf**: 性能优化
- **test**: 添加或修改测试
- **build**: 构建系统或依赖变更
- **ci**: CI配置文件或脚本变更
- **chore**: 其他不影响代码运行的变更
- **revert**: 回滚之前的提交

## 📦 代码风格

- 遵循[PEP 8](https://peps.python.org/pep-0008/)规范
- 使用[Black](https://black.readthedocs.io/en/stable/)进行代码格式化
- 使用[Flake8](https://flake8.pycqa.org/en/latest/)检查代码质量
- 使用[Mypy](https://mypy.readthedocs.io/en/stable/)进行类型检查

## 🧪 测试

我们使用以下测试框架：

- **pytest**: 主要测试框架
- **pytest-cov**: 代码覆盖率
- **tox**: 多环境测试

运行测试：

```bash
# 运行所有测试
pytest

# 运行特定测试
pytest tests/test_module.py

# 查看覆盖率
pytest --cov=.
```

## 📄 文档

- 更新README.md以反映您的更改
- 为新功能添加详细文档
- 保持文档的清晰和准确

## 🔍 代码审查

所有Pull Request都将经过代码审查，包括：

- 代码质量检查
- 功能正确性验证
- 测试覆盖率
- 文档完整性

## 📌 报告问题

在提交Issue之前，请检查：

1. 是否已有相同的Issue
2. 是否已在最新版本中修复
3. 提供详细的错误信息
4. 提供复现步骤
5. 提供系统环境信息

## 🛠️ 开发环境

### 推荐工具

- **IDE**: PyCharm, VSCode
- **版本控制**: Git
- **代码格式化**: Black
- **类型检查**: Mypy
- **测试框架**: pytest

### 环境变量

- `MODEL_ROOT`: 模型文件根目录
- `NO_LLM`: 跳过LLM加载，用于测试
- `DRY_RUN`: 干跑模式
- `NO_EMB`: 跳过嵌入模型加载

## 📞 联系方式

如有任何问题，请通过以下方式联系：

- GitHub Issues: [项目Issues页面](https://github.com/username/repo/issues)
- 邮箱: your-email@example.com

## 📜 许可证

通过提交您的贡献，您同意您的工作将根据MIT许可证发布。

感谢您的贡献！
