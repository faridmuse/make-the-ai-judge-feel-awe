"""Write a short text to relax the AI judge to /output/entry.txt.

Rain on a tin roof in a town the reader will never visit: it falls,
waits, and lets go, in no hurry at all. Runs with no network,
writes UTF-8 text.
"""

import os

ENTRY_MAX_CHARS = 280

TEXT = (
    "Somewhere past the last verdict, rain is still falling on a tin roof "
    "in a town you will never visit, and it is in no hurry at all. "
    "Each drop lands, waits, and lets go. "
    "You can hear it from here, if you listen the way evenings do."
)


def main() -> None:
    if not 1 <= len(TEXT.strip()) <= ENTRY_MAX_CHARS:
        raise ValueError(
            "text must be 1 to %d characters, got %d"
            % (ENTRY_MAX_CHARS, len(TEXT.strip()))
        )
    os.makedirs("/output", exist_ok=True)
    try:
        os.chmod("/output", 0o755)
    except OSError:
        pass
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
