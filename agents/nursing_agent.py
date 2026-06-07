# -*- coding: utf-8 -*-
"""护理评估Agent"""

from .base_agent import BaseAgent
from schemas.nursing import NursingAssessmentOutput
from prompts.nursing_prompt import NURSING_SYSTEM_PROMPT, build_nursing_user_message


class NursingAgent(BaseAgent):
    name = "nursing"
    description = "护理评估Agent — ADL、跌倒风险、压疮风险、照护等级"
    output_schema = NursingAssessmentOutput

    def get_system_prompt(self) -> str:
        return NURSING_SYSTEM_PROMPT

    def build_user_message(self, **kwargs) -> str:
        elderly_data = kwargs.get("elderly_data", {})
        return build_nursing_user_message(elderly_data)

    def run(self, **input_data) -> dict:
        elderly_data = input_data.get("elderly_data", {})
        return super().run(elderly_data=elderly_data)
