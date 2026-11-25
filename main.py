#!/usr/bin/env python3
"""Snooze Button Roast — one line roasting an alarm clock for ringing at 6 AM on a Saturday."""

import os

LINE = "It's 6 AM on a Saturday and you're screaming like I owe you rent — relax, the only thing getting unplugged today is you."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
