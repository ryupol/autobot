"""Shared Cookie Run round lifecycle."""

from abc import ABC, abstractmethod
import random

from gamebots.core import Action
from gamebots.games.cookie_run import strategy_config as _strategy_config


# Dynamic double-coin segment — resolves to the 4-step block or empty
# based on the current config value at import time.
_DOUBLE_COIN_STEPS = (
    ("key", "1"), ("key", "2"), ("key", "1"), ("load",),
) if _strategy_config.DOUBLE_COIN else ()


# Normal route — used 70 % of the time.
#   d, [1,2,1,<load>], d
NORMAL_ROUTE = (
    ("key", "d"),
    *_DOUBLE_COIN_STEPS,
    ("key", "d"),
)


# Alternate navigation routes to the Double Coin start. Every route eventually
# presses the play button; the varied prefixes/suffixes break the byte-identical
# start() macro that a bot detector can fingerprint across rounds.
#
# Step forms:
#   ("key", name)         -> press a menu key (with jitter + occasional hesitation)
#   ("wait", low, high)   -> pause a randomised amount (human orienting)
#   ("load",)             -> wait for the ~27s stage loading after the 1,2,1 block
#
# The `1,2,1` block selects Double Coin. If the selection was still cycling, the
# trailing `1` (or `d,d`) doubles as "press any button" to cancel and continue.
NAV_ROUTES = (
    # z, wait>=2s, b,b,b, d, [1,2,1,<load>], d, d
    (
        ("key", "z"), ("wait", 2.0, 2.8),
        ("key", "b"), ("key", "b"), ("key", "b"), ("key", "d"),
        *_DOUBLE_COIN_STEPS, ("key", "d"), ("key", "d"),
    ),
    # d, v, d, [1,2,1,<load>], d, d
    (
        ("key", "d"), ("key", "v"), ("key", "d"),
        *_DOUBLE_COIN_STEPS, ("key", "d"), ("key", "d"),
    ),
    # d, v, v, w, d, [1,2,1,<load>], d, d
    (
        ("key", "d"), ("key", "v"), ("key", "v"), ("key", "w"), ("key", "d"),
        *_DOUBLE_COIN_STEPS, ("key", "d"), ("key", "d"),
    ),
    # d, [1,2,1,<load>], v, v, w, d, d
    (
        ("key", "d"),
        *_DOUBLE_COIN_STEPS,
        ("key", "v"), ("key", "v"), ("key", "w"), ("key", "d"), ("key", "d"),
    ),
    # d, v, d, v, d, [1,2,1,<load>], d, d
    (
        ("key", "d"), ("key", "v"), ("key", "d"), ("key", "v"), ("key", "d"),
        *_DOUBLE_COIN_STEPS, ("key", "d"), ("key", "d"),
    ),
)


# Harmless home-screen detours: open a menu and back out. They add no farming
# value — their only job is to break the pure start/end loop so the behaviour
# isn't a metronome. Every route must land back on the episode home page.
DETOUR_ROUTES = (
    # open pet menu, close
    (("key", "p"), ("key", "b")),
    # open settings, close
    (("key", "q"), ("key", "w")),
    # open task menu, close
    (("key", "v"), ("key", "w")),
    # open task menu, route to common task, close
    (("key", "v"), ("key", "v"), ("key", "w")),
    # open settings, switch to game info, close
    (("key", "q"), ("key", "2"), ("key", "w")),
    # enter party run, pick solo race, quit back to home (needs settle waits)
    (
        ("key", "w"), ("wait", 3.5, 4.5),
        ("key", "o"), ("wait", 2.0, 3.0),
        ("key", "w"), ("wait", 3.5, 4.5),
    ),
)


class FarmCoinBase(Action, ABC):
    delay = staticmethod(lambda minimum, maximum: random.uniform(minimum, maximum))
    reward_press_range = (7, 13)
    reward_wait_range = (0.9, 1.7)
    starts_run_manually = True

    def __init__(self, **action_kwargs):
        super().__init__(**action_kwargs)
        self.release_delay = self.delay(0.25, 0.3)

    def _nav_press(self, key):
        """Press one navigation key with jitter and occasional hesitation."""
        if random.random() < 0.08:
            self.wait(self.delay(0.3, 0.9))
        self.press(
            key,
            hold_time=self.delay(0.15, 0.3),
            release_delay=self.delay(0.15, 0.28),
        )
        self.wait(self.delay(0.8, 1.2))

    def _human_taps(
        self,
        count,
        cadence,
        slowdown=(0.15, 0.4),
        hold=(0.06, 0.16),
        release=(0.05, 0.12),
        pause_chance=0.12,
        stray_chance=0.06,
        key="1",
    ):
        """Emit an irregular burst of taps that speeds up then tires out.

        Intervals are serially correlated (AR(1)) and drift upward with
        progress, so the burst clusters like a real hand instead of the
        uniform machine cadence a detector flags as a macro.
        """
        interval = self.delay(*cadence)
        last = max(1, count - 1)
        for index in range(count):
            self.press(
                key,
                hold_time=self.delay(*hold),
                release_delay=self.delay(*release),
            )
            progress = index / last
            target = self.delay(*cadence) + progress * self.delay(*slowdown)
            interval = 0.65 * interval + 0.35 * target

            if random.random() < pause_chance:
                self.wait(self.delay(0.4, 1.1))
            if random.random() < stray_chance:
                self.press(
                    key,
                    hold_time=self.delay(0.04, 0.09),
                    release_delay=self.delay(0.04, 0.08),
                )
            self.wait(interval)

    def start(self):
        if random.random() < 0.7:
            route = NORMAL_ROUTE
        else:
            route = random.choice(NAV_ROUTES)

        for step in route:
            kind = step[0]
            if kind == "load":
                self.wait(self.delay(25.5, 29.5))
                if not self.starts_run_manually:
                    return
            elif kind == "wait":
                self.wait(self.delay(step[1], step[2]))
            else:
                self._nav_press(step[1])

    def detour(self):
        """Poke a harmless home-screen menu and return, like an idle player."""
        route = random.choice(DETOUR_ROUTES)
        for step in route:
            if step[0] == "wait":
                self.wait(self.delay(step[1], step[2]))
            else:
                self._nav_press(step[1])

    @abstractmethod
    def run(self):
        """Play one game."""

    def end(self):

        # Close the result screen, then collect rewards — both as human-style
        self._human_taps(
            random.randint(*self.reward_press_range),
            cadence=self.reward_wait_range,
            slowdown=(0.06, 0.5),
            hold=(0.05, 0.2),
            release=(0.12, 0.6),
        )

        self.press(
            "q",
            hold_time=self.delay(0.18, 0.28),
            release_delay=self.delay(0.2, 0.3),
        )
        self.wait(self.delay(0.2, 1.6))

    def force_end_run(self):
        self.press(
            "esc",
            hold_time=self.delay(0.17, 0.21),
            release_delay=self.delay(0.2, 0.3),
        )
        self.press(
            "o",
            hold_time=self.delay(0.12, 0.25),
            release_delay=self.delay(0.2, 0.3),
        )
        self.wait(self.delay(0.4, 1.2))
        self.press(
            "o",
            hold_time=self.delay(0.1, 0.23),
            release_delay=self.delay(0.2, 0.3),
        )
        self.wait(self.delay(2.5, 4.5))
