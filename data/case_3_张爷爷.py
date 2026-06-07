# -*- coding: utf-8 -*-
"""案例3：张爷爷 — 重度失能·长期卧床·护理主导型（反客体化实践典型）"""

# ════════════════════════════════════════════════════════════
# 老人全维档案
# ════════════════════════════════════════════════════════════

ELDERLY_PROFILE = {
    "name": "张爷爷",
    "age": 89,
    "gender": "男",
    "care_setting": "机构养老",
    "days_in_care": 420,

    "diagnoses": [
        {"name": "重度阿尔茨海默病（CDR3级）", "control_status": "未控制", "notes": "完全无法交流，不认识家人，无自主语言"},
        {"name": "高血压3级（很高危）", "control_status": "尚可", "notes": "用药控制中，但波动受感染/疼痛影响"},
        {"name": "陈旧性脑梗死（左侧基底节区）", "control_status": "后遗症期", "notes": "右侧肢体偏瘫，2019年发病"},
        {"name": "吸入性肺炎（反复发作）", "control_status": "欠佳", "notes": "过去1年发作2次住院，最近一次2个月前"},
        {"name": "完全性卧床状态", "control_status": "不可逆", "notes": "卧床2年+，全身肌肉萎缩"},
    ],
    "medications": [
        {"name": "多奈哌齐", "dosage": "10mg qd", "indication": "阿尔茨海默病"},
        {"name": "美金刚", "dosage": "10mg bid", "indication": "阿尔茨海默病"},
        {"name": "氨氯地平", "dosage": "5mg qd", "indication": "高血压"},
        {"name": "氯吡格雷", "dosage": "75mg qd", "indication": "抗血小板（脑梗二级预防）"},
        {"name": "奥美拉唑", "dosage": "20mg qd", "indication": "胃黏膜保护（与抗血小板药联用）"},
        {"name": "劳拉西泮", "dosage": "0.5mg prn", "indication": "必要时镇静（烦躁时）"},
    ],
    "vitals": {
        "systolic_bp": 142, "diastolic_bp": 80, "heart_rate": 78,
        "fasting_glucose": None, "hba1c": None, "spo2": 94, "temperature": 37.1,
    },
    "labs": {
        "albumin": 28.0, "hemoglobin": 102, "creatinine": 95,
        "egfr": 62, "potassium": 3.6, "uric_acid": None,
    },
    "allergies": [],
    "fall_history": "完全不适用（长期卧床）",

    "adl_scores": {
        "feeding": 0, "bathing": 0, "grooming": 0, "dressing": 0,
        "bowels": 0, "bladder": 0, "toilet_use": 0,
        "transfers": 0, "mobility": 0, "stairs": 0,
    },
    "morse_score": None,  # 完全卧床不适用
    "braden_score": 9,
    "mobility_note": "完全卧床，无法自主翻身，右侧肢体偏瘫挛缩，左侧肢体偶有无目的性活动",
    "has_catheter": True,
    "has_ng_tube": True,

    "gds_score": None,  # 无法评估（重度痴呆）
    "mmse_score": None,  # 不可测（重度痴呆）
    "social_activities": "无法参与任何活动。照护者的日常护理是他唯一的人际接触。",
    "family_visit_frequency": "女儿每周六下午来1次（约1小时），坐在床边握着老人的手说话，但老人无回应。",
    "family_relationship": "女儿非常孝顺但内心痛苦——'爸爸已经不认得我了，我不知道我来还有什么意义'",
    "life_story": "退休前是中学历史教师，喜欢京剧和养花。患病前性格开朗健谈。女儿是他唯一的亲人（妻子已故12年）。女儿保留着他年轻时长衫拉京胡的照片。",

    "height_cm": 172,
    "weight_kg": 48.0,
    "weight_change_1m": -2.0,
    "swallowing_test": "5级（完全不能吞咽，已置鼻饲管）",
    "dental_status": "全口义齿（已取下，卧床不佩戴）",
    "dietary_restrictions": ["鼻饲流质", "高蛋白", "糖尿病饮食(已置鼻饲暂不适用)"],
}

