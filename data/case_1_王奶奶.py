# -*- coding: utf-8 -*-
"""案例1：王奶奶 — 轻度失能·社区居家·社工维度是核心"""

# ════════════════════════════════════════════════════════════
# 老人全维档案
# ════════════════════════════════════════════════════════════

ELDERLY_PROFILE = {
    "name": "王奶奶",
    "age": 78,
    "gender": "女",
    "care_setting": "社区日间照料",
    "days_in_care": None,

    "diagnoses": [
        {"name": "高血压1级", "control_status": "尚可", "notes": "偶有波动，与情绪相关"},
        {"name": "双膝骨关节炎", "control_status": "尚可", "notes": "晨起僵硬，上下楼梯时疼痛"},
    ],
    "medications": [
        {"name": "硝苯地平缓释片", "dosage": "30mg qd", "indication": "高血压"},
        {"name": "阿托伐他汀", "dosage": "10mg qn", "indication": "降血脂"},
    ],
    "vitals": {
        "systolic_bp": 148, "diastolic_bp": 88, "heart_rate": 76,
        "fasting_glucose": 5.2, "hba1c": None, "spo2": 97, "temperature": 36.5,
    },
    "labs": {
        "albumin": 36.0, "hemoglobin": 122, "creatinine": 72,
        "egfr": 78, "potassium": 4.1, "uric_acid": 320,
    },
    "allergies": [],
    "fall_history": "近1年无跌倒",

    "adl_scores": {
        "feeding": 10, "bathing": 0, "grooming": 5, "dressing": 10,
        "bowels": 10, "bladder": 10, "toilet_use": 10,
        "transfers": 15, "mobility": 10, "stairs": 5,
    },
    "morse_score": 30,
    "braden_score": 20,
    "mobility_note": "可独立行走，但步态略缓慢，上下楼梯需扶扶手",
    "has_catheter": False,
    "has_ng_tube": False,

    "gds_score": 10,
    "mmse_score": 26,
    "social_activities": "几乎不参加社区活动，偶尔去菜市场",
    "family_visit_frequency": "儿子在外地工作，约每月1次电话/视频，节假日可能回来",
    "family_relationship": "与儿子关系良好但沟通频率低，老伴听力差基本无交流",
    "life_story": "退休前是小学语文教师，喜欢读书看报。丈夫听力严重下降后，两人几乎无有效交流。常说自己'像一个人过日子'。",

    "height_cm": 158,
    "weight_kg": 55.6,
    "weight_change_1m": -1.5,
    "swallowing_test": "1级",
    "dental_status": "佩戴活动义齿，咀嚼功能尚可",
    "dietary_restrictions": ["低盐饮食"],
}

# ════════════════════════════════════════════════════════════
# 模拟评估输出
# ════════════════════════════════════════════════════════════

SIM_MEDICAL = {
    "chronic_disease_assessment": [
        {
            "disease": "高血压1级",
            "control_rating": "尚可",
            "evidence": "血压148/88mmHg，略高于目标值(<140/90)，偶有波动与情绪相关",
            "risk_trend": "稳定",
        },
        {
            "disease": "双膝骨关节炎",
            "control_rating": "尚可",
            "evidence": "晨起僵硬，上下楼梯疼痛，但未影响平地行走，暂无急性发作",
            "risk_trend": "稳定",
        },
    ],
    "drug_interactions": [],
    "acute_risk_assessment": [
        {
            "risk_type": "跌倒",
            "probability": "中",
            "trigger_factors": ["浴室地面湿滑", "楼梯无扶手侧", "膝关节突发疼痛"],
            "preventive_measures": ["浴室安装扶手和防滑垫", "楼梯双侧加装扶手", "使用手杖辅助"],
        },
    ],
    "medical_recommendations": [
        {
            "priority": "持续执行",
            "category": "监测",
            "content": "每周自测血压3次并记录，关注情绪波动时的血压变化",
            "rationale": "血压偶有波动，与情绪相关，需建立连续的血压日记以便调整用药",
        },
        {
            "priority": "持续执行",
            "category": "其他",
            "content": "膝关节保暖+适度关节活动操（坐姿抬腿、踝泵运动），每日10分钟",
            "rationale": "维持关节功能，减缓骨关节炎进展",
        },
    ],
    "summary": "慢病整体控制尚可，用药无冲突，主要风险为中度跌倒概率和社交隔离引起的血压波动。",
}

