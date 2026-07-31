"""Command-line entry point for Cookie Run Classic."""

import argparse


def main():
    parser = argparse.ArgumentParser(description="Cookie Run Classic automation")
    parser.add_argument("strategy", choices=("1", "2", "3", "4", "box", "mixed"))
    parser.add_argument("--rounds", type=int, default=1000)
    parser.add_argument("--time", type=float, help="FarmBox duration in minutes")
    parser.add_argument("--no-double-coin", action="store_true")
    args = parser.parse_args()

    if args.no_double_coin:
        from gamebots.games.cookie_run import strategy_config
        strategy_config.DOUBLE_COIN = False

    from gamebots.games.cookie_run import FarmBox, FarmCoin1, FarmCoin2, FarmCoin3, FarmCoin4
    from gamebots.games.cookie_run.runner import run_farm, run_mixed

    STRATEGIES = {
        "1": FarmCoin1,
        "2": FarmCoin2,
        "3": FarmCoin3,
        "4": FarmCoin4,
        "box": FarmBox,
    }

    farm_kwargs = {}
    if args.strategy == "box" and args.time is not None:
        farm_kwargs["box_duration"] = args.time

    if args.strategy == "mixed":
        run_mixed(rounds=args.rounds)
    else:
        run_farm(STRATEGIES[args.strategy], rounds=args.rounds, farm_kwargs=farm_kwargs)


if __name__ == "__main__":
    main()
