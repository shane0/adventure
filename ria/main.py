#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""random island adventure game"""

import sys
import os
import time
import random

import mods.player as p
import mods.item as i
import mods.map as m
import mods.narrate as n
import mods.disasters as d
import mods.treasure as tr
import mods.npc as npc

# debug = True
debug = False
# figlet app is optional and makes big ascii fonts
# install and set to true - apt install figlet - brew install figlet
figlet = True
# figlet = False

if debug == False:
    print("\033c")


def fig(let):
    command = f"figlet {let}"
    os.system(command)


if figlet == True:
    fig("teleporting...")
    time.sleep(0.4)
    fig("you")
    time.sleep(0.4)
    fig("to")
    time.sleep(0.5)

if debug == False:
    print("\033c")
if figlet == True:
    os.system("figlet RANDOM")
    os.system("figlet ISLAND")
    os.system("figlet ADVENTURE")
    time.sleep(1.5)
    print("\033c")

# used by mods to check if coordinates are already unused
coordinate_stack = m.UsedCoordinates()

# load home position 0,0
point = m.home()
coordinate_stack.use(point)
if debug == True:
    print(point)

# tracks movements for game states
full_track = []


# load character
nomer = ["zoomer", "boomer", "doomer"]
name = random.choice(nomer)
player_one = p.Player(name, 15)
if debug == False:
    print("\033c")
print(
    (
        """welcome {name} to rando island 3 
my name is Chip Diamond I'll show you around

you have {hp} hp but MOVEMENT DRAINS 1 HP

to move use -  n s e w 

find the TREASURE to win and avoid DISASTORS Or die

find the maps or compass to unlock skills 

encounter strange people press l to look around press ? to show this menu press q to quit
"""
    ).format(name=player_one.name, hp=player_one.hp)
)
print(
    """you are here:
. . . . .
. . . . .
. . X . .
. . . . .
. . . . .
"""
)

# drop items
treasure_map = i.Item("treasure_map")
disaster_map = i.Item("disaster_map")
compass = i.Item("compass")

if debug:
    print(i.Item.item_locations)

for key, value in i.Item.item_locations.items():
    coordinate_stack.use(value)


def check_for_drops(location):
    drop_check = ""
    for key, value in i.Item.item_locations.items():
        if location == value:
            drop_check = key
    return drop_check


def unlock_ability(item):
    """items unlock features"""
    # print(item)
    if item == "compass":
        player_one.add_ability("display_coordinates")
    elif item == "treasure_map":
        player_one.add_ability("display_treasure")
        print("THERE IS A TREAURE AREA LOCATED AT:")
        print(treasure_area)
    elif item == "disaster_map":
        player_one.add_ability("display_disaster")
        print("THERE IS A DISASTER AREA LOCATED AT:")
        print(disaster_area)


# load rando npc
npc_area = npc.random_npc_area()
npc_dude = npc.random_npc()
npc_area_two = npc.random_npc_area()
npc_dude_two = npc.random_npc()
npc_area_three = npc.random_npc_area()
npc_dude_three = npc.random_npc()
# regenerate coordinates if they are in use
while coordinate_stack.validate(npc_area) == 1:
    npc_area = npc.random_npc_area()
coordinate_stack.use(npc_area)
while coordinate_stack.validate(npc_area_two) == 1:
    npc_area_two = npc.random_npc_area()
coordinate_stack.use(npc_area_two)
while coordinate_stack.validate(npc_area_three) == 1:
    npc_area_three = npc.random_npc_area()
coordinate_stack.use(npc_area_three)

if debug == True:
    print(npc_dude)
    print("npc at")
    print(npc_area)
    print(coordinate_stack.validate(npc_area))
    print(npc_dude_two)
    print("npc two  at")
    print(npc_area_two)
    print(coordinate_stack.validate(npc_area_two))
    print(npc_dude_three)
    print("npc three at")
    print(npc_area_three)
    print(coordinate_stack.validate(npc_area_three))

# load rando treasure
reward = tr.random_treasure()
treasure_area = tr.random_treasure_area()
while coordinate_stack.validate(treasure_area) == 1:
    treasure_area = tr.random_treasure_area()
coordinate_stack.use(treasure_area)
if debug == True:
    print("treasure at")
    print(treasure_area)
    print(reward)

# load rando disaster
disaster_area = d.random_disaster_area()
while coordinate_stack.validate(disaster_area) == 1:
    disaster_area = d.random_disaster_area()
coordinate_stack.use(disaster_area)
cause_of_death = d.die_by_natural_causes()

