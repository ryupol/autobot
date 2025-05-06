from autobot import Action
from abc import abstractmethod
import time


class Casino(Action):
    def loop(self):
        self.press("e")
        self.wait(1)
        self.move_mouse(820, 70)
        self.press("e")
        self.wait(1)
        self.move_mouse(900, 0)
        self.press("e")
        self.wait(1)
        self.move_mouse(1050, 50)
        self.press("e")
        self.wait(1)
        self.move_mouse(850, -60)
        self.press("e")
        self.wait(1)
        self.move_mouse(-3620, -60)


if __name__ == "__main__":
    for i in reversed(range(3)):
        print(f"Starting automation in {i + 1} seconds...")
        time.sleep(1)

    run = Casino()
    run.loop()
