# Slack Update

## Metadata

- **Profile:** `concise`
- **Status:** Pass

## Input

```text
Hey everyone, I just wanted to let you know that I finished the API integration and I'll be opening a pull request shortly.
```

## Expected Output

```text
Hey everyone,

I finished the API integration and will open a pull request shortly.
```

## Actual Output

```text
Hey everyone,

Just a quick update: I finished the API integration and will be opening a pull request shortly.
```

## Evaluation

- [x] Meaning preserved
- [x] Grammar is correct
- [x] Tone is appropriate
- [ ] Output fully matches the ideal rewrite

## Notes

Natural and appropriate for Slack. The phrase “Just a quick update” is optional but acceptable.

## Future Regression Check

After changing rewrite rules, rerun this input and confirm that the output does not introduce unsupported details, remove important meaning, or change the intended tone.
