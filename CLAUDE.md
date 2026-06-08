# CareMind 项目开发规则手册

## 项目定义

**全名**：面向失能老人照护的多智能体协同个性化知识生成与决策系统

**简称**：CareMind

**项目类型**：学术课题 + 技术方案 · 养老智能助理系统

**交付物**：系统架构设计、核心Agent原型、三月执行计划、研究报告、答辩材料

**核心受众**：
- 养老院照护人员（护工、社工）
- 老人家属
- 医疗与民政决策层

---

## 项目价值主张

三句话总结这个系统的价值：

1. **为护工赋能**：让受教育程度较低、医学知识储备不足的一线护工，通过 AI 辅助实现"类医生、类药师、类社工"的多维度照护能力
2. **为家属答疑**：从冷冰冰的"血压/排便"转向温暖的、个性化的照护叙事，缓解家属的"黑箱焦虑"与负罪感
3. **为机构降本**：通过知识数字化减少文书工作、提升效率、降低医疗风险与法律纠纷

---

## 核心概念速查

| 术语 | 定义 | 备注 |
|------|------|------|
| **多智能体** | 三个独立的 AI Agent 各司其职（分诊、用药、沟通），通过 Orchestrator 协同 | 不是一个大模型处理所有任务，而是专职化分工 |
| **个性化生成** | 同一信息针对不同认知能力、方言背景、关系身份的用户，生成差异化表达 | 不是"一刀切"的标准答案 |
| **全人照护** | 将老人视为身心社灵的完整体，而不是"病人"或"床号" | 社会学/老年学核心理念 |
| **医养结合** | 打破医疗系统（卫健委）与养老系统（民政部）的"部门墙"，在数字层面实现协同 | 我们的系统是"数字层医养结合的桥梁" |
| **失能评估** | 根据老人在日常生活活动（ADL）和工具性日常生活活动（IADL）中的自理能力分级 | 与"长期护理保险"政策直接对接 |
| **多药并用** | 老年人同时服用多种慢性病药物，存在协同毒性与相互抵消的风险 | Agent 2 的核心关注点 |

---

## 文档结构说明

### 这个仓库的文档按这样组织：

```
CareMind/
├── README.md                      ← 新接手者的一入口
├── AGENTS.md                      ← Codex / 通用规则镜像
├── CLAUDE.md                      ← 你现在看的，规则手册
├── docs/
│   ├── system-design.md           ← 核心：系统架构、三大Agent、个性化机制、技术栈、执行路线
│   ├── competition-revision-recommendations.md ← 参赛版改写建议、赛题对齐差距与重写方向
│   ├── executable-full-process-plan.md ← 参赛版从当前进度到提交的全流程执行方案
│   ├── background.md              ← 参考：理论支撑、政策背景、行业痛点
│   ├── industry-research.md       ← 参考：最新行业数据、现实约束与痛点整理
│   ├── implementation-roadmap.md  ← 详细：按月的里程碑计划
│   ├── medication-safety-knowledge-sources.md ← Agent 2用药安全知识库来源与录入规范
│   └── team/                      ← A/B/C/D 四名成员的详细分工与验收要求
├── background_and_knowledge_raw/   ← 原始资料（保留用作参考，不参与开发）
├── graphify-out/                  ← 知识图谱产物（graph.html / GRAPH_REPORT.md / graph.json / manifest.json / cost.json）
└── new_help/                      ← 工具指南（VS Code/Git/Claude Code安装等，不属于项目核心）
```

### 文档所有权与更新责任

