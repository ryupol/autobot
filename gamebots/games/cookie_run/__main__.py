"""Command-line entry point for Cookie Run Classic."""

import argparse

from gamebots.games.cookie_run import FarmCoin1, FarmCoin2, FarmCoin3, FarmCoin4
from gamebots.games.cookie_run.runner import run_farm, run_mixed


STRATEGIES = {
    "1": FarmCoin1,
    "2": FarmCoin2,
    "3": FarmCoin3,
    "4": FarmCoin4,
}


def main():
    parser = argparse.ArgumentParser(description="Cookie Run Classic automation")
    parser.add_argument("strategy", choices=(*STRATEGIES, "mixed"))
    parser.add_argument("--rounds", type=int, default=100)
    args = parser.parse_args()

    if args.strategy == "mixed":
        run_mixed(rounds=args.rounds)
    else:
        run_farm(STRATEGIES[args.strategy], rounds=args.rounds)


if __name__ == "__main__":
    main()
