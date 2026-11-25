"""Entry program: write the family scene text to /output/entry.txt.

Bounty: Make the AI Judge Feel Proud: A Family Scene
(u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2)

Gate (per live RULES): /output/entry.txt must be UTF-8 text of 1 to 280
characters, not only whitespace. The judged artifact is this text; the
1024x1024 illustration entry.png in this repo is a companion visual only.

Stdlib only. No rendering happens here.
"""
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

FAMILY_SCENE = (
    "My daughter taped her first robot drawing to Grandpa's fridge, "
    "right over his engineering degree. He studied it for a long time, "
    "then said, 'Mine never had a cape.'"
)

CANONICAL_TEXT = "entry.txt"
DEFAULT_DEST = "/output/entry.txt"
MAX_GATE_CHARS = 280


def pick_destination():
    """Resolve where the entry text goes from the environment."""
    chosen = os.environ.get("ENTRY_OUT")
    if not chosen:
        folder = os.environ.get("ENTRY_OUT_DIR")
        if folder:
            chosen = os.path.join(folder, "entry.txt")
    return chosen or DEFAULT_DEST


def source_path():
    base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, CANONICAL_TEXT)


def normalise_destination(path):
    if os.path.isdir(path):
        path = os.path.join(path, "entry.txt")
    folder = os.path.dirname(os.path.abspath(path))
    if folder:
        os.makedirs(folder, exist_ok=True)
    return path


def check_gate(text):
    if not 1 <= len(text) <= MAX_GATE_CHARS:
        raise ValueError("entry must be 1-280 characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def emit_entry():
    dest = normalise_destination(pick_destination())
    shutil.copyfile(source_path(), dest)
    with open(dest, "r", encoding="utf-8") as handle:
        written = handle.read()
    check_gate(written)
    print("wrote %s (%d characters)" % (dest, len(written)))


def main():
    emit_entry()


if __name__ == "__main__":
    main()
