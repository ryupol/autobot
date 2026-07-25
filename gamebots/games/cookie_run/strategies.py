"""Cookie Run gameplay strategy variants."""

import random
import time

from gamebots.games.cookie_run.base import FarmCoinBase
from gamebots.games.cookie_run.delays import (
    beta_delay,
    gaussian_delay,
    varied_beta_delay,
)


class FarmCoin1(FarmCoinBase):
    delay = staticmethod(gaussian_delay)
    reward_press_range = (8, 12)
    reward_wait_range = (0.7, 0.9)

    def run(self):
        end_time = time.time() + self.delay(3.7, 4.2) * 60
        is_already_paused = False

        while time.time() < end_time:
            pattern = random.choices(
                ["normal", "stutter", "hesitate"], weights=[85, 10, 5]
            )[0]

            if pattern == "normal":
                self.press(
                    "a",
                    hold_time=self.delay(0.06, 0.1),
                    release_delay=self.delay(0.06, 0.1),
                )
                self.wait(self.delay(0.18, 0.25))
                self.press(
                    "space",
                    hold_time=self.delay(0.06, 0.1),
                    release_delay=self.delay(0.06, 0.1),
                )
            elif pattern == "stutter":
                self.press(
                    "a",
                    hold_time=self.delay(0.04, 0.07),
                    release_delay=self.delay(0.03, 0.06),
                )
                self.wait(self.delay(0.05, 0.1))
                self.press(
                    "a",
                    hold_time=self.delay(0.05, 0.08),
                    release_delay=self.delay(0.04, 0.07),
                )
                self.wait(self.delay(0.1, 0.15))
                self.press(
                    "space",
                    hold_time=self.delay(0.07, 0.12),
                    release_delay=self.delay(0.06, 0.1),
                )
            else:
                self.wait(self.delay(0.2, 0.4))
                self.press(
                    "space",
                    hold_time=self.delay(0.08, 0.15),
                    release_delay=self.delay(0.08, 0.15),
                )

            if random.randint(1, 100) < 5:
                self.press(
                    "d",
                    hold_time=self.delay(0.15, 0.25),
                    release_delay=self.delay(0.1, 0.2),
                )

            if not is_already_paused and random.randint(1, 1000) < 3:
                is_already_paused = True
                rest = self.delay(2, 30)
                end_time += rest
                self.press(
                    "esc",
                    hold_time=self.delay(0.15, 0.25),
                    release_delay=self.delay(0.2, 0.3),
                )
                print(f"Pausing for {rest:.0f} seconds...")
                self.wait(rest)
                self.press(
                    "space",
                    hold_time=self.delay(0.10, 0.25),
                    release_delay=self.delay(0.2, 0.3),
                )
                self.wait(self.delay(1, 1.3))

            self.wait(self.delay(0.05, 0.12))

        self.force_end_run()


class PatternFarmCoin(FarmCoinBase):
    duration_range = (3.8, 4.5)
    initial_wait_range = None
    pattern_weights = (20, 71, 3, 1, 5)

    def run(self):
        end_time = time.time() + self.delay(*self.duration_range) * 60
        if self.initial_wait_range:
            self.wait(self.delay(*self.initial_wait_range))

        while time.time() < end_time:
            jump_key = random.choice(["a", "space"])
            pattern = random.choices(
                ["single_jump", "double_jump", "short_slide", "long_slide", "panic"],
                weights=self.pattern_weights,
            )[0]
            self._play_pattern(pattern, jump_key)

            if random.random() < 0.002:
                rest = self.delay(1, 29)
                end_time += rest
                self.press(
                    "esc",
                    hold_time=self.delay(0.09, 0.95),
                    release_delay=self.delay(0.08, 0.3),
                )
                print(f"Pausing for {rest:.0f} seconds...")
                self.wait(rest)
                self.press(
                    "space",
                    hold_time=self.delay(0.05, 0.45),
                    release_delay=self.delay(0.08, 0.3),
                )
                self.wait(self.delay(1, 1.3))

            self.wait(self.delay(0.08, 0.189))

        self.force_end_run()

    def _play_pattern(self, pattern, jump_key):
        if pattern == "single_jump":
            self.press(
                jump_key,
                hold_time=self.delay(0.08, 0.15),
                release_delay=self.delay(0.1, 0.2),
            )
            self.wait(self.delay(0.18, 0.23))
        elif pattern == "double_jump":
            self.press(
                jump_key,
                hold_time=self.delay(0.08, 0.12),
                release_delay=self.delay(0.05, 0.1),
            )
            self.wait(self.delay(0.04, 0.11))
            next_jump = random.choice(
                [jump_key, "space" if jump_key == "a" else "a"]
            )
            self.press(
                next_jump,
                hold_time=self.delay(0.09, 0.14),
                release_delay=self.delay(0.1, 0.2),
            )
            self.wait(self.delay(0.09, 0.19))
        elif pattern == "short_slide":
            self.press(
                "d",
                hold_time=self.delay(0.03, 0.1),
                release_delay=self.delay(0.04, 0.19),
            )
        elif pattern == "long_slide":
            self.press(
                "d",
                hold_time=self.delay(0.12, 0.23),
                release_delay=self.delay(0.05, 0.21),
            )
        else:
            for _ in range(random.randint(2, 4)):
                self.press(
                    random.choice(["a", "space"]),
                    hold_time=self.delay(0.05, 0.09),
                    release_delay=self.delay(0.04, 0.08),
                )
            self.wait(self.delay(0.09, 0.2))


class FarmCoin2(PatternFarmCoin):
    delay = staticmethod(beta_delay)


class FarmCoin3(PatternFarmCoin):
    delay = staticmethod(varied_beta_delay)
    initial_wait_range = (7, 9)
    pattern_weights = (91, 0, 3, 1, 5)
    reward_press_range = (9, 13)
    reward_wait_range = (0.7, 2.2)


class FarmCoin4(FarmCoinBase):
    delay = staticmethod(beta_delay)
    reward_press_range = (6, 11)
    reward_wait_range = (0.3, 0.6)
    starts_run_manually = False

    def run(self):
        load_key = random.choice(["0", "minus", "equals"])
        duration_minutes = self.delay(4.8, 4.9)
        self.press(
            "right_alt",
            load_key,
            hold_time=self.delay(0.1, 0.3),
            release_delay=self.delay(0.4, 0.6),
        )
        self.wait(60 * duration_minutes)
