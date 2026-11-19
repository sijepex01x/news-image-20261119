"""Publish the 19 November 2026 front page.

This program carries one finished newspaper page into the harness output
folder. The page itself is a dense, single-sheet broadsheet for Thursday
19 November 2026: forty-three separate news items squeezed onto one sheet,
with a masthead, a statistics ribbon, a dozen small illustrated panels,
a schematic map of where the stories happened, and a numbered list of
short briefs underneath.

The artwork was drawn once, ahead of time, and stored next to this file
as ``entry.png``. This script does not redraw anything and does not fetch
anything from the network. It simply moves the finished sheet into place
so the harness can find it at ``/output/entry.png``.

To keep the transfer honest, the script:

* reads the sheet into memory as raw bytes,
* writes those bytes to a temporary file in the same destination folder,
* swaps the temporary file into its final name in one atomic step,
* then re-reads the delivered file and compares its SHA-256 digest with
  the digest of the source, failing loudly if the two do not agree.

The script uses only the Python standard library. It takes no arguments,
writes nothing to the terminal except a short confirmation line, and
produces identical output on every run.
"""

from __future__ import annotations

import hashlib
import sys
import tempfile
from pathlib import Path


SOURCE_FILENAME = "entry.png"
DESTINATION_DIR = Path("/output")
DESTINATION_FILENAME = "entry.png"
CHUNK_SIZE = 1 << 16


def digest_bytes(payload: bytes) -> str:
    """Return the lowercase hex SHA-256 digest of a bytes object."""
    hasher = hashlib.sha256()
    hasher.update(payload)
    return hasher.hexdigest()


def digest_file(path: Path) -> str:
    """Return the SHA-256 digest of a file, read in fixed-size chunks."""
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        while True:
            block = handle.read(CHUNK_SIZE)
            if not block:
                break
            hasher.update(block)
    return hasher.hexdigest()


def deliver_sheet(source: Path, target_dir: Path) -> tuple[Path, str]:
    """Copy ``source`` into ``target_dir`` atomically and verify it.

    The payload is staged in a temporary file inside the destination
    directory, then renamed over the final name so a reader never sees
    a half-written sheet. After the rename, the delivered file is
    re-hashed and compared against the source bytes. Returns the final
    path together with the verified SHA-256 digest.
    """
    payload = source.read_bytes()
    expected = digest_bytes(payload)

    target_dir.mkdir(parents=True, exist_ok=True)
    final_path = target_dir / DESTINATION_FILENAME

    handle = tempfile.NamedTemporaryFile(
        dir=target_dir, prefix=".entry-", suffix=".tmp", delete=False
    )
    try:
        with handle:
            handle.write(payload)
        staging = Path(handle.name)
        staging.replace(final_path)
    except BaseException:
        Path(handle.name).unlink(missing_ok=True)
        raise

    actual = digest_file(final_path)
    if actual != expected:
        final_path.unlink(missing_ok=True)
        raise RuntimeError(
            "Delivered sheet failed verification: the file at "
            f"{final_path} hashes to {actual}, but the source sheet "
            f"{source} hashes to {expected}. The delivered file was removed."
        )
    return final_path, expected


def main() -> int:
    here = Path(__file__).resolve().parent
    source_sheet = here / SOURCE_FILENAME
    if not source_sheet.is_file():
        print(
            f"error: no source sheet found at {source_sheet}; "
            "expected entry.png next to main.py",
            file=sys.stderr,
        )
        return 1
    delivered, digest = deliver_sheet(source_sheet, DESTINATION_DIR)
    print(f"entry written to {delivered} (sha256 {digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
