# Cortical Style Manual Regression Tests

This directory contains manual regression tests for the Cortical Style rewrite engine.

## How to Use

1. Open a test file.
2. Run the text under **Input** through the specified profile.
3. Replace the text under **Actual Output** with the new result.
4. Compare it with **Expected Output**.
5. Update the status, checklist, and notes.
6. Run all tests again after changing rewrite rules.

## Status Definitions

- **Pass:** The output is acceptable and preserves meaning and tone.
- **Partial pass:** The output is usable but has a clear improvement opportunity.
- **Fail:** The output changes meaning, introduces unsupported details, or uses the wrong tone.

## Test Files

- `recruiter.md`
- `linkedin.md`
- `cover_letter.md`
- `readme.md`
- `bug_report.md`
- `slack.md`
- `performance_review.md`
- `customer_support.md`
- `documentation.md`
- `pull_request.md`
- `academic.md`
- `resume.md`
- `meeting_notes.md`
- `grammar.md`
- `long_sentence.md`
- `technical.md`
- `marketing.md`
- `stress_test.md`
