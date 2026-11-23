"""One Line, Zero Use: The Useless Superpower Sprint.

Writes one original line naming a hilariously useless superpower to
entry.txt in the output directory (MAKEFUN_OUTPUT_DIR, default /output).
Standard library only. The line is judged on naming a useless superpower,
landing a laugh with a payoff in the last few words, freshness, tight
wording, and specific, vivid uselessness.

Chosen line: sensing Wi-Fi drops one second early — a "power" that helps
nobody, since knowing never prevents it. The twist lands on the last words.
"""

import os

LINE = "I can sense exactly when the Wi-Fi is about to drop \u2014 one second before it does."


def main() -> None:
    text = LINE.strip()
    if not text or len(text) > 200:
        raise SystemExit("entry line must be 1 to 200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    tmp = target + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(text)
    os.chmod(tmp, 0o644)  # readable by the grader even under a strict umask
    os.replace(tmp, target)


if __name__ == "__main__":
    main()
