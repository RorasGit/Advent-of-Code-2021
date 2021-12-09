from functools import reduce
import operator
def access(obj, indexes):
    def _get_item(subobj, index): 
        if isinstance(subobj, list) and index < len(subobj):
            return subobj[index]
        return None
    return reduce(_get_item, indexes, obj)

def inbound(x, y):
    return 0 <= x < width and 0 <= y < height

def findLowpoints(grid):
    lowpoints = []
    for i in range(height):
        for j in range (width):
            if(lowpoint((i, j), grid)):
                lowpoints.append((i,j))
    return lowpoints
    
def lowpoint(point, grid):
    for newDir in [tuple(map(operator.add, dir, point)) for dir in dir]:
        if(inbound(*newDir) and access(grid, newDir) <= access(grid, point)):
            return False
    return True

def findBasin (lowpoint):
    neighbours = []   
    findNeighbours(lowpoint, neighbours)
    return sum(1 for n in neighbours if access(grid, n) < 9)
    
def findNeighbours (point, neighbours):
        if(point not in neighbours): 
            neighbours.append(point)
            if(access(grid, point) != 9):
                for newDir in [tuple(map(operator.add, dir, point)) for dir in dir]:
                    if(inbound(*newDir)):
                        findNeighbours(newDir, neighbours)
                
     
with open("input.txt") as f:
    
    grid = []
    for line in f.read().splitlines():
        grid.append([int(x) for x in line])

    height = len(grid)
    width = len(grid[0])
    dir = [(1,0),(-1,0), (0,1), (0,-1)]

    lowpoints = findLowpoints(grid)
    print(sum(access(grid, point)+1 for point in lowpoints))

    basins = [findBasin(point) for point in lowpoints]
    basins.sort()
    print(basins[-3]*basins[-2]*basins[-1])

