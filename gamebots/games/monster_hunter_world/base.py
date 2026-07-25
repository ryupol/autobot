"""Shared Monster Hunter: World controls and configuration."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path

from gamebots.core import Action


@dataclass(frozen=True)
class MhwConfig:
    loading_time: int = 15

    @classmethod
    def from_file(cls, path="loading_time.txt"):
        config_path = Path(path)
        if not config_path.exists():
            return cls()

        value = config_path.read_text(encoding="utf-8").strip()
        return cls(loading_time=int(value)) if value else cls()


class MhwBase(Action, ABC):
    def __init__(self, config=None, **action_kwargs):
        super().__init__(**action_kwargs)
        self.config = config or MhwConfig.from_file()
        self.release_delay = 0.2

    @property
    def loading_time(self):
        return self.config.loading_time

    def interact(self):
        self.press("f")
        self.wait(0.2)

    def confirm(self):
        self.press("f")
        self.wait(0.2)

    def back(self, times=1):
        self.press("esc", loops=times)
        self.wait(0.2)

    def exit(self):
        self.press("esc")
        self.wait(0.2)

    def wait_for_loading(self):
        self.wait(self.loading_time)

    def move_down(self, times=1):
        self.press("down", loops=times)

    def move_up(self, times=1):
        self.press("up", loops=times)

    def click_and_confirm(self, default_no=False):
        self.interact()
        if default_no:
            self.press("left")
        self.confirm()

    @abstractmethod
    def run(self):
        """Execute this component."""
