from autobot import Action
from abc import abstractmethod
import time

# Farm by fighting the merchant in Renior's Draft
# more information: https://www.youtube.com/watch?v=_SijRHlymo4

""" Condition to use: 
        1. Maelle must use Phantom Strike skill 1 time to make all enemies die (try to find a way to do that) 
        2. the skill must be in E slot (lowest slot of left side)

# Note: To use this marco, You must manual fight the merchant 1 time first and go back by tap "F" (We Continue) just 1 time to go to dialog screen.
"""


class FarmExp(Action):
    def __init__(self):
        super().__init__()
        self.release_delay = 0.3

    def first_dialog(self):
        # Dialog talking
        self.press("f")
        self.wait(1)
        self.press("s")
        self.press("f")
        self.wait(1)

    def dialog(self):
        # Dialog talking
        self.press("f")
        self.wait(0.3)
        self.press("f")
        self.wait(0.5)

    def fight(self):
        # Start Fight Merchant
        self.press("e", hold_time=2.5)
        for _ in range(3):
            self.press("d")
            self.wait(0.5)
        self.press("enter", hold_time=2.5)

        # Fight
        self.wait(5)
        self.press("e")
        self.press("e")
        self.press("f")
        self.wait(0.2)
        self.press("space")
        self.press("space")

        # Go back
        self.wait(5)
        self.press("f")
        self.wait(3)


if __name__ == "__main__":
    for i in reversed(range(3)):
        print(f"Starting automation in {i + 1} seconds...")
        time.sleep(1)

    farm = FarmExp()

    for i in range(100):
        farm.dialog()
        farm.fight()
