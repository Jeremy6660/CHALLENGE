# 详细执行计划：CareMind 三月行动计划

> 团队 4 人 · vibe coding 模式 · 极简技术栈 · 目标：2026 年 9 月答辩

---

## 团队分工

| 成员 | 负责 Agent | 核心产出 | 需要的技能 |
|------|-----------|---------|-----------|
| **A** | Agent 1 分诊评估 | Prompt 设计 + 10 个测试案例 + Python 函数 | 能读代码、能设计 Prompt |
| **B** | Agent 2 用药安全 | 50 条药物禁忌 JSON + Python 函数 | 细心整理数据（最重要）、能读代码 |
| **C** | Agent 3 家属沟通 | 5 组报告模板 + 老人画像 JSON + Python 函数 | 文字表达好、能设计 Prompt |
| **D** | 集成 + 前端 + 答辩 | Gradio 界面 + 系统串联 + 报告 + PPT | 能读代码、能做 PPT |

成员个人详细任务、阶段要求和验收标准见 `docs/team/`：

- A：[member-a-triage.md](team/member-a-triage.md)
- B：[member-b-medication-safety.md](team/member-b-medication-safety.md)
- C：[member-c-family-communication.md](team/member-c-family-communication.md)
- D：[member-d-integration-delivery.md](team/member-d-integration-delivery.md)

---

## 技术栈（降级到最简）

| 做什么 | 用什么 | 为什么用这个 |
|--------|--------|------------|
| 调大模型 | 直接调 API（HTTP request） | 不需要 LangGraph/AutoGen |
| 存数据 | JSON 文件 | 不需要 MongoDB |
| 查知识 | 关键词匹配 | 不需要向量数据库 |
| 做界面 | Gradio | 一个 `pip install gradio` + 20 行代码出 Web UI |
| 写代码 | Claude Code | 你们描述需求，AI 生成代码 |

---

## 6 月：准备期（数据 + Prompt + 环境）

### 第 1 周（6/1 – 6/7）：环境搭建 + 跑通第一个 API 调用

**目标**：每个人都能在自己的电脑上跑通一次 LLM API 调用

| 日期 | 任务 | 负责人 | 产出 |
|------|------|--------|------|
| 6/1-6/2 | 安装 Python 3.9+、pip、VS Code | 全员 | 开发环境就绪 |
| 6/3 | `pip install openai gradio`（两个依赖就够了） | 全员 | 依赖装好 |
| 6/4 | 申请 LLM API key（Claude 或 DeepSeek 或 Qwen） | D 统一申请，全员共用 | API key 到手 |
| 6/5 | 写一个最简单的 Python 脚本：发一条消息给 LLM，打印回复 | 全员各自写（用 Claude Code 辅助） | 每个人都能跑通 |
| 6/6-6/7 | 把跑通的脚本改成"输入用药清单 → LLM 判断有没有冲突"的原型 | 全员练手 | 理解 Prompt 是怎么工作的 |

**第 1 周验收标准**：每个人终端里 `python test.py` 能正常调通 LLM。

---

### 第 2 周（6/8 – 6/14）：A/B/C 各自准备数据（本周最忙）

**目标**：三份数据初稿完成

#### A 的任务：准备 10 个老人症状场景

写一个 JSON 文件 `test_cases_agent1.json`，每个案例包含：

```json
{
  "id": 1,
  "name": "张奶奶",
  "age": 77,
  "cognitive_level": "正常",
  "symptoms": "2026-06-08 早上起来说头晕，走路有点飘，早餐吃了半碗粥就说不想吃了",
  "history": "高血压 10 年，平时血压控制在 140/85 左右",
  "expected_risk": "黄色",
  "expected_action": "建议测血压，观察 2 小时，如持续头晕联系医生"
}
```

覆盖场景：绿色 3 个、黄色 4 个、红色 3 个。三种认知水平各至少 2 个。

#### B 的任务：整理 50 条药物禁忌记录（最重要，最花时间）

写一个 JSON 文件 `medication_conflicts.json`，每条记录：

```json
{
  "drug_a": "阿司匹林",
  "drug_b": "布洛芬",
  "risk_level": "高",
  "effect": "增加消化道出血风险，两者均抑制 COX-1",
  "evidence_level": "B",
  "suggestion": "以对乙酰氨基酚替代布洛芬止痛",
  "source": "中国 Beers 标准"
}
```