# ════════════════════════════════════════════════════════════
# 模拟评估输出
# ════════════════════════════════════════════════════════════

SIM_MEDICAL = {
    "chronic_disease_assessment": [
        {
            "disease": "重度阿尔茨海默病（CDR3级）",
            "control_rating": "未控制",
            "evidence": "疾病已进展至终末期，完全丧失认知和沟通能力。多奈哌齐+美金刚的获益在CDR3阶段有限，但停药可能加速衰退。",
            "risk_trend": "缓慢恶化",
        },
        {
            "disease": "高血压3级",
            "control_rating": "尚可",
            "evidence": "氨氯地平控制下血压142/80mmHg，可接受（高龄+卧床目标<150/90）",
            "risk_trend": "稳定",
        },
        {
            "disease": "吸入性肺炎（反复发作）",
            "control_rating": "欠佳",
            "evidence": "近1年发作2次住院，虽已置鼻饲管减少了经口进食的误吸，但口腔分泌物和胃食管反流仍是感染源",
            "risk_trend": "周期性恶化",
        },
        {
            "disease": "低蛋白血症+贫血",
            "control_rating": "欠佳",
            "evidence": "白蛋白28g/L（<30为低蛋白血症），血红蛋白102g/L（轻度贫血），体重持续下降2kg/月",
            "risk_trend": "恶化",
        },
    ],
    "drug_interactions": [
        {
            "severity": "中",
            "drugs_involved": ["劳拉西泮", "多奈哌齐"],
            "mechanism": "苯二氮䓬类药物的中枢抑制作用可能拮抗胆碱酯酶抑制剂（多奈哌齐）的促认知效果，且两者均有镇静作用，可能增加吸入性肺炎风险（过度镇静→分泌物清除减弱）",
            "clinical_consequence": "认知改善效果被部分抵消，过度镇静可能增加误吸风险",
            "recommendation": "劳拉西泮仅在明确烦躁时使用（prn），避免常规使用。考虑替代为非药物安抚方法（如音乐、触觉刺激）。",
        },
        {
            "severity": "低",
            "drugs_involved": ["氯吡格雷", "奥美拉唑"],
            "mechanism": "奥美拉唑（CYP2C19抑制剂）可能减弱氯吡格雷（经CYP2C19活化）的抗血小板效果",
            "clinical_consequence": "理论上可能降低氯吡格雷疗效，但临床争议较大",
            "recommendation": "可考虑换用对CYP2C19影响较小的泮托拉唑（40mg qd），或继续当前方案但密切观察。",
        },
    ],
    "acute_risk_assessment": [
        {
            "risk_type": "感染（吸入性肺炎+尿路感染）",
            "probability": "高",
            "trigger_factors": ["长期卧床分泌物清除差", "留置导尿管", "低蛋白血症→免疫力下降", "口腔细菌定植"],
            "preventive_measures": ["严格口腔护理Q4H", "鼻饲时床头抬高30-45°", "导尿管护理+评估拔管时机", "肺炎球菌疫苗接种", "监测CRP/PCT每周"],
        },
        {
            "risk_type": "营养不良-感染恶性循环",
            "probability": "高",
            "trigger_factors": ["低蛋白血症(28g/L)→免疫力下降→感染→消耗→更低的蛋白→更易感染"],
            "preventive_measures": ["优化肠内营养方案（高热高蛋白）", "短期肠外营养补充评估", "每周监测白蛋白和前白蛋白"],
        },
    ],
    "medical_recommendations": [
        {
            "priority": "紧急",
            "category": "用药调整",
            "content": "评估劳拉西泮使用频率——如近1周使用>3次，应制定非药物安抚方案（音乐疗法、触觉刺激、芳香疗法）减少镇静药物依赖",
            "rationale": "劳拉西泮的镇静作用在吞咽反射消失的卧床老人中可能增加吸入风险，且与多奈哌齐存在药效拮抗",
        },
        {
            "priority": "紧急",
            "category": "检查",
            "content": "查前白蛋白（反映近3天蛋白摄入）+ CRP（炎症指标），评估是否存在潜在的亚临床感染消耗",
            "rationale": "白蛋白28g/L+体重骤降2kg/月，需区分是'摄入不足'还是'感染消耗'，两者处理策略不同",
        },
        {
            "priority": "持续执行",
            "category": "监测",
            "content": "每周监测体温、CRP、前白蛋白。每2周复查白蛋白。如CRP持续升高即使无发热也应排查隐性感染灶。",
            "rationale": "卧床老人的感染可'无声'进展——老人无法表达不适，只能靠化验指标做哨兵",
        },
    ],
    "summary": "终末期阿尔茨海默病+吸入性肺炎反复+低蛋白血症。最紧急的不是认知药物调整，而是阻断'营养不良→感染→更差营养'的恶性循环。",
}

