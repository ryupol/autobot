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


class FarmCoin2(Action):
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

        # Double Coin - ซื้อไอเทมแบบเป็นจังหวะ
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

        # Start Run
        self.press(
            "d",
            hold_time=human_delay(0.18, 0.28),
            release_delay=human_delay(0.15, 0.25),
        )
        self.wait(human_delay(0.7, 1.1))
        self.press(
            "d", hold_time=human_delay(0.15, 0.22), release_delay=human_delay(0.12, 0.2)
        )
        self.wait(human_delay(1.9, 2.2))

    def run(self):
        duration_minutes = human_delay(3.8, 4.5)
        end_time = time.time() + duration_minutes * 60
        is_already_paused = False

        while time.time() < end_time:
            # Dynamically pick a jump key for this action to mix things up
            jump_key = random.choice(["a", "space"])
            slide_key = "d"

            # Cookie Run specific gameplay patterns
            pattern = random.choices(
                ["single_jump", "double_jump", "short_slide", "long_slide", "panic"],
                weights=[20, 71, 3, 1, 5],
            )[0]

            if pattern == "single_jump":
                # Standard clear over an obstacle
                self.press(
                    jump_key,
                    hold_time=human_delay(0.08, 0.15),
                    release_delay=human_delay(0.1, 0.2),
                )
                self.wait(human_delay(0.18, 0.23))

            elif pattern == "double_jump":
                # First jump
                self.press(
                    jump_key,
                    hold_time=human_delay(0.08, 0.12),
                    release_delay=human_delay(0.05, 0.1),
                )
                # Brief pause at peak of the first jump
                self.wait(human_delay(0.04, 0.11))

                # Second jump (sometimes uses the other key, like a dual-finger press)
                next_jump = random.choice(
                    [jump_key, "space" if jump_key == "a" else "a"]
                )
                self.press(
                    next_jump,
                    hold_time=human_delay(0.09, 0.14),
                    release_delay=human_delay(0.1, 0.2),
                )
                self.wait(human_delay(0.09, 0.19))

            elif pattern == "short_slide":
                # D is slide: Quick duck under a low barrier
                self.press(
                    slide_key,
                    hold_time=human_delay(0.03, 0.1),
                    release_delay=human_delay(0.04, 0.19),
                )

            elif pattern == "long_slide":
                # D is slide: Holding down to slide through a long tunnel/under low ceiling
                self.press(
                    slide_key,
                    hold_time=human_delay(0.12, 0.23),
                    release_delay=human_delay(0.05, 0.21),
                )

            elif pattern == "panic":
                # Inhumanly rhythmic spamming gets flagged, so we add variance here
                for _ in range(random.randint(2, 4)):
                    self.press(
                        random.choice(["a", "space"]),
                        hold_time=human_delay(0.05, 0.09),
                        release_delay=human_delay(0.04, 0.08),
                    )
                self.wait(human_delay(0.09, 0.2))

            # Randomly trigger the emulator pause check (Esc key) like before
            if random.random() < 0.002:
                rest = human_delay(1, 29)
                end_time += rest

                self.press(
                    "esc",
                    hold_time=human_delay(0.09, 0.95),
                    release_delay=human_delay(0.08, 0.3),
                )
                print(f"Pausing for {rest:.0f} seconds...")
                self.wait(rest)

                # Unpause using the jump key or space
                self.press(
                    "space",
                    hold_time=human_delay(0.05, 0.45),
                    release_delay=human_delay(0.08, 0.3),
                )
                self.wait(human_delay(1, 1.3))

            self.wait(human_delay(0.08, 0.189))

        # Force End Run - กดปุ่มออกจากเกม
        self.press(
            "esc",
            hold_time=human_delay(0.17, 0.21),
            release_delay=human_delay(0.2, 0.3),
        )
        self.press(
            "o", hold_time=human_delay(0.12, 0.25), release_delay=human_delay(0.2, 0.3)
        )
        self.wait(human_delay(0.4, 1.2))
        self.press(
            "o", hold_time=human_delay(0.1, 0.23), release_delay=human_delay(0.2, 0.3)
        )

        self.wait(human_delay(2.5, 4.5))

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

        for _ in range(random.randint(7, 13)):
            self.press(
                "1",
                hold_time=human_delay(0.1, 0.2),
                release_delay=human_delay(0.3, 0.6),
            )
            self.wait(human_delay(0.9, 1.7))

        self.press(
            "q", hold_time=human_delay(0.18, 0.28), release_delay=human_delay(0.2, 0.3)
        )
        self.wait(human_delay(1.2, 2.2))


if __name__ == "__main__":
    for i in reversed(range(3)):
        print(f"Starting automation in {i + 1} seconds...")
        time.sleep(1)

    farm = FarmCoin2()

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
