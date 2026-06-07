# -*- coding: utf-8 -*-
"""案例2：李爷爷 — 中度失能·机构养老·医疗护理并重（Polypharmacy典型）"""

# ════════════════════════════════════════════════════════════
# 老人全维档案
# ════════════════════════════════════════════════════════════

ELDERLY_PROFILE = {
    "name": "李爷爷",
    "age": 82,
    "gender": "男",
    "care_setting": "机构养老",
    "days_in_care": 180,

    "diagnoses": [
        {"name": "2型糖尿病", "control_status": "欠佳", "notes": "近3月HbA1c 8.2%，空腹血糖波动大(6.5-10.2)"},
        {"name": "冠心病（支架术后2年）", "control_status": "尚可", "notes": "偶有胸闷，活动耐量下降"},
        {"name": "慢性肾功能不全CKD3期", "control_status": "尚可", "notes": "eGFR 48，需限蛋白限钾"},
        {"name": "高尿酸血症", "control_status": "欠佳", "notes": "尿酸520μmol/L"},
        {"name": "良性前列腺增生", "control_status": "尚可", "notes": "夜尿2-3次"},
    ],
    "medications": [
        {"name": "二甲双胍", "dosage": "500mg tid", "indication": "糖尿病"},
        {"name": "格列美脲", "dosage": "2mg qd", "indication": "糖尿病"},
        {"name": "阿司匹林", "dosage": "100mg qd", "indication": "抗血小板"},
        {"name": "氯吡格雷", "dosage": "75mg qd", "indication": "抗血小板（支架术后）"},
        {"name": "瑞舒伐他汀", "dosage": "10mg qn", "indication": "降脂稳定斑块"},
        {"name": "美托洛尔", "dosage": "25mg bid", "indication": "冠心病/心率控制"},
        {"name": "呋塞米", "dosage": "20mg qd", "indication": "利尿（下肢轻度水肿）"},
        {"name": "别嘌醇", "dosage": "100mg qd", "indication": "降尿酸"},
    ],
    "vitals": {
        "systolic_bp": 135, "diastolic_bp": 78, "heart_rate": 62,
        "fasting_glucose": 8.8, "hba1c": 8.2, "spo2": 96, "temperature": 36.6,
    },
    "labs": {
        "albumin": 34.0, "hemoglobin": 118, "creatinine": 148,
        "egfr": 48, "potassium": 4.8, "uric_acid": 520,
    },
    "allergies": ["青霉素（皮试阳性）"],
    "fall_history": "3个月前在房间内跌倒1次（被地毯绊倒），右髋部软组织挫伤",

    "adl_scores": {
        "feeding": 10, "bathing": 0, "grooming": 5, "dressing": 5,
        "bowels": 10, "bladder": 5, "toilet_use": 5,
        "transfers": 10, "mobility": 5, "stairs": 0,
    },
    "morse_score": 55,
    "braden_score": 14,
    "mobility_note": "需使用助行器，步态不稳，转身时需扶持。起床和坐下需协助。",
    "has_catheter": False,
    "has_ng_tube": False,

    "gds_score": 6,
    "mmse_score": 22,
    "social_activities": "参加院内下棋活动（每周2-3次），其他活动参与少",
    "family_visit_frequency": "儿子儿媳每周探视2次（周三晚上+周末），女儿在外省很少来",
    "family_relationship": "融洽，儿子关心但缺乏照护知识",
    "life_story": "退休前是国企工程师，性格温和但固执（不承认自己需要控制饮食，常偷吃甜食）。与同房间老人关系良好。",

    "height_cm": 170,
    "weight_kg": 55.2,
    "weight_change_1m": -1.0,
    "swallowing_test": "2级",
    "dental_status": "佩戴活动义齿，咀嚼功能尚可",
    "dietary_restrictions": ["糖尿病饮食", "低盐", "低嘌呤"],
}

# 注意：eGFR 48 → CKD3期，二甲双胍需减量（eGFR 30-59时最大1000mg/日）
# 呋塞米+别嘌醇 → 注意肾功能监测
# 格列美脲+美托洛尔 → β阻滞剂可能掩盖低血糖症状，这是关键药物相互作用

# ════════════════════════════════════════════════════════════
# 模拟评估输出
# ════════════════════════════════════════════════════════════

