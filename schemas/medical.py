# -*- coding: utf-8 -*-
"""医疗评估Agent的输入输出模型"""

from pydantic import BaseModel, Field
from typing import Optional


class ChronicDiseaseItem(BaseModel):
    disease: str = Field(..., description="疾病名称")
    control_rating: str = Field(..., description="控制评级: 良好/尚可/欠佳/未控制")
    evidence: str = Field(..., description="评级依据")
    risk_trend: str = Field(..., description="风险趋势: 稳定/好转/恶化")


class DrugInteraction(BaseModel):
    severity: str = Field(..., description="严重程度: 高/中/低")
    drugs_involved: list[str] = Field(..., description="涉及药物")
    mechanism: str = Field(..., description="相互作用机制")
    clinical_consequence: str = Field(..., description="可能的临床后果")
    recommendation: str = Field(..., description="处理建议")


class AcuteRisk(BaseModel):
    risk_type: str = Field(..., description="风险类型: 跌倒/心梗/脑卒中/低血糖/感染/其他")
    probability: str = Field(..., description="概率评估: 高/中/低")
    trigger_factors: list[str] = Field(default_factory=list, description="诱发因素")
    preventive_measures: list[str] = Field(default_factory=list, description="预防措施")


class MedicalRecommendation(BaseModel):
    priority: str = Field(..., description="优先级: 紧急/本周内/持续执行")
    category: str = Field(..., description="类别: 用药调整/检查/会诊/转诊/监测/其他")
    content: str = Field(..., description="具体建议内容")
    rationale: str = Field(..., description="建议理由")


class MedicalAssessmentOutput(BaseModel):
    """医疗评估Agent的结构化输出"""
    chronic_disease_assessment: list[ChronicDiseaseItem] = Field(
        default_factory=list, description="慢病管理评估"
    )
    drug_interactions: list[DrugInteraction] = Field(
        default_factory=list, description="药物相互作用检测结果"
    )
    acute_risk_assessment: list[AcuteRisk] = Field(
        default_factory=list, description="急性风险评估"
    )
    medical_recommendations: list[MedicalRecommendation] = Field(
        default_factory=list, description="医疗干预建议(按优先级排序)"
    )
    summary: str = Field("", description="医疗维度一句话总结")
