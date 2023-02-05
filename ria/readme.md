# random island adventure

```sh
cd ria
python main.py
```

## story

you're on an island, Chip Diamond is your guide

you can move using (nsew) north, south, east and west to explore and find good and bad surprises

## figlet

optional program that requires installation

figlet draws ascii text - set `figlet=True` in main.py to use

`apt install figlet`

`brew install figlet`

## version three

- bugfix - objects do not spawn in home position (0,0)
- bugfix - multiple objects cannot spawn in the same location

## version two

- items
  - compass unlocks abilities
    - displays coordinates
    - reveals a map that displays position
  - treasure map reveals the coordinates of the treasure
  - disaster map reveals the coordinates of the disaster
- npc characters

## version one

- 5x5 x,y coordinate map with boundaries
- navigation
- narration
- treasures (to win)
- disasters (to lose)
