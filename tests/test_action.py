import unittest

from gamebots.core import Action


class FakeInput:
    def __init__(self):
        self.events = []

    def press_key(self, scan_code):
        self.events.append(("press", scan_code))

    def release_key(self, scan_code):
        self.events.append(("release", scan_code))

    def move_mouse(self, dx, dy):
        self.events.append(("move", dx, dy))


class ActionTest(unittest.TestCase):
    def setUp(self):
        self.backend = FakeInput()
        self.sleeps = []
        self.action = Action(backend=self.backend, sleeper=self.sleeps.append)

    def test_press_translates_keys_and_preserves_event_order(self):
        self.action.press("w", "left_shift", hold_time=1.25, release_delay=0.1)

        self.assertEqual(
            self.backend.events,
            [
                ("press", 17),
                ("press", 42),
                ("release", 17),
                ("release", 42),
            ],
        )
        self.assertEqual(self.sleeps, [1.25, 0.1])

    def test_press_supports_loops_and_default_release_delay(self):
        self.action.release_delay = 0.2
        self.action.press("f", loops=2, hold_time=0.4)

        self.assertEqual(
            self.backend.events,
            [
                ("press", 33),
                ("release", 33),
                ("press", 33),
                ("release", 33),
            ],
        )
        self.assertEqual(self.sleeps, [0.4, 0.2, 0.4, 0.2])

    def test_move_mouse_delegates_to_backend(self):
        self.action.move_mouse(4, -2)
        self.assertEqual(self.backend.events, [("move", 4, -2)])
