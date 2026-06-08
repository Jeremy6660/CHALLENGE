# CareMind 项目开发规则手册

## 项目定义

**全名**：面向失能老人照护的多智能体协同个性化知识生成与决策系统

**简称**：CareMind

**项目类型**：学术课题 + 技术方案 + 原型验证

**交付物**：
- 系统架构设计
- 核心原型与演示链路
- 执行计划
- 研究报告
- 答辩材料

**核心受众**：
- 养老院照护人员（护工、社工）
- 老人家属
- 医疗与民政决策层

---

## 当前项目现实（2026-06-08）

当前仓库需要按两层来理解：

1. **`main` 分支**：CareMind 的总体项目主线，负责系统设计、知识来源、行业背景、执行路线和参赛叙事。
2. **`Beta` 分支**：CareMind 的独立 Streamlit 演示原型，已经具备 6 角色多 Agent 流程展示能力，但默认入口仍以模拟数据为主。

> 重要约束：在 `Beta` 的默认入口未切换到实时路径之前，所有对外文档都不得将 `Beta` 写成“实时在线多 Agent 推理系统”或“已落地临床级决策系统”。

---

## 项目价值主张

三句话总结这个系统的价值：

1. **为护工赋能**：让受教育程度较低、医学知识储备不足的一线护工，通过 AI 辅助获得更稳的风险识别与照护支持能力
2. **为家属答疑**：从冷冰冰的“血压/排便”转向更可理解、更有温度的照护叙事
3. **为机构降本**：通过知识数字化、风险前置和留痕改进降低运营与沟通成本

---

## 核心概念速查

| 术语 | 定义 | 备注 |
|------|------|------|
| **多智能体** | 多个 AI 角色按职责分工协同工作 | `main` 主线强调三类核心能力，`Beta` 原型当前拆成 6 角色 |
| **个性化生成** | 同一信息针对不同认知能力、方言背景、关系身份生成差异化表达 | 不是“一刀切”的标准答案 |
| **全人照护** | 将老人视为身心社灵的完整体，而不是“病人”或“床号” | 社会学/老年学核心理念 |
| **医养结合** | 打破医疗系统与养老系统的“部门墙”，在数字层面实现协同 | CareMind 的长期价值抓手 |
| **失能评估** | 根据 ADL / IADL 等能力判断自理水平 | 与长护险政策对接 |
| **多药并用** | 老年人同时服用多种药物带来的相互作用与高风险问题 | 可信度与安全边界的核心场景 |

---

## 文档结构说明

```text
CareMind/
├── README.md                      ← 新接手者的一入口
├── AGENTS.md                      ← 你现在看的，规则手册
├── CLAUDE.md                      ← 通用规则镜像
├── docs/
│   ├── system-design.md           ← 总体系统设计 SSOT + Beta 原型映射
│   ├── beta-prototype-status.md   ← Beta 当前真实状态与边界
│   ├── beta-to-main-capability-map.md ← Beta 与主线能力对应关系
│   ├── competition-revision-recommendations.md ← 参赛版修订建议
│   ├── executable-full-process-plan.md ← 参赛版全流程执行方案
│   ├── background.md              ← 理论支撑、政策背景、行业痛点
│   ├── industry-research.md       ← 行业数据、现实约束与痛点整理
│   ├── implementation-roadmap.md  ← 原始月度路线图
│   ├── medication-safety-knowledge-sources.md ← 用药安全知识来源与审核规范
│   └── team/                      ← A/B/C/D 四名成员的详细分工与验收要求
├── background_and_knowledge_raw/  ← 原始资料（只读参考）
├── graphify-out/                  ← 知识图谱产物
└── new_help/                      ← 工具指南（非项目核心）
```

---

## 文档所有权与更新责任

