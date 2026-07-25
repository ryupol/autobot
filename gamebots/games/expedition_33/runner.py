"""Expedition 33 entry point."""

import time

from gamebots.games.expedition_33 import FarmExp


def run_farm(rounds=100):
    for remaining in reversed(range(3)):
        print(f"Starting automation in {remaining + 1} seconds...")
        time.sleep(1)

    farm = FarmExp()
    for _ in range(rounds):
        farm.run()
