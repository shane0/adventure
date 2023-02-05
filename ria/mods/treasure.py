import random

treasures = [
    "pirate gold and a ship to sail away",
    "the instructions for stonehenge and a 1950 rolls royce",
    "bags of diamonds and keys to the helicopter",
]


def random_treasure_area():
    """random treasure generator"""
    x = 0
    y = 0
    while x == 0:
        x = random.randint(-2, +2)
    while y == 0:
        y = random.randint(-2, +2)
    point = (x, y)
    return point


def random_treasure():
    reason = random.choice(treasures)
    return reason


def check_your_luck(booty, location):
    """did I find treasure?"""
    reward = random_treasure()
    if booty == location:
        text = "you find a treasure! ", reward
        return text
    else:
        return 0