SIM_MEDICAL = {
    "chronic_disease_assessment": [
        {
            "disease": "2型糖尿病",
            "control_rating": "欠佳",
            "evidence": "HbA1c 8.2%（目标<7.0%），空腹血糖波动大(6.5-10.2mmol/L)，饮食控制差(自述偷吃甜食)",
            "risk_trend": "恶化",
        },
        {
            "disease": "冠心病（支架术后2年）",
            "control_rating": "尚可",
            "evidence": "双抗治疗中，偶有胸闷但无急性事件。心率62bpm控制良好。",
            "risk_trend": "稳定",
        },
        {
            "disease": "慢性肾功能不全CKD3期",
            "control_rating": "尚可",
            "evidence": "eGFR 48 ml/min，血钾4.8偏高但未超标。需警惕二甲双胍蓄积和造影剂肾损伤。",
            "risk_trend": "稳定",
        },
        {
            "disease": "高尿酸血症",
            "control_rating": "欠佳",
            "evidence": "尿酸520μmol/L，远高于目标(<360)，痛风发作风险高",
            "risk_trend": "恶化",
        },
    ],
    "drug_interactions": [
        {
            "severity": "高",
            "drugs_involved": ["格列美脲", "美托洛尔"],
            "mechanism": "β受体阻滞剂（美托洛尔）可掩盖低血糖的交感神经预警症状（心悸、震颤、出汗），使低血糖在无征兆下进展为严重低血糖昏迷",
            "clinical_consequence": "老人可能在无预警的情况下发生严重低血糖，尤其在夜间。这对独居或仅有护工照护的场景极其危险。",
            "recommendation": "建议将格列美脲更换为SGLT-2抑制剂（如达格列净）或DPP-4抑制剂，低血糖风险显著降低。如必须保留磺脲类，则需加强夜间血糖监测。",
        },
        {
            "severity": "中",
            "drugs_involved": ["呋塞米", "别嘌醇"],
            "mechanism": "利尿剂可降低肾脏对尿酸的排泄能力，可能加重高尿酸血症；同时呋塞米与别嘌醇合用可能增加别嘌醇过敏反应风险",
            "clinical_consequence": "尿酸控制效果打折扣，且增加别嘌醇超敏反应综合征风险（尤其在CKD患者中）",
            "recommendation": "监测尿酸变化；若尿酸持续不降，可考虑将别嘌醇更换为非布司他（CKD3-4期可用，不需调整剂量）。呋塞米若仅为轻度水肿，可评估能否减量或停用。",
        },
        {
            "severity": "中",
            "drugs_involved": ["二甲双胍", "CKD3期"],
            "mechanism": "eGFR 48时二甲双胍剂量应减至最大1000mg/日（当前为500mg tid=1500mg/日，超量），过量使用增加乳酸酸中毒风险",
            "clinical_consequence": "二甲双胍蓄积→乳酸酸中毒风险升高（罕见但致死率高），尤其在脱水、感染、使用造影剂时",
            "recommendation": "将二甲双胍减量至500mg bid（1000mg/日）或更换为经肝脏代谢的降糖药。行增强CT等需用造影剂时，提前48小时停用二甲双胍。",
        },
    ],
    "acute_risk_assessment": [
        {
            "risk_type": "低血糖昏迷",
            "probability": "高",
            "trigger_factors": ["格列美脲+美托洛尔掩盖低血糖症状", "进食不规律", "肾功能减退延缓药物清除"],
            "preventive_measures": ["更换降糖方案（停磺脲类换SGLT-2i）", "加强血糖监测(每日4次)", "睡前必须测血糖"],
        },
        {
            "risk_type": "跌倒",
            "probability": "高",
            "trigger_factors": ["步态不稳(Morse 55)", "夜尿2-3次", "低血糖可能", "利尿剂致体位性低血压"],
            "preventive_measures": ["床旁放置助行器", "夜间使用床旁便器避免去卫生间", "起身时先坐30秒再站立"],
        },
        {
            "risk_type": "心血管事件",
            "probability": "中",
            "trigger_factors": ["糖尿病+冠心病多重危险因素", "血糖控制差加速动脉硬化"],
            "preventive_measures": ["严格血糖管理", "继续双抗治疗（需评估消化道出血风险）", "定期心电图"],
        },
    ],
    "medical_recommendations": [
        {
            "priority": "紧急",
            "category": "用药调整",
            "content": "【药物重整】建议与处方医生沟通以下调整：①格列美脲→达格列净5mg qd（降糖+心肾双获益）②二甲双胍减量为500mg bid ③评估呋塞米可否减量为20mg qod或停用",
            "rationale": "消除格列美脲+美托洛尔的'隐形低血糖'风险，控制二甲双胍在CKD安全剂量内，减少利尿剂对尿酸和电解质的干扰",
        },
        {
            "priority": "紧急",
            "category": "监测",
            "content": "即日起血糖监测频率增至每日4次（晨起空腹+三餐后2h），睡前必测。建立血糖日记。低血糖(<3.9mmol/L)立即口服15g葡萄糖。",
            "rationale": "当前降糖方案存在高隐匿性低血糖风险，加强监测是最低成本的保护措施",
        },
        {
            "priority": "本周内",
            "category": "会诊",
            "content": "建议药剂科+内分泌科联合会诊，做一次完整的药物重整(Medication Reconciliation)",
            "rationale": "8种药物中存在3处需处理的相互作用/剂量问题，单一科室难以全面评估",
        },
    ],
    "summary": "医疗维度是本案例最复杂维度：糖尿病控制欠佳+3处药物相互作用（其中格列美脲+美托洛尔为高风险）+低血糖昏迷和跌倒两项高风险。需紧急药物重整。",
}

