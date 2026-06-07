# -*- coding: utf-8 -*-
"""案例数据模块"""

from .case_1_王奶奶 import CASE_DATA as CASE_1
from .case_2_李爷爷 import CASE_DATA as CASE_2
from .case_3_张爷爷 import CASE_DATA as CASE_3

ALL_CASES = {
    "case_1": CASE_1,
    "case_2": CASE_2,
    "case_3": CASE_3,
}

CASE_NAMES = {
    "case_1": "王奶奶 — 轻度失能·社区居家·社工主导",
    "case_2": "李爷爷 — 中度失能·机构养老·医疗护理并重",
    "case_3": "张爷爷 — 重度失能·长期卧床·护理主导",
}