SIM_NURSING = {
    "adl_assessment": {
        "barthel_total": 0,
        "dependency_level": "完全依赖",
        "strengths": [],
        "deficits": ["全部10项Barthel项目均完全依赖（0分）"],
        "assistance_required": "所有日常生活活动均100%依赖照护者：鼻饲喂养、完全被动翻身、留置导尿护理、口腔护理、皮肤护理、床上擦浴",
    },
    "fall_risk": {
        "morse_score": 0,
        "risk_level": "不适用",
        "key_risk_factors": ["不适用（完全卧床）"],
        "environmental_risks": [],
    },
    "pressure_ulcer_risk": {
        "braden_score": 9,
        "risk_level": "极高风险",
        "weakest_dimension": "活动能力（完全无法自主活动）和移动能力（完全无法改变体位）",
        "current_ulcers": "骶尾部1期压疮（非苍白性红斑，面积3×4cm），双侧足跟皮肤发红",
    },
    "recommended_care_level": 5,
    "nursing_recommendations": [
        {
            "priority": "紧急",
            "category": "体位管理",
            "content": "严格Q2H翻身计划（左右侧卧+平卧交替），使用30°侧卧体位减少骶尾压力。每次翻身前5分钟给予被动关节活动（踝泵+膝屈伸+肩关节），减轻翻身时的僵硬和疼痛。",
            "frequency": "每2小时1次（含夜间），24小时内12次",
            "rationale": "Braden 9分+骶尾部已有1期压疮，如不严格控制，进展为2期→3期→深部组织感染只是时间问题。Q2H翻身是压疮预防的基石，无任何替代方案。",
        },
        {
            "priority": "紧急",
            "category": "皮肤护理",
            "content": "使用高规格交替压力气垫床（动态减压）。骶尾部1期压疮处贴水胶体敷料保护，禁止按摩（1期压疮按摩反而加重微循环损伤）。每日评估压疮进展（拍照记录）。",
            "frequency": "持续使用气垫床+每日评估",
            "rationale": "1期压疮是可逆的最后时机——进入2期后愈合困难且容易感染，保护措施必须立即升级",
        },
        {
            "priority": "紧急",
            "category": "其他",
            "content": "口腔护理升级：每4小时用氯己定漱口液+软海绵刷清洁口腔和舌面。鼻饲前检查胃残留量（>150ml暂停喂养），鼻饲时和鼻饲后1小时床头抬高30-45°。",
            "frequency": "Q4H口腔护理+每次鼻饲前后检查",
            "rationale": "口腔细菌是吸入性肺炎的主要病原来源。严格口腔护理可降低吸入性肺炎发生率40-60%。配合体位管理，双管齐下防肺炎。",
        },
        {
            "priority": "本周内",
            "category": "排泄护理",
            "content": "评估拔除留置导尿管的可行性——长期留置是尿路感染和菌血症的持续风险源。如无法拔除，改用间歇导尿（Q6H）或使用硅胶尿管（降低生物膜形成）+严格无菌护理。",
            "frequency": "一次性评估+持续护理",
            "rationale": "留置导尿管超过30天，菌尿发生率接近100%。间歇导尿可显著降低UTI发生率但需要更多人力。",
        },
        {
            "priority": "持续执行",
            "category": "其他",
            "content": "每日床上被动全关节活动（ROM exercise）30分钟，预防关节挛缩加重和深静脉血栓。操作时观察面部表情（唯一疼痛信号来源）。",
            "frequency": "每日1次",
            "rationale": "长期不动→关节挛缩+肌腱缩短→翻身时剧痛→护理困难→护理质量下降。被动ROM是维持护理可行性的基础。",
        },
    ],
    "summary": "完全依赖(Barthel 0)+Braden 9极高危+骶尾部已有1期压疮+吸入性肺炎高风险。建议最高照护等级(5级)，护理强度需1:1.5(一个护理员最多管1.5个此类老人)。Q2H翻身+气垫床+口腔护理是三条生命线。",
}