SIM_NURSING = {
    "adl_assessment": {
        "barthel_total": 55,
        "dependency_level": "中度依赖",
        "strengths": ["进食可独立完成", "大便控制正常"],
        "deficits": ["洗澡完全依赖", "穿衣需协助", "小便偶有失禁", "如厕需协助", "行走需助行器+陪伴", "上下楼梯不能"],
        "assistance_required": "日常起居需持续辅助：沐浴完全依赖、穿衣50%协助、如厕需搀扶、室内行走需助行器+1人陪同",
    },
    "fall_risk": {
        "morse_score": 55,
        "risk_level": "高风险",
        "key_risk_factors": ["步态不稳需助行器", "近3月有跌倒史", "夜尿2-3次", "使用利尿剂（体位性低血压风险）", "使用降糖药（低血糖）"],
        "environmental_risks": ["房间地毯（已导致1次跌倒）", "夜间去卫生间路径昏暗", "床旁无扶手"],
    },
    "pressure_ulcer_risk": {
        "braden_score": 14,
        "risk_level": "中风险",
        "weakest_dimension": "活动能力（久坐下棋时间长，不愿主动变换姿势）",
        "current_ulcers": None,
    },
    "recommended_care_level": 3,
    "nursing_recommendations": [
        {
            "priority": "紧急",
            "category": "安全防护",
            "content": "立即移除房间地毯（已导致1次跌倒），床旁安装可移动扶手，床旁放置呼叫铃。夜间使用床旁便器，避免摸黑去卫生间。",
            "frequency": "一次性改造+持续执行",
            "rationale": "Morse 55分高风险+3月内跌倒史，二次跌倒可能导致骨折→卧床→压疮→感染的下行螺旋",
        },
        {
            "priority": "紧急",
            "category": "安全防护",
            "content": "护理员每2小时巡视1次（尤其夜间），重点关注起床/如厕安全。起身前协助老人先坐30秒再站立，预防体位性低血压。",
            "frequency": "Q2H",
            "rationale": "利尿剂+降压药联合使用易致体位性低血压，结合夜尿频繁，夜间是跌倒最高危时段",
        },
        {
            "priority": "本周内",
            "category": "活动训练",
            "content": "康复师评估后，在护理员监护下开展坐姿平衡训练（3次/周×20分钟）和助行器安全使用训练",
            "frequency": "3次/周",
            "rationale": "维持残余肌力，延缓功能衰退。注意：必须有人监护，不可独立训练。",
        },
        {
            "priority": "持续执行",
            "category": "皮肤护理",
            "content": "鼓励每坐1小时起身活动5分钟（利用下棋间隙）。坐垫使用减压凝胶垫。每日检查骶尾部和足跟皮肤。",
            "frequency": "每日",
            "rationale": "Braden 14分中风险，久坐下棋是主要风险行为，需行为干预而非仅靠设备",
        },
    ],
    "summary": "ADL中度依赖(Barthel 55)，跌倒高风险(Morse 55)，照护等级建议上调至3级。最紧急的是环境安全改造和加强夜间巡视。",
}

