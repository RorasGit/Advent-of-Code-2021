
from typing import Counter
import os

adjecant =  [(1,0),(-1,0), (0,1), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)]


def flash(pos_x, pos_y, grid, flashed, height, width):
    if grid[pos_x][pos_y] > 9 and not flashed[(pos_x,pos_y)] :
        flashed[(pos_x, pos_y)] = True
        for pos_a, pos_b in [(dir[0]+pos_x, dir[1]+pos_y) for dir in adjecant] :
            if 0 <= pos_a < width and 0 <= pos_b < height:
                grid[pos_a][pos_b] +=1
                flash(pos_a, pos_b, grid, flashed, height, width)

def next_step(grid,  height, width):
    grid = [[x+1 for x in line] for line in grid]
    flashed = Counter()
    for pos_x in range(height):
        for pos_y in range(width):
            flash(pos_x, pos_y, grid, flashed, height, width)
    return len(flashed), [[0 if x > 9 else x for x in line] for line in grid]
def main():
    with open(os.path.join(os.path.dirname(__file__),"input.txt"), "r", encoding="utf-8") as file:

        octopuses  = [[int(x) for x in line] for line in file.read().splitlines()]
        height = len(octopuses)
        width = len(octopuses[0])

        total = 0
        for steps in range(1, 101):
            flashes, octopuses = next_step(octopuses, height, width)
            total += flashes

        print(total)
        while True:
            steps+=1
            flashes, octopuses = next_step(octopuses, height, width)
            if flashes == 100:
                break

        print(steps)

if __name__ == '__main__':
    main()