if debug == True:
    print(cause_of_death)
    print("at")
    print(disaster_area)


if debug == True:
    coordinate_stack.used_coordinates()
    print("total 9: 1 home,2 maps, 1 compass, 1 disaster, 1 treasure, 3 npc")
    print(coordinate_stack.size())

# def move_checks(player, coordinate):


def move_checks(coordinate):
    """check stuff before moving"""
    global coordinate_stack
    global player_one
    global full_track
    if player_one.hp <= 0:
        if figlet == True:
            os.system("figlet whoops you STARVED TO DEATH!!")
        print("you survied for ", len(full_track), " moves")
        print("but adios sucker, you starved to death")
        print("add another smelly corpse to random island")
        print("you float up into the clouds playing a harp")
        sys.exit()
    global point
    global npc_area
    global npc_dude
    global disaster_area
    global cause_of_death
    global treasure_area
    global reward
    luck = d.test_your_luck(disaster_area, coordinate)
    drop = check_for_drops(coordinate)
    loot = tr.check_your_luck(treasure_area, coordinate)
    rando = npc.check_your_npc(npc_area, coordinate)
    rando_two = npc.check_your_npc(npc_area_two, coordinate)
    rando_three = npc.check_your_npc(npc_area_three, coordinate)
    # check movement
    # returns 0 if moving on map
    # returns message if hits boundry
    result = m.check_boundry(coordinate[0], coordinate[1])
    if result != 0:
        # hit boundry
        print(result)
        if debug == True:
            print("out of boundry")
            print("you remain at location ")
    if result == 0:
        # moving character
        if debug == False:
            print("\033c")
        if drop != "":
            player_one.add_item(drop)
            print(player_one.items)
            print(f"added {drop} to inventory")
            if figlet == True:
                os.system(f"figlet you found an item! {drop} ")
            response = n.narrate_item(drop)
            print(response)
            unlock_ability(drop)
        if luck != 0:
            # disaster
            print(luck)
            print("you survied for ", len(full_track), " moves")
            print("cya pshh...")
            if figlet == True:
                os.system("figlet YOU ARE DEAD")
            sys.exit()
        if loot != 0:
            # victory
            if figlet == True:
                os.system("figlet YOU WIN")
            print(loot)
            print("you won in ", len(full_track), " moves")
            print("here are you tracks")
            print(inputs)
            print(full_track)
            print("cya weiner... pfft... pshh...")
            sys.exit()
        if rando != 0:
            # npc
            print(rando)
            print("cya pshh...")
            # sys.exit()
        if rando_two != 0:
            # npc
            print(rando_two)
            print("adios pfft...")
            # sys.exit()
        if rando_three != 0:
            # npc
            print(rando_three)
            # sys.exit()
        if "display_coordinates" in player_one.abilities:
            print(m.draw_grid(coordinate))
            print("coordinates:", coordinate)
        player_one.move_hunger()
        point = movement_attempt
        print("you walk to a new area ")
        print(n.conditions())
        print(n.surroundings())
        if debug == True:
            print(point)
            return point
        full_track.append(coordinate)
        if debug == True:
            coordinate_stack.used_coordinates()


# cardinal navigation
inputs = []
while True:
    movement = input(
        """choose (n)orth (s)outh (e)ast or (w)est
    """
    )
    inputs.append(movement)
    if movement not in ["?", "n", "s", "e", "w", "l", "q", "compass"]:
        print("nsew")
    elif movement == "?":
        print(
            (
                """welcome {name} to Rando Island Adventure !
My name is Chip Diamond!
I'll be showing you around the island

to move around use - n s e w 

find the TREASURE and avoid DISASTORS Or die

you have {hp} hp and MOVEMENT DRAINS 1 HP

find maps or a compass, encounter strange people

press l to look around press ? to show this menu or q to quit
"""
            ).format(name=player_one.name, hp=player_one.hp)
        )
    elif movement == "n":
        movement_attempt = m.north(point)
        move_checks(movement_attempt)
    elif movement == "s":
        movement_attempt = m.south(point)
        move_checks(movement_attempt)
    elif movement == "e":
        movement_attempt = m.east(point)
        move_checks(movement_attempt)
    elif movement == "w":
        movement_attempt = m.west(point)
        move_checks(movement_attempt)
    elif movement == "l":
        print("you look around... ")
        lookie = n.look()
        print(lookie)
    elif movement == "q":
        break
        print("go figure, look at that quitter..")
    # cheat code for compass
    elif movement == "compass":
        player_one.add_ability("display_coordinates")
        print(treasure_area)
        print(disaster_area)
