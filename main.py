from config import load_style
import argparse
from pathlib import Path

from rewriter import rewrite


def read_input(file_path: str | None, direct_text: str | None) -> str:
    if direct_text:
        return direct_text

    if file_path:
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"Input file not found: {file_path}")

        return path.read_text(encoding="utf-8")

    raise ValueError("Provide text with --text or a file with --file.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Rewrite text using a clear and concise AI writing style."
    )

    input_group = parser.add_mutually_exclusive_group(required=True)

    input_group.add_argument(
        "--text",
        help="Text to rewrite.",
    )

    input_group.add_argument(
        "--file",
        help="Path to a text file to rewrite.",
    )

    args = parser.parse_args()

    try:
        original_text = read_input(args.file, args.text)
        config = load_style()
        rewritten_text = rewrite(original_text, config)
        print(rewritten_text)
    except (FileNotFoundError, ValueError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()