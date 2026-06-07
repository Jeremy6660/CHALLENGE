# -*- coding: utf-8 -*-
"""编排层Agent的输入输出模型"""

from pydantic import BaseModel, Field
from typing import Optional
from .medical import MedicalAssessmentOutput
from .nursing import NursingAssessmentOutput
from .social import SocialAssessmentOutput
from .dietary import DietaryAssessmentOutput


class ConflictItem(BaseModel):
    """跨域冲突记录"""
    conflict_id: str = Field(..., description="冲突编号")
    agents_involved: list[str] = Field(..., description="涉及的Agent")
    description: str = Field(..., description="冲突描述")
    resolution: str = Field(..., description="消解方案")
    resolution_rule: str = Field(..., description="使用的消解规则")


class UnifiedIntervention(BaseModel):
    """统一干预项"""
    intervention_id: str = Field(..., description="干预编号")
    category: str = Field(..., description="所属维度: 医疗/护理/社工/餐饮")
    priority: str = Field(..., description="优先级: 紧急/本周内/持续执行")
    content: str = Field(..., description="干预内容")
    source_agent: str = Field(..., description="来源Agent")
    human_resources: Optional[str] = Field(None, description="所需人力资源")
    equipment: Optional[str] = Field(None, description="所需设备/物资")
    estimated_cost: Optional[str] = Field(None, description="预估费用级别: 无/低/中/高")


class RiskHeatmapItem(BaseModel):
    """风险热力图单项"""
    dimension: str = Field(..., description="维度")
    risk_level: str = Field(..., description="风险等级: 低/中/高/极高")


class OrchestratorOutput(BaseModel):
    """编排层Agent的结构化输出"""
    # 四份原始评估的引用
    medical_assessment: MedicalAssessmentOutput
    nursing_assessment: NursingAssessmentOutput
    social_assessment: SocialAssessmentOutput
    dietary_assessment: DietaryAssessmentOutput

    # 综合产物
    unified_care_plan: list[UnifiedIntervention] = Field(
        default_factory=list, description="统一干预计划"
    )
    conflict_resolutions: list[ConflictItem] = Field(
        default_factory=list, description="冲突消解记录"
    )
    risk_heatmap: list[RiskHeatmapItem] = Field(
        default_factory=list, description="综合风险热力图"
    )
    overall_priority: str = Field(..., description="综合优先级评估: 医疗主导型/护理主导型/社工主导型/均衡型")
    summary: str = Field("", description="综合评估总结")
