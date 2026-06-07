# -*- coding: utf-8 -*-
"""餐饮评估Agent"""

from .base_agent import BaseAgent
from schemas.dietary import DietaryAssessmentOutput
from prompts.dietary_prompt import DIETARY_SYSTEM_PROMPT, build_dietary_user_message


class DietaryAgent(BaseAgent):
    name = "dietary"
    description = "餐饮评估Agent — 营养状态、吞咽功能、膳食方案"
    output_schema = DietaryAssessmentOutput

    def get_system_prompt(self) -> str:
        return DIETARY_SYSTEM_PROMPT

    def build_user_message(self, **kwargs) -> str:
        elderly_data = kwargs.get("elderly_data", {})
        return build_dietary_user_message(elderly_data)

    def run(self, **input_data) -> dict:
        elderly_data = input_data.get("elderly_data", {})
        return super().run(elderly_data=elderly_data)
