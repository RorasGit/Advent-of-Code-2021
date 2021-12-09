from functools import reduce
import heapq
def access(obj, indexes):
    def _get_item(subobj, index): 
        if isinstance(subobj, list) and index < len(subobj):
            return subobj[index]
        return None
    return reduce(_get_item, indexes, obj)

def inbound(i, size):
    return i < size and i >= 0 
def lowpoint(x, y, grid):

    height = len(grid)
    width = len(grid[0])
    if(inbound(x+1, height)):
        if(grid[x+1][y] <= grid[x][y]):
            return False
    
    if(inbound(x-1, height)):
        if(grid[x-1][y] <= grid[x][y]):
            return False
    
    if(inbound(y+1, width)):
        if(grid[x][y+1] <= grid[x][y]):
            return False
    
    if(inbound(y-1, width)):
        if(grid[x][y-1] <= grid[x][y]):
            return False
    return True

def findBasin (x, y, grid):
    
    def findNeighbours (x, y, grid, neighbours):
        height = len(grid)
        width = len(grid[0])
        if((x, y) not in neighbours): 
            neighbours.append((x , y))
            if(grid[x][y] != 9):
                if(inbound(x+1, height)):
                    findNeighbours(x+1, y, grid, neighbours)
            
                if(inbound(x-1, height)):
                    findNeighbours(x-1, y, grid, neighbours)
                
                if(inbound(y+1, width)):
                    findNeighbours(x, y+1, grid, neighbours)
                
                if(inbound(y-1, width)):
                    findNeighbours(x, y-1, grid, neighbours)
     
    neighbours = []   
    findNeighbours(x, y, grid, neighbours)
    return sum(1 for n in neighbours if access(grid, n) < 9)

with open("input.txt") as f:
    
    grid = []

    for line in f.read().splitlines():
        grid.append([int(x) for x in line])

    lowpoints = []
    height = len(grid)
    width = len(grid[0])
    for i in range(height):
        for j in range (width):
            if(lowpoint(i, j, grid)):
                lowpoints.append((i,j))
                
    print(sum(access(grid, x)+1 for x in lowpoints))
    print(reduce((lambda x, y: x * y),heapq.nlargest(3, [findBasin(*x, grid) for x in lowpoints])))