SIM_SOCIAL = {
    "mental_health": {
        "gds_score": None,
        "depression_risk": "无法评估（重度痴呆）",
        "anxiety_level": "无法评估，但观察到烦躁行为（可能反映不适或疼痛）",
        "emotional_state": "老人无法用语言表达情绪。照护者观察到：女儿探视时握着他的手说话，他的呼吸会变平稳，手指偶有轻微回握动作。播放京剧时有短暂的'安静倾听'状态——这可能是他仅存的情感连接方式。",
        "key_concerns": ["无法表达疼痛和不适（照护者需高度依赖非语言信号）", "感官剥夺风险（长期卧床+无交流+无活动）"],
    },
    "social_engagement": {
        "activity_participation": "不适用",
        "peer_relationship": "不适用",
        "social_isolation_risk": "极高——唯一的'社交'来自护理操作和女儿每周1次探视",
        "recommended_activities": [
            "感官刺激活动：播放京剧录音（他年轻时的最爱）",
            "触觉连接：女儿探视时引导手部按摩（不仅是握手）",
            "气味记忆：他以前养花的植物气味（茉莉、米兰花香包放枕边）",
        ],
    },
    "family_support": {
        "visit_frequency": "女儿每周六下午1小时",
        "relationship_quality": "极深的情感连接，但女儿因'爸爸不认得我'而痛苦",
        "caregiver_burden": "女儿存在中度'预期性悲伤'(anticipatory grief)和'模糊性丧失'(ambiguous loss)——父亲身体还在但'人'已经走了",
        "support_gaps": ["女儿需要哀伤辅导和心理支持", "女儿不知道如何与失智末期父亲'有意义地相处'", "缺乏对家属的临终关怀教育"],
    },
    "cognitive_status": {
        "mmse_score": None,
        "cognitive_level": "重度认知障碍（CDR3期）",
        "preserved_abilities": ["对熟悉声音（女儿/京剧）仍有生理层面的反应", "触觉感知可能部分保留"],
        "declined_areas": ["语言", "记忆", "定向力", "判断力", "执行功能全部丧失"],
        "communication_ability": "无语言沟通能力。唯一交流渠道：观察面部表情、呼吸节律、肌肉张力变化、对特定刺激（音乐/触摸/熟悉声音）的生理反应。",
    },
    "social_recommendations": [
        {
            "priority": "紧急",
            "category": "家属沟通",
            "content": "为女儿提供1次'有意义的告别'辅导：①解释父亲仍保留感官层面的情感接收能力（即使认知层面无法理解）②教她如何通过触摸+声音+气味与父亲'对话'——'他可能不认得你是谁，但他的身体认得你的温度'",
            "rationale": "女儿的'模糊性丧失'痛苦是当前家庭支持的核心问题。赋权她找到新的'有意义相处'方式，可以将痛苦的探视转变为珍贵的告别时光。",
        },
        {
            "priority": "本周内",
            "category": "精神关怀",
            "content": "为老人创建'感官地图'：①每天固定时段播放京剧录音（根据女儿提供的信息选择他最喜欢的唱段）②枕边放置茉莉花香包 ③护理操作时播放女儿录制的音频（'爸，我来给你翻个身，很快就好'）",
            "rationale": "对于失智末期老人，感官刺激是最后的沟通桥梁。这不仅是'舒适护理'，更是对老人主体性和生命的尊重——即使他无法说谢谢，我们仍然把他当作一个完整的、有偏好的人来对待。",
        },
        {
            "priority": "持续执行",
            "category": "家属沟通",
            "content": "每周为女儿生成一段'非语言照护叙事'——不写'今日体温正常'，而是记录'今天播放京剧《空城计》时，他的呼吸变得更平稳了。你的照片放在他枕头右边，护理员说他有时会朝那个方向转头。'",
            "rationale": "CareMind反客体化实践的核心：让家属看到'人'而不是'数据'。在终末期照护中，这种叙事是给生者的礼物。",
        },
    ],
    "narrative_for_family": "今天下午阳光从窗帘缝隙里漏进来，正落在张老师的枕边。护理员放了一段《空城计》——他突然安静了，平时无意识摆动的左手停了下来。我们觉得他在'听'。虽然他说不出来，但京剧是他的语言。你的声音也是。上周六你走后，他的右手食指还轻轻勾着——那个动作保持了快1分钟。他不认识'女儿'这个词了，但他的身体还记得'温暖'的感觉。",
    "summary": "社工维度在终末期照护中的角色转换：从'促进社会参与'转向'守护生命尊严+赋能家属告别'。核心是通过感官连接和非语言叙事对抗'客体化'——他是人，不是护理清单上的Barthel 0分。",
}

