# -*- coding: utf-8 -*-
"""LLM API 客户端封装 — 支持真实API调用和模拟模式"""

import json
import hashlib
import time
from typing import Optional, Type
from pydantic import BaseModel
import config


class LLMClient:
    """大模型调用客户端，支持缓存和模拟模式"""

    def __init__(self):
        self._cache: dict[str, dict] = {}
        self._call_count = 0

    @property
    def is_simulation(self) -> bool:
        return config.SIMULATION_MODE

    def _cache_key(self, system_prompt: str, user_message: str) -> str:
        raw = f"{system_prompt}|||{user_message}"
        return hashlib.sha256(raw.encode()).hexdigest()

    def call(
        self,
        system_prompt: str,
        user_message: str,
        output_schema: Optional[Type[BaseModel]] = None,
        temperature: float = None,
    ) -> dict:
        """
        调用LLM，返回解析后的dict。
        在模拟模式下直接返回预置结果(需外部注入)。
        """
        if temperature is None:
            temperature = config.LLM_TEMPERATURE

        # 检查缓存
        key = self._cache_key(system_prompt, user_message)
        if key in self._cache:
            return self._cache[key]

        if self.is_simulation:
            # 模拟模式: 返回空dict，由调用方注入模拟数据
            return {}

        # 真实API调用
        result = self._call_anthropic(system_prompt, user_message, output_schema, temperature)

        # 缓存结果
        self._cache[key] = result
        self._call_count += 1
        return result

    def _call_anthropic(
        self,
        system_prompt: str,
        user_message: str,
        output_schema: Optional[Type[BaseModel]],
        temperature: float,
    ) -> dict:
        """调用Claude API"""
        import anthropic

        client = anthropic.Anthropic(api_key=config.LLM_API_KEY)

        messages = [{"role": "user", "content": user_message}]

        kwargs = {
            "model": config.LLM_MODEL,
            "max_tokens": config.LLM_MAX_TOKENS,
            "temperature": temperature,
            "system": system_prompt,
            "messages": messages,
        }

        response = client.messages.create(**kwargs)

        # 提取文本内容
        text = ""
        for block in response.content:
            if hasattr(block, "text"):
                text += block.text

        # 尝试解析JSON
        return self._extract_json(text)

    def _extract_json(self, text: str) -> dict:
        """从LLM回复中提取JSON"""
        text = text.strip()
        # 尝试直接解析
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            pass

        # 尝试提取 ```json ... ``` 块
        if "```json" in text:
            start = text.find("```json") + 7
            end = text.find("```", start)
            if end > start:
                try:
                    return json.loads(text[start:end].strip())
                except json.JSONDecodeError:
                    pass

        # 返回原始文本包装
        return {"raw_response": text, "parse_error": True}

    def inject_simulation_result(self, system_prompt: str, user_message: str, result: dict):
        """为模拟模式注入预置结果"""
        key = self._cache_key(system_prompt, user_message)
        self._cache[key] = result

    def clear_cache(self):
        self._cache.clear()
        self._call_count = 0

    @property
    def call_count(self) -> int:
        return self._call_count


# 全局单例
_llm_client: Optional[LLMClient] = None


def get_llm_client() -> LLMClient:
    global _llm_client
    if _llm_client is None:
        _llm_client = LLMClient()
    return _llm_client