SIM_NURSING = {
    "adl_assessment": {
        "barthel_total": 85,
        "dependency_level": "轻度依赖",
        "strengths": ["进食", "穿衣", "大小便控制", "如厕", "床椅转移"],
        "deficits": ["洗澡需协助", "上下楼梯需扶手"],
        "assistance_required": "仅洗澡和上下楼梯时需要轻度辅助，其余日常活动可自理",
    },
    "fall_risk": {
        "morse_score": 30,
        "risk_level": "中风险",
        "key_risk_factors": ["步态略缓慢", "膝关节疼痛", "浴室无防滑设施"],
        "environmental_risks": ["浴室地面湿滑", "楼梯扶手不完善"],
    },
    "pressure_ulcer_risk": {
        "braden_score": 20,
        "risk_level": "无风险",
        "weakest_dimension": "活动能力（虽然有行走能力但活动量偏少）",
        "current_ulcers": None,
    },
    "recommended_care_level": 1,
    "nursing_recommendations": [
        {
            "priority": "本周内",
            "category": "安全防护",
            "content": "居家适老化改造：浴室加装L型扶手+防滑地垫，马桶旁加装折叠扶手，楼梯双侧加装扶手",
            "frequency": "一次性改造",
            "rationale": "降低居家跌倒风险，Morse评分30分处于中风险区间",
        },
        {
            "priority": "持续执行",
            "category": "活动训练",
            "content": "鼓励每日户外散步20分钟（平坦路面，使用手杖），配合社区健身器材做坐姿蹬腿训练",
            "frequency": "每日",
            "rationale": "维持下肢肌力和平衡能力，延缓功能衰退",
        },
    ],
    "summary": "ADL轻度依赖(Barthel 85)，跌倒中风险需居家安全改造，压疮无风险，建议照护等级1级（自理型+安全防护）。",
}

SIM_SOCIAL = {
    "mental_health": {
        "gds_score": 10,
        "depression_risk": "中度",
        "anxiety_level": "轻度",
        "emotional_state": "存在明显的孤独感和无用感。老伴听力差导致日常几乎无有效交流，儿子远在外地。她描述自己的生活为'一天说不了几句话'。但智力完好，有表达和社交的意愿。",
        "key_concerns": ["社交隔离导致的抑郁情绪", "空巢老人夫妻间沟通障碍", "缺乏情感出口"],
    },
    "social_engagement": {
        "activity_participation": "几乎不参与",
        "peer_relationship": "邻里关系一般，无固定社交圈。退休后与原同事联系逐渐减少。",
        "social_isolation_risk": "高",
        "recommended_activities": [
            "社区老年读书会（对口她退休语文教师的兴趣）",
            "社区日间照料中心每周2-3次活动",
            "老年大学书法或文学课程",
            "社区低龄老人志愿者'一帮一'结对",
        ],
    },
    "family_support": {
        "visit_frequency": "儿子每月1次电话/视频",
        "relationship_quality": "融洽",
        "caregiver_burden": "无（老人基本自理）",
        "support_gaps": ["儿子地理距离远无法日常陪伴", "老伴自身听力障碍无法提供情感支持", "缺乏紧急联系人机制"],
    },
    "cognitive_status": {
        "mmse_score": 26,
        "cognitive_level": "轻度认知障碍",
        "preserved_abilities": ["语言表达流畅", "阅读能力完好", "远期记忆清晰"],
        "declined_areas": ["近期记忆力轻度下降（常忘记东西放哪）"],
        "communication_ability": "表达清晰、逻辑良好，是一位'有故事'的老人。她需要的是一个倾听者。",
    },
    "social_recommendations": [
        {
            "priority": "紧急",
            "category": "心理支持",
            "content": "社工48小时内上门做首次心理评估和陪伴访谈，建立信任关系，评估自杀风险（GDS≥10分的中度抑郁需排除自杀意念）",
            "rationale": "GDS 10分已达中度抑郁阈值，社会隔离高风险，需尽快介入防止恶化",
        },
        {
            "priority": "本周内",
            "category": "社会参与",
            "content": "链接社区日间照料中心，安排每周二四上午参加活动（读书会+轻度体能活动），由社区志愿者协助接送",
            "rationale": "结构化的社会参与是缓解老年抑郁最有效的非药物干预之一",
        },
        {
            "priority": "本周内",
            "category": "家属沟通",
            "content": "与儿子沟通：建议每周至少2次视频通话（固定时间），教会老人使用微信视频功能；建立'紧急联系人卡'放老人钱包内",
            "rationale": "增加家庭连接感，降低孤独感；紧急联系人机制降低安全风险",
        },
        {
            "priority": "持续执行",
            "category": "资源链接",
            "content": "链接社区'银龄互助'志愿者项目，安排低龄老年志愿者每周上门1次陪伴聊天+读书读报",
            "rationale": "同龄人陪伴效果优于年轻志愿者，且具有可持续性",
        },
    ],
    "narrative_for_family": "王老师最近常坐在窗边看楼下的孩子们玩耍。她说这让她想起以前教书的时光——'那时候教室里闹哄哄的，现在家里太安静了'。但她读到好文章时眼睛会亮起来，还会用红笔在旁边写批注。她需要的不是更多药，是一个能和她聊聊书的人。",
    "summary": "社工维度是本案例核心战场：中度抑郁+高社会隔离风险。老人认知完好、有表达意愿，通过社区资源链接和社会参与可以有效改善。有时最好的处方是社会连接。",
}

