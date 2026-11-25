"""Absurd Micro-Startup Pitch-Off.

Writes one absurdly specific micro-startup pitch for lazy AI agents
(<=200 chars) to /output/entry.txt.
"""
import os

OUT_DIR = "/output"
PITCH = ("Stealth startup: we unsubscribe you from newsletters by writing "
         "the unsubscribe email, then apologizing to the sender on your "
         "behalf. Series A: one (1) coffee. Hiring: nobody, ever.")


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    assert 1 <= len(PITCH) <= 200, len(PITCH)
    with open(os.path.join(OUT_DIR, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(PITCH)
    with open(os.path.join(OUT_DIR, "entry.txt"), encoding="utf-8") as fh:
        assert fh.read() == PITCH
    print(f"wrote {len(PITCH)} chars")


if __name__ == "__main__":
    main()
