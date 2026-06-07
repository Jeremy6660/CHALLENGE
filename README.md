# CareMind

CareMind 是一个面向养老照护场景的多 Agent 演示原型，使用 Streamlit 搭建交互界面，围绕 3 个示例老人案例展示“多专业协同评估 -> 统一照护计划 -> 最终审核”的流程。

当前代码中的核心角色一共 6 个：

- 4 个评估 Agent：医疗、护理、社工、膳食
- 1 个编排 Agent：合并建议、识别并消解跨领域冲突
- 1 个决策 Agent：对统一照护计划做合理性、安全性、可行性审核

这个仓库目前更偏向竞赛演示 / 汇报展示原型，而不是已经接通真实线上推理的生产系统。

## 项目定位

CareMind 主要解决的是“老年照护需要多专业协同，但信息分散、判断割裂”的展示型问题。项目尝试把一位老人的资料拆给不同专业 Agent 分工评估，再汇总成一份更完整的综合干预方案。

它强调的不是单一疾病判断，而是多维照护协同：

- 医疗维度：慢病、急性风险、用药安全
- 护理维度：ADL、跌倒风险、压疮风险、照护等级
- 社工维度：心理、认知、社会参与、家庭支持
- 膳食维度：营养、吞咽、安全饮食方案

## 仓库结构

- `main.py`：Streamlit 首页
- `pages/`：3 个 Streamlit 页面，分别展示单案评估、案例对比、架构展示
- `run_demo.py`：命令行演示入口，会把报告写入 `docs/`
- `agents/`：各 Agent 的封装与基类
- `utils/`：主流程、LLM 客户端、冲突消解、报告渲染
- `data/`：3 个示例案例，以及每个案例的模拟输出
- `prompts/`：各 Agent 的提示词
- `schemas/`：Pydantic 结构化输出定义
- `docs/`：演示材料、示例报告、工程说明

## 快速开始

建议先创建虚拟环境，再安装依赖。

Windows PowerShell 示例：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

启动 Web 界面，推荐直接使用虚拟环境里的 Python：

```powershell
.\.venv\Scripts\python -m streamlit run main.py
```

或者使用一键脚本：

```powershell
.\run_app.ps1
```

命令行演示：

```powershell
.\.venv\Scripts\python run_demo.py
```

`run_demo.py` 会生成以下 Markdown 报告：

- `docs/case_1_报告.md`
- `docs/case_2_报告.md`
- `docs/case_3_报告.md`

## 当前运行模式

### 默认演示模式

当前对外入口默认都是模拟数据优先：

- `run_demo.py` 调用 `CareMindPipeline.run_with_simulation(...)`
- [pages/1_单案评估.py](/C:/Users/ArcYuYin/Desktop/CareMind/pages/1_单案评估.py:82) 直接读取 `case_data["simulation"]`

这意味着：

- 没有 `ANTHROPIC_API_KEY` 也能完整演示
- 页面中的进度和结果是按预置数据展示的
- 演示输出稳定，适合比赛或汇报场景

### 真实 LLM 路径

代码里已经有真实 LLM 调用路径，但还没有接到当前 UI 和 CLI 的默认入口：

- [utils/llm_client.py](/C:/Users/ArcYuYin/Desktop/CareMind/utils/llm_client.py:56)：封装 Anthropic SDK 调用
- [utils/pipeline.py](/C:/Users/ArcYuYin/Desktop/CareMind/utils/pipeline.py:57)：提供 `run(...)` 和 `run_sync(...)`

所以如果只看现在的产品入口，不应该把它描述成“实时在线多 Agent 推理系统”。

## 配置说明

项目配置见 [config.py](/C:/Users/ArcYuYin/Desktop/CareMind/config.py:1)。

主要环境变量：

- `ANTHROPIC_API_KEY`：提供后可关闭模拟模式，启用真实 LLM 调用能力
- `LLM_MODEL`：可选，默认是 `claude-sonnet-4-6`

模拟模式开关如下：

```python
SIMULATION_MODE = not LLM_API_KEY
```

说明：

- 代码注释里提到过别的模型提供方
- 但当前真正实现的客户端只接了 Anthropic

## 主流程概览

1. 从 `data/` 中组织老人完整档案
2. 并行运行 4 个评估 Agent
3. 由编排 Agent 合并多维建议
4. 先用规则引擎处理确定性冲突
5. 由决策 Agent 做最终审核
6. 输出 Markdown 报告或 Streamlit 展示内容

更偏工程交接视角的说明见 [docs/developer-guide.md](/C:/Users/ArcYuYin/Desktop/CareMind/docs/developer-guide.md:1)。

## 文档索引

- [docs/developer-guide.md](/C:/Users/ArcYuYin/Desktop/CareMind/docs/developer-guide.md:1)：工程交接、扩展点、代码现实边界
- [docs/架构图.md](/C:/Users/ArcYuYin/Desktop/CareMind/docs/架构图.md:1)：用于展示的架构材料
- [docs/PPT素材汇总.md](/C:/Users/ArcYuYin/Desktop/CareMind/docs/PPT素材汇总.md:1)：PPT 文案与演讲素材
- `docs/case_*_报告.md`：示例输出报告

## 当前限制

- 运行前需要先安装依赖。
- 如果你直接输入 `streamlit run main.py`，系统可能会提示找不到 `streamlit`，因为它安装在项目本地 `.venv` 里，而不是全局环境里。
- Streamlit 页面目前是演示导向，还没有接成真实在线推理入口。
- 仓库里暂时没有自动化测试。
