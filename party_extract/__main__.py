import argparse
from pathlib import Path

from party_extract.engine import find_parties, render


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract the two named parties from a between-recital.")
    parser.add_argument("contract")
    parser.add_argument("--out", default="parties.json")
    args = parser.parse_args()
    parties = find_parties(Path(args.contract).read_text())
    Path(args.out).write_text(render(parties))
    print(f"{args.out}: {len(parties)} parties")


if __name__ == "__main__":
    main()
