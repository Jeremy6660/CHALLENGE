# -*- coding: utf-8 -*-
"""编排层Agent — 融合四份评估，消解冲突，生成统一干预计划"""

from .base_agent import BaseAgent
from schemas.orchestration import OrchestratorOutput
from prompts.orchestrator_prompt import (
    ORCHESTRATOR_SYSTEM_PROMPT,
    build_orchestrator_user_message,
)
from utils.conflict_resolver import resolve_conflicts


class OrchestratorAgent(BaseAgent):
    name = "orchestrator"
    description = "编排层Agent — 跨域协同、冲突消解、统一干预计划生成"
    output_schema = OrchestratorOutput

    def get_system_prompt(self) -> str:
        return ORCHESTRATOR_SYSTEM_PROMPT

    def run(
        self,
        medical_output: dict,
        nursing_output: dict,
        social_output: dict,
        dietary_output: dict,
        elderly_basic: dict,
        use_rules_engine: bool = True,
    ) -> dict:
        """
        运行编排层。
        use_rules_engine: 是否先用规则引擎做第一层冲突消解
        """
        # 第一层：规则引擎预处理
        if use_rules_engine:
            pre_resolved = resolve_conflicts(
                medical_output, nursing_output, social_output, dietary_output
            )
            # 将预消解结果提示给LLM
            if pre_resolved:
                elderly_basic = dict(elderly_basic)
                elderly_basic["_pre_resolved_conflicts"] = pre_resolved

        # 第二层：LLM深度编排
        result = super().run(
            medical_output=medical_output,
            nursing_output=nursing_output,
            social_output=social_output,
            dietary_output=dietary_output,
            elderly_basic=elderly_basic,
        )

        return result

    def build_user_message(self, **kwargs) -> str:
        return build_orchestrator_user_message(
            medical_output=kwargs.get("medical_output", {}),
            nursing_output=kwargs.get("nursing_output", {}),
            social_output=kwargs.get("social_output", {}),
            dietary_output=kwargs.get("dietary_output", {}),
            elderly_basic=kwargs.get("elderly_basic", {}),
        )
