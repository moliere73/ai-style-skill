#!/usr/bin/env python3
"""Run Cortical Style regression tests stored as Markdown files.

Expected test format:

# Test title

## Metadata

- **Profile:** `concise`

## Input

```text
Original text
```

## Expected Output

```text
Expected rewritten text
```

The runner imports ``rewrite_text`` from ``rewriter.py``. If your project uses a
different function name or signature, update ``run_rewriter`` below.
"""

from __future__ import annotations

import argparse
import difflib
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable
from datetime import datetime

@dataclass(frozen=True)
class BenchmarkCase:
    """A single Markdown regression test."""

    path: Path
    title: str
    profile: str
    input_text: str
    expected_output: str


@dataclass(frozen=True)
class BenchmarkResult:
    """The result of running one benchmark case."""

    case: BenchmarkCase
    actual_output: str
    passed: bool
    similarity: float


SECTION_PATTERN = re.compile(
    r"^##\s+(?P<name>[^\n]+)\n(?P<body>.*?)(?=^##\s+|\Z)",
    re.MULTILINE | re.DOTALL,
)

CODE_BLOCK_PATTERN = re.compile(
    r"```(?:text|markdown)?\s*\n(?P<content>.*?)\n```",
    re.DOTALL,
)

PROFILE_PATTERN = re.compile(
    r"\*\*Profile:\*\*\s*`?(?P<profile>[A-Za-z0-9_-]+)`?"
)


def normalize_text(text: str) -> str:
    """Normalize line endings and surrounding whitespace for comparison."""

    return text.replace("\r\n", "\n").replace("\r", "\n").strip()


def extract_code_block(section_body: str, section_name: str, path: Path) -> str:
    """Extract the first fenced code block from a Markdown section."""

    match = CODE_BLOCK_PATTERN.search(section_body)
    if not match:
        raise ValueError(
            f"{path}: section '{section_name}' must contain a fenced code block."
        )
    return normalize_text(match.group("content"))


def parse_markdown_test(path: Path) -> BenchmarkCase:
    """Parse one Markdown test file into a BenchmarkCase."""

    content = path.read_text(encoding="utf-8")
    title_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else path.stem

    sections = {
        match.group("name").strip().lower(): match.group("body")
        for match in SECTION_PATTERN.finditer(content)
    }

    metadata = sections.get("metadata", "")
    profile_match = PROFILE_PATTERN.search(metadata)
    if not profile_match:
        raise ValueError(f"{path}: missing '- **Profile:** `profile_name`' metadata.")

    input_body = sections.get("input")
    expected_body = sections.get("expected output")

    if input_body is None:
        raise ValueError(f"{path}: missing '## Input' section.")
    if expected_body is None:
        raise ValueError(f"{path}: missing '## Expected Output' section.")

    return BenchmarkCase(
        path=path,
        title=title,
        profile=profile_match.group("profile"),
        input_text=extract_code_block(input_body, "Input", path),
        expected_output=extract_code_block(expected_body, "Expected Output", path),
    )


def load_cases(test_dir: Path) -> list[BenchmarkCase]:
    """Load all Markdown benchmark cases from a directory."""

    if not test_dir.exists():
        raise FileNotFoundError(f"Test directory does not exist: {test_dir}")

    paths = sorted(
        path
        for path in test_dir.glob("*.md")
        if path.name.lower() != "readme.md"
    )

    if not paths:
        raise FileNotFoundError(f"No Markdown test files found in {test_dir}")

    return [parse_markdown_test(path) for path in paths]

def load_profile(profile: str) -> dict:
    """Load the current rewrite configuration.

    The MVP currently uses one shared style.yaml configuration.
    Profile names remain in the test files for future profile support.
    """

    import yaml

    style_path = Path("style.yaml")

    if not style_path.exists():
        raise FileNotFoundError(
            "Could not find style.yaml. "
            "Run benchmark.py from the repository root."
        )

    with style_path.open("r", encoding="utf-8") as file:
        config = yaml.safe_load(file) or {}

    if not isinstance(config, dict):
        raise TypeError(
            "style.yaml must contain a YAML mapping, "
            f"but found {type(config).__name__}."
        )

    return config

def run_rewriter(text: str, profile: str) -> str:
    """Load the selected profile and run the rewrite engine."""

    try:
        from rewriter import rewrite
    except ImportError as exc:
        raise RuntimeError(
            "Could not import rewrite from rewriter.py. "
            "Run benchmark.py from the repository root."
        ) from exc

    config = load_profile(profile)
    output = rewrite(text, config)

    if not isinstance(output, str):
        raise TypeError(
            f"rewrite returned {type(output).__name__}; expected str."
        )

    return normalize_text(output)

def calculate_similarity(expected: str, actual: str) -> float:
    """Return a similarity score from 0.0 to 1.0."""

    return difflib.SequenceMatcher(
        None,
        normalize_text(expected),
        normalize_text(actual),
    ).ratio()


def unified_diff(expected: str, actual: str) -> str:
    """Create a readable unified diff."""

    lines = difflib.unified_diff(
        expected.splitlines(),
        actual.splitlines(),
        fromfile="expected",
        tofile="actual",
        lineterm="",
    )
    return "\n".join(lines)


