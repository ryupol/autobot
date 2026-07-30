"""Cookie Run entry points."""

import random
import time

from gamebots.games.cookie_run import FarmCoin1, FarmCoin2, FarmCoin3


def countdown(seconds=5):
    for remaining in reversed(range(seconds)):
        print(f"Starting automation in {remaining + 1} seconds...")
        time.sleep(1)


def run_farm(farm_class, rounds=100, farm_kwargs=None):
    countdown()
    farm = farm_class(**(farm_kwargs or {}))
    for round_index in range(rounds):
        _run_round(farm, round_index)
        _rest_between_rounds(farm)


def run_mixed(rounds=100, farm_classes=(FarmCoin1, FarmCoin2, FarmCoin3)):
    countdown()
    for round_index in range(rounds):
        farm_class = random.choice(farm_classes)
        farm = farm_class()
        _run_round(farm, round_index, strategy_name=farm_class.__name__)
        _rest_between_rounds(farm)


def _run_round(farm, round_index, strategy_name=None):
    farm.start()
    farm.run()
    farm.end()
    suffix = f" (using {strategy_name})" if strategy_name else ""
    print(f"Round {round_index + 1} completed{suffix}.")


def _rest_between_rounds(farm):
    """Wait before the next round with a lumpy, human-like rhythm.

    Most gaps are short, but there is a real chance of a long idle (phone
    down) or a harmless menu detour, and sometimes almost no gap at all
    (a burst of quick rounds). This breaks the fixed start/end metronome.
    """
    if random.random() < 0.15:
        farm.detour()

    roll = random.random()
    if roll < 0.08:
        rest = farm.delay(5, 100)
        print(f"Idling for {rest / 60:.1f} minutes...")
    elif roll < 0.28:
        rest = farm.delay(0.5, 2.5)
    else:
        rest = farm.delay(3, 8)

    time.sleep(rest)
