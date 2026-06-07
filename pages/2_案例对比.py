# -*- coding: utf-8 -*-
"""案例对比页 — 3个案例并排对比"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
import pandas as pd

from data import ALL_CASES, CASE_NAMES

st.set_page_config(page_title="案例对比", page_icon="📊", layout="wide")

st.title("📊 三案例对比分析")
st.markdown("展示CareMind系统在不同失能等级、不同照护场景下的差异化Agent工作逻辑")

st.divider()

# ── 基本信息对比 ──
st.subheader("📌 基本信息对比")

cases_basic = []
for key in ["case_1", "case_2", "case_3"]:
    e = ALL_CASES[key]["elderly"]
    cases_basic.append({
        "案例": e["name"],
        "年龄": e["age"],
        "性别": e["gender"],
        "照护场景": e["care_setting"],
        "慢病数": len(e["diagnoses"]),
        "用药数": len(e["medications"]),
        "ADL总分": sum(e["adl_scores"].values()) if e["adl_scores"] else "N/A",
        "Morse跌倒": e.get("morse_score", "N/A"),
        "Braden压疮": e.get("braden_score", "N/A"),
        "GDS抑郁": e.get("gds_score", "N/A"),
        "MMSE认知": e.get("mmse_score", "N/A"),
        "BMI": f"{e.get('weight_kg', 0) / (e.get('height_cm', 1) / 100) ** 2:.1f}" if e.get("height_cm") and e.get("weight_kg") else "N/A",
    })

df_basic = pd.DataFrame(cases_basic)
st.dataframe(df_basic.set_index("案例"), use_container_width=True)

st.divider()

# ── Agent关注度热力图 ──
st.subheader("🌡️ 四维度关注度/干预强度热力图")

heatmap_data = {
    "维度": ["医疗", "护理", "社工", "餐饮"],
    "王奶奶\n（轻度失能）": ["★★☆☆☆ (低)", "★★☆☆☆ (低)", "★★★★★ (极高)", "★★★☆☆ (中)"],
    "李爷爷\n（中度失能）": ["★★★★★ (极高)", "★★★★☆ (高)", "★★☆☆☆ (低)", "★★★★☆ (高)"],
    "张爷爷\n（重度失能）": ["★★★★☆ (高)", "★★★★★ (极高)", "★★★☆☆ (中)", "★★★★★ (极高)"],
}

df_heatmap = pd.DataFrame(heatmap_data)
st.dataframe(df_heatmap.set_index("维度"), use_container_width=True)

st.markdown("""
| 强度 | 含义 |
|------|------|
| ★★★★★ 极高 | 该维度是案例核心战场，紧急干预项≥3 |
| ★★★★☆ 高 | 该维度风险显著，干预项≥2 |
| ★★★☆☆ 中 | 该维度有风险但非首要，以监测和常规干预为主 |
| ★★☆☆☆ 低 | 该维度整体稳定，以维持现状为主 |
""")

st.divider()

# ── 关键差异对比 ──
st.subheader("🔑 关键差异对比")

comparisons = [
    {
        "对比维度": "系统定位",
        "王奶奶": "社工主导型 — 社会连接是最佳处方",
        "李爷爷": "医疗主导型 — 药物重整是核心任务",
        "张爷爷": "护理主导型 — Q2H翻身是生命线",
    },
    {
        "对比维度": "最紧急风险",
        "王奶奶": "中度抑郁+社会隔离(GDS 10分)",
        "李爷爷": "隐匿性低血糖昏迷(格列美脲+美托洛尔)",
        "张爷爷": "压疮恶化(Braden 9+已有1期压疮)",
    },
    {
        "对比维度": "药物安全",
        "王奶奶": "✅ 2种药，无相互作用",
        "李爷爷": "🚨 8种药，3处相互作用(1高2中)",
        "张爷爷": "⚠️ 6种药，2处相互作用(1中1低)",
    },
    {
        "对比维度": "照护等级",
        "王奶奶": "1级(自理型+安全防护)",
        "李爷爷": "3级(中度照护，多数ADL需协助)",
        "张爷爷": "5级(特级照护，1:1.5配比)",
    },
    {
        "对比维度": "跨域冲突",
        "王奶奶": "无 — 社工主导，其他维度配合",
        "李爷爷": "2处 — 医疗限制vs护理训练/餐饮蛋白限制",
        "张爷爷": "2处 — 翻身疼痛vs镇静风险/高容量喂养vs误吸",
    },
    {
        "对比维度": "社工角色",
        "王奶奶": "主角 — 社区资源链接+社会参与恢复",
        "李爷爷": "辅助 — 赋能家属+动机访谈提升依从性",
        "张爷爷": "尊严守护者 — 感官地图+非语言叙事+家属哀伤辅导",
    },
    {
        "对比维度": "CareMind核心价值体现",
        "王奶奶": "全人照护：识别'孤独'比'疾病'更需要干预",
        "李爷爷": "医养协同：药物相互作用是护工无法识别的隐性杀手",
        "张爷爷": "反客体化：即使Barthel 0分，人的价值不归零",
    },
]

for comp in comparisons:
    with st.expander(f"📌 {comp['对比维度']}", expanded=False):
        cols = st.columns(3)
        for col, case_name in zip(cols, ["王奶奶", "李爷爷", "张爷爷"]):
            with col:
                st.markdown(f"**{case_name}**")
                st.markdown(comp[case_name])

st.divider()

# ── 系统适应性总结 ──
st.subheader("💡 CareMind 系统适应性总结")
st.markdown("""
三个案例展示了CareMind在不同照护场景下的**自适应能力**：

1. **轻度失能·社区居家**：系统自动识别"社工维度是主战场"，将资源集中在社会参与和社区链接上，避免过度医疗化
2. **中度失能·机构养老**：系统精准发现多药并用的隐性风险（Polypharmacy），通过药物重整消解安全威胁——这类问题是传统养老管理系统中完全缺失的能力
3. **重度失能·长期卧床**：系统在'维持生命'和'维护尊严'两条线上同时发力——Q2H翻身+营养升级保生命，感官地图+非语言叙事护尊严

**与传统养老管理系统的本质区别**：
- 传统系统：记录"今天体温36.8℃，排便1次"
- CareMind：看见"他听到京剧时呼吸变平稳了，女儿的声音让他的手指轻轻动了一下"
""")

st.divider()
st.caption("💡 提示：前往「单案评估」页可查看每个案例完整的Agent运行过程和干预计划")