**数据来源**：优先参考 `docs/medication-safety-knowledge-sources.md` 中整理的 PIM-China、AGS Beers、STOPP/START、WHO、DailyMed、RxNorm、DDInter、ISMP 等来源，手工摘录并保留来源链接。

高频药物清单（优先整理这些相关的组合）：
- 阿司匹林、华法林、氯吡格雷（抗凝血类）
- 布洛芬、双氯芬酸、塞来昔布（NSAIDs）
- 硝苯地平、氨氯地平、卡托普利（降压药）
- 二甲双胍、格列齐特、胰岛素（降糖药）
- 奥美拉唑、西咪替丁（胃药）
- 地高辛、胺碘酮（心脏类）

> **B 的这份数据直接决定 Agent 2 能不能用，是整个项目最重要的交付物。宁可少（50 条），不能错。**

#### C 的任务：准备 5 组报告对比 + 3 个老人画像

**5 组对照报告**（每组包含"传统版"和"CareMind 版"）：

```
【传统版】
张奶奶 2026.6.8：体温36.5℃，血压142/88，排便1次，进食正常。

【CareMind 温暖版】
张奶奶这周精神不错。周二下午她主动拉着护工小王聊天，
说起年轻时在纺织厂的事，还哼了几句那时的歌。
这周血压稍微有点偏高（142/88），我们已经记录并持续观察。
她提到想吃家里做的红烧肉——如果方便探视时可以带一份。
```

覆盖场景：常规周报、有异常需关注、康复进展、节日/生日、家属久未探视。

**3 个老人画像 JSON**：

```json
{
  "id": "elder_001",
  "name": "张奶奶",
  "age": 77,
  "cognitive_level": "正常",
  "dialect": "普通话",
  "family_contacts": [
    {"relation": "儿子", "name": "王先生", "prefer_weekly_report": true}
  ],
  "conditions": ["高血压", "骨关节炎"],
  "medications": ["氨氯地平 5mg qd", "阿司匹林 100mg qd"],
  "allergies": ["青霉素"],
  "personality": "开朗健谈，喜欢回忆年轻时的事，怕孤独",
  "hobbies": ["唱歌", "散步", "红烧肉"]
}
```

3 个画像要覆盖：认知正常（张奶奶）、轻度认知障碍（李爷爷）、中重度（王奶奶）。

#### D 的任务：搭项目骨架 + 开始写报告

- 创建 `code/` 目录结构
- 创建 `agents/triage/`、`agents/medication_safety/`、`agents/family_communication/`、`orchestrator/`
- 写一个 `main.py` 骨架（先什么都不做，只打印 "CareMind v0.1"）
- 研究报告背景部分写初稿（2000 字）

---

### 第 3 周（6/15 – 6/21）：每个人把自己的 Agent Prompt 写出来

**目标**：每个人都有一个"能用的 Prompt 模板"，不写代码，只写 Prompt。

#### A：Agent 1 分诊评估 Prompt

在 Claude Code 里反复调试，直到满足：

- 输入症状描述 + 历史 → 输出风险等级（绿/黄/红）+ 处置建议 + 是否触发其他 Agent
- 对 10 个测试案例跑一遍，看准确率
- 认知正常用开放式对话，轻度用简化语言，重度转护工代理

#### B：Agent 2 用药安全 Prompt

在 Claude Code 里反复调试，直到满足：

- 输入用药列表 → 与 `medication_conflicts.json` 对比 → 输出预警
- 对 50 条禁忌数据做覆盖测试
- 宁可误报（假正），不能漏报（假负）

#### C：Agent 3 家属沟通 Prompt

在 Claude Code 里反复调试，直到满足：

- 输入健康数据 + 老人画像 → 输出温暖周报
- 同一组数据生成三个版本：给老人的、给护工的、给家属的
- 对照 5 组传统版 vs 温暖版，看是否达到预期效果

#### D：继续写报告 + 准备 Gradio 骨架

- 研究报告相关工作总结部分初稿
- 画系统架构图（用 draw.io 或 Excalidraw）
- 搭 `app.py` 骨架（Gradio 最简界面）

---

### 第 4 周（6/22 – 6/30）：缓冲周

- 数据没整理完的这周补完
- Prompt 没调好的继续调
- A/B/C 互相测试对方的 Prompt（换人测试，发现盲区）
- 确认 7 月开发可以启动

