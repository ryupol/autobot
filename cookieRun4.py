from autobot import Action
import time
import random

def human_delay(min_val, max_val):
    """
    Simulates authentic human delay using a right-skewed Beta Distribution.
    Eliminates edge-clipping spikes and creates a natural human reaction tail.
    """
    # alpha=2, beta=5 creates a perfect right-skewed curve
    # The value will naturally peak early and taper off smoothly toward max_val
    skewed_factor = random.betavariate(2, 5)

    return min_val + (max_val - min_val) * skewed_factor


class FarmCoin4(Action):
    def __init__(self):
        super().__init__()
        self.release_delay = human_delay(0.25, 0.3)

    def start(self):
        # Go prep - กดแบบน้ำหนักนิ้วปกติ
        self.press(
            "d",
            hold_time=human_delay(0.18, 0.28),
            release_delay=human_delay(0.15, 0.25),
        )
        self.wait(human_delay(0.8, 1.2))

        # Double Coin - ซื้อไอเทม
        self.press(
            "1", hold_time=human_delay(0.2, 0.3), release_delay=human_delay(0.18, 0.25)
        )
        self.wait(human_delay(0.2, 0.4))
        self.press(
            "2",
            hold_time=human_delay(0.15, 0.25),
            release_delay=human_delay(0.15, 0.25),
        )
        self.wait(human_delay(0.2, 0.4))
        self.press(
            "1",
            hold_time=human_delay(0.22, 0.32),
            release_delay=human_delay(0.18, 0.28),
        )
        self.wait(human_delay(25.5, 29.5))

        # # Start Run
        # self.press(
        #     "d",
        #     hold_time=human_delay(0.18, 0.28),
        #     release_delay=human_delay(0.15, 0.25),
        # )
        # self.wait(human_delay(0.7, 1.1))
        # self.press(
        #     "d", hold_time=human_delay(0.15, 0.22), release_delay=human_delay(0.12, 0.2)
        # )
        # self.wait(human_delay(1.9, 2.2))

    def run(self):
        rand_ld_key = random.choice(["0", "minus","equals"])

        duration_minutes = human_delay(4.8, 4.9)

        self.press(
            "right_alt",
            rand_ld_key,
            hold_time=human_delay(0.1, 0.3),
            release_delay=human_delay(0.4, 0.6),
        )

        self.wait(60 * duration_minutes)

    def end(self):
        # Collect reward
        self.press(
            "1", hold_time=human_delay(0.15, 0.25), release_delay=human_delay(0.4, 0.6)
        )
        self.wait(human_delay(0.4, 0.6))

        for _ in range(random.randint(3, 5)):
            self.press(
                "1",
                hold_time=human_delay(0.05, 0.15),
                release_delay=human_delay(0.12, 0.22),
            )
            self.wait(human_delay(0.1, 0.2))

        for _ in range(random.randint(6, 11)):
            self.press(
                "1",
                hold_time=human_delay(0.1, 0.2),
                release_delay=human_delay(0.3, 0.6),
            )
            self.wait(human_delay(0.3, 0.6))

        self.press(
            "q", hold_time=human_delay(0.18, 0.28), release_delay=human_delay(0.2, 0.3)
        )
        self.wait(human_delay(1.2, 2.2))


if __name__ == "__main__":
    for i in reversed(range(3)):
        print(f"Starting automation in {i + 1} seconds...")
        time.sleep(1)

    farm = FarmCoin4()

    for i in range(100):
        farm.start()
        farm.run()
        farm.end()
        print(f"Round {i + 1} completed.")

        # จำลองการพักสายตาของมนุษย์ระหว่างรอบ
        if (i + 1) % random.randint(7, 12) == 0:
            rest = human_delay(10, 60)
            print(f"Taking a human break for {rest:.0f} seconds...")
            time.sleep(rest)
        else:
            # พักปกติก่อนกดเริ่มรอบใหม่
            time.sleep(human_delay(3, 7))
