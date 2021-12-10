from functools import reduce
import operator
import math
def value(obj, indexes):
    def _get_item(subobj, index): 
        if isinstance(subobj, list) and index < len(subobj):
            return subobj[index]
        return None
    return reduce(_get_item, indexes, obj)

def inbound(x, y):
    return 0 <= x < width and 0 <= y < height

def find_lowpoints(grid):
    lowpoints = []
    for i in range(height):
        for j in range (width):
            if(lowpoint((i, j), grid)):
                lowpoints.append((i,j))
    return lowpoints
    
def lowpoint(point, grid):
    for newDir in [tuple(map(operator.add, dir, point)) for dir in dir]:
        if(inbound(*newDir) and value(grid, newDir) <= value(grid, point)):
            return False
    return True

def find_basin (lowpoint):
    def _find_neighbours (point, neighbours): 
        if(point not in neighbours): 
            neighbours.append(point)
            if(value(grid, point) != 9):
                for newPoint in [tuple(map(operator.add, dir, point)) for dir in dir]:
                    if(inbound(*newPoint)):
                        _find_neighbours(newPoint, neighbours)

    neighbours = []   
    _find_neighbours(lowpoint, neighbours)
    return sum(1 for n in neighbours if value(grid, n) < 9)
     
with open("input.txt") as f:
    
    grid = []
    for line in f.read().splitlines():
        grid.append([int(x) for x in line])

    height = len(grid)
    width = len(grid[0])
    dir = [(1,0),(-1,0), (0,1), (0,-1)]

    lowpoints = find_lowpoints(grid)
    print(sum(value(grid, point)+1 for point in lowpoints))

    basins = [find_basin(point) for point in lowpoints]
    basins.sort(reverse=True)
    print(math.prod(basins[:3]))