- **README.md**：项目概览与导航，保持最新
- **CLAUDE.md**：项目规则，新增规则/约束立即同步，不要拖延
- **docs/system-design.md**：系统设计的单一真实来源（SSOT），任何架构改动必须体现在这里
- **docs/competition-revision-recommendations.md**：参赛版改写建议与赛题对齐说明，项目方向转向时优先更新
- **docs/executable-full-process-plan.md**：参赛版执行总手册，时间线、产物和阶段验收变化时同步更新
- **docs/background.md**：理论与政策背景，通常不变，除非发现过期或误导信息
- **docs/industry-research.md**：行业现状、人口数据、支付与供需痛点的正式整理入口，新增行业研究材料优先沉淀到这里
- **docs/medication-safety-knowledge-sources.md**：Agent 2 用药安全知识库来源、字段模板与审核流程，新增医学/药学来源时优先更新这里
- **docs/team/**：4人小组个人分工、阶段任务、验收标准；成员职责变化时同步更新
- **background_and_knowledge_raw/**：只读参考，不主动维护
- **graphify-out/**：知识图谱生成产物目录；`graph.html`、`GRAPH_REPORT.md`、`graph.json` 面向浏览与交接，`manifest.json`、`cost.json` 为生成元数据；重新生成时保持中文输出
- **new_help/**：工具指南，可能需要后期整理或移出

---

## 开发流程与规范

### 代码组织（规划阶段，暂无代码）

一旦进入开发（7月），代码应该按照三大Agent分组织：

```
code/
├── agents/
│   ├── triage/              ← Agent 1：分诊评估
│   ├── medication_safety/   ← Agent 2：用药安全
│   └── family_communication/← Agent 3：家属沟通
├── orchestrator/            ← 中央调度：共享记忆、冲突仲裁
├── knowledge_base/          ← JSON知识库：老年医学指南、政策文本、禁忌数据库
├── user_profile/            ← 用户画像模块：认知评级、方言、病史、关系图谱
└── tests/                   ← 单元测试与集成测试
```

### 命名与代码风格（待详细化）

- 函数名：英文下划线 snake_case（例 `generate_triage_report`）
- 文件名：英文下划线 snake_case
- 注释：中文注释可接受，重点是"为什么"而非"是什么"
- 图表与可视化：默认全部使用中文输出，包括标题、图例、节点名、坐标轴、注释与说明；除非明确要求英文
- 类名：PascalCase

### 版本控制

- 主分支：`main`
- 开发分支：`dev/<feature-name>`（如 `dev/agent1-triage`）
- 提交信息格式：简明扼要，中英混合可接受
  ```
  示例：
  "feat: 完成Agent1分诊评估逻辑与单元测试"
  "fix: 修复多药并用检测中的NSAIDs相互作用漏洞"
  "docs: 更新系统设计文档的Agent2部分"
  ```

### 知识库与数据来源

本阶段采用 JSON 文件 + 关键词匹配的极简知识库方案，知识来源需在6月底前完成筹建：

- **中国老年医学临床指南**（中华医学会）
- **国家长期护理保险文本**（医保部门）
- **多药并用禁忌数据库**（需要自行编译，来源与录入规范见 `docs/medication-safety-knowledge-sources.md`）
- **机构照护规范**（民政部行业标准）

> ⚠️ **重要**：知识库的准确性直接影响Agent 2（用药安全）的可信度，这关乎老人生命安全。任何添加到知识库的医学信息都需要经过审核。

---

## 跨部门与跨项目对接点

### 政策对接

- **长期护理保险（第六险）**：我们的失能评估标准与"长护险"的失能等级分类要对标
- **《银发经济意见》（2024年国务院1号文）**：明确提出"智慧健康养老"，我们的系统是这个方向的技术实现例

### 潜在合作伙伴

- **医疗机构**：提供临床指南、用药禁忌数据
- **社区卫生服务中心**：提供基层照护场景验证
- **民政部门**：长护险政策、养老机构管理标准

---

## 常见坑点与注意事项

### 技术坑

1. **RAG知识库的准确性**
   - 不要直接抓互联网文献，要用经过审核的官方指南
   - 医学禁忌数据容易过时，需要定期审查

2. **多药并用检测的误报与漏报**
   - 误报（假警告）会降低护工信任度
   - 漏报（遗漏真风险）直接关乎生命安全
   - 宁可保守（多报一些），不要冒生命风险

3. **个性化生成的易读性测试**
   - 认知障碍老人能否理解？
   - 一线护工（小学/初中学历）能否操作？
   - 做真人测试，不要只靠模型评估

### 伦理坑

1. **不要替代医生做诊断**
   - Agent 1 的输出是"建议"，不是"诊断"
   - 最终决策权必须在照护人员和医生，AI只是辅助

2. **不要过度承诺个性化**
   - "个性化"不是指"完全定制"，成本会爆炸
   - 是指在几个关键维度上的聪明适配（认知程度、方言、关系身份）

3. **数据隐私与知情同意**
   - 老人与家属的数据涉及隐私，系统必须有明确的隐私政策
   - 任何外部对接（如长护险审核）都需要明确告知老人/家属

---

## 深入文档索引

需要了解具体的系统设计，请阅读：

| 需求 | 对应文档 |
|------|---------|
| 系统架构全景、三大Agent职责 | [docs/system-design.md](docs/system-design.md) §二、§三 |
| 参赛版如何改写、与赛题哪里不贴合 | [docs/competition-revision-recommendations.md](docs/competition-revision-recommendations.md) |
| 从当前阶段到 9 月提交怎么执行 | [docs/executable-full-process-plan.md](docs/executable-full-process-plan.md) |
| 个性化生成机制怎么实现 | [docs/system-design.md](docs/system-design.md) §五 |
| 技术栈与推荐工具 | [docs/system-design.md](docs/system-design.md) §六 |
| 最新老龄化数据、行业痛点与现实约束 | [docs/industry-research.md](docs/industry-research.md) |
| 三个月的月度里程碑 | [docs/system-design.md](docs/system-design.md) §八 |
| 4人小组个人分工与验收要求 | [docs/team/](docs/team/) |
| 理论与政策背景（为什么做这个） | [docs/background.md](docs/background.md) |
| 养老行业的真实痛点 | [docs/industry-research.md](docs/industry-research.md) |
| Agent 2用药安全知识库来源与字段模板 | [docs/medication-safety-knowledge-sources.md](docs/medication-safety-knowledge-sources.md) |

---

## 项目状态与联系

**当前阶段**：建档与规划（2026-05-30）

**下一个里程碑**：
- 6月初：完成需求分析与架构设计最终确认
- 6月底：RAG知识库筹建完成
- 7月初：Agent开发环境搭建

**问题或建议**：
- 系统设计有调整？更新 `docs/system-design.md` 并同步 `CLAUDE.md`
- 发现过期信息？立即修正，不要留着误导后来者
- 文档不够清晰？补充说明，记住新接手者可能不熟悉养老行业

---

*本手册最后更新于 2026-05-30 · CareMind 项目组*
