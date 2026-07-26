"""Cookie Run Classic gameplay strategy variants."""

import random
import time

from gamebots.games.cookie_run.base import FarmCoinBase
from gamebots.games.cookie_run.delays import (
    beta_delay,
    gaussian_delay,
    varied_beta_delay,
)
from gamebots.games.cookie_run.strategy_config import (
    FARM_COIN_1_DURATION_RANGE,
    FARM_COIN_1_PATTERN_WEIGHTS,
    FARM_COIN_1_REWARD_PRESS_RANGE,
    FARM_COIN_1_REWARD_WAIT_RANGE,
    FARM_COIN_3_INITIAL_WAIT_RANGE,
    FARM_COIN_3_PATTERN_WEIGHTS,
    FARM_COIN_3_REWARD_PRESS_RANGE,
    FARM_COIN_3_REWARD_WAIT_RANGE,
    FARM_COIN_4_DURATION_RANGE,
    FARM_COIN_4_REWARD_PRESS_RANGE,
    FARM_COIN_4_REWARD_WAIT_RANGE,
    PATTERN_DURATION_RANGE,
    PATTERN_BREAK_CHANCE,
    PATTERN_BREAK_RANGE,
    PATTERN_INITIAL_WAIT_RANGE,
    PATTERN_WEIGHTS,
)


def _slightly_varied_range(minimum, maximum, variation=0.02):
    """Return a nearby timing range with independently varied endpoints."""
    return (
        random.uniform(minimum - variation, minimum + variation),
        random.uniform(maximum - variation, maximum + variation),
    )


class PatternFarmCoin(FarmCoinBase):
    duration_range = PATTERN_DURATION_RANGE
    initial_wait_range = PATTERN_INITIAL_WAIT_RANGE
    pattern_weights = PATTERN_WEIGHTS

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

            if random.random() < PATTERN_BREAK_CHANCE:
                rest = self.delay(*PATTERN_BREAK_RANGE)
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


class FarmCoin1(PatternFarmCoin):
    """Pattern-based strategy using Gaussian timing variation."""

    delay = staticmethod(gaussian_delay)
    duration_range = FARM_COIN_1_DURATION_RANGE
    pattern_weights = FARM_COIN_1_PATTERN_WEIGHTS
    reward_press_range = FARM_COIN_1_REWARD_PRESS_RANGE

    def __init__(self, **action_kwargs):
        super().__init__(**action_kwargs)
        self.reward_wait_range = _slightly_varied_range(
            *FARM_COIN_1_REWARD_WAIT_RANGE
        )


class FarmCoin2(PatternFarmCoin):
    delay = staticmethod(beta_delay)


class FarmCoin3(PatternFarmCoin):
    delay = staticmethod(varied_beta_delay)
    initial_wait_range = FARM_COIN_3_INITIAL_WAIT_RANGE
    pattern_weights = FARM_COIN_3_PATTERN_WEIGHTS
    reward_press_range = FARM_COIN_3_REWARD_PRESS_RANGE

    def __init__(self, **action_kwargs):
        super().__init__(**action_kwargs)
        self.reward_wait_range = _slightly_varied_range(
            *FARM_COIN_3_REWARD_WAIT_RANGE
        )


class FarmCoin4(FarmCoinBase):
    delay = staticmethod(beta_delay)
    reward_press_range = FARM_COIN_4_REWARD_PRESS_RANGE
    starts_run_manually = False

    def __init__(self, **action_kwargs):
        super().__init__(**action_kwargs)
        # Keep the original 0.3-0.6s cadence, but vary each run very slightly.
        self.reward_wait_range = _slightly_varied_range(
            *FARM_COIN_4_REWARD_WAIT_RANGE
        )

    def run(self):
        load_key = random.choice(["0", "minus", "equals"])
        duration_minutes = self.delay(*FARM_COIN_4_DURATION_RANGE)
        self.press(
            "right_alt",
            load_key,
            hold_time=self.delay(0.1, 0.3),
            release_delay=self.delay(0.4, 0.6),
        )
        self.wait(60 * duration_minutes)
