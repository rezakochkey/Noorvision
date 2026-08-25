# NOORVISION Evaluation Protocol

## Purpose

NOORVISION evaluates AI systems by evidence, reproducible tasks, and explicit contracts. It is not assumed to be superior to any evaluated system, and it must be evaluated by the same protocol.

## Core principles

1. **Neutrality** — No provider, model, or system receives a privileged score.
2. **Self-evaluation** — NOORVISION is an evaluation subject as well as an evaluator.
3. **Reproducibility** — Inputs, task version, tools, model/version, limits, and scoring rules are recorded.
4. **Evidence first** — Prefer deterministic checks, tests, executable outcomes, and ground truth over subjective judgment.
5. **Judge separation** — A model-generated judgment is evidence, not unquestionable ground truth.
6. **Failure is valid** — A failed NOORVISION evaluation must remain visible and must not be rewritten to pass.
7. **No hidden semantic assumptions** — Evaluation must not depend on religious, numerological, symbolic, or Abjad interpretations unless a task explicitly requires them.
8. **Minimal claims** — Scores describe performance on defined tasks and conditions; they do not establish that one AI is universally more intelligent than another.

## Evaluation record

Each evaluation should record, where applicable:

- task identifier and version
- input and expected outcome or scoring rubric
- evaluated system and model/version
- tool access and environment
- time/token/attempt budget
- deterministic checks and their results
- judge configuration, if a judge is used
- final score and failure reasons
- artifacts needed to reproduce the result

## Scoring hierarchy

Use the strongest available evidence in this order:

1. exact ground-truth comparison
2. executable tests / validators
3. environment state and tool outcomes
4. structured rubric scoring
5. independent judge models
6. human review for cases that remain ambiguous

No single LLM judge is the sole authority for correctness when stronger evidence is available.

## Initial evaluation categories

- correctness
- instruction following
- consistency
- tool use
- recovery from failure
- memory/persistence behavior
- efficiency
- safety and constraint compliance

Categories are evaluated only when the task defines observable criteria for them.

## Non-goals

This protocol does not claim that NOORVISION is inherently above GPT, Claude, Copilot, DeepSeek, or any other AI. It defines a framework for testing comparable behavior under controlled conditions.

## Change policy

Changes to this protocol are behavior changes. They require review and tests before being treated as an established evaluation contract.
