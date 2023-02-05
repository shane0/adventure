import random
import mods.disasters as d

# text = ['whoa meteors', 'watch out for tornadoes', 'this is a medium sized island',
#         'watch out for sinkholes', 'i heard there are treasures here']


def random_npc_area():
    """random npc generator"""
    x = 0
    y = 0
    while x == 0:
        x = random.randint(-2, +2)
    while y == 0:
        y = random.randint(-2, +2)
    point = (x, y)
    return point


def random_npc():
    name = ["steve", "arthur", "claptrap"]
    insults = ["look", "smell", "act"]
    phrase = [
        " look at that, i dropped my compass somewhere keep an eye out for it and look out for ",
        " oh my gosh just look at this stuff and watch out for ",
        " look at that, i dropped my map somewhere, keep an eye out for it and look out for ",
        " just look at it, imagine that, look for the  ",
    ]
    text = ""
    text = "..."
    text += ("hi, my name is {name} ").format(name=random.choice(name))
    text += random.choice(phrase)
    text += d.die_by_natural_causes()
    text += " do you need some rest or a bath? you do not "
    text += random.choice(insults)
    text += " quite right "
    reason = text
    return reason


def check_your_npc(npc_location, location):
    """did I find treasure?"""
    npc = random_npc()
    if npc_location == location:
        text = "you find an npc! ", npc
        return text
    else:
        return 0
