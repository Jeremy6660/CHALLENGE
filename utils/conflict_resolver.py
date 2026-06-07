# -*- coding: utf-8 -*-
"""冲突检测与消解规则引擎

双层机制：
- 第一层(本文件)：硬编码规则处理可枚举的冲突类型
- 第二层(LLM)：Orchestrator的prompt处理规则无法覆盖的柔性冲突
"""

from typing import Optional


# ── 冲突规则定义 ──

def _detect_activity_conflict(
    medical: dict, nursing: dict, social: dict
) -> Optional[dict]:
    """
    规则1: 医疗限制活动 vs 护理/社工要求增加活动
    消解: 安全优先，设计替代活动
    """
    med_recs = medical.get("medical_recommendations", [])
    nursing_recs = nursing.get("nursing_recommendations", [])
    social_recs = social.get("social_recommendations", [])

    med_restricts = any(
        "限制活动" in r.get("content", "") or "卧床" in r.get("content", "")
        for r in med_recs
    )
    nursing_activates = any(
        "活动" in r.get("content", "") or "行走" in r.get("content", "") or "训练" in r.get("content", "")
        for r in nursing_recs
    )
    social_activates = any(
        "活动" in r.get("content", "") or "外出" in r.get("content", "") or "社交" in r.get("content", "")
        for r in social_recs
    )

    if med_restricts and (nursing_activates or social_activates):
        return {
            "conflict_id": "CON-R1",
            "agents_involved": ["medical", "nursing", "social"],
            "description": "医疗Agent要求限制活动，但护理/社工Agent建议增加活动和社交参与",
            "resolution": "在医疗安全范围内设计替代方案：将集体活动改为床边一对一交流，"
                         "将行走训练改为床上/坐姿肢体活动训练，由护理员在旁监护。"
                         "待医疗评估风险降低后再逐步恢复离床活动。",
            "resolution_rule": "safety_first",
        }
    return None


def _detect_diet_medical_conflict(
    medical: dict, dietary: dict
) -> Optional[dict]:
    """
    规则2: 餐饮高蛋白/高热量建议 vs 医疗肾功能不全/糖尿病
    消解: 医疗优先，调整饮食方案
    """
    med_recs = medical.get("medical_recommendations", [])
    dietary_plan = dietary.get("dietary_plan", {})
    chronic = medical.get("chronic_disease_assessment", [])

    # 检查是否有肾病
    has_ckd = any(
        "肾" in d.get("disease", "") for d in chronic
    )
    # 检查是否有糖尿病
    has_dm = any(
        "糖尿" in d.get("disease", "") for d in chronic
    )

    dietary_type = dietary_plan.get("dietary_type", "")
    dietary_protein = dietary_plan.get("daily_protein_g", 60)

    if has_ckd and dietary_protein > 50:
        return {
            "conflict_id": "CON-R2",
            "agents_involved": ["medical", "dietary"],
            "description": f"餐饮Agent建议蛋白质{dietary_protein}g/日，但老人存在肾功能不全",
            "resolution": "以医疗指征优先。调整为优质低蛋白饮食，蛋白质控制在0.6-0.8g/kg/d。"
                         "选用鸡蛋、鱼肉等优质蛋白来源，避免红肉和加工肉制品。"
                         "同时监测血肌酐和尿素氮变化。",
            "resolution_rule": "medical_first",
        }

    if has_dm and "糖尿病" not in dietary_type and "低糖" not in dietary_type:
        return {
            "conflict_id": "CON-R2b",
            "agents_involved": ["medical", "dietary"],
            "description": "老人有糖尿病但膳食方案未明确标注糖尿病饮食",
            "resolution": "调整膳食类型为糖尿病适宜饮食，控制碳水化合物总量和GI值，"
                         "采用三餐两点制(上午加餐+下午加餐)，避免血糖大幅波动。",
            "resolution_rule": "medical_first",
        }

    return None


def _detect_social_medical_conflict(
    medical: dict, social: dict
) -> Optional[dict]:
    """
    规则3: 社工建议频繁探视/外出 vs 医疗感染/跌倒风险
    消解: 折中方案
    """
    acute_risks = medical.get("acute_risk_assessment", [])
    social_recs = social.get("social_recommendations", [])

    has_infection_risk = any(
        "感染" in r.get("risk_type", "") for r in acute_risks
        if r.get("probability", "低") in ("高", "中")
    )
    has_fall_risk_high = any(
        "跌倒" in r.get("risk_type", "") and r.get("probability", "低") in ("高", "中")
        for r in acute_risks
    )

    social_visits = any(
        "探视" in r.get("content", "") or "外出" in r.get("content", "")
        for r in social_recs
    )

    if social_visits and (has_infection_risk or has_fall_risk_high):
        restrictions = []
        if has_infection_risk:
            restrictions.append("探视需佩戴口罩、手消毒")
        if has_fall_risk_high:
            restrictions.append("仅在护理人员陪同下在室内活动")

        return {
            "conflict_id": "CON-R3",
            "agents_involved": ["medical", "social"],
            "description": "社工建议增加探视/外出，但医疗评估提示存在感染/跌倒风险",
            "resolution": f"折中方案：{'; '.join(restrictions)}。"
                         "同时鼓励使用视频通话等远程探视方式。"
                         "探视时间控制在30分钟内，预约制。",
            "resolution_rule": "compromise",
        }
    return None


def _detect_swallow_nutrition_conflict(
    dietary: dict
) -> Optional[dict]:
    """
    规则4: 吞咽困难 vs 经口营养目标
    消解: 根据吞咽等级调整食物质地和进食方式
    """
    swallow = dietary.get("swallow_function", {})
    nutrition = dietary.get("nutrition_status", {})

    swallow_safety = swallow.get("swallow_safety", "安全")
    recommended_texture = swallow.get("recommended_texture", "普食")

    if swallow_safety == "需鼻饲" and recommended_texture != "鼻饲":
        return {
            "conflict_id": "CON-R4",
            "agents_involved": ["dietary"],
            "description": "吞咽评估建议鼻饲，但膳食方案未采用鼻饲途径",
            "resolution": "统一调整为鼻饲方案。选择高热高蛋白肠内营养制剂，"
                         "目标热量和蛋白量不变，通过持续滴注方式给予。"
                         "每4小时检查胃残留量，床头抬高30-45°防反流。",
            "resolution_rule": "safety_first",
        }
    return None


# ── 主入口 ──

def resolve_conflicts(
    medical_output: dict,
    nursing_output: dict,
    social_output: dict,
    dietary_output: dict,
) -> list[dict]:
    """
    规则引擎冲突消解主函数。
    返回消解后的冲突列表，可注入到Orchestrator做提示。
    """
    conflicts = []

    # 规则1: 活动限制冲突
    c1 = _detect_activity_conflict(medical_output, nursing_output, social_output)
    if c1:
        conflicts.append(c1)

    # 规则2: 饮食vs疾病冲突
    c2 = _detect_diet_medical_conflict(medical_output, dietary_output)
    if c2:
        conflicts.append(c2)

    # 规则3: 社交vs医疗冲突
    c3 = _detect_social_medical_conflict(medical_output, social_output)
    if c3:
        conflicts.append(c3)

    # 规则4: 吞咽vs营养冲突
    c4 = _detect_swallow_nutrition_conflict(dietary_output)
    if c4:
        conflicts.append(c4)

    return conflicts
