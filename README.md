# CareMind

> 面向失能老人照护的多智能体协同个性化知识生成与决策系统

## 当前口径

截至 2026 年 6 月 8 日，CareMind 需要按两层来理解：

1. **CareMind 总体项目**  
   这是 `main` 分支承载的研究与方案主线，关注失能老人照护中的分诊评估、用药安全、家属沟通、知识可信度和项目交付路径。

2. **`Beta` 分支独立演示原型**  
   这是新成员重构出的 Streamlit 演示系统，已经具备可运行的目录结构和多 Agent 流程展示能力，但默认入口仍以模拟数据演示为主，不能直接等同于 CareMind 的完整项目落地形态。

最稳妥的结论是：

> `Beta` 已经是一个能展示流程的原型，但还不能单独代表 CareMind 的完整项目叙事。

---

## 项目愿景

CareMind 试图解决失能老人照护中的三类核心问题：

- **风险识别难**：老人病情变化、多药并用、跌倒与认知问题常常被一线照护者分散处理。
- **知识门槛高**：护工、社工、家庭照护者并不天然具备医学和药学判断能力。
- **沟通留痕弱**：家属难以理解真实照护状态，机构也缺少兼顾温度与责任边界的记录方式。

因此，`main` 分支中的 CareMind 仍然是一个以“失能照护 + 用药安全 + 个性化沟通”为中心的总体设计，而不是单纯的页面演示项目。

---

## `Beta` 分支评估结论

`Beta` 的进展主要体现在工程原型层面：

- 已形成 `agents/`、`schemas/`、`prompts/`、`utils/`、`pages/`、`requirements.txt` 等结构。
- 已提供 6 个核心角色：医疗、护理、社工、膳食、编排、决策。
- 已提供 Streamlit 页面和 `run_demo.py`，便于竞赛演示和汇报。

但 `Beta` 当前也有清晰边界：

- 默认入口仍是**模拟演示**，不是默认实时在线推理。
- 原有高层文档、理论背景、知识来源和执行路线在 `Beta` 中被明显削弱。
- 原本更有辨识度的“失能照护 + 用药安全 + 家属沟通”主线，被重心更平均的“多专业协同评估演示”替代了一部分。

详细说明见：

- [docs/beta-prototype-status.md](docs/beta-prototype-status.md)
- [docs/beta-to-main-capability-map.md](docs/beta-to-main-capability-map.md)

---

## 快速导航

- [docs/system-design.md](docs/system-design.md)：CareMind 总体架构，以及 `Beta` 原型与主线能力的映射
- [docs/beta-prototype-status.md](docs/beta-prototype-status.md)：`Beta` 的真实运行方式、边界、依赖与未完成项
- [docs/beta-to-main-capability-map.md](docs/beta-to-main-capability-map.md)：`Beta` 6 Agent 与 `main` 主线目标的对应关系
- [docs/competition-revision-recommendations.md](docs/competition-revision-recommendations.md)：结合 `Beta` 现状后的参赛版修订建议
- [docs/executable-full-process-plan.md](docs/executable-full-process-plan.md)：以“已有 `Beta` 演示原型”为基线的执行总手册
- [docs/background.md](docs/background.md)：理论与政策背景
- [docs/industry-research.md](docs/industry-research.md)：行业数据、痛点和现实约束
- [docs/medication-safety-knowledge-sources.md](docs/medication-safety-knowledge-sources.md)：用药安全知识来源与审核规范
- [AGENTS.md](AGENTS.md) / [CLAUDE.md](CLAUDE.md)：项目规则与协作文档

---

## 仓库结构

当前 `main` 分支仍以文档和方案为主：

```text
CareMind/
├── README.md
├── AGENTS.md
├── CLAUDE.md
├── docs/
│   ├── system-design.md
│   ├── beta-prototype-status.md
│   ├── beta-to-main-capability-map.md
│   ├── competition-revision-recommendations.md
│   ├── executable-full-process-plan.md
│   ├── background.md
│   ├── industry-research.md
│   ├── implementation-roadmap.md
│   ├── medication-safety-knowledge-sources.md
│   └── team/
├── background_and_knowledge_raw/
├── graphify-out/
└── new_help/
```

而 `Beta` 分支对应的是一套独立原型，核心目录大致为：

```text
Beta/
├── main.py
├── run_demo.py
├── config.py
├── agents/
├── data/
├── pages/
├── prompts/
├── schemas/
├── utils/
└── docs/
```

---

## 关于 `Beta` 的诚实表述

在 `Beta` 默认入口未改造前，对外描述必须遵守以下边界：

- 可以写“**Streamlit 演示原型**”
- 可以写“**具备多 Agent 流程展示能力**”
- 可以写“**代码中存在 live path，但未接入默认入口**”
- 不应写“**实时在线多 Agent 推理系统**”
- 不应写“**已落地临床级决策系统**”
- 不应写“**已完成自动药学级审核闭环**”

---

## 推荐阅读顺序

1. 先读 [docs/system-design.md](docs/system-design.md)，理解 CareMind 总体目标和 `Beta` 的位置。
2. 再读 [docs/beta-prototype-status.md](docs/beta-prototype-status.md)，确认 `Beta` 当前到底能做什么、不能做什么。
3. 然后读 [docs/beta-to-main-capability-map.md](docs/beta-to-main-capability-map.md)，避免把 `Beta` 当成原始项目目标的完全替代。
4. 如果要做参赛材料，继续读 [docs/competition-revision-recommendations.md](docs/competition-revision-recommendations.md) 和 [docs/executable-full-process-plan.md](docs/executable-full-process-plan.md)。

---

## 当前状态

**项目状态**：`main` 方案主线与 `Beta` 独立原型并存  
**当前日期基线**：2026 年 6 月 8 日  
**当前判断**：`Beta` 在工程原型上前进明显，但在项目定位、知识可信性、文档完整性上相对 `main` 有明显退步
