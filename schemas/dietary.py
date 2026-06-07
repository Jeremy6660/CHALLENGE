# -*- coding: utf-8 -*-
"""餐饮评估Agent的输入输出模型"""

from pydantic import BaseModel, Field
from typing import Optional


class NutritionStatus(BaseModel):
    bmi: Optional[float] = Field(None, description="BMI")
    albumin: Optional[float] = Field(None, description="白蛋白 g/L")
    hemoglobin: Optional[float] = Field(None, description="血红蛋白 g/L")
    weight_trend: str = Field(..., description="体重变化趋势: 稳定/下降/上升")
    nutrition_rating: str = Field(..., description="营养评级: 正常/轻度不良/中度不良/重度不良")
    key_deficits: list[str] = Field(default_factory=list, description="主要营养缺乏")


class SwallowFunction(BaseModel):
    test_result: Optional[str] = Field(None, description="洼田饮水试验结果")
    swallow_safety: str = Field(..., description="吞咽安全性: 安全/需调整食物质地/需鼻饲")
    recommended_texture: str = Field(..., description="推荐食物质地: 普食/软食/半流质/流质/鼻饲")


class DietaryPlan(BaseModel):
    dietary_type: str = Field(..., description="膳食类型")
    daily_calories_kcal: int = Field(..., ge=800, le=3000, description="每日推荐热量")
    daily_protein_g: int = Field(..., ge=20, le=120, description="每日推荐蛋白质克数")
    restrictions: list[str] = Field(default_factory=list, description="饮食限制")
    forbidden_foods: list[str] = Field(default_factory=list, description="禁忌食物")
    recommended_foods: list[str] = Field(default_factory=list, description="推荐食物")


class DietaryRecommendation(BaseModel):
    priority: str = Field(..., description="优先级: 紧急/本周内/持续执行")
    category: str = Field(..., description="类别: 膳食调整/营养补充/进食辅助/监测/会诊")
    content: str = Field(..., description="具体建议")
    rationale: str = Field(..., description="理由")


class DietaryAssessmentOutput(BaseModel):
    """餐饮评估Agent的结构化输出"""
    nutrition_status: NutritionStatus = Field(..., description="营养状态评估")
    swallow_function: SwallowFunction = Field(..., description="吞咽功能评估")
    dietary_plan: DietaryPlan = Field(..., description="膳食方案")
    dietary_recommendations: list[DietaryRecommendation] = Field(
        default_factory=list, description="餐饮干预建议"
    )
    summary: str = Field("", description="餐饮维度一句话总结")
