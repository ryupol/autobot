"""Command-line entry point for Monster Hunter: World."""

import argparse

from gamebots.games.monster_hunter_world.runner import run_icebloom, run_tailraider


def main():
    parser = argparse.ArgumentParser(description="Monster Hunter: World automation")
    parser.add_argument("mode", choices=("icebloom", "tailraider"))
    parser.add_argument(
        "--rounds",
        type=int,
        help="Big rounds for Icebloom, interaction rounds for Tailraider",
    )
    parser.add_argument("--camp", type=int, default=3, help="Icebloom camp number")
    parser.add_argument(
        "--gather-item",
        action="store_true",
        help="Collect harvest and refill fertilizer during Icebloom farming",
    )
    args = parser.parse_args()

    if args.mode == "icebloom":
        run_icebloom(
            big_rounds=args.rounds if args.rounds is not None else 20,
            camp_no=args.camp,
            gather_item=args.gather_item,
        )
    else:
        run_tailraider(rounds=args.rounds if args.rounds is not None else 40)


if __name__ == "__main__":
    main()
