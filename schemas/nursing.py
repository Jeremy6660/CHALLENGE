# -*- coding: utf-8 -*-
"""护理评估Agent的输入输出模型"""

from pydantic import BaseModel, Field
from typing import Optional


class ADLAssessment(BaseModel):
    barthel_total: int = Field(..., description="Barthel总分")
    dependency_level: str = Field(..., description="依赖等级: 自理/轻度依赖/中度依赖/重度依赖/完全依赖")
    strengths: list[str] = Field(default_factory=list, description="自理优势项")
    deficits: list[str] = Field(default_factory=list, description="主要功能缺陷")
    assistance_required: str = Field(..., description="所需辅助程度描述")


class FallRiskAssessment(BaseModel):
    morse_score: int = Field(..., description="Morse评分")
    risk_level: str = Field(..., description="风险等级: 无风险/低风险/中风险/高风险")
    key_risk_factors: list[str] = Field(default_factory=list, description="主要风险因素")
    environmental_risks: list[str] = Field(default_factory=list, description="环境风险因素")


class PressureUlcerRisk(BaseModel):
    braden_score: int = Field(..., description="Braden评分")
    risk_level: str = Field(..., description="风险等级: 无风险/低风险/中风险/高风险/极高风险")
    weakest_dimension: str = Field(..., description="最薄弱维度")
    current_ulcers: Optional[str] = Field(None, description="现有压疮描述")


class NursingRecommendation(BaseModel):
    priority: str = Field(..., description="优先级: 紧急/本周内/持续执行")
    category: str = Field(..., description="类别: 体位管理/皮肤护理/排泄护理/活动训练/安全防护/其他")
    content: str = Field(..., description="具体护理措施")
    frequency: Optional[str] = Field(None, description="执行频率")
    rationale: str = Field(..., description="理由")


class NursingAssessmentOutput(BaseModel):
    """护理评估Agent的结构化输出"""
    adl_assessment: ADLAssessment = Field(..., description="ADL评估")
    fall_risk: FallRiskAssessment = Field(..., description="跌倒风险评估")
    pressure_ulcer_risk: PressureUlcerRisk = Field(..., description="压疮风险评估")
    recommended_care_level: int = Field(..., ge=1, le=5, description="建议照护等级(1-5)")
    nursing_recommendations: list[NursingRecommendation] = Field(
        default_factory=list, description="护理干预建议"
    )
    summary: str = Field("", description="护理维度一句话总结")
