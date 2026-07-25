"""Command-line entry point for Expedition 33."""

import argparse

from gamebots.games.expedition_33.runner import run_farm


def main():
    parser = argparse.ArgumentParser(description="Expedition 33 EXP farming")
    parser.add_argument("--rounds", type=int, default=100)
    args = parser.parse_args()
    run_farm(rounds=args.rounds)


if __name__ == "__main__":
    main()
