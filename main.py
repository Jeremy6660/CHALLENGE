# -*- coding: utf-8 -*-
"""CareMind 智慧养老多Agent系统 — Streamlit 主页"""

import sys
import os

# Allow plain "python main.py" to reopen itself through Streamlit.
if __name__ == "__main__" and os.environ.get("CAREMIND_STREAMLIT_BOOTSTRAPPED") != "1":
    try:
        from streamlit.runtime.scriptrunner import get_script_run_ctx
    except Exception:
        get_script_run_ctx = None

    ctx = get_script_run_ctx() if get_script_run_ctx else None
    if ctx is None:
        from streamlit.web import bootstrap

        os.environ["CAREMIND_STREAMLIT_BOOTSTRAPPED"] = "1"
        bootstrap.run(os.path.abspath(__file__), False, [], {})
        raise SystemExit

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import streamlit as st

st.set_page_config(
    page_title="CareMind 智慧养老",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── 侧边栏 ──
with st.sidebar:
    st.image("https://img.icons8.com/color/96/hospital-3.png", width=64)
    st.title("CareMind")
    st.caption("智慧养老多Agent系统")
    st.divider()

    st.markdown("### 📋 系统导航")
    st.markdown("- 🏠 **主页**（当前）")
    st.markdown("- 📋 单案评估 → `单案评估`页")
    st.markdown("- 📊 案例对比 → `案例对比`页")
    st.markdown("- 🏗️ 系统架构 → `架构展示`页")

    st.divider()
    st.caption("v1.0 | 医养结合·全人照护·反客体化实践")
    st.caption("竞赛演示版")

# ── 主内容 ──
st.title("🏥 CareMind 智慧养老多Agent系统")
st.markdown("> *在数字层面充当医养结合的桥梁 —— 用AI赋能一线护工，让每一位老人被当作'人'来对待*")

st.divider()

# 系统简介
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("评估维度", "4", "医疗·护理·社工·餐饮")
with col2:
    st.metric("Agent层级", "3层", "评估→编排→决策")
with col3:
    st.metric("典型案例", "3套", "轻/中/重度失能")
with col4:
    st.metric("技术理念", "全人照护", "反客体化实践")

st.divider()

# 案例选择
st.subheader("📋 选择评估案例")

case_info = {
    "case_1": {
        "title": "案例一：王奶奶",
        "subtitle": "78岁 · 轻度失能 · 社区居家",
        "focus": "🎯 社工主导型",
        "desc": "社会隔离导致抑郁和饮食下降。有时最好的处方不是药，而是社会连接。",
        "tags": "高血压 | 骨关节炎 | GDS 10分 | Barthel 85",
    },
    "case_2": {
        "title": "案例二：李爷爷",
        "subtitle": "82岁 · 中度失能 · 机构养老",
        "focus": "🎯 医疗护理并重型",
        "desc": "8种药物、3处相互作用风险。Polypharmacy是隐形杀手，多Agent协同精准识别。",
        "tags": "糖尿病 | 冠心病 | CKD3期 | 8种药 | Barthel 55",
    },
    "case_3": {
        "title": "案例三：张爷爷",
        "subtitle": "89岁 · 重度失能 · 长期卧床",
        "focus": "🎯 护理主导型",
        "desc": "完全依赖+压疮+吸入性肺炎。终末期照护的'反客体化'实践——Barthel 0分，人的价值不是0分。",
        "tags": "阿尔茨海默 | 鼻饲 | Braden 9 | Barthel 0",
    },
}

cols = st.columns(3)

for i, (key, info) in enumerate(case_info.items()):
    with cols[i]:
        with st.container(border=True):
            st.markdown(f"### {info['title']}")
            st.caption(info['subtitle'])
            st.markdown(f"**{info['focus']}**")
            st.markdown(info['desc'])
            st.caption(f"📌 {info['tags']}")
            if st.button(f"🚀 运行评估", key=f"btn_{key}", use_container_width=True):
                st.session_state["selected_case"] = key
                st.switch_page("pages/1_单案评估.py")

st.divider()

# 系统架构概览
st.subheader("🏗️ 系统架构概览")
st.markdown("""
```
输入层: 老人全维档案（结构化数据 + 自然语言描述）
    │
    ▼
┌──────────────────────────────────────────────────────┐
│  评估层 — 4 Agent 并行                                │
│  ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐       │
│  │ 🏥医疗 │ │ 💉护理 │ │ 🤝社工 │ │ 🍽️餐饮 │       │
│  │慢病管理│ │ADL评估 │ │心理健康│ │营养需求│       │
│  │用药安全│ │跌倒风险│ │社会参与│ │吞咽功能│       │
│  │急性风险│ │压疮风险│ │家庭支持│ │特殊膳食│       │
│  └───┬────┘ └───┬────┘ └───┬────┘ └───┬────┘       │
└──────┼───────────┼───────────┼───────────┼──────────┘
       └───────────┴─────┬─────┴───────────┘
                         │ 4份结构化评估报告
                         ▼
┌──────────────────────────────────────────────────────┐
│  编排层 — Orchestrator Agent                          │
│  冲突检测·消解·优先级排序·统一干预计划生成            │
└──────────────────────┬───────────────────────────────┘
                       │ 统一干预计划草案
                       ▼
┌──────────────────────────────────────────────────────┐
│  决策层 — Decision Agent                              │
│  合理性审核·安全性审核·资源可行性审核·PASS/REVISE     │
└──────────────────────┬───────────────────────────────┘
                       │ 审核通过
                       ▼
输出层: 📋综合干预计划 + ⚠️风险预警 + 💬家属沟通报告
```
""")

st.divider()
st.caption("📎 更多详情请查看侧边栏中的「架构展示」页面")
