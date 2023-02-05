---
tags:
  - python
---
# python

this is a retro game you play in the terminal

[download python code](./ria.zip){ .md-button }

or clone it

```sh
git clone https://github.com/shane0/adventure
```

## when this started

I made this retro game for the portfolio project assignment in the nucamp back end devops bootcamp

this was the first version of random island adventure

it is a python app played in the terminal

this was for the nucamp back end devops course portfolio projects

<iframe width="752" height="501" src="https://www.youtube.com/embed/kHC_aeUxyMI" title="python retro game - random island adventure nucamp devops workshop" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## code layout

```sh
├── main.py
├── mods
│   ├── disasters.py
│   ├── item.py
│   ├── map.py
│   ├── narrate.py
│   ├── npc.py
│   ├── player.py
│   └── treasure.py
└── readme.md
```

## `main.py`

- this is how you code when you're a noob
- this file is a hot mess but it works
- it does way too much
- maybe I'll explain it if I ever clean it up :)

## `mods/map.py`

- to start with an island...
- I made a "map", ironically I wanted to practice using the python built in type `map`[^1]
- this could be reused to create a space for any cartesian based game
- it allows you to move north, south, east and west

```py
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
```

### boundaries

- the map is infinite
- this code added borders for north, south, east and west

```py
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
```

### drawing the map (compass feature)

- later I added a compass that reveals the map
- this draws the draw a map
- this also provided a visual way to debug during development

```py
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
```

### map coordinate stack[^2]

- to make this a random island adventure, a treasure and disaster gets dropped on the map
- it was possible that they both land on the same location
- or even land on `0,0` where the player starts
- so I created a stack to store and validate used coordinates

```py
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
```

## `mods/`

I wanted to be able to plug these into other games so I put everything in `mods/`

in case later I make different themes, like a survival based hunt and gather game, or a crafty creative mode game, etc.

## `mods/player.py`

this tracks the player

## `mods/treasure.py`

games are for winning

## `mods/disasters.py`

games are less fun if you always win, this is basically a copy of treasure

## `mods/narrate.py`

for giggles

## `mods/item.py`

the only feature I actually implemented with items is the compass

if you find the compass, the map gets drawn

the idea with this was to tie it to `npcs.py` but that hasn't happened yet

## `mods/npc.py`

wip: later I'll do the typical game move, npcs give you quests, to go collect items, and return a reward...

[^1]:<https://docs.python.org/3/library/functions.html#map>
[^2]:<https://docs.python.org/3/tutorial/datastructures.html?highlight=stack#using-lists-as-stacks>
