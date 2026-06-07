# -*- coding: utf-8 -*-
"""决策审核Agent的输入输出模型"""

from pydantic import BaseModel, Field
from typing import Optional
from .orchestration import OrchestratorOutput, UnifiedIntervention


class AuditDimension(BaseModel):
    """单一审核维度"""
    passed: bool = Field(..., description="是否通过")
    score: int = Field(..., ge=0, le=100, description="评分")
    notes: list[str] = Field(default_factory=list, description="评语")


class RevisionNote(BaseModel):
    """修改建议"""
    target_intervention_id: Optional[str] = Field(None, description="针对的干预项ID")
    issue: str = Field(..., description="问题描述")
    suggested_change: str = Field(..., description="建议修改")


class DecisionOutput(BaseModel):
    """决策审核Agent的结构化输出"""
    verdict: str = Field(..., description="审核结论: PASS/REVISE/REJECT")

    # 三维审核
    rationality_audit: AuditDimension = Field(..., description="合理性审核(是否覆盖关键风险点)")
    safety_audit: AuditDimension = Field(..., description="安全性审核(干预与用药/疾病是否有矛盾)")
    feasibility_audit: AuditDimension = Field(..., description="资源可行性审核(人力/设备/费用)")

    revision_notes: list[RevisionNote] = Field(
        default_factory=list, description="修改建议(verdict为REVISE时必填)"
    )

    # 最终输出
    final_care_plan: list[UnifiedIntervention] = Field(
        default_factory=list, description="审核后的最终干预计划"
    )
    risk_alerts: list[str] = Field(
        default_factory=list, description="风险预警(需要立即关注的事项)"
    )
    executive_summary: str = Field("", description="管理层执行摘要")