SIM_SOCIAL = {
    "mental_health": {
        "gds_score": 6,
        "depression_risk": "轻度",
        "anxiety_level": "轻度",
        "emotional_state": "情绪总体尚可，但对自己的疾病管理有轻度焦虑。对'不能吃甜食'有抵触情绪，表现出一定的'控制的丧失感'(loss of control)。与室友关系好，下棋是他主要的快乐来源。",
        "key_concerns": ["对饮食限制的抵触和挫败感", "轻度疾病焦虑", "因跌倒史对活动产生恐惧"],
    },
    "social_engagement": {
        "activity_participation": "一般",
        "peer_relationship": "与室友关系良好，有固定棋友。社会参与以'下棋'为核心，活动类型单一。",
        "social_isolation_risk": "低",
        "recommended_activities": ["院内健康讲座(糖尿病自我管理)", "轻度手工活动", "与室友一起参加院内合唱或棋类比赛"],
    },
    "family_support": {
        "visit_frequency": "每周2次（周三晚+周末）",
        "relationship_quality": "融洽",
        "caregiver_burden": "儿子承担主要照护协调责任，目前负担尚可",
        "support_gaps": ["家属缺乏糖尿病管理和用药安全知识", "女儿远在外省几乎不参与"],
    },
    "cognitive_status": {
        "mmse_score": 22,
        "cognitive_level": "轻度认知障碍",
        "preserved_abilities": ["逻辑思维尚好（下棋策略性思考仍强）", "远期记忆清晰", "计算能力保留"],
        "declined_areas": ["近期记忆力下降", "执行功能轻度下降（疾病自我管理能力不足）"],
        "communication_ability": "交流基本正常，但有时固执己见，对健康建议接受度偏低",
    },
    "social_recommendations": [
        {
            "priority": "本周内",
            "category": "家属沟通",
            "content": "为儿子提供30分钟'照护者教育'：①解释药物相互作用风险（为何要换降糖药）②糖尿病饮食核心原则 ③跌倒预防的关键措施。让家属成为'同盟'而非'旁观者'。",
            "rationale": "家属每周探视2次但缺乏照护知识，赋能家属可显著提升照护质量和老人依从性",
        },
        {
            "priority": "本周内",
            "category": "心理支持",
            "content": "以'下棋'为切入点建立信任，通过棋局中的策略讨论引导他理解'健康管理也是一种策略'——不是剥夺自由，而是赢得更多下棋的时间",
            "rationale": "老人的核心心理冲突是'丧失控制感'。直接说教无效，需用他熟悉的语言（下棋策略类比健康管理）建立内在动机",
        },
        {
            "priority": "持续执行",
            "category": "认知训练",
            "content": "利用下棋活动本身作为认知训练（策略思考、前瞻规划、对手行为预测），鼓励参加院内棋类比赛增加参与感",
            "rationale": "MMSE 22分轻度认知障碍，丰富的认知活动可延缓认知功能下降。下棋是最适合他的认知刺激",
        },
    ],
    "narrative_for_family": "李工今天又赢了两盘棋。他下棋时特别认真，每一步都要想很久——他的室友说'他这是在用工程师的方式下棋'。不过今天下午他主动问护理员'我这个药换了对血糖有什么好处'——这是他第一次自己提健康问题。也许他开始愿意成为自己健康的'总工程师'了。",
    "summary": "社工维度风险较低（GDS 6分轻度抑郁，社会参与一般但非孤立），核心任务是赋能家属+以兴趣为切入点提升健康自我管理动机。",
}

