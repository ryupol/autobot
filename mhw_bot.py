from mhw import IcebloomBot
import time

if __name__ == "__main__":

    for i in reversed(range(3)):
        print(f"Starting automation in {i + 1} seconds...")
        time.sleep(1)

    """
    - Quest No. => IceBroom: 3
        - Camp No. => Camp7: 3
    """

    # Edit your code here -------------------------------------------------------------

    bot = IcebloomBot(camp_no=3)
    for i in range(20):  # ถ้าใส่เลข 20 = วิ่ง 100 รอบ
        print(f"Big Round {i+1} =============")

        ## เลือกคำสั่ง
        # bot.run()  # ฟาร์มเควสอย่างเดียว 5 รอบ ต่อ 1 loop
        # bot.run(gather_item=True)  # ฟาร์มเควส 4 รอบ + Refillปุ๋ยและเก็บเกี่ยว + วิ่งไปฟาร์มเควสอีกรอบ รวม 5 รอบ
        bot.run()
