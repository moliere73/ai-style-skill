# 2026-07-27

## Completed
- Created SKILL.md
- Designed three writing profiles
- Tested rewrite behavior
- Planned Custom GPT architecture

## Next
- Build Custom GPT
- Connect rewrite API

Decision Log

2026-07-28 — Rule-Based Rewrite Engine

Decision

Build the initial rewrite engine using deterministic text transformation rules instead of an LLM.

Rationale

* Keeps behavior predictable and reproducible.
* Makes debugging straightforward.
* Supports fast local execution without external API dependencies.
* Provides a stable baseline before introducing more advanced techniques.

Tradeoffs

* Limited flexibility compared to LLMs.
* Requires manual maintenance as new rewrite patterns are added.

⸻

2026-07-28 — YAML Configuration

Decision

Store rewrite configuration separately from the application logic.

Rationale

* Separates configuration from implementation.
* Makes profiles easier to modify without changing Python code.
* Simplifies experimentation with different writing styles.

Future Direction

Expand to multiple profile-specific configuration files and reusable rule sets.

⸻

2026-07-28 — Manual Regression Suite

Decision

Create a collection of Markdown-based regression tests.

Rationale

* Documents expected behavior using realistic writing examples.
* Makes regressions easier to detect during development.
* Provides examples that can also be used in demonstrations.

Future Direction

Automatically generate benchmark reports after each run.

⸻

2026-07-28 — Benchmark Runner

Decision

Build a standalone benchmark runner (benchmark.py) to evaluate rewrite quality.

Rationale

* Measures improvements over time.
* Provides repeatable evaluation.
* Supports future CI/CD integration.

Current Limitation

The benchmark currently compares outputs using exact string matching.

Future Direction

Introduce semantic comparison metrics and richer benchmark reports.

⸻

2026-07-28 — Preserve Meaning First

Decision

Prioritize preserving the author’s intent over aggressively rewriting text.

Rationale

* Reduces the risk of introducing unsupported claims.
* Produces more trustworthy rewrites.
* Makes the system appropriate for professional writing such as emails, documentation, and technical communication.

⸻

2026-07-28 — Modular Rewrite Pipeline

Decision

Design the rewrite engine as a sequence of independent transformations.

Rationale

Each rewrite rule should have a single responsibility and be independently testable.

Examples include:

* Remove em dashes
* Simplify words
* Normalize spacing
* Capitalize sentences
* Future grammar improvements
* Future style-specific transformations

This modular structure will make it easier to add, remove, reorder, and test individual rewrite rules as the project evolves.

