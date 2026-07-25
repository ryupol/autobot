import time
import random

from cookieRun import FarmCoin1 as FarmCoinV1
from cookieRun2 import FarmCoin2 as FarmCoinV2
from cookieRun3 import FarmCoin3 as FarmCoinV3
from cookieRun4 import FarmCoin4 as FarmCoinV4


if __name__ == "__main__":
    for i in reversed(range(3)):
        print(f"Starting automation in {i + 1} seconds...")
        time.sleep(1)

    farm_classes = [FarmCoinV1, FarmCoinV2, FarmCoinV3]

    for i in range(100):
        FarmClass = random.choice(farm_classes)
        farm = FarmClass()

        farm.start()
        farm.run()
        farm.end()
        print(f"Round {i + 1} completed (using {FarmClass.__name__}).")

        if (i + 1) % random.randint(7, 12) == 0:
            rest = random.uniform(10, 60)
            print(f"Taking a human break for {rest:.0f} seconds...")
            time.sleep(rest)
        else:
            time.sleep(random.uniform(3, 7))
