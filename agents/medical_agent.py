# -*- coding: utf-8 -*-
"""医疗评估Agent"""

from .base_agent import BaseAgent
from schemas.medical import MedicalAssessmentOutput
from prompts.medical_prompt import MEDICAL_SYSTEM_PROMPT, build_medical_user_message


class MedicalAgent(BaseAgent):
    name = "medical"
    description = "医疗评估Agent — 慢病管理、用药安全、急性风险评估"
    output_schema = MedicalAssessmentOutput

    def get_system_prompt(self) -> str:
        return MEDICAL_SYSTEM_PROMPT

    def build_user_message(self, **kwargs) -> str:
        elderly_data = kwargs.get("elderly_data", {})
        return build_medical_user_message(elderly_data)

    def run(self, **input_data) -> dict:
        """从ElderlyProfile提取数据并运行"""
        elderly_data = input_data.get("elderly_data", {})
        return super().run(elderly_data=elderly_data)
