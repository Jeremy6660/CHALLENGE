# CareMind：面向失能老人照护的多智能体协同个性化决策系统

> **让每一位老人被真正看见** ——基于多智能体协同的照护个性化智能系统

## 一句话描述

用多智能体技术（分诊评估 + 用药安全 + 家属沟通）破局养老院的"医养分离、信息孤岛、沟通缺失"难题，为低线护理人员和家属赋能。

---

## 项目背景

中国失能与半失能老人照护正面临更深层的结构性压力。根据当前项目已整理的原始行业材料，2025 年末全国 60 岁及以上人口已达 3.23 亿，占总人口 23.0%；其中 65 岁及以上人口 2.24 亿，占比 15.9%，失能、半失能老人规模已超过 4500 万。

在这样的背景下，照护一线同时承受多重难题：
- **信息孤岛**：病历、用药、日常状态分散，照护人员难以整合
- **沟通断层**：医疗信息与家属认知存在鸿沟，家属长期"不知情"
- **个性缺失**：现有系统采用打勾式标准化记录，忽视老人的个体差异需求
- **人才短缺与支付压力**：护理员供给紧张、专业训练不足，而多数家庭又难以承担高质量机构照护费用

CareMind 聚焦于**养老院与居家照护场景**，通过 AI Agent 的协同，在**数字层面实现"医养结合"** —— 即便现实中的行政体制尚未打通。

---

## 核心创新

| 维度 | 方案 |
|------|------|
| **分诊评估** | Agent 1 判断老人健康状态、评估风险等级、决定是否触发其他Agent |
| **用药安全** | Agent 2 检测多药并用禁忌、生成个性化预警（老年人平均5+种药，协同毒性风险巨大） |
| **家属沟通** | Agent 3 将冷冰冰的指标转化为情感温暖的故事式报告，缓解家属"黑箱焦虑" |
| **个性化生成** | 根据认知能力、方言、病史、家庭关系图谱生成差异化输出 |

---

## 快速导航

- **系统设计详解**：[docs/system-design.md](docs/system-design.md)
- **参赛版完整修改建议**：[docs/competition-revision-recommendations.md](docs/competition-revision-recommendations.md)
- **参赛版全流程执行方案**：[docs/executable-full-process-plan.md](docs/executable-full-process-plan.md)
- **理论与政策背景**：[docs/background.md](docs/background.md)
- **行业研究与痛点整理**：[docs/industry-research.md](docs/industry-research.md)
- **用药安全知识库来源**：[docs/medication-safety-knowledge-sources.md](docs/medication-safety-knowledge-sources.md)
- **三月执行路线**：[docs/implementation-roadmap.md](docs/implementation-roadmap.md)
- **4人团队分工**：[docs/team/](docs/team/)
- **知识图谱与可视化产物**：[graphify-out/graph.html](graphify-out/graph.html) / [graphify-out/GRAPH_REPORT.md](graphify-out/GRAPH_REPORT.md)
- **项目规则与开发说明**：[AGENTS.md](AGENTS.md) / [CLAUDE.md](CLAUDE.md)

---

## 项目结构

```
CareMind/
├── README.md                    ← 你在这里
├── AGENTS.md                    ← Codex/通用 Agent 项目规则手册
├── CLAUDE.md                    ← 项目规则手册
├── docs/
│   ├── system-design.md         ← 系统架构与三大Agent详细设计
│   ├── competition-revision-recommendations.md ← 参赛版改写建议与差距分析
│   ├── executable-full-process-plan.md ← 从当前进度到 9 月提交的全流程执行手册
│   ├── background.md            ← 理论基础、政策背景、行业痛点
│   ├── industry-research.md     ← 最新行业数据、现实约束与痛点整理
│   ├── implementation-roadmap.md ← 技术栈与执行计划
│   ├── medication-safety-knowledge-sources.md ← Agent 2用药安全知识库来源
│   └── team/                    ← A/B/C/D 四名成员的详细分工文档
├── background_and_knowledge_raw/ ← 原始理论输入（保留用作参考）
├── graphify-out/                ← 知识图谱产物（graph.html / GRAPH_REPORT.md / graph.json）
└── new_help/                    ← 工具使用指南（安装、配置等）
```

> 图谱和图表默认使用中文输出；如需重新生成知识图谱，优先保持 `graphify-out/` 中的标题、图例、节点名和说明为中文。

---

## 项目周期

- **6月**：设计期 —— 需求分析、架构设计、知识库筹建
- **7月**：开发期 —— 单Agent开发、单元测试
- **8月**：集成期 —— 多Agent集成、Orchestrator开发
- **9月**：冲刺期 —— 系统测试、研究报告、答辩材料

---

## 技术栈

| 组件 | 推荐方案 |
|------|---------|
| LLM 调用 | 直接调 API（Claude / GPT-4o / Qwen / DeepSeek 均可） |
| 知识库 | JSON 文件 + 关键词匹配 |
| 用户画像 | JSON 文件存储 |
| 前端 Demo | Gradio / Streamlit |
| 语音与方言 | 后期可选集成，6-7 月不做 |

---

## 下一步

1. 阅读 [docs/system-design.md](docs/system-design.md) 了解系统设计全景
2. 阅读 [docs/industry-research.md](docs/industry-research.md) 了解最新行业数据与项目问题锚点
3. 阅读 [docs/implementation-roadmap.md](docs/implementation-roadmap.md) 了解三个月执行节奏
4. 按成员阅读 [docs/team/](docs/team/) 下的个人分工文档
5. 阅读 [AGENTS.md](AGENTS.md) / [CLAUDE.md](CLAUDE.md) 了解项目规则与开发流程
6. 筹备用药安全数据时，先阅读 [docs/medication-safety-knowledge-sources.md](docs/medication-safety-knowledge-sources.md)

---

**项目状态**：建档与规划阶段 · 4人小组分工已拆分 · 2026-05-30 · 2026年9月前交付