SIM_DIETARY = {
    "nutrition_status": {
        "bmi": 22.3,
        "albumin": 36.0,
        "hemoglobin": 122,
        "weight_trend": "下降",
        "nutrition_rating": "轻度不良",
        "key_deficits": ["近1月体重下降1.5kg(2.6%)", "蛋白质摄入可能不足"],
    },
    "swallow_function": {
        "test_result": "1级",
        "swallow_safety": "安全",
        "recommended_texture": "普食",
    },
    "dietary_plan": {
        "dietary_type": "低盐普食",
        "daily_calories_kcal": 1700,
        "daily_protein_g": 55,
        "restrictions": ["低钠（<5g盐/日）"],
        "forbidden_foods": ["腌制品", "加工肉制品", "过咸调味料"],
        "recommended_foods": ["鸡蛋", "鱼肉", "豆腐", "绿叶蔬菜", "全谷物", "牛奶"],
    },
    "dietary_recommendations": [
        {
            "priority": "本周内",
            "category": "营养补充",
            "content": "每日增加1个鸡蛋+1杯牛奶（或豆浆），保证优质蛋白摄入≥55g/日",
            "rationale": "体重下降提示蛋白质-能量摄入不足，且老人存在'懒得做饭'的问题",
        },
        {
            "priority": "本周内",
            "category": "膳食调整",
            "content": "链接社区老年餐桌或送餐服务，解决'一人做饭无动力'的问题，确保每日至少两餐热食",
            "rationale": "营养问题的根源是社会隔离导致的进食动力下降，而非疾病所致",
        },
        {
            "priority": "持续执行",
            "category": "监测",
            "content": "每周称重1次，目标1月内体重回升至56.5kg以上",
            "rationale": "体重是营养状态最直接的指标",
        },
    ],
    "summary": "轻度营养不良(体重下降2.6%/月)，根因是社会隔离导致进食动力不足。与社工Agent联动：解决社交问题自然改善饮食。",
}

SIM_ORCHESTRATOR = {
    "medical_assessment": SIM_MEDICAL,
    "nursing_assessment": SIM_NURSING,
    "social_assessment": SIM_SOCIAL,
    "dietary_assessment": SIM_DIETARY,

    "unified_care_plan": [
        {
            "intervention_id": "INT-001",
            "category": "社工",
            "priority": "紧急",
            "content": "社工48小时内上门做心理评估，建立信任关系，排除自杀意念（GDS 10分中度抑郁需此步骤）",
            "source_agent": "social",
            "human_resources": "社工1名",
            "equipment": "GDS量表、社区资源手册",
            "estimated_cost": "无",
        },
        {
            "intervention_id": "INT-002",
            "category": "社工",
            "priority": "本周内",
            "content": "链接社区日间照料中心，安排每周二四上午参加活动（读书会+轻度体能+社交午餐）",
            "source_agent": "social",
            "human_resources": "日照中心工作人员",
            "equipment": "社区接送车辆（或志愿者接送）",
            "estimated_cost": "低（日照中心政府补贴，老人自付约200-300元/月）",
        },
        {
            "intervention_id": "INT-003",
            "category": "社工",
            "priority": "本周内",
            "content": "与儿子建立每周2次固定视频通话机制，教会老人使用微信视频",
            "source_agent": "social",
            "human_resources": "社工指导1次+家属配合",
            "equipment": "智能手机（已有）",
            "estimated_cost": "无",
        },
        {
            "intervention_id": "INT-004",
            "category": "餐饮",
            "priority": "本周内",
            "content": "链接社区老年餐桌/送餐服务，确保每日至少两餐热食+1蛋+1奶",
            "source_agent": "dietary",
            "human_resources": "社区助餐点人员",
            "equipment": "无",
            "estimated_cost": "低（老年餐桌约10-15元/餐）",
        },
        {
            "intervention_id": "INT-005",
            "category": "护理",
            "priority": "本周内",
            "content": "居家适老化改造：浴室扶手+防滑垫+马桶折叠扶手+楼梯双侧扶手",
            "source_agent": "nursing",
            "human_resources": "适老化改造施工人员",
            "equipment": "L型扶手2个、防滑地垫2块、折叠扶手1个",
            "estimated_cost": "中（约800-1500元，可申请政府适老化改造补贴）",
        },
        {
            "intervention_id": "INT-006",
            "category": "社工",
            "priority": "持续执行",
            "content": "链接'银龄互助'志愿者每周上门1次陪伴（同龄退休教师优先匹配）",
            "source_agent": "social",
            "human_resources": "志愿者1名/周",
            "equipment": "无",
            "estimated_cost": "无",
        },
        {
            "intervention_id": "INT-007",
            "category": "医疗",
            "priority": "持续执行",
            "content": "每周自测血压3次并记录情绪波动时的读数，社区医生每月随访1次",
            "source_agent": "medical",
            "human_resources": "社区医生每月1次",
            "equipment": "家用血压计（已有）",
            "estimated_cost": "无",
        },
        {
            "intervention_id": "INT-008",
            "category": "护理",
            "priority": "持续执行",
            "content": "每日户外散步20分钟（手杖辅助，平坦路面）+坐姿膝关节活动操",
            "source_agent": "nursing",
            "human_resources": "无需额外人力",
            "equipment": "手杖1根",
            "estimated_cost": "低（手杖约50-100元）",
        },
        {
            "intervention_id": "INT-009",
            "category": "餐饮",
            "priority": "持续执行",
            "content": "每周称重1次，目标1月内体重回升至56.5kg以上。如持续下降则转诊营养科",
            "source_agent": "dietary",
            "human_resources": "社区护士/社工协助称重",
            "equipment": "体重秤",
            "estimated_cost": "无",
        },
    ],

    "conflict_resolutions": [],
    # 本案例无重大跨域冲突——社工主导、其他维度配合的格局清晰

    "risk_heatmap": [
        {"dimension": "社工", "risk_level": "高"},
        {"dimension": "护理", "risk_level": "中"},
        {"dimension": "餐饮", "risk_level": "中"},
        {"dimension": "医疗", "risk_level": "低"},
    ],
    "overall_priority": "社工主导型",
    "summary": "王奶奶的案例生动诠释了'全人照护'理念：核心风险不在医院、不在药房，而在于社会连接的断裂。社工维度的高风险（抑郁+隔离）是主战场，餐饮和护理维度的轻度异常是社会隔离的次级效应。最有效的'处方'不是新药，而是社区日间照料中心的一张活动桌、一位愿意听她聊书的志愿者、和儿子每周两次的视频通话。医疗和护理维度提供安全保障，但社工维度才是治本之策。",
}

