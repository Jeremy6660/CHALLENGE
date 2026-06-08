# `Beta` 原型状态说明

> 文档用途：用最直接的方式说明 `Beta` 分支当前真实能做什么、不能做什么。  
> 更新日期：2026-06-08

---

## 一句话结论

`Beta` 是 CareMind 的**独立 Streamlit 演示原型**，已经具备多 Agent 协同流程的展示能力，但默认入口仍以模拟数据为主，不应被写成默认实时在线推理系统。

---

## 当前已经具备的内容

- `main.py` 和 `pages/`：Streamlit 展示入口
- `run_demo.py`：命令行演示入口
- `agents/`：医疗、护理、社工、膳食、编排、决策 6 个角色
- `schemas/`：结构化输出契约
- `prompts/`：各角色提示词
- `utils/`：主流程、冲突消解、报告渲染、LLM 客户端
- `requirements.txt`：依赖列表

这些内容说明 `Beta` 已经不是“只有文档”的状态，而是一套可继续迭代的工程原型。

---

## 当前默认运行方式

### 1. Web 入口

`pages/1_单案评估.py` 当前直接读取 `case_data["simulation"]` 做展示。

这意味着：

- 页面效果稳定
- 不依赖实时模型调用就能完整演示
- 默认行为不是实时推理

### 2. CLI 入口

`run_demo.py` 当前使用 `CareMindPipeline.run_with_simulation(...)`。

这意味着：

- 命令行演示也是模拟路径优先
- 报告输出更适合比赛演示和汇报复现

---

## 代码中已经存在但未接入默认入口的能力

`Beta` 代码中已经包含：

- `utils/pipeline.py`
- `utils/llm_client.py`
- `agents/*.py`

因此，更准确的说法是：

> `Beta` 具备继续接入真实 LLM 调用的工程基础，但当前默认入口还没有把这条路径作为标准行为。

---

## 当前最重要的边界

### 可以对外怎么说

- “Streamlit 演示原型”
- “多 Agent 协同流程展示”
- “默认模拟案例路径”
- “代码中保留 live path 扩展能力”

### 不应对外怎么说

- “实时在线多 Agent 推理系统”
- “临床级智能决策系统”
- “已完成自动药学级审核闭环”
- “真实运行结果默认来自在线模型协同”

---

## 当前缺口

- 默认入口与 live path 还未统一
- 用药安全来源和审核依据没有完整显式到默认演示链
- 自动化测试缺失
- 评估指标缺失
- 项目总愿景与原型现实需要靠主文档重新对齐

---

## 推荐配套阅读

- [docs/system-design.md](docs/system-design.md)
- [docs/beta-to-main-capability-map.md](docs/beta-to-main-capability-map.md)
- [docs/medication-safety-knowledge-sources.md](docs/medication-safety-knowledge-sources.md)

---

## 当前判断

如果只用一句话定义 `Beta`：

> 它已经是一个可展示的工程原型，但还不是 CareMind 全部目标的默认实现形态。
