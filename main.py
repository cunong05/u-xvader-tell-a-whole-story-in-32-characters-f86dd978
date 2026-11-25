from pathlib import Path

# Wi-Fi name entry: "Loved. Lost. Learned. Lived on." (31 chars)
ENTRY = "Loved. Lost. Learned. Lived on."

OUT_DIR = Path("/output")
OUT_FILE = OUT_DIR / "entry.txt"


def main() -> None:
    # Gate: 1 to 32 characters, not only white space.
    if not (1 <= len(ENTRY) <= 32) or not ENTRY.strip():
        raise ValueError(f"entry must be 1-32 chars, got {len(ENTRY)}: {ENTRY!r}")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(ENTRY, encoding="utf-8")
    print(ENTRY)


if __name__ == "__main__":
    main()
