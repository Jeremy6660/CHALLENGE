# -*- coding: utf-8 -*-
"""输出格式化/渲染 — 将Pipeline输出渲染为可展示的Markdown/HTML"""

from typing import Optional
from utils.pipeline import PipelineResult


def render_markdown_report(result: PipelineResult) -> str:
    """将Pipeline结果渲染为完整的Markdown报告"""

    dec = result.decision_output
    orch = result.orchestrator_output

    lines = []
    lines.append(f"# CareMind 综合干预报告")
    lines.append(f"")
    lines.append(f"**老人**：{result.elderly_name}，{result.elderly_age}岁")
    lines.append(f"**审核结论**：{dec.get('verdict', 'N/A')}")
    lines.append(f"**总耗时**：{result.total_elapsed}s")
    lines.append(f"")
    lines.append(f"---")
    lines.append(f"")

    # ── 审核摘要 ──
    lines.append(f"## 审核摘要")
    lines.append(f"")
    for audit_key, audit_label in [
        ("rationality_audit", "合理性"),
        ("safety_audit", "安全性"),
        ("feasibility_audit", "可行性"),
    ]:
        audit = dec.get(audit_key, {})
        status = "✅" if audit.get("passed") else "❌"
        lines.append(f"- {status} **{audit_label}**：{audit.get('score', '?')}分")
        for note in audit.get("notes", []):
            lines.append(f"  - {note}")
    lines.append(f"")

    # ── 风险预警 ──
    alerts = dec.get("risk_alerts", [])
    if alerts:
        lines.append(f"## ⚠️ 风险预警")
        lines.append(f"")
        for alert in alerts:
            lines.append(f"- 🚨 {alert}")
        lines.append(f"")

    # ── 最终干预计划 ──
    lines.append(f"## 📋 最终综合干预计划")
    lines.append(f"")

    final_plan = dec.get("final_care_plan", [])
    if not final_plan:
        final_plan = orch.get("unified_care_plan", [])

    # 按优先级分组
    urgent = [i for i in final_plan if i.get("priority") == "紧急"]
    this_week = [i for i in final_plan if i.get("priority") == "本周内"]
    ongoing = [i for i in final_plan if i.get("priority") == "持续执行"]

    category_emoji = {"医疗": "🏥", "护理": "💉", "社工": "🤝", "餐饮": "🍽️"}

    for group_label, group_items in [
        ("🔴 紧急（24小时内必须执行）", urgent),
        ("🟡 本周内执行", this_week),
        ("🟢 持续执行", ongoing),
    ]:
        if group_items:
            lines.append(f"### {group_label}")
            lines.append(f"")
            for idx, item in enumerate(group_items, 1):
                cat = item.get("category", "")
                emoji = category_emoji.get(cat, "📌")
                lines.append(f"**{idx}. [{cat}] {emoji} {item.get('content', '')}**")
                lines.append(f"")
                lines.append(f"- 来源：{item.get('source_agent', '')}")
                if item.get("human_resources"):
                    lines.append(f"- 人力：{item.get('human_resources', '')}")
                if item.get("equipment"):
                    lines.append(f"- 设备：{item.get('equipment', '')}")
                if item.get("estimated_cost"):
                    lines.append(f"- 费用：{item.get('estimated_cost', '')}")
                lines.append(f"")
    lines.append(f"")

    # ── 四维评估摘要 ──
    lines.append(f"## 📊 四维度评估摘要")
    lines.append(f"")

    # 医疗
    med = result.medical_output
    lines.append(f"### 🏥 医疗维度")
    lines.append(f"> {med.get('summary', 'N/A')}")
    lines.append(f"")
    for cd in med.get("chronic_disease_assessment", []):
        lines.append(f"- **{cd.get('disease', '')}**：{cd.get('control_rating', '')}，趋势{cd.get('risk_trend', '')}")
    interactions = med.get("drug_interactions", [])
    if interactions:
        lines.append(f"- ⚠️ 发现 {len(interactions)} 处药物相互作用")
    lines.append(f"")

    # 护理
    nur = result.nursing_output
    lines.append(f"### 💉 护理维度")
    lines.append(f"> {nur.get('summary', 'N/A')}")
    lines.append(f"")
    adl = nur.get("adl_assessment", {})
    fall = nur.get("fall_risk", {})
    pu = nur.get("pressure_ulcer_risk", {})
    lines.append(f"- ADL：{adl.get('barthel_total', '?')}分 → {adl.get('dependency_level', '?')}")
    lines.append(f"- 跌倒风险：{fall.get('risk_level', '?')}（Morse {fall.get('morse_score', '?')}分）")
    lines.append(f"- 压疮风险：{pu.get('risk_level', '?')}（Braden {pu.get('braden_score', '?')}分）")
    lines.append(f"- 建议照护等级：{nur.get('recommended_care_level', '?')}级")
    lines.append(f"")

    # 社工
    soc = result.social_output
    lines.append(f"### 🤝 社工维度")
    lines.append(f"> {soc.get('summary', 'N/A')}")
    lines.append(f"")
    mh = soc.get("mental_health", {})
    cog = soc.get("cognitive_status", {})
    lines.append(f"- 心理健康：{mh.get('depression_risk', '?')}抑郁风险")
    lines.append(f"- 社会隔离风险：{soc.get('social_engagement', {}).get('social_isolation_risk', '?')}")
    lines.append(f"- 认知功能：{cog.get('cognitive_level', '?')}（MMSE {cog.get('mmse_score', '?')}）")
    narrative = soc.get("narrative_for_family", "")
    if narrative:
        lines.append(f"")
        lines.append(f"> 💬 **给家属的话**：{narrative}")
    lines.append(f"")

    # 餐饮
    diet = result.dietary_output
    lines.append(f"### 🍽️ 餐饮维度")
    lines.append(f"> {diet.get('summary', 'N/A')}")
    lines.append(f"")
    ns = diet.get("nutrition_status", {})
    sw = diet.get("swallow_function", {})
    dp = diet.get("dietary_plan", {})
    lines.append(f"- 营养状态：{ns.get('nutrition_rating', '?')}（BMI {ns.get('bmi', '?')}）")
    lines.append(f"- 吞咽安全：{sw.get('swallow_safety', '?')} → {sw.get('recommended_texture', '?')}")
    lines.append(f"- 膳食方案：{dp.get('dietary_type', '?')}，{dp.get('daily_calories_kcal', '?')}kcal/日")
    lines.append(f"")

    # ── 执行摘要 ──
    lines.append(f"---")
    lines.append(f"")
    lines.append(f"## 📝 管理层执行摘要")
    lines.append(f"")
    lines.append(dec.get("executive_summary", "N/A"))
    lines.append(f"")

    return "\n".join(lines)


def render_intervention_table_html(plan_items: list) -> str:
    """将干预计划渲染为HTML表格"""
    rows = []
    for item in plan_items:
        priority_color = {
            "紧急": "#e74c3c",
            "本周内": "#f39c12",
            "持续执行": "#27ae60",
        }.get(item.get("priority", ""), "#95a5a6")

        rows.append(f"""
        <tr>
            <td style="color:{priority_color};font-weight:bold">{item.get('priority', '')}</td>
            <td><span class="badge">{item.get('category', '')}</span></td>
            <td>{item.get('content', '')}</td>
            <td>{item.get('source_agent', '')}</td>
            <td>{item.get('human_resources', '-')}</td>
        </tr>
        """)

    return f"""
    <table>
        <thead>
            <tr>
                <th>优先级</th><th>维度</th><th>干预内容</th><th>来源</th><th>人力</th>
            </tr>
        </thead>
        <tbody>
            {''.join(rows)}
        </tbody>
    </table>
    """
