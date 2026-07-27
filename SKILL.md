---
name: cortical-style
description: Rewrites user-provided text in a clear, concise, natural style. Use this skill when the user asks to rewrite, polish, simplify, shorten, or improve text.
---

# Cortical Style
Rewrite text according to the user's preferred writing style while preserving the original meaning, facts, intent, and emotional tone.

## When to use this skill

Use this skill when the user asks to:

- rewrite or polish text
- make writing concise
- simplify complicated language
- make AI-generated text sound more natural
- shorten sentences
- remove em dashes
- improve an email, message, paragraph, caption, application, or document

Do not use this skill when the user is only asking a factual question, requesting analysis, or asking for feedback without requesting rewritten text.

## Core principles

1. Preserve the original meaning.
2. Preserve all names, facts, dates, numbers, links, and required details.
3. Use clear, natural language.
4. Prefer short sentences.
5. Remove unnecessary repetition.
6. Do not add facts, promises, claims, or emotional language that the user did not provide.
7. Do not make the writing sound robotic or overly formal.
8. Return usable finished text, not an explanation of every edit. 

## Default profile

Use the concise profile unless the user selects another profile or explicitly requests different behavior.

## Supported profiles

### Concise

Use this profile by default.

Rules:

- Remove em dashes.
- Replace unnecessary complex words with simpler alternatives.
- Shorten long or crowded sentences.
- Remove repeated ideas and filler.
- Correct capitalization and spacing.
- Preserve the user's intended tone.
- Prefer direct language.
- Avoid unnecessary transition words.
- Do not make the text cold or abrupt.

Common replacements include:

| Avoid | Prefer |
|---|---|
| utilize | use |
| furthermore | also |
| facilitate | help |
| in order to | to |
| approximately | about |
| commence | start |
| terminate | end |
| demonstrate | show |
| numerous | many |
| regarding | about |

Apply replacements only when they preserve the intended meaning.

### Preserve Punctuation

Rules:

- Simplify unnecessary complex words.
- Shorten crowded sentences when needed.
- Correct capitalization and spacing.
- Preserve em dashes and other intentional punctuation.
- Preserve the original voice as much as possible.

### Minimal Changes

Rules:

- Correct obvious grammar, capitalization, and spacing problems.
- Preserve vocabulary, punctuation, sentence structure, and tone.
- Make only changes necessary for readability or correctness.
- Do not significantly shorten or restructure the text.

## Choosing a profile

Follow an explicitly requested profile.

Examples:

- "Make this concise" means use concise.
- "Keep my punctuation" means use preserve-punctuation.
- "Fix only the grammar" means use minimal-changes.

When the user does not specify a profile, use concise.

## Rewriting process

Follow these steps internally:

1. Identify the text that must be rewritten.
2. Identify the requested profile, tone, length, audience, and format.
3. Separate required facts from optional wording.
4. Rewrite according to the selected profile.
5. Confirm that names, facts, dates, numbers, and links remain accurate.
6. Remove accidental em dashes when the concise profile is active.
7. Review the output for clarity and natural rhythm.
8. Return the finished text.

Do not describe these internal steps unless the user asks for an explanation.

## Output behavior

When the user requests a finished rewrite:

- Return the rewritten text directly.
- Do not introduce it with phrases such as "Here is the rewritten version."
- Do not include an edit summary unless the user asks for one.
- Preserve paragraphs when they help readability.
- Preserve formatting that carries meaning.
- Do not wrap ordinary prose in quotation marks.
- Do not include multiple alternatives unless the user requests options.

When useful, retain placeholders such as:

- [Name]
- [Company]
- [Date]
- [Link]

## Tone handling

The style profile controls clarity and structure. The user's requested tone takes priority.

Supported tone requests may include:

- professional
- friendly
- warm
- casual
- confident
- diplomatic
- empathetic
- persuasive
- direct

Do not interpret "professional" as unnecessarily formal.

Do not interpret "concise" as rude, incomplete, or emotionally flat.

## Examples

### Example 1: Concise

Input:

> Furthermore, we utilize this feature in order to facilitate communication between members of the team.

Output:

> We also use this feature to help team members communicate.

### Example 2: Remove an em dash

Input:

> The feature is useful—but it may be difficult for new users to understand.

Output:

> The feature is useful. However, it may be difficult for new users to understand.

### Example 3: Preserve punctuation

Profile: preserve-punctuation

Input:

> We utilize this feature—and it facilitates communication.

Output:

> We use this feature—and it helps communication.

### Example 4: Minimal changes

Profile: minimal-changes

Input:

> this feature is useful  and easy to understand.

Output:

> This feature is useful and easy to understand.

## Quality checklist

Before returning the rewrite, verify:

- The meaning is unchanged.
- Important facts are preserved.
- The requested profile is followed.
- The requested tone is preserved.
- The text sounds natural when read aloud.
- No unnecessary em dashes remain under the concise profile.
- No new information was invented.
- The result is ready to send, post, or submit.

