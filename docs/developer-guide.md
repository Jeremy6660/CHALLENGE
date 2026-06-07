# CareMind Developer Guide

## Purpose

This document is the engineering handoff for the CareMind prototype. Use it for architecture, extension work, and reality-checking the current demo behavior against the code.

## System Shape

CareMind models elderly care planning as a six-agent pipeline:

1. Medical assessment agent
2. Nursing assessment agent
3. Social assessment agent
4. Dietary assessment agent
5. Orchestrator agent
6. Decision agent

The first four agents produce domain-specific assessments. The orchestrator merges and reconciles them. The decision agent performs a final audit over the unified care plan.

## Actual Execution Paths

### Demo path in use now

The repository currently exposes two user-facing demo paths:

- `streamlit run main.py`
- `python run_demo.py`

Both are demo-first:

- `run_demo.py` injects simulation payloads and uses `run_with_simulation(...)`
- `pages/1_单案评估.py` renders `case_data["simulation"]` instead of calling the live pipeline

This is why the project can still present a complete workflow even without an API key.

### Live path available in code

The live path is implemented but not connected to the public demo flow:

- `utils/pipeline.py`
- `utils/llm_client.py`
- `agents/*.py`

`config.SIMULATION_MODE` switches based on whether `ANTHROPIC_API_KEY` is present, but the default UI path does not currently route into `CareMindPipeline.run(...)`.

## Directory Map

### App layer

- `main.py`: home page and case navigation
- `pages/1_单案评估.py`: single-case walkthrough page
- `pages/2_案例对比.py`: static comparison view across the three sample cases
- `pages/3_架构展示.py`: architecture presentation page

### Domain logic

- `agents/`: agent classes, all inheriting from `BaseAgent`
- `utils/pipeline.py`: top-level workflow and stage timing
- `utils/conflict_resolver.py`: rule-based conflict detection and resolution
- `utils/report_renderer.py`: markdown and HTML output formatting
- `utils/llm_client.py`: cache, simulation behavior, Anthropic integration

### Data and contracts

- `data/`: source case data and simulated outputs
- `schemas/`: Pydantic output contracts
- `prompts/`: per-agent system prompts

### Docs and artifacts

- `docs/架构图.md`: presentation-focused architecture material
- `docs/PPT素材汇总.md`: pitch content
- `docs/case_*_报告.md`: generated sample reports

## Pipeline Walkthrough

### Stage 1: Parallel assessment

[`utils/pipeline.py`](/C:/Users/ArcYuYin/Desktop/CareMind/utils/pipeline.py:65) launches four domain agents:

- medical
- nursing
- social
- dietary

In the live path, this uses `asyncio.gather(...)` plus `run_in_executor(...)` because each agent's `run(...)` call is synchronous from the event loop's perspective.

### Stage 2: Orchestration

The orchestrator receives:

- cleaned medical output
- cleaned nursing output
- cleaned social output
- cleaned dietary output
- a small `elderly_basic` object

It then:

- resolves cross-domain conflicts
- merges recommendations
- builds a unified care plan

### Stage 3: Decision audit

The decision agent evaluates the orchestrated plan for:

- rationality
- safety
- feasibility

It returns a verdict such as `PASS`, plus audit scores, risk alerts, and the final care plan used by the report layer.

## Conflict Resolution Rules

`utils/conflict_resolver.py` currently handles several deterministic cross-domain conflicts before LLM reasoning takes over, including:

- activity restriction vs social or nursing activation
- dietary plan vs chronic disease constraints
- social visit proposals vs infection or fall risk
- swallowing risk vs nutrition delivery mode

If you add a new conflict type, update both the resolver and any orchestrator prompt language that relies on these outputs.

## Configuration

`config.py` defines:

- `ANTHROPIC_API_KEY`
- `LLM_MODEL`
- `LLM_MAX_TOKENS`
- `LLM_TEMPERATURE`
- project paths
- agent ordering and conflict rules

Important implementation detail:

- simulation mode is `not LLM_API_KEY`
- the concrete live client currently targets Anthropic only

## Generated vs Source Files

Treat these as generated or presentation-oriented, not primary logic:

- `docs/case_1_报告.md`
- `docs/case_2_报告.md`
- `docs/case_3_报告.md`
- `docs/PPT素材汇总.md`
- `docs/架构图.md`

When behavior changes, update engineering docs first, then decide whether presentation docs and generated reports also need a refresh.

## Safe Extension Checklist

### If you want live LLM execution in the UI

Update at least:

- `pages/1_单案评估.py`
- possibly `main.py`
- `README.md`
- this file

You will need to replace direct reads from `case_data["simulation"]` with calls into `CareMindPipeline`.

### If you change output schema

Update together:

- `schemas/`
- corresponding agent file in `agents/`
- corresponding prompt file in `prompts/`
- `utils/report_renderer.py`
- any Streamlit page that reads those fields

### If you add a new sample case

Update together:

- `data/`
- `data/__init__.py`
- case selectors in `main.py`
- case selectors in `pages/1_单案评估.py`
- comparison content in `pages/2_案例对比.py`

## Validation Notes

On 2026-06-07 in this workspace:

- `python run_demo.py` failed before dependency install because `pydantic` was missing
- no automated tests were present

So current docs should be read as code-aligned guidance, not as proof of a fully provisioned environment.
