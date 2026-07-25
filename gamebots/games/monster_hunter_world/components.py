"""Reusable Monster Hunter: World workflow components."""

from gamebots.games.monster_hunter_world.base import MhwBase


class Relocate(MhwBase):
    def __init__(self, config=None, **action_kwargs):
        super().__init__(config=config, **action_kwargs)
        self.release_delay = 0.3
        self.current_area = None

    def open_worldmap(self):
        self.press("m")
        self.wait(2)
        self.press("n")
        print("Open World Map")

    def select_area(self, area_name, down_presses=0):
        self.open_worldmap()
        self.interact()
        self.move_down(times=down_presses)
        self.current_area = area_name
        self.click_and_confirm()
        self.wait(8)
        print(f"Select Area: {area_name}")

    def run(self):
        print("Execute for reset position to 'Central Area'.")
        self.open_worldmap()
        self.select_area("Gathering Hub", 3)
        self.open_worldmap()
        self.select_area("Central Area", 0)


class GatherItem(MhwBase):
    def go_to_npc(self):
        print("Walking to Gathering NPC")
        self.press("w", hold_time=3.5)
        self.press("a", hold_time=0.6)
        self.wait(1)

    def talk_to_npc(self):
        print("Talk and skip gather NPC dialog")
        for _ in range(4):
            self.interact()
            self.wait(0.5)
        self.wait(0.5)

    def fill_fertilize(self):
        print("Fill fertilize in the botanical research area.")
        self.interact()
        self.wait(0.7)
        self.move_down()
        self.interact()
        self.wait(1)
        self.move_up()
        self.click_and_confirm()
        self.back()

    def collect_harvest(self):
        print("Collect harvested materials from the research center.")
        self.interact()
        self.move_up()
        self.interact()
        self.wait(1)
        self.move_up()
        self.click_and_confirm(default_no=True)
        self.confirm()
        self.back()

    def run(self):
        print("Execute the full gathering sequence.")
        self.go_to_npc()
        self.talk_to_npc()
        self.fill_fertilize()
        self.collect_harvest()
        self.exit()


class Quest(MhwBase):
    def __init__(self, quest_no, camp_no, is_online, config=None, **action_kwargs):
        super().__init__(config=config, **action_kwargs)
        self.quest_no = quest_no
        self.camp_no = camp_no
        self.is_online = is_online

    def gathering_to_quest(self):
        print("Walking from GatherItem to QuestBoard.")
        self.press("s", "d", hold_time=3.2)
        self.press("s", "a", hold_time=0.8)
        self.interact()

    def default_to_quest(self):
        print("Walking from Start to QuestBoard.")
        self.press("w", "d", hold_time=2)
        self.press("s", "d", hold_time=1)
        self.wait(0.2)
        self.interact()

    def select_quest(self):
        print("Select Quest from QuestBoard.")
        self.interact()
        self.wait(1.2)
        self.interact()
        self.wait(0.6)
        self.move_down(self.quest_no - 1)
        self.wait(0.6)
        self.confirm()
        if self.is_online:
            self.confirm()

        self.move_down(self.camp_no - 1)
        self.click_and_confirm()
        self.wait(self.loading_time // 3)

    def travel(self):
        self.press("space")
        self.wait(self.loading_time // 4)
        if self.is_online:
            self.move_down()
            self.interact()
        self.confirm()
        print("Go to do quest.")
        self.wait_for_loading()

    def run(self, from_gather_item=False):
        print("Execute Quest Journey.")
        if from_gather_item:
            self.gathering_to_quest()
        else:
            self.default_to_quest()
        self.select_quest()
        self.travel()


class Tailraider(MhwBase):
    def __init__(self, config=None, **action_kwargs):
        super().__init__(config=config, **action_kwargs)
        self.release_delay = 0.1

    def run(self):
        self.press("e")
        self.wait(2)
        for _ in range(18):
            self.press("f")
        self.wait(2.3)