**6 月底验收标准**：
- [ ] 每人能跑通 LLM API 调用
- [ ] A：10 个测试案例 JSON + Agent 1 Prompt 初版（准确率 > 70%）
- [ ] B：50 条药物禁忌 JSON + Agent 2 Prompt 初版
- [ ] C：5 组报告对比 + 3 个老人画像 JSON + Agent 3 Prompt 初版
- [ ] D：项目代码骨架 + Gradio 界面骨架 + 报告背景部分初稿

---

## 7 月：开发期（把 Prompt 变成能跑的代码）

### 第 5 周（7/1 – 7/7）：Agent 1 代码开发

**A 负责，D 协助。**

在 Claude Code 中说：

> "我有一个 Agent 1 分诊评估的 Prompt，帮我把它包成一个 Python 函数 `triage_assessment(symptoms, history, cognitive_level) -> dict`，输入是症状描述和历史，输出是风险等级、处置建议、是否触发其他 Agent。"

产出：
- `agents/triage/agent.py` — 核心函数
- `agents/triage/prompt.py` — Prompt 模板
- `agents/triage/test_cases.json` — 10 个测试案例
- 跑通 10 个案例，记录准确率

---

### 第 6 周（7/8 – 7/14）：Agent 2 代码开发

**B 负责，D 协助。**

在 Claude Code 中说：

> "我有一个药物禁忌 JSON 文件，帮我写一个 Python 函数 `check_medication_safety(medications_list, patient_info) -> dict`，先跟禁忌库做关键词匹配，再把匹配结果发给 LLM 生成预警报告。"

产出：
- `agents/medication_safety/agent.py`
- `agents/medication_safety/conflicts.json` — 50 条禁忌
- 跑通 20 组测试药物组合

---

### 第 7 周（7/15 – 7/21）：Agent 3 代码开发

**C 负责，D 协助。**

在 Claude Code 中说：

> "我有一个家属沟通的 Prompt 和老人画像 JSON，帮我写一个 Python 函数 `generate_family_report(elder_id, weekly_data) -> dict`，根据老人画像和本周健康数据，生成三个版本（老人/护工/家属）的照护报告。"

产出：
- `agents/family_communication/agent.py`
- `agents/family_communication/elder_profiles.json` — 3 个画像
- `agents/family_communication/report_templates.py` — 5 种报告模板

---

### 第 8 周（7/22 – 7/31）：缓冲 + 内部测试

- 三个 Agent 互相联调（A 的输出能不能给 B 用？B 的预警能不能给 C 用来写报告？）
- 修复发现的问题
- D 完善 Gradio 界面：三个 tab 分别对应三个 Agent

**7 月底验收标准**：
- [ ] 三个 Agent 的 Python 函数都能独立运行
- [ ] Agent 1 准确率 > 80%
- [ ] Agent 2 漏报率 = 0%
- [ ] Agent 3 生成报告人类可读，比传统版明显好
- [ ] Gradio 界面可演示

---

## 8 月：集成期（串起来 + Demo）

### 第 9 周（8/1 – 8/7）：Orchestrator 开发

**D 负责。**

写一个 `orchestrator.py`，逻辑非常简单：

```python
def run_caremind(elder_id, input_data):
    # 1. 读老人画像
    # 2. 调 Agent 1 → 得到风险等级
    # 3. 如果风险等级 ≥ 黄色 或 有用药变更 → 调 Agent 2
    # 4. 调 Agent 3 → 生成三方报告
    # 5. 返回完整结果
    return full_result
```

**不需要复杂的冲突仲裁**，先跑通再说。

---

### 第 10 周（8/8 – 8/14）：端到端联调

- 准备 5 个完整的老人档案（包含画像 + 本周数据 + 用药清单）
- 从"护工输入症状"到"生成家属报告"全流程跑通
- 记录每个环节的耗时、准确率、问题

---

### 第 11 周（8/15 – 8/21）：Gradio Demo 完善

- 界面做成三个步骤：①输入症状 → ②显示分诊结果和用药预警 → ③生成家属报告
- 找 2-3 个外部人试用（可以是同学），收集反馈
- 根据反馈修改

---

### 第 12 周（8/22 – 8/31）：录制演示视频

