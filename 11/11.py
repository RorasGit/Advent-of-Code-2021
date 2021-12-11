
from typing import Counter

adjecant =  [(1,0),(-1,0), (0,1), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)]


def flash(x, y, grid, flashed):
    if grid[x][y] > 9 and not flashed[(x,y)] :
        flashed[(x, y)] = True
        for a, b in [(s[0]+x, s[1]+y) for s in adjecant] :
            if(0 <= a < width and 0 <= b < height):
                grid[a][b] +=1
                flash(a, b, grid, flashed)

def next_step(grid):
    grid = [[x+1 for x in line] for line in grid]
    flashed = Counter()
    for x in range(height):
        for y in range(width):
            flash(x, y, grid, flashed)
    return sum(flashed.values()), [[0 if x > 9 else x for x in line] for line in grid]

with open("input.txt") as f:
    
    octopuses  = [[int(x) for x in line] for line in f.read().splitlines()]
    height = len(octopuses)
    width = len(octopuses[0])
    
    total = 0
    for steps in range(1, 101):
        flashes, octopuses = next_step(octopuses)
        total += flashes

    print(total)
    while True:
        steps+=1
        flashes, octopuses = next_step(octopuses)
        if(flashes == 100):
            break
        
    print(steps)
