# Recruiter Follow-up

## Metadata

- **Profile:** `concise`
- **Status:** Partial pass

## Input

```text
Hi Sarah,

I hope you're doing well. I wanted to reach out because I was wondering if there have been any updates regarding my application. I completely understand that these processes take time, but I wanted to ask whether you need anything else from me.

Thank you for your time.

Best,
Meredith
```

## Expected Output

```text
Hi Sarah,

I hope you're doing well. I wanted to follow up to see if there are any updates on my application. I know these processes take time, but please let me know if you need anything else from me.

Thank you for your time. I appreciate it.

Best,
Meredith
```

## Actual Output

```text
Hi Sarah,

I hope you're doing well. I wanted to follow up to see if there are any updates on my application. I know these processes take time, but I wanted to check in and see if you need anything else from me.

Thank you for your time. I appreciate it.

Best,
Meredith
```

## Evaluation

- [x] Meaning preserved
- [x] Grammar is correct
- [x] Tone is appropriate
- [ ] Output fully matches the ideal rewrite

## Notes

Natural and polite, but it repeats the intention with both “follow up” and “check in.”

## Future Regression Check

After changing rewrite rules, rerun this input and confirm that the output does not introduce unsupported details, remove important meaning, or change the intended tone.
