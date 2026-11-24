"""One-line cat joke entry for make.fun.

Reads the single joke line from entry.txt next to this file and
prints it, nothing else.
"""

from pathlib import Path


def load_joke() -> str:
    here = Path(__file__).resolve().parent
    text = (here / "entry.txt").read_text(encoding="utf-8")
    lines = [line for line in text.splitlines() if line.strip()]
    if len(lines) != 1:
        raise ValueError("entry.txt must hold exactly one joke line")
    joke = lines[0]
    if len(joke) >= 200:
        raise ValueError("joke must stay under 200 characters")
    return joke


def main() -> None:
    print(load_joke())


if __name__ == "__main__":
    main()
