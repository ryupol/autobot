from pathlib import Path
import tempfile
import unittest

from gamebots.games.cookie_run.delays import (
    beta_delay,
    gaussian_delay,
    varied_beta_delay,
)
from gamebots.games.monster_hunter_world.base import MhwConfig
from gamebots.games.monster_hunter_world.icebloom import IcebloomBot


class FakeInput:
    def press_key(self, scan_code):
        pass

    def release_key(self, scan_code):
        pass

    def move_mouse(self, dx, dy):
        pass


class DelayTest(unittest.TestCase):
    def test_delay_distributions_stay_inside_requested_bounds(self):
        for delay in (gaussian_delay, beta_delay, varied_beta_delay):
            for _ in range(100):
                self.assertTrue(2 <= delay(2, 5) <= 5)


class MhwComponentTest(unittest.TestCase):
    def test_empty_loading_time_file_uses_default(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "loading_time.txt"
            path.write_text("", encoding="utf-8")
            self.assertEqual(MhwConfig.from_file(path).loading_time, 15)

    def test_icebloom_components_share_config_and_input(self):
        backend = FakeInput()
        config = MhwConfig(loading_time=9)
        bot = IcebloomBot(
            camp_no=3,
            config=config,
            backend=backend,
            sleeper=lambda _: None,
        )

        self.assertIs(bot.gather_item.config, config)
        self.assertIs(bot.relocate.config, config)
        self.assertIs(bot.quest.config, config)
        self.assertIs(bot.quest._backend, backend)
