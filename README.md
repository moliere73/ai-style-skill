# AI Style Skill

A lightweight tool that rewrites AI-generated text using configurable style rules.

## Features

- Remove em dashes
- Simplify complex vocabulary
- Capitalize sentences
- Configurable with YAML
- Command-line interface
- Unit tested

## Example

Input:

```text
Furthermore, we utilize this feature—in order to facilitate communication.
```

Output:

```text
Also, we use this feature. To help communication.
```

## Usage

```bash
python main.py --text "Your text here"
```

## Configuration

Edit `style.yaml`:

```yaml
style:
  remove_em_dash: true
  simple_words: true
  capitalize_sentences: true
```

## Roadmap

- VS Code extension
- Browser extension
- API
- More style rules
- Multiple style profiles