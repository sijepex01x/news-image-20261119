#!/usr/bin/env python3
"""Entry for make.fun bounty news-image-20261119.

Sums up 19 November 2026 world news in one dense daily front page:
43 stories, a stat strip, 12 illustrated tiles, a world map and a
numbered brief list. The image is held in this repository as entry.png
(1024x1024 PNG). Running this program copies it, byte for byte, to
/output/entry.png.

Deterministic: no network, no randomness, no timestamps, no generated
content. Two runs produce identical output bytes.
"""

import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
DEST_DIR = "/output"
DEST = os.path.join(DEST_DIR, "entry.png")


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    if not os.path.isfile(SOURCE):
        raise SystemExit("entry.png missing next to main.py")
    os.makedirs(DEST_DIR, exist_ok=True)
    # Copy through a temporary file and replace atomically, so a
    # failed run never leaves a partial /output/entry.png behind.
    # The copy is verified by size and by SHA-256 before the replace.
    tmp = DEST + ".tmp"
    shutil.copyfile(SOURCE, tmp)
    if os.path.getsize(tmp) != os.path.getsize(SOURCE):
        os.remove(tmp)
        raise SystemExit("entry.png copy is incomplete")
    if _sha256(tmp) != _sha256(SOURCE):
        os.remove(tmp)
        raise SystemExit("entry.png copy failed integrity check")
    os.replace(tmp, DEST)


if __name__ == "__main__":
    main()
