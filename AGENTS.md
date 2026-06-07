# CareMind 协作说明

## 项目性质

CareMind 是一个基于 Python + Streamlit 的养老照护多 Agent 演示原型。它有真实的代码结构和清晰的流程分层，但当前仍应按**演示项目 / 竞赛原型**理解，而不是生产级系统。

## 关键事实

- 主要入口：`main.py`、`run_demo.py`
- 核心链路：4 个评估 Agent -> 1 个编排 Agent -> 1 个决策 Agent
- 案例数据和模拟输出都放在 `data/`
- 结构化输出契约在 `schemas/`
- 提示词在 `prompts/`
- 报告渲染在 `utils/report_renderer.py`

## 修改前必须先知道的现实边界

- 当前 Streamlit 和 CLI 默认都走模拟数据
- `run_demo.py` 使用 `CareMindPipeline.run_with_simulation(...)`
- [pages/1_单案评估.py](/C:/Users/ArcYuYin/Desktop/CareMind/pages/1_单案评估.py:82) 直接读取预置的 `simulation` 内容，而不是调用真实 pipeline
- `utils/llm_client.py` 和 `utils/pipeline.py` 里已经有真实 LLM 路径，但还没有接入当前对外入口

除非你同时改了入口逻辑，否则不要把项目文档写成“实时在线多 Agent 推理系统”。

## 文档分工

- `README.md`：给人看的快速理解与运行说明
- `AGENTS.md`：给后续协作 Agent 和维护者看的约束说明
- `docs/developer-guide.md`：放更长的工程交接内容
- `docs/架构图.md`、`docs/PPT素材汇总.md`：偏展示材料，不是工程事实唯一来源
- `docs/case_*_报告.md`：`run_demo.py` 生成的示例输出

## 改动规则

- 如果修改 Agent 输出结构，同时检查 `schemas/`、`prompts/`、`utils/report_renderer.py`，以及所有直接读取这些字段的 Streamlit 页面
- 如果修改 `data/` 里的案例结构，同时验证 Streamlit 页面和 CLI 演示是否还使用相同 key
- 如果把真实 LLM 执行接入产品入口，必须同步更新 `README.md` 和 `docs/developer-guide.md`
- 除非用户明确要求移除，否则尽量保留“无 API key 也能跑演示”的模拟路径
- 代码注释可能描述的是目标形态；更新文档时优先以当前真实代码行为为准

## 环境规则

- 运行时配置在 `config.py`
- 提供 `ANTHROPIC_API_KEY` 后会关闭模拟模式
- `LLM_MODEL` 是可选项，默认值为 `claude-sonnet-4-6`
- 当前真正实现的 LLM 客户端只调用 Anthropic

## 常用命令

```powershell
pip install -r requirements.txt
streamlit run main.py
python run_demo.py
```

## 当前验证状态

- 在 2026-06-07，这个工作区里直接执行 `python run_demo.py` 会因为缺少 `pydantic` 而失败
- 仓库当前没有自动化测试
