# -*- coding: utf-8 -*-
"""Agent 抽象基类 — 所有Agent继承此类"""

import json
import time
from abc import ABC, abstractmethod
from typing import Optional, Type
from pydantic import BaseModel
from utils.llm_client import get_llm_client, LLMClient


class BaseAgent(ABC):
    """Agent基类，封装LLM调用、重试、缓存逻辑"""

    # 子类覆盖
    name: str = "base"
    description: str = ""
    output_schema: Optional[Type[BaseModel]] = None

    def __init__(self):
        self.llm: LLMClient = get_llm_client()

    @abstractmethod
    def get_system_prompt(self) -> str:
        """返回此Agent的System Prompt"""
        ...

    def build_user_message(self, **kwargs) -> str:
        """根据输入数据构建user message(子类可覆盖)"""
        return json.dumps(kwargs, ensure_ascii=False, indent=2)

    def run(self, **input_data) -> dict:
        """
        运行Agent: 组装prompt → 调LLM → 解析输出
        返回解析后的dict
        """
        system_prompt = self.get_system_prompt()
        user_message = self.build_user_message(**input_data)

        start_time = time.time()
        result = self.llm.call(
            system_prompt=system_prompt,
            user_message=user_message,
            output_schema=self.output_schema,
        )
        elapsed = time.time() - start_time

        # 记录耗时(可用于UI展示)
        result["_meta"] = {
            "agent": self.name,
            "elapsed_seconds": round(elapsed, 2),
            "simulation": self.llm.is_simulation,
        }

        return result

    def run_structured(self, **input_data) -> Optional[BaseModel]:
        """运行Agent并返回结构化Pydantic对象"""
        result = self.run(**input_data)

        if self.output_schema is None:
            return None

        try:
            # 去除元数据后解析
            clean = {k: v for k, v in result.items() if k != "_meta"}
            return self.output_schema(**clean)
        except Exception as e:
            # 解析失败时打印错误并返回None
            print(f"[{self.name}] Schema解析失败: {e}")
            print(f"原始输出: {json.dumps(result, ensure_ascii=False, indent=2)[:500]}")
            return None

    def inject_simulation(self, input_data: dict, output_data: dict):
        """为模拟模式注入此Agent的预置响应"""
        system_prompt = self.get_system_prompt()
        user_message = self.build_user_message(**input_data)
        self.llm.inject_simulation_result(system_prompt, user_message, output_data)

    def __repr__(self):
        return f"<Agent:{self.name}>"