- 选一个最典型的使用场景（如"张奶奶头晕 + 用药冲突"）
- 录屏 5-8 分钟，展示完整流程
- D 负责剪辑 + 配音

**8 月底验收标准**：
- [ ] 5 个完整案例端到端跑通
- [ ] Gradio Demo 可演示
- [ ] 演示视频完成

---

## 9 月：冲刺期（测试 + 报告 + 答辩）

### 第 13 周（9/1 – 9/7）：系统测试

- A/B/C 每人用 5 个案例完整跑一遍，记录所有问题
- D 汇总问题，修 bug
- 准备最终版测试报告

---

### 第 14 周（9/8 – 9/14）：研究报告定稿

按此大纲分工写：

| 章节 | 负责人 | 字数 |
|------|--------|------|
| 摘要与背景 | D | 1500 |
| 相关工作（已有方案对标） | A | 1500 |
| 系统设计（架构 + 三大 Agent） | D | 3000 |
| 个性化生成机制 | C | 1500 |
| 实验评估（测试结果 + 用户反馈） | A/B/C 各 500 | 1500 |
| 结论与展望 | D | 1000 |
| 附录（代码片段 + 案例） | D 汇总 | - |

---

### 第 15 周（9/15 – 9/21）：答辩 PPT + 彩排

**PPT 结构（10 页）**：

| 页码 | 内容 | 负责人 |
|------|------|--------|
| 1 | 标题页 | D |
| 2 | 问题与背景（4000 万失能老人 + 三大痛点） | D |
| 3 | 系统架构图（一张大图） | D |
| 4 | Agent 1 分诊评估 — 怎么工作 | A |
| 5 | Agent 2 用药安全 — 为什么是救命功能 | B |
| 6 | Agent 3 家属沟通 — 冰冷版 vs 温暖版对比 | C |
| 7 | 个性化生成机制（三个维度的适配） | C |
| 8 | 测试结果与数据 | A/B |
| 9 | 应用前景与社会价值 | D |
| 10 | 致谢 | D |

彩排至少 2 次：
- 第一次：内部互评，挑问题
- 第二次：限时模拟（5-7 分钟），确保不超时

---

### 第 16 周（9/22 – 9/30）：最终修订 + 答辩

- 根据彩排反馈修改 PPT 和报告
- 打印报告、准备 U 盘备份
- 答辩

---

## 每周固定节奏

| 时间 | 事项 |
|------|------|
| 每周一 10:00 | 15 分钟站会：每人说"上一周期完成了什么、本周期要做什么、有没有卡住" |
| 每周五 17:00 | 把本周产出推到 Git，commit message 写清楚 |
| 每月最后一天 | 对照月底验收标准逐项打勾 |

---

## 关键风险

| 风险 | 谁负责 | 怎么防 |
|------|--------|--------|
| B 的药物禁忌数据不准确 | B | 每条标注来源，6 月底找医学院同学帮审 |
| LLM API 太贵 | D | 优先用 DeepSeek（便宜），关键测试用 Claude |
| 某个人进度落后 | 全员 | 每周一站会及时发现，别人顶上 |
| Gradio Demo 太简陋 | D | 没关系，答辩看的是逻辑和数据，不是 UI |
| 答辩超时 | D | 提前 2 周彩排，严格控制 5-7 分钟 |

---

## 依赖关系（不要搞错顺序）

```
安装环境 (全员, 6/1-6/3)
    ↓
跑通 API (全员, 6/4-6/7)
    ↓
准备数据 (A/B/C, 6/8-6/21)  ← 最花时间
    ↓
Prompt 调试 (A/B/C, 6/15-6/30)
    ↓
写 Python 代码 (A/B/C + Claude Code, 7/1-7/21)
    ↓
Gradio 联调 (D, 7/22-8/14)
    ↓
演示视频 (D, 8/22-8/31)
    ↓
报告 + PPT (全员, 9/1-9/21)
    ↓
答辩 (9/22-9/30)
```

---

*本路线图于 2026-05-27 根据团队实际情况（4 人、vibe coding、极简技术栈）重写。*
> 历史说明：本文形成于 `Beta` 原型出现之前，仍保留“代码骨架待搭建”等旧假设。若涉及当前真实状态，请以 [system-design.md](./system-design.md)、[beta-prototype-status.md](./beta-prototype-status.md) 和 [executable-full-process-plan.md](./executable-full-process-plan.md) 为准。
