# -*- coding: utf-8 -*-
"""决策审核Agent — 对综合干预计划做三审终审"""

from .base_agent import BaseAgent
from schemas.decision import DecisionOutput
from prompts.decision_prompt import DECISION_SYSTEM_PROMPT, build_decision_user_message


class DecisionAgent(BaseAgent):
    name = "decision"
    description = "决策审核Agent — 合理性、安全性、可行性三审终审"
    output_schema = DecisionOutput

    def get_system_prompt(self) -> str:
        return DECISION_SYSTEM_PROMPT

    def run(self, orchestrator_output: dict) -> dict:
        return super().run(orchestrator_output=orchestrator_output)

    def build_user_message(self, **kwargs) -> str:
        return build_decision_user_message(
            kwargs.get("orchestrator_output", {})
        )
