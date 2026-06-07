# -*- coding: utf-8 -*-
"""单案评估页 — CareMind 核心交互页"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
import time

from utils.pipeline import CareMindPipeline
from data import ALL_CASES, CASE_NAMES

st.set_page_config(page_title="单案评估", page_icon="📋", layout="wide")

# ── 初始化 ──
if "pipeline" not in st.session_state:
    st.session_state.pipeline = CareMindPipeline()
if "result" not in st.session_state:
    st.session_state.result = None
if "running" not in st.session_state:
    st.session_state.running = False

# ── 路由：如果从主页跳转过来 ──
selected = st.session_state.get("selected_case", "case_1")

# ── 顶栏 ──
st.title("📋 单案评估")

# 案例选择器
col_sel, col_btn, col_space = st.columns([2, 1, 3])
with col_sel:
    case_key = st.selectbox(
        "选择案例",
        ["case_1", "case_2", "case_3"],
        format_func=lambda x: CASE_NAMES[x],
        index=["case_1", "case_2", "case_3"].index(selected),
        key="case_selector",
    )
with col_btn:
    st.write("")  # spacing
    run_clicked = st.button("🚀 运行多Agent评估", type="primary", use_container_width=True)

# ── 老人档案 ──
case_data = ALL_CASES[case_key]
elderly = case_data["elderly"]

st.divider()
st.subheader(f"👤 {elderly['name']} · {elderly['age']}岁 · {elderly['gender']}")

tab_info, tab_detail = st.tabs(["📌 摘要", "📋 详细档案"])

with tab_info:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("照护场景", elderly["care_setting"])
        st.metric("ADL总分", f"{sum(elderly['adl_scores'].values()) if elderly['adl_scores'] else '?'}/100")
    with col2:
        diagnoses = [d["name"] for d in elderly["diagnoses"]]
        st.metric("慢病数", f"{len(diagnoses)}种")
        for d in diagnoses[:3]:
            st.caption(f"• {d}")
    with col3:
        st.metric("用药数", f"{len(elderly['medications'])}种")
        st.metric("跌倒风险", f"Morse {elderly.get('morse_score', 'N/A')}")
    with col4:
        gds = elderly.get("gds_score", "N/A")
        mmse = elderly.get("mmse_score", "N/A")
        st.metric("抑郁(GDS)", f"{gds}")
        st.metric("认知(MMSE)", f"{mmse}")

with tab_detail:
    st.json(elderly)

st.divider()

# ── 运行Pipeline ──
if run_clicked or st.session_state.running:
    st.session_state.running = True

    pipeline = st.session_state.pipeline
    sim = case_data["simulation"]

    # ── 阶段1: 并行评估 ──
    st.subheader("🔍 阶段1：四维度并行评估")
    progress_text = "4个评估Agent并行运行中..."
    progress_bar = st.progress(0, text=progress_text)

    # 模拟并行评估的视觉效果
    cols_assess = st.columns(4)
    placeholders = {}
    agent_icons = {"medical": "🏥 医疗", "nursing": "💉 护理", "social": "🤝 社工", "dietary": "🍽️ 餐饮"}

    for i, key in enumerate(["medical", "nursing", "social", "dietary"]):
        with cols_assess[i]:
            placeholders[key] = st.empty()
            placeholders[key].info(f"{agent_icons[key]}Agent\n\n⏳ 评估中...")

    # 模拟逐步完成
    for i, key in enumerate(["medical", "nursing", "social", "dietary"]):
        time.sleep(0.4)  # 动画延迟
        agent_output = sim[key]
        summary = agent_output.get("summary", "")
        with cols_assess[i]:
            placeholders[key].success(f"{agent_icons[key]}Agent\n\n✅ 完成\n\n_{summary[:80]}..._")
        progress_bar.progress((i + 1) / 10, text=f"{agent_icons[key]}Agent 完成")

    time.sleep(0.3)

    # 展示各Agent结果
    with st.expander("📊 查看四维度评估详情", expanded=False):
        tabs = st.tabs(["🏥 医疗评估", "💉 护理评估", "🤝 社工评估", "🍽️ 餐饮评估"])
        for tab, key in zip(tabs, ["medical", "nursing", "social", "dietary"]):
            with tab:
                st.json(sim[key])

    # ── 阶段2: 编排层 ──
    st.subheader("🧠 阶段2：编排层 — 冲突消解 + 统一干预计划")
    progress_bar.progress(0.6, text="Orchestrator 工作中...")

    orch_out = sim["orchestrator"]
    time.sleep(0.5)

    conflicts = orch_out.get("conflict_resolutions", [])
    plan_items = orch_out.get("unified_care_plan", [])

    col_c1, col_c2 = st.columns(2)
    with col_c1:
        if conflicts:
            st.warning(f"⚠️ 检测到 **{len(conflicts)}处** 跨域冲突")
            for c in conflicts:
                with st.expander(f"冲突: {c.get('description', '')[:60]}...", expanded=False):
                    st.markdown(f"**涉及Agent**: {', '.join(c.get('agents_involved', []))}")
                    st.markdown(f"**消解方案**: {c.get('resolution', '')}")
        else:
            st.success("✅ 未检测到跨域冲突，各维度建议一致")
    with col_c2:
        st.metric("生成干预项", f"{len(plan_items)}项")
        urgent = sum(1 for i in plan_items if i.get("priority") == "紧急")
        week = sum(1 for i in plan_items if i.get("priority") == "本周内")
        ongoing = sum(1 for i in plan_items if i.get("priority") == "持续执行")
        st.caption(f"🔴 紧急: {urgent} | 🟡 本周内: {week} | 🟢 持续: {ongoing}")

    progress_bar.progress(0.8, text="Orchestrator 完成")

    # 风险热力图
    st.markdown("### 🌡️ 综合风险热力图")
    heatmap = orch_out.get("risk_heatmap", [])
    if heatmap:
        cols_h = st.columns(len(heatmap))
        risk_colors = {"低": "green", "中": "orange", "高": "red", "极高": "darkred"}
        for col_h, item in zip(cols_h, heatmap):
            dim = item.get("dimension", "")
            level = item.get("risk_level", "")
            color = risk_colors.get(level, "grey")
            with col_h:
                st.markdown(f"""
                <div style="text-align:center;padding:10px;border-radius:10px;background-color:{color}20;border:2px solid {color}">
                    <h4>{dim}</h4>
                    <h2 style="color:{color}">{level}</h2>
                </div>
                """, unsafe_allow_html=True)

    # ── 阶段3: 决策审核 ──
    st.subheader("⚖️ 阶段3：决策审核层 — 三审终审")
    progress_bar.progress(0.9, text="Decision Agent 审核中...")

    dec_out = sim["decision"]
    time.sleep(0.5)

    verdict = dec_out.get("verdict", "UNKNOWN")
    verdict_color = {"PASS": "green", "REVISE": "orange", "REJECT": "red"}.get(verdict, "grey")

    col_a1, col_a2, col_a3 = st.columns(3)
    for col_a, (key, label) in zip(
        [col_a1, col_a2, col_a3],
        [("rationality_audit", "合理性"), ("safety_audit", "安全性"), ("feasibility_audit", "可行性")],
    ):
        audit = dec_out.get(key, {})
        passed = "✅" if audit.get("passed") else "❌"
        with col_a:
            st.metric(f"{passed} {label}", f"{audit.get('score', '?')}分")

    # 审核结论
    st.markdown(f"### 审核结论：<span style='color:{verdict_color};font-size:1.5em'>{verdict}</span>", unsafe_allow_html=True)

    progress_bar.progress(1.0, text="✅ 评估完成")
    time.sleep(0.3)
    progress_bar.empty()

    # ── 最终干预计划 ──
    st.divider()
    st.subheader("📋 最终综合干预计划")

    final_plan = dec_out.get("final_care_plan", plan_items)
    category_emoji = {"医疗": "🏥", "护理": "💉", "社工": "🤝", "餐饮": "🍽️"}

    for priority_level, label, color in [
        ("紧急", "🔴 紧急（24小时内执行）", "#ffebee"),
        ("本周内", "🟡 本周内执行", "#fff8e1"),
        ("持续执行", "🟢 持续执行", "#e8f5e9"),
    ]:
        items = [i for i in final_plan if i.get("priority") == priority_level]
        if items:
            st.markdown(f"#### {label}")
            for item in items:
                cat = item.get("category", "")
                emoji = category_emoji.get(cat, "📌")
                with st.container(border=True):
                    cols_item = st.columns([6, 2, 2, 2])
                    with cols_item[0]:
                        st.markdown(f"**{emoji} [{cat}] {item.get('content', '')}**")
                    with cols_item[1]:
                        st.caption(f"来源: {item.get('source_agent', '')}")
                    with cols_item[2]:
                        st.caption(f"人力: {item.get('human_resources', '-')}")
                    with cols_item[3]:
                        st.caption(f"费用: {item.get('estimated_cost', '-')}")

    # ── 风险预警 ──
    alerts = dec_out.get("risk_alerts", [])
    if alerts:
        st.divider()
        st.subheader("⚠️ 风险预警")
        for alert in alerts:
            st.warning(alert)

    # ── 家属叙事 ──
    narrative = sim.get("social", {}).get("narrative_for_family", "")
    if narrative:
        st.divider()
        st.subheader("💬 给家属的话")
        st.info(f"> {narrative}")

    # ── 执行摘要 ──
    st.divider()
    st.subheader("📝 管理层执行摘要")
    st.markdown(dec_out.get("executive_summary", ""))

    # 保存结果
    st.session_state.result = {
        "medical": sim["medical"],
        "nursing": sim["nursing"],
        "social": sim["social"],
        "dietary": sim["dietary"],
        "orchestrator": orch_out,
        "decision": dec_out,
        "elderly_name": elderly["name"],
        "elderly_age": elderly["age"],
    }

    st.session_state.running = False

else:
    st.info("👆 选择一个案例后点击「运行多Agent评估」按钮开始")