SIM_DIETARY = {
    "nutrition_status": {
        "bmi": 19.1,
        "albumin": 34.0,
        "hemoglobin": 118,
        "weight_trend": "下降",
        "nutrition_rating": "中度不良",
        "key_deficits": ["BMI 19.1偏瘦", "白蛋白34处于临界低值", "体重持续下降", "蛋白质摄入不足"],
    },
    "swallow_function": {
        "test_result": "2级",
        "swallow_safety": "安全",
        "recommended_texture": "软食",
    },
    "dietary_plan": {
        "dietary_type": "糖尿病肾病软食（低GI+优质低蛋白+低盐+低嘌呤）",
        "daily_calories_kcal": 1800,
        "daily_protein_g": 48,
        "restrictions": [
            "糖尿病：控制碳水化合物总量与GI值，分餐制（三餐+两加餐）",
            "CKD3期：优质低蛋白 0.6-0.8g/kg/d（约48g/日），限钾（香蕉、橙子、土豆去皮泡水），限磷（动物内脏、坚果）",
            "低盐（<5g/日）",
            "低嘌呤（红肉、内脏、海鲜、啤酒禁忌）",
        ],
        "forbidden_foods": [
            "甜食、含糖饮料（糖尿病）",
            "香蕉、橙子、土豆（高钾，CKD）",
            "动物内脏、沙丁鱼（高嘌呤+高磷）",
            "腌制品、加工肉（高盐）",
            "浓茶、咖啡（利尿+刺激）",
        ],
        "recommended_foods": [
            "鸡蛋清（优质蛋白+低磷）",
            "鱼肉（清蒸，每周2-3次）",
            "豆腐（适量，植物蛋白）",
            "绿叶蔬菜（焯水去钾）",
            "全谷物（燕麦、荞麦，低GI）",
            "低GI水果（苹果、梨、草莓，限量）",
        ],
    },
    "dietary_recommendations": [
        {
            "priority": "紧急",
            "category": "膳食调整",
            "content": "即日起严格执行糖尿病肾病饮食。食堂需标注'李爷爷专用餐'，禁止其购买或接受甜食。三餐+两加餐模式稳定血糖。",
            "rationale": "糖尿病控制不佳+体重持续下降+CKD，饮食是三项疾病管理的共同基石。偷吃甜食必须从环境层面阻断。",
        },
        {
            "priority": "本周内",
            "category": "营养补充",
            "content": "每日提供肾病专用肠内营养补充剂1份（如 Nepro 或同类产品，237ml≈425kcal+19g优质蛋白+低钾低磷配方），作为下午加餐",
            "rationale": "常规食物难以在48g蛋白限制下满足营养需求，肾病专用补充剂可精准填补营养缺口",
        },
        {
            "priority": "持续执行",
            "category": "监测",
            "content": "每周称重1次，每月复查白蛋白和电解质（尤其血钾），根据指标动态调整膳食方案",
            "rationale": "CKD患者的饮食限制必须与化验结果联动，避免过度限制导致营养不良",
        },
    ],
    "summary": "中度营养不良，需在CKD3期+糖尿病+痛风三重限制下设计膳食（1800kcal+48g蛋白），食堂需专人专餐+肾病专用补充剂。",
}

# ════════════════════════════════════════════════════════════
# 编排层模拟输出
# ════════════════════════════════════════════════════════════

