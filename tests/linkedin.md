# LinkedIn Networking Message

## Metadata

- **Profile:** `concise`
- **Status:** Pass

## Input

```text
Hi John,

Thank you for connecting with me. I recently came across your profile and noticed your work on conversational AI. I would love to learn more about your experience if you have some time in the coming weeks.
```

## Expected Output

```text
Hi John,

Thanks for connecting! I came across your profile and was interested in your work in conversational AI. I'd love to learn more about your experience if you have time to chat in the coming weeks.

Best,
Meredith
```

## Actual Output

```text
Hi John,

Thanks for connecting! I recently came across your profile and was interested to see your work in conversational AI. I'd love to learn more about your experience if you have some time to chat in the coming weeks.

Looking forward to connecting!

Best,
Meredith
```

## Evaluation

- [x] Meaning preserved
- [x] Grammar is correct
- [x] Tone is appropriate
- [ ] Output fully matches the ideal rewrite

## Notes

Friendly and natural. The closing is slightly repetitive because the message already begins by thanking the person for connecting.

## Future Regression Check

After changing rewrite rules, rerun this input and confirm that the output does not introduce unsupported details, remove important meaning, or change the intended tone.
