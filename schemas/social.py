# -*- coding: utf-8 -*-
"""社工评估Agent的输入输出模型"""

from pydantic import BaseModel, Field
from typing import Optional


class MentalHealthAssessment(BaseModel):
    gds_score: Optional[int] = Field(None, description="GDS-15评分")
    depression_risk: str = Field(..., description="抑郁风险: 无/轻度/中度/重度")
    anxiety_level: Optional[str] = Field(None, description="焦虑程度")
    emotional_state: str = Field(..., description="情绪状态描述")
    key_concerns: list[str] = Field(default_factory=list, description="主要心理问题")


class SocialEngagement(BaseModel):
    activity_participation: str = Field(..., description="活动参与度: 活跃/一般/偏低/几乎不参与")
    peer_relationship: str = Field(..., description="同伴关系质量")
    social_isolation_risk: str = Field(..., description="社会隔离风险: 高/中/低")
    recommended_activities: list[str] = Field(default_factory=list, description="推荐活动")


class FamilySupport(BaseModel):
    visit_frequency: Optional[str] = Field(None, description="探视频率")
    relationship_quality: str = Field(..., description="家庭关系质量")
    caregiver_burden: Optional[str] = Field(None, description="主要照护者负担评估")
    support_gaps: list[str] = Field(default_factory=list, description="家庭支持缺口")


class CognitiveStatus(BaseModel):
    mmse_score: Optional[int] = Field(None, description="MMSE评分")
    cognitive_level: str = Field(..., description="认知功能水平")
    preserved_abilities: list[str] = Field(default_factory=list, description="保留的认知能力")
    declined_areas: list[str] = Field(default_factory=list, description="下降的认知领域")
    communication_ability: str = Field(..., description="沟通能力评估")


class SocialRecommendation(BaseModel):
    priority: str = Field(..., description="优先级: 紧急/本周内/持续执行")
    category: str = Field(..., description="类别: 心理支持/社会参与/家属沟通/认知训练/资源链接/精神关怀")
    content: str = Field(..., description="具体建议")
    rationale: str = Field(..., description="理由")


class SocialAssessmentOutput(BaseModel):
    """社工评估Agent的结构化输出"""
    mental_health: MentalHealthAssessment = Field(..., description="心理健康评估")
    social_engagement: SocialEngagement = Field(..., description="社会参与评估")
    family_support: FamilySupport = Field(..., description="家庭支持评估")
    cognitive_status: CognitiveStatus = Field(..., description="认知状态评估")
    social_recommendations: list[SocialRecommendation] = Field(
        default_factory=list, description="社工干预建议"
    )
    narrative_for_family: Optional[str] = Field(None, description="给家属的情感叙事段落")
    summary: str = Field("", description="社工维度一句话总结")
