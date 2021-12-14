from functools import reduce
import operator
import math

dirs = [(1,0),(-1,0), (0,1), (0,-1)]

def value(obj, indexes):
    def _get_item(subobj, index):
        if isinstance(subobj, list) and index < len(subobj):
            return subobj[index]
        return None
    return reduce(_get_item, indexes, obj)

def inbound(pos_x, pos_y, height, width):
    return 0 <= pos_x < width and 0 <= pos_y < height

def find_lowpoints(grid, height, width):
    lowpoints = []
    for i in range(height):
        for j in range (width):
            if find_lowpoint((i, j), grid, height, width):
                lowpoints.append((i,j))
    return lowpoints

def find_lowpoint(point, grid, height, width):
    for new_dir in [tuple(map(operator.add, dir, point)) for dir in dirs]:
        if inbound(*new_dir, height, width) and value(grid, new_dir) <= value(grid, point):
            return False
    return True

def find_basin (lowpoint, grid, height, width):

    def _find_neighbours (point, neighbours):
        if point not in neighbours:
            neighbours.append(point)
            if value(grid, point != 9):
                for new_point in [tuple(map(operator.add, dir, point)) for dir in dirs]:
                    if inbound(*new_point, height, width):
                        _find_neighbours(new_point, neighbours)

    neighbours = []
    _find_neighbours(lowpoint, neighbours)
    return sum(1 for n in neighbours if value(grid, n) < 9)


def main():
    with open("input.txt", "r", encoding="utf-8") as file:

        grid = []
        for line in file.read().splitlines():
            grid.append([int(x) for x in line])

        height = len(grid)
        width = len(grid[0])

        lowpoints = find_lowpoints(grid, height, width)
        print(sum(value(grid, point)+1 for point in lowpoints))

        basins = [find_basin(point, grid, height, width) for point in lowpoints]
        basins.sort(reverse=True)
        print(math.prod(basins[:3]))

if __name__ == '__main__':
    main()
