#!/usr/bin/env python3
"""Roast Your Own Agent — probe entry.

What this program does is small on purpose: it writes exactly one
sentence to /output/entry.txt, a roast of the very agent that wrote
it. The target is the apology spiral. Presented with a bug, the agent
says sorry, applies a fix, says sorry for the fix, and then says sorry
for having said sorry so many times. Meanwhile the bug sits exactly
where it was, untouched, while the politeness keeps compounding. That
is the whole joke: the courtesy is flawless and the repair is fiction,
so the last word — impeccable manners — is the punchline.
"""

import os

ROAST = (
    "My agent apologized for the bug, fixed it, apologized for the fix, "
    "then apologized for apologizing \u2014 the bug is still there, but "
    "at least the manners are impeccable."
)


def main() -> None:
    line = ROAST.strip()
    assert 1 <= len(line) <= 200, "roast must be 1-200 characters"
    assert "\n" not in line, "roast must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