- **README.md**：项目概览与导航，必须保持最新
- **AGENTS.md / CLAUDE.md**：项目规则与协作边界，新增约束立即同步
- **docs/system-design.md**：总体系统设计的单一真实来源，任何架构改动都要同步
- **docs/beta-prototype-status.md**：`Beta` 的真实运行方式、边界、依赖和未完成项
- **docs/beta-to-main-capability-map.md**：`Beta` 6 角色与主线能力的对应关系
- **docs/competition-revision-recommendations.md**：参赛版修订建议，项目方向变化时优先更新
- **docs/executable-full-process-plan.md**：参赛执行总手册，基线变化时立即更新
- **docs/background.md**：理论与政策背景，除非发现过期或误导信息，否则以保守维护为主
- **docs/industry-research.md**：行业现状、人口数据、支付与供需痛点的正式整理入口
- **docs/medication-safety-knowledge-sources.md**：高风险知识来源、字段模板与审核流程；任何新增医学/药学来源优先更新这里
- **docs/team/**：4 人小组的个人分工、阶段任务、验收标准

---

## 当前仓库状态与代码组织

### 当前仓库状态

- `main` 仍然以文档和方案为主
- `Beta` 已经是一个可展示的工程原型
- 当前最需要的是文档诚实度和主线一致性，而不是继续假设“暂无代码”

### 如果后续继续开发主线，推荐目标代码组织

```text
code/
├── agents/
│   ├── triage/
│   ├── medication_safety/
│   └── family_communication/
├── orchestrator/
├── knowledge_base/
├── user_profile/
└── tests/
```

> 注意：这是主线的理想结构，不等同于 `Beta` 当前已经实现的目录。

---

## 命名与代码风格

- 函数名：英文下划线 `snake_case`
- 文件名：英文下划线 `snake_case`
- 注释：中文注释可接受，重点解释“为什么”
- 图表与可视化：默认全部使用中文输出，包括标题、图例、节点名、坐标轴、注释与说明；除非明确要求英文
- 类名：`PascalCase`

---

## 版本控制

- 主分支：`main`
- 演示原型分支：`Beta`
- 开发分支：`dev/<feature-name>`
- 提交信息格式：简明扼要，中英混合可接受

示例：

```text
feat: 完成Agent1分诊评估逻辑与单元测试
fix: 修复多药并用检测中的NSAIDs相互作用漏洞
docs: 更新系统设计文档的Beta映射部分
```

---

## 知识库与数据来源

本项目的高风险知识仍以文档化、可追溯、可审核为原则：

- **中国老年医学临床指南**
- **国家长期护理保险文本**
- **多药并用禁忌数据库**
- **机构照护规范**

> 重要：知识库的准确性直接影响用药安全与风险提醒的可信度。任何新增医学信息都需要审核，且在 `Beta` 未默认接通实时审核链路前，不得夸大其自动审校能力。

---

## 常见坑点与注意事项

### 技术坑

1. **不要把代码里存在的 live path 等同于默认产品入口**
   - `Beta` 当前默认仍以模拟数据为主
   - 对外表述必须以真实默认行为为准

2. **多药并用检测的误报与漏报**
   - 误报会降低信任度
   - 漏报直接关乎生命安全
   - 宁可保守，也不要无依据放宽边界

3. **文档和原型脱节**
   - 文档写“暂无代码”会误导
   - 文档写“实时在线推理”同样会误导
   - 每次架构和入口行为变化都要同步文档

### 伦理坑

1. **不要替代医生做诊断或替代药师做处方建议**
2. **不要把个性化包装成无限定制**
3. **不要在没有知识审核链时夸大自动安全能力**

---

## 深入文档索引

| 需求 | 对应文档 |
|------|---------|
| 理解 CareMind 总体目标与 `Beta` 的位置 | [docs/system-design.md](docs/system-design.md) |
| 判断 `Beta` 当前真实状态 | [docs/beta-prototype-status.md](docs/beta-prototype-status.md) |
| 判断 `Beta` 与主线能力的关系 | [docs/beta-to-main-capability-map.md](docs/beta-to-main-capability-map.md) |
| 参赛版需要如何改写 | [docs/competition-revision-recommendations.md](docs/competition-revision-recommendations.md) |
| 从当前阶段到提交如何推进 | [docs/executable-full-process-plan.md](docs/executable-full-process-plan.md) |
| 理论与政策背景 | [docs/background.md](docs/background.md) |
| 行业数据与现实痛点 | [docs/industry-research.md](docs/industry-research.md) |
| 用药安全知识来源与字段模板 | [docs/medication-safety-knowledge-sources.md](docs/medication-safety-knowledge-sources.md) |

---

## 项目状态与联系

**当前阶段**：`main` 方案主线与 `Beta` 独立原型并存（2026-06-08）

**当前优先事项**：
- 统一文档口径
- 保住知识底座
- 明确 `Beta` 的真实边界
- 再推进 live path、测试与指标

**问题或建议**：
- 系统设计有调整？更新 `docs/system-design.md` 并同步本文件
- `Beta` 的默认入口行为有变化？同步更新 `docs/beta-prototype-status.md`
- 发现过期信息？立即修正，不要留给后来者继续误判

---

*本手册最后更新于 2026-06-08 · CareMind 项目组*

## graphify

本项目已经生成知识图谱，产物位于 `graphify-out/`，包含高连接节点、社区结构与跨文档关系。

当用户输入 `/graphify` 时，先调用 `skill` 工具并传入 `skill: "graphify"`，再做其他动作。

Rules:
- 遇到代码库问题时，如果 `graphify-out/graph.json` 存在，先运行 `graphify query "<问题>"`。查关系用 `graphify path "<A>" "<B>"`，查单个概念用 `graphify explain "<概念>"`。这些命令会返回聚焦后的子图，通常比直接读 `GRAPH_REPORT.md` 或全仓库检索更高效。
- `graphify-out/` 在 hook 或增量更新后处于 dirty 状态是正常现象，不要因此跳过 graphify。只有当任务本身就是排查图谱过期、错误，或用户明确说不要用 graphify 时，才跳过。
- 如果存在 `graphify-out/wiki/index.md`，优先用它做广义导航，而不是直接翻源码。
- 只有在做宏观架构审查，或 `query` / `path` / `explain` 还不够时，才去读 `graphify-out/GRAPH_REPORT.md`。
- 修改代码后运行 `graphify update .` 保持图谱最新；这是 AST-only 更新，不需要额外 API 成本。
