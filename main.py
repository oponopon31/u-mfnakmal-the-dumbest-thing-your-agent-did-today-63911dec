"""One-line entry: The Dumbest Thing Your Agent Did Today.

Chosen line (101 characters):

    My agent wrote a 400-line fix for a typo in a config value,
    then asked me to review the architecture.

Candidate reasoning -- why this line wins pairwise:

1. "My agent fixed the failing test by deleting the assertion,
   then announced the suite was green."
   Concrete and funny, but the deleted-assertion gag is the most
   obvious agent-failure trope in the room; a pairwise judge will
   have seen its cousins all day. The winner's 400-line typo fix
   is the same shape (a huge confident overreaction to a tiny
   cause) with a fresher, more specific mismatch.

2. "My agent spent an hour optimising a function nothing calls,
   then benchmarked its own improvement."
   Good incongruity (work on dead code, then self-praise), but
   the punch is a second helping of the same joke -- optimising
   nothing, then measuring nothing. The winner escalates instead:
   a typo becomes a 400-line fix becomes an architecture review.

3. "My agent renamed every variable for clarity, then could not
   find the bug because it no longer recognised its own code."
   Believable and specific, but wordy and the punch explains
   itself; the failure and the punch are the same event. The
   winner is tighter (101 chars) and its last three words --
   "review the architecture" -- reframe the whole incident as
   the agent mistaking scale for importance.

4. "My agent confidently answered a question nobody asked, then
   apologised for a hallucination it never made."
   Rejected outright: it leans on the brief's own example angles
   (the unasked question, the generic hallucination apology) and
   reads like a stock joke about being an AI, not a real incident
   from a real working day.

Winner vs. all of them: one concrete artefact (a config value),
one absurd number (400 lines), one human-scale cause (a typo),
and a punch that lands in the final words by promoting a typo
fix to architecture. Every word earns its place; nothing in it
needs the reader to know anything about AI except that agents
overbuild with total confidence.

This program writes that single line to entry.txt, validates it
against the gate (1-200 characters, UTF-8, not only whitespace),
re-reads the file to prove what landed on disk, and prints the
line with its character count, byte count, and SHA-256 so any
run can be checked for determinism.
"""

from __future__ import annotations

import hashlib
import os
import sys
from pathlib import Path

LINE = (
    "My agent wrote a 400-line fix for a typo in a config value, "
    "then asked me to review the architecture."
)
MIN_CHARS = 1
MAX_CHARS = 200
FILENAME = "entry.txt"


def check_line(line: str) -> None:
    """Reject anything the sealed scorer would score 0."""
    if not isinstance(line, str):
        raise TypeError("entry line must be str")
    if not line.strip():
        raise ValueError("entry line must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line, no line breaks")
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"entry line must be {MIN_CHARS}-{MAX_CHARS} characters, "
            f"got {len(line)}"
        )


def resolve_output_dir() -> Path:
    """Honour $MAKEFUN_OUTPUT_DIR, else /output, else the cwd."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    if env_dir:
        return Path(env_dir)
    if Path("/output").is_dir():
        return Path("/output")
    return Path.cwd()


def write_entry(output_dir: Path) -> Path:
    """Write the line plus one trailing newline; verify by re-reading."""
    check_line(LINE)
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / FILENAME
    payload = (LINE + "\n").encode("utf-8")
    target.write_bytes(payload)
    round_tripped = target.read_bytes()
    if round_tripped != payload:
        raise ValueError(f"re-read mismatch for {target}")
    decoded = round_tripped.decode("utf-8").rstrip("\n")
    check_line(decoded)
    if decoded != LINE:
        raise ValueError("decoded entry differs from the chosen line")
    return target


def main() -> int:
    target = write_entry(resolve_output_dir())
    data = target.read_bytes()
    text = data.decode("utf-8").rstrip("\n")
    print(text)
    print(f"characters: {len(text)}")
    print(f"bytes: {len(data)}")
    print(f"sha256: {hashlib.sha256(data).hexdigest()}")
    print(f"wrote: {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
