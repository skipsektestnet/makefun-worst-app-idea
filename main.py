"""The Worst App Idea Ever Pitched: writes the entry text to /output/entry.txt.

Why this line: One sentence, a named product, founder-certain pitch, and a function nobody needs: plants rating their owner, plus a premium apology text to a fern.
"""

import os

# The entry itself: one line, punch at the end, no explanation.
ENTRY = 'Plumb: an app that lets your houseplants rate your watering technique in real time, with a premium tier that texts your fern an apology when you forget.'

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    assert 1 <= len(ENTRY) <= 240, "gate: entry must be 1-240 characters"
    assert "\n" not in ENTRY, "gate: entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
