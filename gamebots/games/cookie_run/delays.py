"""Timing distributions used by Cookie Run strategies."""

import random


def gaussian_delay(minimum, maximum):
    mean = (minimum + maximum) / 2
    deviation = (maximum - minimum) / 6
    value = random.gauss(mean, deviation)
    return max(minimum, min(value, maximum))


def beta_delay(minimum, maximum):
    factor = random.betavariate(2, 5)
    return minimum + (maximum - minimum) * factor


def varied_beta_delay(minimum, maximum):
    if random.random() < 0.85:
        alpha = random.uniform(1.6, 2.6)
        beta = random.uniform(3.5, 6.5)
    else:
        alpha = random.uniform(0.9, 3.5)
        beta = random.uniform(0.9, 4.5)

    factor = max(0.0, min(1.0, random.betavariate(alpha, beta)))
    return minimum + (maximum - minimum) * factor
