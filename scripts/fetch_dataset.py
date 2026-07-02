#!/usr/bin/env python3
"""Fetch the full Hermetica ingredient + interaction datasets to local files.

The encyclopedia API serves both datasets live under CC BY-NC-SA 4.0, so this
just streams them to disk. No auth required.

Usage:
    python3 scripts/fetch_dataset.py --out ./data
"""
import argparse
import urllib.request
from pathlib import Path

BASE = "https://ingredients.hermeticasuperfoods.com/api/dataset"
FILES = ["ingredients.jsonl", "ingredients.csv", "interactions.jsonl", "interactions.csv"]


def fetch(name: str, out_dir: Path) -> None:
    url = f"{BASE}/{name}"
    dest = out_dir / name
    print(f"→ {url}")
    req = urllib.request.Request(url, headers={"User-Agent": "hermetica-dataset-fetch/1.0"})
    with urllib.request.urlopen(req) as resp, open(dest, "wb") as fh:
        total = 0
        while True:
            chunk = resp.read(1 << 16)
            if not chunk:
                break
            fh.write(chunk)
            total += len(chunk)
    print(f"  saved {dest} ({total:,} bytes)")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="./data", help="output directory")
    args = ap.parse_args()
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    for name in FILES:
        fetch(name, out_dir)
    print("done.")


if __name__ == "__main__":
    main()
