"""User-editable settings for the Cookie Run farming strategies.

The values in this file control timing and behavior.  They are kept separate
from the strategy code so they can be tuned without changing the automation
logic.

Timing values are in seconds unless otherwise noted.  Range values are
inclusive in spirit: the selected delay distribution chooses a value between
the lower and upper bounds.
"""


# FarmCoin1: Gaussian timing with double jumps as the primary pattern.
FARM_COIN_1_DURATION_RANGE = (3.7, 4.2)  # Farming duration, in minutes.
# Pattern order: single jump, double jump, short slide, long slide, panic.
FARM_COIN_1_PATTERN_WEIGHTS = (90, 7, 2, 0, 1)
FARM_COIN_1_REWARD_PRESS_RANGE = (8, 12)  # Number of taps on the reward screen.
FARM_COIN_1_REWARD_WAIT_RANGE = (0.7, 0.9)  # Delay between reward-screen taps.


# PatternFarmCoin / FarmCoin2: shared gameplay configuration.
PATTERN_DURATION_RANGE = (3.8, 4.5)  # Farming duration, in minutes.
PATTERN_INITIAL_WAIT_RANGE = None  # Optional wait before farming starts.

# Pattern order: single jump, double jump, short slide, long slide, panic.
# Larger numbers make a pattern more likely to be selected.
PATTERN_WEIGHTS = (85, 11, 1.5, 0.5, 2)
PATTERN_BREAK_CHANCE = 0.0001  # Chance of taking a break after each pattern.
PATTERN_BREAK_RANGE = (1, 49)  # Break duration, in seconds.


# FarmCoin3: mostly single jumps and a longer, more variable reward cadence.
FARM_COIN_3_INITIAL_WAIT_RANGE = (7, 9)  # Wait before farming starts.
FARM_COIN_3_PATTERN_WEIGHTS = (100, 0, 0, 0, 0)
FARM_COIN_3_REWARD_PRESS_RANGE = (9, 13)
FARM_COIN_3_REWARD_WAIT_RANGE = (0.7, 2.2)


# FarmCoin4: manually loads a run, then waits for it to finish.
FARM_COIN_4_REWARD_PRESS_RANGE = (6, 11)
FARM_COIN_4_REWARD_WAIT_RANGE = (0.3, 0.6)
FARM_COIN_4_DURATION_RANGE = (4.8, 4.9)  # Farming duration, in minutes.


# FarmBox: idle strategy — no key presses, just waits for the run to finish.
FARM_BOX_DEFAULT_DURATION = 3.6  # Farming duration, in minutes (overridable via --time).


# Double Coin toggle. When True, routes include the 1,2,1 selection + load wait.
# When False, routes navigate directly to the play button.
DOUBLE_COIN = False
