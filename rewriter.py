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
    """Replace unnecessarily complex words with simpler alternatives."""
    result = text

    for complex_phrase, simple_phrase in WORD_REPLACEMENTS.items():
        pattern = re.compile(
            rf"\b{re.escape(complex_phrase)}\b",
            flags=re.IGNORECASE,
        )
        result = pattern.sub(simple_phrase, result)

    return result


def remove_repeated_spaces(text: str) -> str:
    """Clean up spacing introduced by other transformations."""
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\.\s*\.", ".", text)
    text = re.sub(r"\s+([,.!?])", r"\1", text)
    return text.strip()


def rewrite(text: str) -> str:
    """Apply all supported style rules."""
    result = remove_em_dashes(text)
    result = simplify_words(result)
    result = remove_repeated_spaces(result)
    result = capitalize_sentences(result)
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