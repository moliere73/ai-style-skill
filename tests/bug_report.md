# Bug Report

## Metadata

- **Profile:** `concise`
- **Status:** Pass

## Input

```text
When users click Submit multiple times, the application occasionally creates duplicate records. This appears to happen when the request takes longer than expected.
```

## Expected Output

```text
When users click Submit multiple times, the application occasionally creates duplicate records. This appears to happen when a slow request allows multiple submissions to be processed before the first request completes.
```

## Actual Output

```text
When users click Submit multiple times, the application occasionally creates duplicate records. This appears to occur when the request takes longer than expected, allowing multiple submissions to be processed before the initial request completes.
```

## Evaluation

- [x] Meaning preserved
- [x] Grammar is correct
- [x] Tone is appropriate
- [ ] Output fully matches the ideal rewrite

## Notes

Preserves the technical meaning and clarifies the likely cause. “Happen” would be slightly simpler than “occur.”

## Future Regression Check

After changing rewrite rules, rerun this input and confirm that the output does not introduce unsupported details, remove important meaning, or change the intended tone.
