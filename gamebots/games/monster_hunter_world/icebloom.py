"""Icebloom farming workflow."""

import math

from gamebots.games.monster_hunter_world.base import MhwBase
from gamebots.games.monster_hunter_world.components import GatherItem, Quest, Relocate


class IcebloomBot(MhwBase):
    def __init__(self, camp_no, is_online=True, config=None, **action_kwargs):
        super().__init__(config=config, **action_kwargs)
        self.release_delay = 0
        self.camp_no = camp_no
        self.is_online = is_online
        shared_action = {"backend": self._backend, "sleeper": self._sleep}
        self.relocate = Relocate(config=self.config, **shared_action)
        self.gather_item = GatherItem(config=self.config, **shared_action)

    @property
    def quest(self):
        return Quest(
            quest_no=3,
            camp_no=self.camp_no,
            is_online=self.is_online,
            config=self.config,
            backend=self._backend,
            sleeper=self._sleep,
        )

    def pickup(self):
        print("Pick up Iceblooms")
        self.press("f", hold_time=13)
        self.wait(0.7)

    def camp7_zero_to_one(self):
        print("Going to icebloom 1...")
        self.press("w", "left_shift", hold_time=0.6)
        self.press("w", "d", "left_shift", hold_time=1.5)
        self.press("d", "left_shift", hold_time=2.3)
        self.wait(1.5)
        self.press("a", hold_time=1)
        self.press("a", "s", "left_shift", hold_time=8.5)
        self.press("s", hold_time=1.5)
        self.pickup()

    def camp7_one_to_two(self):
        print("Going to icebloom 2...")
        self.press("a", "left_shift", hold_time=7.5)
        self.wait(0.7)
        self.press("a", "s", hold_time=1.2)
        self.press("s", "left_shift", hold_time=1)
        self.pickup()

    def camp7_two_to_three(self):
        print("Going to icebloom 3...")
        self.press("a", hold_time=1.3)
        self.press("a", "s", "left_shift", hold_time=5.7)
        self.press("a", hold_time=1)
        self.pickup()

    def complete_quest(self):
        print("Getting Quest Reward...")
        self.wait(7)
        self.wait(20)
        presses = math.ceil((self.loading_time * 2) // 0.25)
        for _ in range(presses):
            self.press("f", hold_time=0.1)
            self.wait(0.1)
        self.wait(2)

    def abandon_quest(self):
        print("Reset the quest if it's not complete. (Just in case)")
        self.exit()
        self.wait(0.7)
        self.press("right")
        self.move_down()
        self.interact()
        self.confirm()
        self.back()
        self.wait(7)
        self.wait_for_loading()

    def camp7_progress(self):
        print("Let's Rock.")
        self.camp7_zero_to_one()
        self.camp7_one_to_two()
        self.camp7_two_to_three()
        self.complete_quest()
        self.abandon_quest()

    def run_quest(self, from_gather_item, i):
        print(f"Round {i + 1} -------------")
        self.quest.run(from_gather_item)
        if self.camp_no == 3:
            self.camp7_progress()

    def run(self, gather_item=False):
        for i in range(4):
            self.run_quest(from_gather_item=False, i=i)

        if gather_item:
            self.gather_item.run()
        self.run_quest(from_gather_item=gather_item, i=5)