def run_case(case: BenchmarkCase) -> BenchmarkResult:
    """Execute one benchmark case."""

    actual = run_rewriter(case.input_text, case.profile)
    expected = normalize_text(case.expected_output)
    passed = actual == expected

    return BenchmarkResult(
        case=case,
        actual_output=actual,
        passed=passed,
        similarity=calculate_similarity(expected, actual),
    )


def print_result(result: BenchmarkResult, show_diff: bool) -> None:
    """Print one result to the terminal."""

    status = "PASS" if result.passed else "FAIL"
    print(
        f"[{status}] {result.case.path.name} "
        f"({result.case.profile}, similarity={result.similarity:.1%})"
    )

    if show_diff and not result.passed:
        diff = unified_diff(
            result.case.expected_output,
            result.actual_output,
        )
        if diff:
            print(diff)
        print()


def run_benchmark(
    cases: Iterable[BenchmarkCase],
    show_diff: bool = False,
) -> list[BenchmarkResult]:
    """Run all benchmark cases."""

    results: list[BenchmarkResult] = []
    for case in cases:
        try:
            result = run_case(case)
        except Exception as exc:
            print(f"[ERROR] {case.path.name}: {exc}", file=sys.stderr)
            continue

        results.append(result)
        print_result(result, show_diff)

    return results


def print_summary(results: list[BenchmarkResult]) -> None:
    """Print aggregate benchmark results."""

    total = len(results)
    passed = sum(result.passed for result in results)
    failed = total - passed
    average_similarity = (
        sum(result.similarity for result in results) / total if total else 0.0
    )

    print("\nSummary")
    print("-------")
    print(f"Cases run:          {total}")
    print(f"Exact matches:      {passed}")
    print(f"Non-exact matches:  {failed}")
    print(f"Average similarity: {average_similarity:.1%}")

def write_markdown_report(
    results: list[BenchmarkResult],
    output_path: Path,
) -> None:
    """Write benchmark results to a Markdown report."""

    total = len(results)
    passed = sum(result.passed for result in results)
    failed = total - passed
    average_similarity = (
        sum(result.similarity for result in results) / total
        if total
        else 0.0
    )

    lines = [
        "# Cortical Style Benchmark Report",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        "",
        "## Summary",
        "",
        f"- Cases run: {total}",
        f"- Exact matches: {passed}",
        f"- Non-exact matches: {failed}",
        f"- Average similarity: {average_similarity:.1%}",
        "",
        "## Results",
        "",
    ]

    for result in results:
        status = "PASS" if result.passed else "FAIL"

        lines.extend(
            [
                f"### {result.case.title}",
                "",
                f"- File: `{result.case.path.name}`",
                f"- Profile: `{result.case.profile}`",
                f"- Status: **{status}**",
                f"- Similarity: {result.similarity:.1%}",
                "",
                "#### Input",
                "",
                "```text",
                result.case.input_text,
                "```",
                "",
                "#### Expected Output",
                "",
                "```text",
                result.case.expected_output,
                "```",
                "",
                "#### Actual Output",
                "",
                "```text",
                result.actual_output,
                "```",
                "",
            ]
        )

        if not result.passed:
            diff = unified_diff(
                result.case.expected_output,
                result.actual_output,
            )

            lines.extend(
                [
                    "#### Difference",
                    "",
                    "```diff",
                    diff or "No readable diff available.",
                    "```",
                    "",
                ]
            )

    output_path.write_text(
        "\n".join(lines),
        encoding="utf-8",
    )

    print(f"\nReport written to {output_path}")


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser."""

    parser = argparse.ArgumentParser(
        description="Run Cortical Style Markdown regression tests."
    )
    parser.add_argument(
        "--tests",
        type=Path,
        default=Path("tests"),
        help="Directory containing Markdown test files (default: tests).",
    )
    parser.add_argument(
        "--diff",
        action="store_true",
        help="Show a unified diff for every non-exact match.",
    )
    parser.add_argument(
        "--minimum-similarity",
        type=float,
        default=None,
        metavar="FLOAT",
        help=(
            "Exit successfully when the average similarity is at least this "
            "value, even if outputs are not exact matches. Example: 0.90"
        ),
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=Path("benchmark_results.md"),
        help=(
            "Path for the generated Markdown report "
            "(default: benchmark_results.md)."
        ),
    )
    return parser


def main() -> int:
    """CLI entry point."""

    args = build_parser().parse_args()

    try:
        cases = load_cases(args.tests)
    except (FileNotFoundError, ValueError) as exc:
        print(f"Benchmark setup error: {exc}", file=sys.stderr)
        return 2

    results = run_benchmark(cases, show_diff=args.diff)
    print_summary(results)
    write_markdown_report(results, args.report)

    if not results:
        return 2

    if all(result.passed for result in results):
        return 0

    if args.minimum_similarity is not None:
        average_similarity = sum(
            result.similarity for result in results
        ) / len(results)
        if average_similarity >= args.minimum_similarity:
            return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
