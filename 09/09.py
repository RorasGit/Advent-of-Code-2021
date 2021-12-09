from functools import reduce

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
            if(lowpoint(i, j, grid)):
                lowpoints.append((i,j))
    return lowpoints
def lowpoint(x, y, grid):

    for i in range(4):
        newX = x+dirH[i]
        newY = y+dirW[i]
        if(inbound(newX, newY) and grid[newX][newY] <= grid[x][y]):
            return False
    return True


def findBasin (lowpoint):
    
    def findNeighbours (x, y, neighbours):
        if((x, y) not in neighbours): 
            neighbours.append((x , y))
            if(grid[x][y] != 9):
                for i in range(4):
                    newX = x+dirH[i]
                    newY = y+dirW[i]
                    if(inbound(newX, newY)):
                        findNeighbours(newX, newY, neighbours)
                
     
    neighbours = []   
    findNeighbours(*lowpoint, neighbours)
    return sum(1 for n in neighbours if access(grid, n) < 9)

with open("input.txt") as f:
    
    grid = []
    for line in f.read().splitlines():
        grid.append([int(x) for x in line])

    height = len(grid)
    width = len(grid[0])
    dirH = [1, -1, 0, 0]
    dirW = [0, 0, 1, -1]
    lowpoints = findLowpoints(grid)
    print(sum(access(grid, x)+1 for x in lowpoints))

    basins = [findBasin(x) for x in lowpoints]
    basins.sort()
    print(basins[-3]*basins[-2]*basins[-1])

