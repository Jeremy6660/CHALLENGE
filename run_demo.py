# -*- coding: utf-8 -*-
"""CareMind 命令行演示 — 跑通3个案例并生成报告"""

import sys
import os

# 修复Windows控制台UTF-8编码
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils.pipeline import CareMindPipeline
from utils.report_renderer import render_markdown_report
from data import ALL_CASES, CASE_NAMES


def run_case(pipeline: CareMindPipeline, case_key: str, case_data: dict):
    """运行单个案例"""
    print(f"\n{'#'*60}")
    print(f"# {CASE_NAMES[case_key]}")
    print(f"{'#'*60}")

    elderly = case_data["elderly"]
    sim = case_data["simulation"]

    result = pipeline.run_with_simulation(elderly, sim, verbose=True)

    # 生成报告
    report = render_markdown_report(result)

    # 保存报告
    report_dir = os.path.join(os.path.dirname(__file__), "docs")
    os.makedirs(report_dir, exist_ok=True)
    report_path = os.path.join(report_dir, f"{case_key}_报告.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"\n📄 报告已保存: {report_path}")
    return result


def main():
    print("=" * 60)
    print("  CareMind 智慧养老多Agent系统 — 模拟演示")
    print("  医养结合 · 全人照护 · 反客体化实践")
    print("=" * 60)

    pipeline = CareMindPipeline()

    for case_key in ["case_1", "case_2", "case_3"]:
        case_data = ALL_CASES[case_key]
        run_case(pipeline, case_key, case_data)

    print("\n" + "=" * 60)
    print("  ✅ 3个案例全部运行完成")
    print("  📄 报告文件在 docs/ 目录下")
    print("  🌐 运行 streamlit run main.py 启动Web界面")
    print("=" * 60)


if __name__ == "__main__":
    main()
