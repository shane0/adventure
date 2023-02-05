import random

disasters = [
    "sucked into a TORNADO",
    "shredded in an EARTHQUAKE",
    "falling forever donw a SINKHOLE",
    "washed to sea in a TSUNAMI",
    "drowned in a HURRICANE",
    "toasted by LIGHTNING",
    "melted in a FOREST FIRE",
    "pancaked by a METEOR",
    "ALIENS LAND and kidnap you as a pet for their bratty children",
]


def random_disaster_area():
    """random disaster area"""
    x = 0
    y = 0
    while x == 0:
        x = random.randint(-2, +2)
    while y == 0:
        y = random.randint(-2, +2)
    point = (x, y)
    return point


def die_by_natural_causes():
    reason = random.choice(disasters)
    return reason


def test_your_luck(disaster, location):
    """am I dead or alive"""
    cause_of_death = die_by_natural_causes()
    if disaster == location:
        text = "you die from a natural disaster, the cause of death is ", cause_of_death
        return text
    else:
        return 0