SIM_ORCHESTRATOR = {
    "medical_assessment": SIM_MEDICAL,
    "nursing_assessment": SIM_NURSING,
    "social_assessment": SIM_SOCIAL,
    "dietary_assessment": SIM_DIETARY,

    "unified_care_plan": [
        {
            "intervention_id": "INT-001",
            "category": "医疗",
            "priority": "紧急",
            "content": "【药物重整】联系处方医生调整降糖方案：停格列美脲→达格列净5mg qd；二甲双胍减量为500mg bid；评估呋塞米可否减量。目的：消除隐匿性低血糖风险+心肾双保护。",
            "source_agent": "medical",
            "human_resources": "养老院医生+药剂科会诊",
            "equipment": "无",
            "estimated_cost": "低（达格列净已纳入医保）",
        },
        {
            "intervention_id": "INT-002",
            "category": "医疗",
            "priority": "紧急",
            "content": "即日起血糖监测增至每日4次（晨起空腹+三餐后2h），睡前必测。建立血糖日记，低血糖(<3.9)立即口服15g葡萄糖。",
            "source_agent": "medical",
            "human_resources": "护理员执行、护士审核数据",
            "equipment": "血糖仪+试纸（已有）",
            "estimated_cost": "低（试纸消耗）",
        },
        {
            "intervention_id": "INT-003",
            "category": "护理",
            "priority": "紧急",
            "content": "立即移除房间地毯，床旁安装扶手，放置呼叫铃。夜间使用床旁便器，起身前先坐30秒。护理员Q2H巡视（夜间重点关注）。",
            "source_agent": "nursing",
            "human_resources": "护理员3班×2人（已覆盖在常规人力中）",
            "equipment": "床旁扶手1个+呼叫铃1个+床旁便器1个",
            "estimated_cost": "低（设备约200-400元）",
        },
        {
            "intervention_id": "INT-004",
            "category": "餐饮",
            "priority": "紧急",
            "content": "即日起食堂提供'糖尿病肾病专用餐'（1800kcal+48g蛋白），禁止提供甜食。三餐两点制。每日下午加餐Nepro补充剂1份。",
            "source_agent": "dietary",
            "human_resources": "食堂营养配餐员+护理员监督",
            "equipment": "Nepro肾病补充剂（约15元/瓶）",
            "estimated_cost": "中（补充剂约450元/月）",
        },
        {
            "intervention_id": "INT-005",
            "category": "护理",
            "priority": "本周内",
            "content": "康复师评估后开展坐姿平衡训练（3次/周×20分钟，护理员监护下）。注意：不可独立行走训练，必须在监护下进行。",
            "source_agent": "nursing",
            "human_resources": "康复师1名+护理员1名",
            "equipment": "康复椅+弹力带",
            "estimated_cost": "低",
        },
        {
            "intervention_id": "INT-006",
            "category": "社工",
            "priority": "本周内",
            "content": "为儿子提供30分钟照护者教育（药物风险认知+糖尿病饮食+跌倒预防），并发给'家属照护手册'简易版。",
            "source_agent": "social",
            "human_resources": "社工1名",
            "equipment": "照护手册（打印版）",
            "estimated_cost": "无",
        },
        {
            "intervention_id": "INT-007",
            "category": "社工",
            "priority": "本周内",
            "content": "以'下棋策略'类比导入健康管理动机访谈：引导李爷爷将'控制饮食'理解为'为赢得更多下棋时间做的策略选择'而非'被剥夺自由'。",
            "source_agent": "social",
            "human_resources": "社工1名（需具备动机访谈技能）",
            "equipment": "无（下棋桌即可）",
            "estimated_cost": "无",
        },
        {
            "intervention_id": "INT-008",
            "category": "医疗",
            "priority": "持续执行",
            "content": "每月复查HbA1c、肾功能（肌酐+eGFR）、电解质（尤其血钾）、尿酸。每季度心电图。",
            "source_agent": "medical",
            "human_resources": "护士采血+外送检验",
            "equipment": "无",
            "estimated_cost": "中（检验费约200-300元/月，医保可报）",
        },
        {
            "intervention_id": "INT-009",
            "category": "护理",
            "priority": "持续执行",
            "content": "每日检查皮肤（骶尾+足跟），鼓励每坐1小时站立活动5分钟。使用减压凝胶坐垫。",
            "source_agent": "nursing",
            "human_resources": "护理员（已覆盖）",
            "equipment": "凝胶坐垫1个",
            "estimated_cost": "低（约100元）",
        },
        {
            "intervention_id": "INT-010",
            "category": "社工",
            "priority": "持续执行",
            "content": "鼓励参加院内棋类比赛和轻度手工活动，用下棋活动本身作为认知训练手段。",
            "source_agent": "social",
            "human_resources": "活动组织者（院内已有）",
            "equipment": "棋具（已有）",
            "estimated_cost": "无",
        },
    ],

    "conflict_resolutions": [
        {
            "conflict_id": "CON-R1",
            "agents_involved": ["medical", "nursing"],
            "description": "医疗Agent建议严格控制血糖需'限制自由进食'，护理Agent建议为防跌倒需'在监护下活动'——护理的跌倒预防可能因严格限制而间接加剧（老人因受限制产生抵触，自行活动时逃避监护）",
            "resolution": "社工Agent担当'缓冲层'：通过动机访谈（下棋策略类比）提升老人内在依从意愿，而非仅靠外部限制。护理+医疗的'限制'配社工的'赋能'，形成软硬结合的照护策略。",
            "resolution_rule": "compromise",
        },
        {
            "conflict_id": "CON-R2",
            "agents_involved": ["medical", "dietary"],
            "description": "餐饮Agent建议每日蛋白48g（CKD标准0.6-0.8g/kg），但老人BMI 19.1+体重下降——低蛋白可能加重营养不良",
            "resolution": "采用优质蛋白策略：48g蛋白中≥70%来自高生物价蛋白（鸡蛋清、鱼肉、肾病补充剂），最大化有限蛋白的利用效率。同时每月监测白蛋白，若降至<30则重新评估蛋白限制。",
            "resolution_rule": "medical_first",
        },
    ],

    "risk_heatmap": [
        {"dimension": "医疗", "risk_level": "极高"},
        {"dimension": "护理", "risk_level": "高"},
        {"dimension": "餐饮", "risk_level": "高"},
        {"dimension": "社工", "risk_level": "低"},
    ],
    "overall_priority": "医疗主导型",
    "summary": "李爷爷是典型的Polypharmacy高危案例：8种药物中存在3处需处理的相互作用/剂量问题，其中最危险的是格列美脲+美托洛尔的'隐匿性低血糖'风险。医疗维度是绝对主战场（药物重整+密切监测），护理维度紧随其后（跌倒高风险+安全改造），餐饮维度面临CKD+糖尿病+痛风的'三重限制'挑战，社工维度以赋能家属和动机访谈为辅助策略。这个案例充分展示了CareMind多Agent协同的价值：如果没有医疗Agent发现药物相互作用，护理Agent的跌倒预防可能被一次'无征兆低血糖晕厥'瞬间击穿。",
}

