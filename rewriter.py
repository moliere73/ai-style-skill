import re


WORD_REPLACEMENTS = {
    "utilize": "use",
    "utilizes": "uses",
    "utilized": "used",
    "approximately": "about",
    "furthermore": "also",
    "therefore": "so",
    "commence": "start",
    "terminate": "end",
    "facilitate": "help",
    "demonstrate": "show",
    "numerous": "many",
    "in order to": "to",
    "due to the fact that": "because",
}


def remove_em_dashes(text: str) -> str:
    """Replace em dashes with punctuation that is easier to read."""
    text = re.sub(r"\s*—\s*", ". ", text)
    return text


def simplify_words(text: str) -> str:
    phrase_replacements = {
        "in order to": "to",
        "reach out because I was wondering": "ask",
        "reach out to inquire about whether": "ask whether",
        "reach out in order to inquire about whether": "ask whether",
        "would like to take this opportunity to": "would like to",
        "there might potentially be": "there are",
        "regarding the status of my application": "on my application",
        "regarding my application": "on my application",
        "anything else that you might possibly require from me":
            "anything else you need from me",
        "I just wanted to let you know that": "",
        "I completely understand that": "I understand that",
    }

    word_replacements = {
        "Furthermore": "Also",
        "furthermore": "also",
        "utilize": "use",
        "numerous": "many",
        "facilitate": "help",
        "approximately": "about",
    }

    for original, replacement in phrase_replacements.items():
        text = text.replace(original, replacement)

    for original, replacement in word_replacements.items():
        text = text.replace(original, replacement)

    return text

def remove_repeated_spaces(text: str) -> str:
    """Clean up spacing introduced by other transformations."""
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\.\s*\.", ".", text)
    text = re.sub(r"\s+([,.!?])", r"\1", text)
    return text.strip()


def rewrite(text: str, config: dict) -> str:
    """Apply enabled style rules from the configuration."""
    result = text
    rules = config.get("style", {})

    if rules.get("remove_em_dash", False):
        result = remove_em_dashes(result)

    if rules.get("simple_words", False):
        result = simplify_words(result)

    result = remove_repeated_spaces(result)

    if rules.get("capitalize_sentences", False):
        result = capitalize_sentences(result) 

    if rules.get("remove_double_spaces", True):
        result = remove_double_spaces(result)

    return result

def capitalize_sentences(text: str) -> str:
    """Capitalize the first letter of each sentence."""
    parts = re.split(r"([.!?]\s+)", text)
    result = []

    for part in parts:
        if part and not re.fullmatch(r"[.!?]\s+", part):
            part = part[0].upper() + part[1:] if part else part
        result.append(part)

    return "".join(result) 

def remove_double_spaces(text: str) -> str:
    while "  " in text:
        text = text.replace("  ", " ")
    return text