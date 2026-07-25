"""Monster Hunter: World entry points."""

import time

from gamebots.games.monster_hunter_world import IcebloomBot, Tailraider


def countdown(seconds=3):
    for remaining in reversed(range(seconds)):
        print(f"Starting automation in {remaining + 1} seconds...")
        time.sleep(1)


def run_icebloom(big_rounds=20, camp_no=3, gather_item=False):
    countdown()
    bot = IcebloomBot(camp_no=camp_no)
    for round_index in range(big_rounds):
        print(f"Big Round {round_index + 1} =============")
        bot.run(gather_item=gather_item)


def run_tailraider(rounds=40):
    countdown()
    bot = Tailraider()
    for _ in range(rounds):
        bot.run()