SIM_DIETARY = {
    "nutrition_status": {
        "bmi": 16.2,
        "albumin": 28.0,
        "hemoglobin": 102,
        "weight_trend": "下降",
        "nutrition_rating": "重度不良",
        "key_deficits": ["BMI 16.2重度消瘦", "白蛋白28g/L低蛋白血症", "轻度贫血", "体重每月下降2kg(4.2%)", "常规肠内营养方案不足以逆转消耗"],
    },
    "swallow_function": {
        "test_result": "5级（完全不能吞咽）",
        "swallow_safety": "需鼻饲",
        "recommended_texture": "鼻饲",
    },
    "dietary_plan": {
        "dietary_type": "高热高蛋白肠内营养（鼻饲持续滴注）",
        "daily_calories_kcal": 2000,
        "daily_protein_g": 75,
        "restrictions": ["鼻饲途径", "需监测胃残留量", "床头抬高30-45°预防反流误吸"],
        "forbidden_foods": ["经口食物（完全禁忌）", "高渗空肠营养液（可能致腹泻）"],
        "recommended_foods": [
            "高蛋白肠内营养制剂（如 Ensure HP 或同类，1.5kcal/ml）",
            "可联合短肽型制剂提高蛋白吸收率",
            "必要时联合肠外营养(PN)短期补充",
        ],
    },
    "dietary_recommendations": [
        {
            "priority": "紧急",
            "category": "营养补充",
            "content": "将当前肠内营养方案升级为高热高蛋白配方（1.5kcal/ml, ≥20%蛋白供能比）。目标2000kcal/日+75g蛋白/日。若鼻饲耐受不良（胃残留>150ml），改用持续滴注泵（16-20小时慢速泵入）替代间歇推注。",
            "rationale": "当前体重48kg、每月下降2kg(4.2%)远超警戒线(>2%需干预)。低蛋白血症(28g/L)是感染易感性和压疮不愈合的独立危险因素。营养是压疮愈合的'原材料'——没有营养，Q2H翻身也难逆转压疮进程。",
        },
        {
            "priority": "本周内",
            "category": "会诊",
            "content": "请临床营养科会诊，评估联合肠外营养(PN)的指征——若1周内前白蛋白无改善或体重继续下降，应启动短期PN补充（经外周静脉，每日额外500kcal+25g蛋白）。",
            "rationale": "重度营养不良+高消耗状态（可能亚临床感染）下，单纯肠内营养可能需要2-3周才能逆转负氮平衡。PN可作为'桥梁'加速营养重建。",
        },
        {
            "priority": "持续执行",
            "category": "监测",
            "content": "每周称重1次+每3天查前白蛋白（床旁快速检测）+每周查白蛋白/CRP。目标：2周内体重下降速度从-2kg/月减至<0.5kg/月，4周内白蛋白回升至>32g/L。",
            "rationale": "营养干预效果的反馈周期短（前白蛋白半衰期仅2天），需频繁监测动态调整方案",
        },
    ],
    "summary": "重度营养不良(BMI 16.2+白蛋白28+月降2kg)+完全鼻饲依赖。需紧急升级肠内营养方案+评估肠外营养补充。营养是压疮愈合和感染预防的物质基础。",
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
            "category": "护理",
            "priority": "紧急",
            "content": "【压疮防控生命线】严格Q2H翻身（含夜间），30°侧卧体位。使用交替压力气垫床。骶尾部1期压疮贴水胶体敷料，禁止按摩。每日拍照记录压疮进展。",
            "source_agent": "nursing",
            "human_resources": "护理员1:1.5配比（Q2H×24h=12次翻身/日，每次2人操作）",
            "equipment": "高规格气垫床+水胶体敷料+翻身枕×2",
            "estimated_cost": "中（气垫床约2000-5000元，水胶体敷料约30元/片×每周3片）",
        },
        {
            "intervention_id": "INT-002",
            "category": "护理",
            "priority": "紧急",
            "content": "【肺炎预防双保险】①口腔护理Q4H（氯己定+软海绵刷）②鼻饲时和鼻饲后1h床头抬高30-45°③每次鼻饲前查胃残留（>150ml暂停）④使用持续滴注泵替代间歇推注。",
            "source_agent": "nursing",
            "human_resources": "护理员执行Q4H口腔护理+每餐前后体位管理",
            "equipment": "氯己定漱口液+软海绵刷+肠内营养泵",
            "estimated_cost": "低（营养泵约1000元一次性+耗材）",
        },
        {
            "intervention_id": "INT-003",
            "category": "餐饮",
            "priority": "紧急",
            "content": "升级肠内营养：高热高蛋白配方（2000kcal+75g蛋白/日），持续滴注泵16-20h慢速泵入。1周后若前白蛋白无改善→启动联合肠外营养(PN)。",
            "source_agent": "dietary",
            "human_resources": "营养师制定方案+护士执行",
            "equipment": "肠内营养泵+高蛋白制剂",
            "estimated_cost": "中（制剂约40-60元/日+PN若启动约200元/日）",
        },
        {
            "intervention_id": "INT-004",
            "category": "医疗",
            "priority": "紧急",
            "content": "查前白蛋白+CRP，区分'摄入不足'与'感染消耗'。评估劳拉西泮使用频率——若>3次/周，制定非药物安抚替代方案。",
            "source_agent": "medical",
            "human_resources": "医生+检验科",
            "equipment": "床旁快速检测仪或外送检验",
            "estimated_cost": "低（检验约100元）",
        },
        {
            "intervention_id": "INT-005",
            "category": "社工",
            "priority": "紧急",
            "content": "为女儿提供'有意义告别'辅导：解释感官层面的情感连接仍然存在，教她通过触摸+声音+气味与父亲互动。这不是'无用功'——老人在生理层面接收着这一切。",
            "source_agent": "social",
            "human_resources": "社工1名",
            "equipment": "无",
            "estimated_cost": "无",
        },
        {
            "intervention_id": "INT-006",
            "category": "护理",
            "priority": "本周内",
            "content": "评估拔除留置导尿管→间歇导尿(Q6H)或更换硅胶尿管。每日会阴护理2次，监测尿液性状。",
            "source_agent": "nursing",
            "human_resources": "护理员执行+护士评估",
            "equipment": "硅胶导尿管或间歇导尿管",
            "estimated_cost": "低",
        },
        {
            "intervention_id": "INT-007",
            "category": "社工",
            "priority": "本周内",
            "content": "创建老人的'感官地图'：①每日固定时段播放京剧唱段②枕边茉莉花香包③护理操作时播放女儿录制的音频④女儿探视时引导手部按摩而非仅握手。",
            "source_agent": "social",
            "human_resources": "社工+护理员配合",
            "equipment": "蓝牙小音箱+香包+手机录音",
            "estimated_cost": "无",
        },
        {
            "intervention_id": "INT-008",
            "category": "护理",
            "priority": "持续执行",
            "content": "每日床上被动全关节ROM exercise 30分钟，注意观察面部表情识别疼痛。",
            "source_agent": "nursing",
            "human_resources": "护理员或康复师1名",
            "equipment": "无",
            "estimated_cost": "无",
        },
        {
            "intervention_id": "INT-009",
            "category": "医疗",
            "priority": "持续执行",
            "content": "每周监测CRP+前白蛋白，每2周查白蛋白。CRP持续升高即使无发热也需排查隐性感染（肺炎、UTI、压疮感染）。",
            "source_agent": "medical",
            "human_resources": "护士采血",
            "equipment": "检验耗材",
            "estimated_cost": "低（约50-100元/周）",
        },
        {
            "intervention_id": "INT-010",
            "category": "社工",
            "priority": "持续执行",
            "content": "每周为女儿生成'非语言照护叙事'——记录老人对感官刺激的反应（呼吸变化、手指动作、表情变化），用有温度的叙事替代冰冷的指标。",
            "source_agent": "social",
            "human_resources": "护理员观察+社工撰写",
            "equipment": "无",
            "estimated_cost": "无",
        },
    ],

    "conflict_resolutions": [
        {
            "conflict_id": "CON-R1",
            "agents_involved": ["nursing", "medical"],
            "description": "护理Agent要求Q2H翻身（含夜间），但医疗Agent提示翻身可能因关节挛缩引起疼痛→老人烦躁→需劳拉西泮镇静→镇静增加误吸风险",
            "resolution": "翻身前5分钟给予被动关节活动（减轻僵硬），翻身时两人操作减少牵拉。如确实因疼痛烦躁，优先使用非药物干预（播放女儿录音+轻柔触摸），劳拉西泮仅作为最后手段且仅用0.25mg（半量）。Q2H翻身不可妥协——压疮一旦恶化对终末期老人是灾难性的。",
            "resolution_rule": "safety_first",
        },
        {
            "conflict_id": "CON-R2",
            "agents_involved": ["dietary", "medical"],
            "description": "餐饮Agent建议2000kcal+75g蛋白（高负荷），但医疗Agent指出老人有吸入性肺炎史+胃残留风险——高容量喂养可能增加反流和误吸",
            "resolution": "采用持续滴注泵替代间歇推注——将2000ml/日营养液在16-20小时内匀速泵入，降低单位时间胃内容积。同时严格执行床头抬高+每4小时测胃残留。营养目标不变，但通过改变给予方式保障安全。",
            "resolution_rule": "compromise",
        },
    ],

    "risk_heatmap": [
        {"dimension": "护理", "risk_level": "极高"},
        {"dimension": "餐饮", "risk_level": "极高"},
        {"dimension": "医疗", "risk_level": "高"},
        {"dimension": "社工", "risk_level": "中"},
    ],
    "overall_priority": "护理主导型",
    "summary": "张爷爷是典型的终末期照护案例——Barthel 0分完全依赖+Braden 9分极高危+低蛋白血症+反复吸入性肺炎。护理维度是绝对主战场：Q2H翻身+口腔护理+气垫床是维持生命的底线。餐饮维度紧随其后——没有营养支持，压疮不会愈合、感染无法抵抗。但CareMind的价值不止于'维持生命'：社工维度通过感官地图和非语言叙事，让这位重度失智老人仍然被当作一个有喜好、有故事、有尊严的'人'来对待。这是'反客体化'理念在终末期照护中的实践——即使Barthel是0分，人的价值不是0分。",
}

