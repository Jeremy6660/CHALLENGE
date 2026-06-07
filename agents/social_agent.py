# -*- coding: utf-8 -*-
"""社工评估Agent"""

from .base_agent import BaseAgent
from schemas.social import SocialAssessmentOutput
from prompts.social_prompt import SOCIAL_SYSTEM_PROMPT, build_social_user_message


class SocialAgent(BaseAgent):
    name = "social"
    description = "社工评估Agent — 心理健康、社会参与、家庭支持、认知状态"
    output_schema = SocialAssessmentOutput

    def get_system_prompt(self) -> str:
        return SOCIAL_SYSTEM_PROMPT

    def build_user_message(self, **kwargs) -> str:
        elderly_data = kwargs.get("elderly_data", {})
        return build_social_user_message(elderly_data)

    def run(self, **input_data) -> dict:
        elderly_data = input_data.get("elderly_data", {})
        return super().run(elderly_data=elderly_data)
