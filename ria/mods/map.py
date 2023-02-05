# map


def home():
    x, y = 0, 0
    point = (x, y)
    return point


def north(point):
    """move north"""
    y = point[1] + 1
    point = (point[0], y)
    return point


def south(point):
    """move south"""
    y = point[1] - 1
    point = (point[0], y)
    return point


def east(point):
    """move east"""
    x = point[0] + 1
    point = (x, point[1])
    return point


def west(point):
    """move west"""
    x = point[0] - 1
    point = (x, point[1])
    return point


def check_boundry(x, y):
    """check if x or y are off the map"""
    if x in range(-2, 3) and y in range(-2, 3):
        return 0
    elif x > 2:
        text = "you REACHED THE OCEAN and cannot move further east"
        return text
    elif x < -2:
        text = "you REACHED THE OCEAN and cannot move further west"
        return text
    elif y > 2:
        text = "you REACHED THE OCEAN and cannot move further north"
        return text
    elif y < -2:
        text = "you REACHED THE OCEAN and cannot move further south"
        return text


def draw_row(coordinate, column):
    drawing = ""
    for x in range(-2, 3):
        if coordinate[0] == x and coordinate[1] == column:
            drawing += " X"
        else:
            drawing += " ."
    return drawing


def draw_grid(coordinate):
    for x in "abcde":
        if x == "a":
            print(draw_row(coordinate, 2))
        elif x == "b":
            print(draw_row(coordinate, 1))
        elif x == "c":
            print(draw_row(coordinate, 0))
        elif x == "d":
            print(draw_row(coordinate, -1))
        elif x == "e":
            print(draw_row(coordinate, -2))


# coordinate stack
class UsedCoordinates:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def use(self, item):
        self.items.append(item)

    def remove(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def validate(self, item):
        if item in self.items:
            # print('coordinate in use')
            return 1
        else:
            # print('coordinate available')
            return 0

    def used_coordinates(self):
        print(self.items)
        return self.items