# ════════════════════════════════════════════════════════════
# 决策审核层模拟输出
# ════════════════════════════════════════════════════════════

SIM_DECISION = {
    "verdict": "PASS",
    "rationality_audit": {
        "passed": True,
        "score": 95,
        "notes": [
            "终末期照护的四大支柱全部到位：压疮防控、肺炎预防、营养支持、家属赋能",
            "干预粒度优秀：Q2H翻身具体到体位角度(30°)、口腔护理具体到频率(Q4H)和用品(氯己定+软海绵刷)",
            "特别值得肯定的是社工维度的'感官地图'和'非语言叙事'——这是绝大多数养老院完全忽视的维度",
            "排序正确：压疮+肺炎+营养构成'生命支持三角'，社工维度的家属辅导同步进行不延迟",
        ],
    },
    "safety_audit": {
        "passed": True,
        "score": 91,
        "notes": [
            "Q2H翻身+气垫床+水胶体敷料方案符合国际压疮预防指南（NPUAP/EPUAP）",
            "持续滴注泵替代间歇推注有效降低了反流误吸风险",
            "劳拉西泮限制使用+非药物安抚替代方案合理",
            "注意：2000kcal/日对48kg卧床老人偏高——建议从1600kcal/日开始，3-5天内逐步上调至2000kcal，监测胃肠道耐受性",
        ],
    },
    "feasibility_audit": {
        "passed": True,
        "score": 75,
        "notes": [
            "Q2H翻身×12次/日，每次需2人操作——需1:1.5的护理配比，这对多数养老院是人力挑战。建议：评估夜间是否可以延长至Q3H（00:00-06:00），但需配合高规格气垫床动态减压。",
            "持续滴注泵+肠内营养泵需设备投入（约1000-3000元），但属于一次性投入+长期使用",
            "社工每周撰写'非语言叙事报告'需要额外10-15分钟，但价值远超成本——建议将此项作为CareMind的特色卖点而非负担",
            "联合PN（肠外营养）若启动需外周静脉通路+每日输注，人力成本进一步增加——建议仅在肠内营养方案2周无效后启动",
        ],
    },
    "revision_notes": [
        {
            "target_intervention_id": "INT-003",
            "issue": "2000kcal/日对48kg卧床老人的起始剂量偏高，可能引起胃肠道不耐受（腹泻、胃残留增加）",
            "suggested_change": "从1600kcal/日开始，3-5天内逐步上调至2000kcal/日。同时监测每日胃残留量和排便情况，如出现腹泻则调整为短肽型制剂。",
        },
    ],
    "final_care_plan": SIM_ORCHESTRATOR["unified_care_plan"],
    # 注：实际使用时，INT-003应按revision_notes修改后重新输出。此处为模拟保持简洁。

    "risk_alerts": [
        "🚨 骶尾部1期压疮是'最后防线'——如1周内进展为2期（水疱或破溃），愈合时间将从数天变为数月，且感染风险剧增。Q2H翻身无任何妥协余地。",
        "🚨 低蛋白血症(28g/L)+CRP未知——如CRP显著升高，提示存在隐性感染，必须在使用抗生素的同时加强营养（否则感染-消耗恶性循环无法打破）。",
        "⚠️ 劳拉西泮如使用>3次/周提示疼痛或不适管理不足——需优先排查可逆原因（便秘、尿潴留、压疮疼痛、体位不适）而非直接镇静。",
        "⚠️ 女儿存在中度'预期性悲伤'，建议社工做1次正式哀伤辅导评估，必要时转介心理咨询。",
    ],
    "executive_summary": "张爷爷（89岁，重度失智+完全卧床）的照护核心是'生命支持+尊严维护'双轨并行。生命支持轨道：Q2H翻身+气垫床防压疮恶化、Q4H口腔护理+鼻饲体位管理防吸入性肺炎、升级肠内营养方案打破'营养不良→感染→更差营养'的恶性循环。尊严维护轨道：通过感官地图（京剧+茉莉花香+女儿录音）和非语言照护叙事，让这位无法交流的老人仍然被当作'人'来对待——这是CareMind区别于传统养老管理系统的核心价值。护理强度建议1:1.5配比，照护等级5级（最高）。人力成本虽高，但远低于一次吸入性肺炎住院的费用（约1.5-3万元）和一个3期压疮的治疗费用（约2-5万元）。",
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
