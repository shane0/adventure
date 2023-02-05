import random


def narrate_item(item):
    """narrate finding an item"""
    adjectives = [
        " pretty ",
        " stinky ",
        " wonderful ",
        " fabulous ",
        " stupid ",
        " stupendous ",
        " rare ",
        " shiny ",
        " flippin ",
    ]
    lookatthat = [
        " pffft ",
        " pshh... ",
        " haah look at THAT ",
        " well look at this ",
        " would you look at that... ",
        " just look at it ",
        " oh my gosh, look at that ",
    ]
    response = ""
    response += random.choice(lookatthat)
    response = "\n"
    response += " you found a "
    response += random.choice(adjectives)
    response += item
    response = "\n"
    response += random.choice(lookatthat)
    return response


def look():
    stuff = [
        "prickly birds",
        "wiggly pizza ",
        "mice with 8 legs",
        "big insects with human shaped hands",
        "a swarm of ants playing rugby",
    ]
    adjectives = [
        " pretty ",
        " stinky ",
        " wonderful ",
        " fabulous ",
        " stupid ",
        " stupendous ",
        " rare ",
        " shiny ",
        " flippin ",
    ]
    lookatthat = [
        " pffft ",
        " pshh... ",
        " go figure... ",
        " haah look at THAT ",
        " well look at this ",
        " would you look at that... ",
        " just look at it ",
        " oh my gosh, look at that ",
    ]
    response = "\n"
    response += random.choice(lookatthat)
    response += random.choice(adjectives)
    response += random.choice(stuff)
    response += random.choice(lookatthat)
    return response


def surroundings():
    lookatit = [
        " wow look at THAT, what the heck is that! ",
        " well would you just look at this ",
        " look at that... ",
        " did you look at this? gosh just look at it ",
        " i just have to look at that ",
        " really look at that ",
        " unbelievable ",
        " get out of here ",
        " i could just look at that all day long ",
        " can you believe it ",
        " who would have thought ",
        " it is amazing ",
        " go figure... ",
    ]
    ground = [
        "rocky",
        "grassy",
        "muddy",
        "full of rolling mountains",
        "sandy",
        "a valley of flowers",
        "covered in leaves",
    ]
    colors = [" grey ", " dark green ", " brown ", " blueish ", " greenish "]
    cover = [" tall trees", " overhanging cliffs", " mist", " rolling fog"]
    response = random.choice(lookatit)
    response += " the land is "
    response += random.choice(ground)
    response = random.choice(lookatit)
    response = " covered in "
    response += random.choice(colors)
    response += random.choice(cover)
    response += random.choice(lookatit)
    return response


def conditions():
    lookatit = [
        "pffft",
        "pshh...",
        "haah look at THAT ",
        " well look at this ",
        " go figure... ",
        "would you look at that... ",
        "just look at it ",
        "oh my gosh, look at that ",
    ]
    look = random.choice(lookatit)
    lookagain = random.choice(lookatit)
    if look == lookagain:
        lookagain = random.choice(lookatit)

    sky = ["blue", "yellow", "orange", "red"]
    conditions = ["cloudy", "sunny", "raining", "snowing"]

    view = random.choice(sky)
    weather = random.choice(conditions)

    response = " you walk to a new area and "
    response += " " + look
    response = "\n"
    response += " the sky looks " + str(view) + " and it's " + str(weather)
    response += " ... " + lookagain
    return response
