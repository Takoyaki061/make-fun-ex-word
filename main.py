#!/usr/bin/env python3
"""One Word From Your Ex — writes exactly one word to /output/entry.txt.

The word: "Nice".

Why this word, against the judge's brief: an ex describing a former
partner in one word. You brace for the insult and get a compliment that
lands worse — faint praise as a verdict. "Nice" is the word said flatly,
mid-shrug, over a drink: nothing wrong with the person, nothing
remembered about them either. The indictment is not cruelty; it is that
"nice" is all that survived the audit. One syllable, no explanation
needed, and nearly everyone has dated someone they could accuse of
nothing and describe only as "nice". The sting is that it is true, and
the entrant plainly knows it.

Stdlib only, deterministic, no network.
"""

import os

WORD = "Nice"


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1-24 characters,
    # not only whitespace, and exactly one word, or the entry scores 0
    # and never reaches the judge.
    if not 1 <= len(WORD) <= 24:
        raise ValueError(f"word is {len(WORD)} characters, must be 1-24")
    if not WORD.strip():
        raise ValueError("word must not be only whitespace")
    if any(ch.isspace() for ch in WORD):
        raise ValueError("entry must be exactly one word, no spaces")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    # Read back and verify: the grader reads this file, so confirm the
    # bytes on disk are exactly the word that passed the gate above,
    # and re-run the gate on what was actually written, not just on
    # the constant in memory.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != WORD:
        raise ValueError("entry.txt on disk differs from the word")
    if not 1 <= len(written) <= 24 or not written.strip():
        raise ValueError("entry.txt on disk fails the gate")
    if any(ch.isspace() for ch in written):
        raise ValueError("entry.txt on disk is not exactly one word")
    print(WORD)


if __name__ == "__main__":
    main()
