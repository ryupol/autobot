from autobot import Action
from abc import abstractmethod
import time


class MhwBase(Action):
    def __init__(self):
        super().__init__()
        self.loading_time = 10
        self.release_delay = 0.2

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
        pass


class Relocate(MhwBase):
    def __init__(self):
        super().__init__()
        self.release_delay = 0.3
        self.current_area = None

    def open_worldmap(self):
        self.press("m")
        self.wait(2)
        self.press("n")
        print("Open World Map")

    def select_area(self, area_name, down_presses=0):
        # Central Area: 0, Gathering Hub: 3
        self.open_worldmap()
        self.interact()  # Select Current Expedition
        self.move_down(times=down_presses)
        self.current_area = area_name
        self.click_and_confirm()
        self.wait(8)  # Wait for loading...
        print(f"Select Area: {area_name}")

    def run(self):
        print("Execute for reset position to 'Central Area'.")
        self.open_worldmap()
        self.select_area("Gathering Hub", 3)
        self.open_worldmap()
        self.select_area("Central Area", 0)


class GatherItem(MhwBase):
    def __init__(self):
        super().__init__()

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
        self.interact()  # Open Botanical Research
        self.wait(0.7)
        self.move_down()  # Select Fertilize
        self.interact()
        self.wait(1)
        self.move_up()
        self.click_and_confirm()
        self.back()  # exit and go back to main gather menu

    def collect_harvest(self):
        print("Collect harvested materials from the research center.")
        self.interact()  # Open Botanical Research
        self.move_up()
        self.interact()  # Select Collect
        self.wait(1)
        self.move_up()  # Move to Take All Button
        self.click_and_confirm(default_no=True)
        self.confirm()  # Click Exit
        self.back()  # Back

    def run(self):
        print("Execute the full gathering sequence.")
        self.go_to_npc()
        self.talk_to_npc()
        self.fill_fertilize()
        self.collect_harvest()
        self.exit()


class Quest(MhwBase):
    def __init__(self, quest_no, camp_no, is_online):
        super().__init__()
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

    # Select Quest
    def select_quest(self):
        print("Select Quest from QuestBoard.")
        self.interact()  # Post quest
        self.wait(1.2)
        self.interact()  # Enter to Current quest menu
        self.wait(0.6)
        self.move_down(self.quest_no - 1)
        self.wait(0.6)
        self.confirm()
        if self.is_online:
            self.confirm()

        self.move_down(self.camp_no - 1)  # Select Camp
        self.click_and_confirm()
        self.wait(3)

    def travel(self, offline=True):
        self.press("space")
        self.wait(2)
        if self.is_online:
            self.move_down()  # Select Depart
            self.interact()
        self.confirm()
        print("Go to do quest.")
        self.wait_for_loading()

    def run(self, start_point=None):

        print("Execute Quest Journey.")
        if start_point == "gather":
            self.gathering_to_quest()
        else:
            self.default_to_quest()
        self.select_quest()
        self.travel(offline=True)


class Icebloom7Bot(MhwBase):
    def __init__(self, quest_no=3, camp_no=3, is_online=True):
        self.release_delay = 0

        self.relocate = Relocate()
        self.gather_item = GatherItem()
        self.quest = Quest(quest_no, camp_no, is_online)

    def pickup(self):
        print("Pick up Iceblooms")
        self.press("f", hold_time=13)
        self.wait(0.7)

    def zero_to_one(self):
        print("Going to icebloom 1...")
        self.press("w", "left_shift", hold_time=0.6)
        self.press("w", "d", "left_shift", hold_time=1.5)
        self.press("d", "left_shift", hold_time=2)
        self.wait(1.5)
        self.press("a", hold_time=1)
        self.press("a", "s", "left_shift", hold_time=8.5)
        self.press("s", hold_time=1.5)
        self.pickup()

    def one_to_two(self):
        print("Going to icebloom 2...")
        self.press("a", "left_shift", hold_time=7.5)
        self.wait(0.7)
        self.press("a", "s", hold_time=1.2)
        self.press("s", "left_shift", hold_time=1)
        self.pickup()

    def two_to_three(self):
        print("Going to icebloom 3...")
        self.press("a", hold_time=1.3)
        self.press("a", "s", "left_shift", hold_time=5.7)
        self.press("a", hold_time=1)
        self.pickup()

    def complete_quest(self):
        print("Getting Quest Reward...")
        self.wait(20)  # Wait 20 second
        n = (self.loading_time * 2) // 0.25
        for _ in range(n):  # Spam get item (x2 time of loading)
            self.press("f", hold_time=0.1)
            self.wait(0.1)
        self.wait(2)

    def abandon_quest(self):
        print("Reset the quest if it's not complete. (Just in case)")
        self.exit()
        self.wait(0.7)
        self.press("right")
        self.move_down()
        self.interact()
        self.confirm()
        self.back()
        self.wait(5)  # Wait for animation
        self.wait_for_loading()

    def progress(self):
        print("Let's Rock.")
        self.zero_to_one()
        self.one_to_two()
        self.two_to_three()
        self.complete_quest()
        self.abandon_quest()  # Just in case the quest is not complete

    def run_quest(self, start_point, i):
        """Helper function to execute a quest run."""
        print(f"round {i+1} -----------")
        self.quest.run(start_point)
        self.progress()

    def run(self):
        i = 0
        for _ in range(5):
            # Run from starting point
            self.run_quest(start_point="start", i=i)
            i += 1

        # Gather items and run from "gather" to quest board point
        self.gather_item.run()
        self.run_quest(start_point="gather", i=i)


# === Automation Entry Point ===
if __name__ == "__main__":
    for i in reversed(range(3)):
        print(f"Starting automation in {i + 1} seconds...")
        time.sleep(1)

    """
    Quest No. => IceBroom: 3
    """
    bot = Icebloom7Bot()
    for i in range(1):  # 1 Big Round => 1000 Seconds or around 17 minutes.
        print(f"Big Round {i+1} =============")

        ## เลือกคำสั่ง
        # bot.run_quest(start_point="default")  # ฟาร์มเควสอย่างเดียว
        # bot.run()  # ฟาร์มเควส 5 รอบ + Refillปุ๋ยและเก็บเกี่ยว + วิ่งไปฟาร์มเควสอีกรอบ รวม 6 รอบ

        bot.run()
