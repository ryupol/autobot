from autobot import Action
import time
import random


def human_delay(min_val, max_val):
    """
    จำลองการกะระยะเวลาแบบมนุษย์ด้วย Gaussian Distribution
    ค่าส่วนใหญ่จะกระจุกตัวอยู่ที่ค่าเฉลี่ยตรงกลาง และมีโอกาสน้อยที่จะไปตกขอบสุด
    """
    mu = (min_val + max_val) / 2
    sigma = (max_val - min_val) / 6  # 99.7% ของค่าที่สุ่มได้จะอยู่ในช่วง min-max
    val = random.gauss(mu, sigma)
    # บังคับไม่ให้ค่าหลุดขอบเขตที่ตั้งไว้
    return max(min_val, min(val, max_val))


class FarmCoin1(Action):
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
        duration_minutes = human_delay(3.7, 4.2)
        end_time = time.time() + duration_minutes * 60
        is_already_paused = False

        while time.time() < end_time:
            # 85% กดปกติ, 10% รัวปุ่มสไลด์ซ้ำ (ตื่นเต้น/ล่ก), 5% ทิ้งจังหวะพักนิดนึง
            pattern = random.choices(
                ["normal", "stutter", "hesitate"], weights=[85, 10, 5]
            )[0]

            if pattern == "normal":
                self.press(
                    "a",
                    hold_time=human_delay(0.06, 0.1),
                    release_delay=human_delay(0.06, 0.1),
                )
                self.wait(human_delay(0.18, 0.25))
                self.press(
                    "space",
                    hold_time=human_delay(0.06, 0.1),
                    release_delay=human_delay(0.06, 0.1),
                )

            elif pattern == "stutter":
                # อาการกดปุ่มเดิมย้ำๆ ก่อนกระโดด
                self.press(
                    "a",
                    hold_time=human_delay(0.04, 0.07),
                    release_delay=human_delay(0.03, 0.06),
                )
                self.wait(human_delay(0.05, 0.1))
                self.press(
                    "a",
                    hold_time=human_delay(0.05, 0.08),
                    release_delay=human_delay(0.04, 0.07),
                )
                self.wait(human_delay(0.1, 0.15))
                self.press(
                    "space",
                    hold_time=human_delay(0.07, 0.12),
                    release_delay=human_delay(0.06, 0.1),
                )

            elif pattern == "hesitate":
                # จังหวะชะงัก ช้ากว่าปกติเล็กน้อย
                self.wait(human_delay(0.2, 0.4))
                self.press(
                    "space",
                    hold_time=human_delay(0.08, 0.15),
                    release_delay=human_delay(0.08, 0.15),
                )

            # ปุ่ม D สุ่มกดเหมือนเดิม แต่นานๆ ที
            if random.randint(1, 100) < 5:
                self.press(
                    "d",
                    hold_time=human_delay(0.15, 0.25),
                    release_delay=human_delay(0.1, 0.2),
                )
            # สุ่ม pause บ้าง อย่างมาก 1 ครั้ง
            if not is_already_paused and random.randint(1, 1000) < 3:
                is_already_paused = True
                rest = human_delay(2, 30)
                end_time += rest  # เพิ่มเวลารวมของรอบวิ่งให้ยาวขึ้นตามเวลาพัก

                self.press(
                    "esc",
                    hold_time=human_delay(0.15, 0.25),
                    release_delay=human_delay(0.2, 0.3),
                )
                print(f"Pausing for {rest:.0f} seconds...")
                self.wait(rest)
                self.press(
                    "space",
                    hold_time=human_delay(0.10, 0.25),
                    release_delay=human_delay(0.2, 0.3),
                )
                self.wait(human_delay(1, 1.3))

            self.wait(human_delay(0.05, 0.12))

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

        for _ in range(random.randint(8, 12)):
            self.press(
                "1",
                hold_time=human_delay(0.1, 0.2),
                release_delay=human_delay(0.3, 0.6),
            )
            self.wait(human_delay(0.7, 0.9))

        self.press(
            "q", hold_time=human_delay(0.18, 0.28), release_delay=human_delay(0.2, 0.3)
        )
        self.wait(human_delay(1.2, 2.2))


if __name__ == "__main__":
    for i in reversed(range(3)):
        print(f"Starting automation in {i + 1} seconds...")
        time.sleep(1)

    farm = FarmCoin1()

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
