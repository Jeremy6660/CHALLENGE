# -*- coding: utf-8 -*-
"""端到端Pipeline — 串起整个多Agent链路"""

import asyncio
import json
import sys
import time
from typing import Optional
from dataclasses import dataclass, field

# 修复Windows控制台UTF-8编码
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from agents.medical_agent import MedicalAgent
from agents.nursing_agent import NursingAgent
from agents.social_agent import SocialAgent
from agents.dietary_agent import DietaryAgent
from agents.orchestrator_agent import OrchestratorAgent
from agents.decision_agent import DecisionAgent


@dataclass
class PipelineResult:
    """Pipeline完整输出"""
    elderly_name: str = ""
    elderly_age: int = 0
    total_elapsed: float = 0.0

    # 各阶段输出
    medical_output: dict = field(default_factory=dict)
    nursing_output: dict = field(default_factory=dict)
    social_output: dict = field(default_factory=dict)
    dietary_output: dict = field(default_factory=dict)
    orchestrator_output: dict = field(default_factory=dict)
    decision_output: dict = field(default_factory=dict)

    # 元数据
    errors: list[str] = field(default_factory=list)
    stage_times: dict = field(default_factory=dict)


class CareMindPipeline:
    """CareMind 多Agent Pipeline"""

    def __init__(self):
        self.medical_agent = MedicalAgent()
        self.nursing_agent = NursingAgent()
        self.social_agent = SocialAgent()
        self.dietary_agent = DietaryAgent()
        self.orchestrator = OrchestratorAgent()
        self.decision_agent = DecisionAgent()

    def run_sync(self, elderly_data: dict, verbose: bool = True) -> PipelineResult:
        """同步运行完整Pipeline（内部使用asyncio）"""
        return asyncio.run(self.run(elderly_data, verbose))

    async def run(self, elderly_data: dict, verbose: bool = True) -> PipelineResult:
        """异步运行完整Pipeline，4个评估Agent并行调用"""
        result = PipelineResult(
            elderly_name=elderly_data.get("name", ""),
            elderly_age=elderly_data.get("age", 0),
        )
        t_start = time.time()

        # ── 阶段1: 并行评估 ──
        if verbose:
            print(f"\n{'='*60}")
            print(f"🔍 阶段1: 四维度并行评估 — {elderly_data.get('name')}")
            print(f"{'='*60}")

        t1 = time.time()
        medical_task = self._run_agent(self.medical_agent, elderly_data=elderly_data)
        nursing_task = self._run_agent(self.nursing_agent, elderly_data=elderly_data)
        social_task = self._run_agent(self.social_agent, elderly_data=elderly_data)
        dietary_task = self._run_agent(self.dietary_agent, elderly_data=elderly_data)

        medical_out, nursing_out, social_out, dietary_out = await asyncio.gather(
            medical_task, nursing_task, social_task, dietary_task
        )

        result.medical_output = medical_out
        result.nursing_output = nursing_out
        result.social_output = social_out
        result.dietary_output = dietary_out
        result.stage_times["assessment"] = round(time.time() - t1, 2)

        if verbose:
            print(f"  ✅ 医疗Agent 完成 ({medical_out.get('_meta', {}).get('elapsed_seconds', '?')}s)")
            print(f"  ✅ 护理Agent 完成 ({nursing_out.get('_meta', {}).get('elapsed_seconds', '?')}s)")
            print(f"  ✅ 社工Agent 完成 ({social_out.get('_meta', {}).get('elapsed_seconds', '?')}s)")
            print(f"  ✅ 餐饮Agent 完成 ({dietary_out.get('_meta', {}).get('elapsed_seconds', '?')}s)")

        # ── 阶段2: 编排 ──
        if verbose:
            print(f"\n🧠 阶段2: 编排层 — 冲突消解+统一干预计划")

        t2 = time.time()
        elderly_basic = {
            "name": elderly_data.get("name"),
            "age": elderly_data.get("age"),
            "care_setting": elderly_data.get("care_setting"),
        }
        orch_out = self._run_agent_sync(
            self.orchestrator,
            medical_output=self._clean_output(medical_out),
            nursing_output=self._clean_output(nursing_out),
            social_output=self._clean_output(social_out),
            dietary_output=self._clean_output(dietary_out),
            elderly_basic=elderly_basic,
        )
        result.orchestrator_output = orch_out
        result.stage_times["orchestration"] = round(time.time() - t2, 2)

        if verbose:
            conflicts = orch_out.get("conflict_resolutions", [])
            plan_items = orch_out.get("unified_care_plan", [])
            print(f"  ✅ 检测到 {len(conflicts)} 处跨域冲突，已消解")
            print(f"  ✅ 生成 {len(plan_items)} 项统一干预计划")

        # ── 阶段3: 决策审核 ──
        if verbose:
            print(f"\n⚖️ 阶段3: 决策审核层 — 三审终审")

        t3 = time.time()
        dec_out = self._run_agent_sync(
            self.decision_agent,
            orchestrator_output=self._clean_output(orch_out),
        )
        result.decision_output = dec_out
        result.stage_times["decision"] = round(time.time() - t3, 2)

        if verbose:
            verdict = dec_out.get("verdict", "UNKNOWN")
            rationality = dec_out.get("rationality_audit", {}).get("score", "?")
            safety = dec_out.get("safety_audit", {}).get("score", "?")
            feasibility = dec_out.get("feasibility_audit", {}).get("score", "?")
            print(f"  ✅ 审核结论: {verdict}")
            print(f"  ✅ 合理性: {rationality}分 | 安全性: {safety}分 | 可行性: {feasibility}分")

        result.total_elapsed = round(time.time() - t_start, 2)
        if verbose:
            print(f"\n🏁 总耗时: {result.total_elapsed}s")
            print(f"{'='*60}\n")

        return result

    async def _run_agent(self, agent, **kwargs) -> dict:
        """在线程池中运行单个Agent（因为LLM调用可能是同步的）"""
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, lambda: agent.run(**kwargs))

    def _run_agent_sync(self, agent, **kwargs) -> dict:
        """同步运行Agent"""
        return agent.run(**kwargs)

    def _clean_output(self, output: dict) -> dict:
        """去除元数据字段"""
        return {k: v for k, v in output.items() if k != "_meta"}

    def inject_simulation_data(self, elderly_data: dict, simulation_data: dict):
        """
        为模拟模式注入预置数据。
        simulation_data 结构:
        {
            "medical": {...},
            "nursing": {...},
            "social": {...},
            "dietary": {...},
            "orchestrator": {...},
            "decision": {...}
        }
        """
        # 计算所有agent的cache key并注入
        # 评估Agent
        for key in ["medical", "nursing", "social", "dietary"]:
            agent = getattr(self, f"{key}_agent")
            agent.inject_simulation(
                {"elderly_data": elderly_data},
                simulation_data.get(key, {}),
            )

        # Orchestrator - 需要在评估Agent运行后才知输入，这里用通配方式
        # 实际使用时在pipeline运行前调用此方法注入
        self._sim_data = simulation_data

    def run_with_simulation(self, elderly_data: dict, sim_data: dict, verbose: bool = True) -> PipelineResult:
        """使用模拟数据运行完整Pipeline"""
        # 注入评估Agent的模拟数据
        for key in ["medical", "nursing", "social", "dietary"]:
            agent = getattr(self, f"{key}_agent")
            agent.inject_simulation(
                {"elderly_data": elderly_data},
                sim_data.get(key, {}),
            )

        # 运行评估阶段
        result = PipelineResult(
            elderly_name=elderly_data.get("name", ""),
            elderly_age=elderly_data.get("age", 0),
        )
        t_start = time.time()

        if verbose:
            print(f"\n{'='*60}")
            print(f"🔍 阶段1: 四维度并行评估 — {elderly_data.get('name')}")
            print(f"{'='*60}")

        t1 = time.time()
        result.medical_output = self.medical_agent.run(elderly_data=elderly_data)
        result.nursing_output = self.nursing_agent.run(elderly_data=elderly_data)
        result.social_output = self.social_agent.run(elderly_data=elderly_data)
        result.dietary_output = self.dietary_agent.run(elderly_data=elderly_data)
        result.stage_times["assessment"] = round(time.time() - t1, 2)

        if verbose:
            for key in ["medical", "nursing", "social", "dietary"]:
                out = getattr(result, f"{key}_output")
                print(f"  ✅ {key}Agent 完成 (模拟)")

        # Orchestrator模拟注入
        elderly_basic = {
            "name": elderly_data.get("name"),
            "age": elderly_data.get("age"),
            "care_setting": elderly_data.get("care_setting"),
        }
        self.orchestrator.inject_simulation(
            {
                "medical_output": self._clean_output(result.medical_output),
                "nursing_output": self._clean_output(result.nursing_output),
                "social_output": self._clean_output(result.social_output),
                "dietary_output": self._clean_output(result.dietary_output),
                "elderly_basic": elderly_basic,
            },
            sim_data.get("orchestrator", {}),
        )

        if verbose:
            print(f"\n🧠 阶段2: 编排层")

        t2 = time.time()
        result.orchestrator_output = self.orchestrator.run(
            medical_output=self._clean_output(result.medical_output),
            nursing_output=self._clean_output(result.nursing_output),
            social_output=self._clean_output(result.social_output),
            dietary_output=self._clean_output(result.dietary_output),
            elderly_basic=elderly_basic,
        )
        result.stage_times["orchestration"] = round(time.time() - t2, 2)

        # Decision Agent模拟注入
        self.decision_agent.inject_simulation(
            {"orchestrator_output": self._clean_output(result.orchestrator_output)},
            sim_data.get("decision", {}),
        )

        if verbose:
            print(f"\n⚖️ 阶段3: 决策审核层")

        t3 = time.time()
        result.decision_output = self.decision_agent.run(
            orchestrator_output=self._clean_output(result.orchestrator_output),
        )
        result.stage_times["decision"] = round(time.time() - t3, 2)

        if verbose:
            verdict = result.decision_output.get("verdict", "UNKNOWN")
            print(f"  ✅ 审核结论: {verdict}")

        result.total_elapsed = round(time.time() - t_start, 2)
        if verbose:
            print(f"\n🏁 总耗时: {result.total_elapsed}s (模拟模式)")
            print(f"{'='*60}\n")

        return result
