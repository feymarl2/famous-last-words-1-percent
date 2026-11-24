"""Famous Last Words at 1 Percent — make.fun entry.

Writes the approved one-line farewell (77 chars) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Python 3.13 stdlib only. No network, no clock, no randomness, no
environment reads besides the output directory: the same bytes every run.

Gate: /output/entry.txt must be UTF-8 text of 1 to 199 characters, not
only whitespace. This line is 77 characters, no trailing newline.
"""

import os

LINE = "Tell my charger I loved it, and tell my apps I never really liked any of you."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
