"""Renoir's Draft merchant EXP farming workflow."""

from gamebots.core import Action


class FarmExp(Action):
    def __init__(self, **action_kwargs):
        super().__init__(**action_kwargs)
        self.release_delay = 0.3

    def first_dialog(self):
        self.press("f")
        self.wait(1)
        self.press("s")
        self.press("f")
        self.wait(1)

    def dialog(self):
        self.press("f")
        self.wait(0.3)
        self.press("f")
        self.wait(0.5)

    def fight(self):
        self.press("e", hold_time=2.5)
        for _ in range(3):
            self.press("d")
            self.wait(0.5)
        self.press("enter", hold_time=2.5)

        self.wait(5)
        self.press("e")
        self.press("e")
        self.press("f")
        self.wait(0.2)
        self.press("space")
        self.press("space")

        self.wait(5)
        self.press("f")
        self.wait(3)

    def run(self):
        self.dialog()
        self.fight()