# ════════════════════════════════════════════════════════════
# 决策审核层模拟输出
# ════════════════════════════════════════════════════════════

SIM_DECISION = {
    "verdict": "PASS",
    "rationality_audit": {
        "passed": True,
        "score": 94,
        "notes": [
            "覆盖全面：医疗(3紧急+1监测)、护理(2紧急+1训练+1皮肤)、餐饮(1紧急+1补充+1监测)、社工(2教育+1动机访谈)全部到位",
            "干预粒度优秀：'联系处方医生调整方案'而非'注意用药安全'；'移除地毯+床旁扶手+呼叫铃'而非'加强安全'",
            "优先级排序精准：药物重整>血糖监测>环境安全>饮食控制，逻辑链清晰",
        ],
    },
    "safety_audit": {
        "passed": True,
        "score": 90,
        "notes": [
            "药物相互作用处理方案符合指南（SGLT-2i替代磺脲类在CKD3期可用且有心肾获益）",
            "活动训练明确要求'监护下进行'，避免了跌倒风险",
            "餐饮计划充分考虑了CKD+DM双重限制，补充剂选用肾病专用型号正确",
            "需注意：二甲双胍减量后应监测血糖是否进一步失控，必要时加第二种替代药物",
        ],
    },
    "feasibility_audit": {
        "passed": True,
        "score": 82,
        "notes": [
            "药物重整需处方医生配合——养老院需主动联系外部医生，有一定协调成本",
            "Nepro补充剂约450元/月，需确认费用由谁承担（养老院/家属/长护险）",
            "康复师每周3次在多数养老院可行（机构内有康复师），但小型机构可能需要外聘",
            "血糖每日4次监测增加了护理员工作量，需在排班中明确责任人",
        ],
    },
    "revision_notes": [],
    "final_care_plan": SIM_ORCHESTRATOR["unified_care_plan"],

    "risk_alerts": [
        "🚨 格列美脲+美托洛尔组合是'定时炸弹'——低血糖可能在夜间无征兆发生，药物重整完成前务必执行睡前血糖检测",
        "🚨 eGFR 48+二甲双胍1500mg/日已超CKD安全剂量，减量必须在本周内执行",
        "⚠️ 跌倒史+夜尿+Morse 55——如有条件建议使用床旁报警垫（离床即报警）",
    ],
    "executive_summary": "李爷爷（82岁，机构养老，8种药物）是典型的'多药并用+多病共存'复杂案例。最紧急的是药物重整——格列美脲+美托洛尔组合存在隐匿性低血糖风险，二甲双胍在CKD3期超量使用。建议本周内完成降糖方案切换（SGLT-2i替代磺脲类）和二甲双胍减量。同步执行环境安全改造（移除地毯+扶手+呼叫铃）和糖尿病肾病专用餐启动。护理员需加强夜间巡视（Q2H）。社工通过'下棋策略'类比进行动机访谈，提升老人对饮食和用药的依从性。预计药物调整后2-4周血糖趋于稳定，跌倒风险从'高'降至'中'。",
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
