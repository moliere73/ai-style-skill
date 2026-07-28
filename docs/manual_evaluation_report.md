# Cortical Style -- Manual Evaluation Report

**Date:** 2026-07-28

## Objective

Evaluate the initial version of the Cortical Style rewrite engine using
realistic writing samples across multiple domains.

## Test Categories

-   Recruiter emails
-   LinkedIn networking messages
-   Cover letters
-   README documentation
-   Bug reports
-   Slack messages
-   Performance reviews
-   Customer support
-   Technical documentation
-   Pull request descriptions
-   Academic writing
-   Resume bullets
-   Meeting notes
-   Grammar correction
-   Long sentence simplification
-   Technical explanations
-   Marketing copy

## Summary

The current rewrite engine performs well on most practical writing
tasks.

### Strengths

-   Preserves the original meaning.
-   Produces natural, fluent English.
-   Removes unnecessary wording without changing intent.
-   Preserves technical accuracy.
-   Applies only minimal edits to already well-written text.

### Areas for Improvement

1.  Detect and remove repeated intentions (e.g., "follow up" + "check
    in").
2.  Split long sentences into shorter, more readable ones when
    appropriate.
3.  Prefer simpler verbs where meaning is unchanged (e.g., "occur" →
    "happen").
4.  Tighten marketing and promotional copy while preserving tone.

## Overall Assessment

  Category               Result
  ---------------------- -----------
  Meaning preservation   Excellent
  Grammar                Excellent
  Readability            Very Good
  Technical writing      Excellent
  Tone preservation      Very Good
  Over-editing           Low

**Overall score:** 9/10

## Next Steps

-   Expand the benchmark with 30--50 additional real-world examples.
-   Create regression tests using expected outputs.
-   Refine rewrite rules based on failed cases.
-   Add additional writing profiles (Professional, Executive, Plain
    English).
-   Continue iterating before adding new product features.

## Repository Suggestion

Save this file as:

`docs/manual_evaluation_report.md`

Commit message:

`Add initial manual evaluation report for Cortical Style`