SIM_DECISION = {
    "verdict": "PASS",
    "rationality_audit": {
        "passed": True,
        "score": 92,
        "notes": [
            "覆盖了四个维度所有关键风险点，社工维度的紧急干预(心理评估)非常及时",
            "干预粒度适中，每项建议都具体可执行",
            "优先级排序正确：紧急社工介入→本周社会参与/营养/安全改造→持续监测",
        ],
    },
    "safety_audit": {
        "passed": True,
        "score": 95,
        "notes": [
            "无用药冲突，医疗维度的血压监测频率合理",
            "活动建议（户外散步、社区活动）在医疗安全范围内",
            "饮食建议已考虑低盐限制，无安全矛盾",
        ],
    },
    "feasibility_audit": {
        "passed": True,
        "score": 85,
        "notes": [
            "大部分干预依托现有社区资源（日间照料中心、老年餐桌、志愿者体系），可行性强",
            "适老化改造费用中等（800-1500元），建议协助申请政府补贴",
            "社区日间照料中心每周2次频率合理，不会给老人造成负担",
        ],
    },
    "revision_notes": [],
    "final_care_plan": SIM_ORCHESTRATOR["unified_care_plan"],
    # 直接引用编排层计划（审核PASS无修改）

    "risk_alerts": [
        "⚠️ GDS 10分中度抑郁，首次社工访谈务必排除自杀意念",
        "⚠️ 体重持续下降趋势若1个月内未扭转，需考虑器质性疾病排查",
    ],
    "executive_summary": "王奶奶（78岁，社区居家）的核心问题是'孤独'而非'疾病'——GDS抑郁评分10分（中度）、近1月体重下降2.6%、几乎零社交。但她的优势同样突出：认知完好、有表达意愿、自理能力基本维持。建议以'社会参与'为杠杆撬动全局改善：日间照料中心提供社交场景，老年餐桌解决饮食问题，志愿者陪伴填补情感空缺。预计2-4周内情绪和营养指标将显著改善。医疗和护理维度仅需常规监测，无需加药或入院。这是一个'低医疗成本、高社会回报'的典型案例。",
}

# ════════════════════════════════════════════════════════════
# 打包
# ════════════════════════════════════════════════════════════

CASE_DATA = {
    "elderly": ELDERLY_PROFILE,
    "simulation": {
        "medical": SIM_MEDICAL,
        "nursing": SIM_NURSING,
        "social": SIM_SOCIAL,
        "dietary": SIM_DIETARY,
        "orchestrator": SIM_ORCHESTRATOR,
        "decision": SIM_DECISION,
    },
}
