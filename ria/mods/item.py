import random


class Item:
    item_locations = {}

    def __init__(self, name):
        self.name = name
        x = 0
        y = 0
        while x == 0:
            x = random.randint(-2, +2)
        while y == 0:
            y = random.randint(-2, +2)
        rando_coord = (x, y)
        self.coordinate = rando_coord
        self.item_locations[name] = self.coordinate
