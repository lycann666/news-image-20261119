#!/usr/bin/env python3
"""Entry for make.fun news-image-20261119 (Python 3.13, standard library only).

Copies the front-page image shipped beside this file to the output
directory as entry.png. The grader runs the program twice and both runs
must write the same bytes; copying a fixed file guarantees that.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main():
    if not SOURCE.is_file():
        raise SystemExit(f"missing source image: {SOURCE}")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    dest = OUTPUT_DIR / "entry.png"
    shutil.copyfile(SOURCE, dest)
    if dest.stat().st_size != SOURCE.stat().st_size:
        raise SystemExit(f"copy verification failed: {dest} size differs from {SOURCE}")


if __name__ == "__main__":
    main()
