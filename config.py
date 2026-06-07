# -*- coding: utf-8 -*-
"""CareMind 系统配置"""

import os
from dotenv import load_dotenv

load_dotenv()

# ── LLM 配置 ──
LLM_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
LLM_MODEL = os.getenv("LLM_MODEL", "claude-sonnet-4-6")  # 默认用最新 Sonnet
LLM_MAX_TOKENS = 4096
LLM_TEMPERATURE = 0.3  # 评估类任务降低温度以提升一致性

# ── 模拟模式 ──
# 当没有 API key 时自动切换为模拟模式，使用预置的评估结果
SIMULATION_MODE = not LLM_API_KEY

# ── 路径配置 ──
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
PROMPT_DIR = os.path.join(PROJECT_ROOT, "prompts")
DOCS_DIR = os.path.join(PROJECT_ROOT, "docs")

# ── Agent 配置 ──
ASSESSMENT_AGENTS = ["medical", "nursing", "social", "dietary"]
PRIORITY_ORDER = ["safety", "medical", "nursing", "social", "dietary"]

# ── 冲突消解配置 ──
CONFLICT_RULES = {
    "activity_restriction": "safety_first",  # 安全优先
    "diet_vs_medical": "medical_first",       # 医疗优先于餐饮
    "social_vs_medical": "compromise",        # 折中方案
}
