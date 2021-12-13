from operator import itemgetter
def flipGrid(grid, value, vertical, maxX, maxY):
    for y in range(maxY):
        for x in range (maxX):
            if(grid[x][y] > 0):
                newX = x
                newY = y
                if(vertical):
                    newX = x - (x - value)*2
                else:
                    newY = y - (y - value)*2
                grid[x][y] = 0
                grid[newX][newY] = 1

with open("input.txt") as f:
    
    input, instructions = [line for line in f.read().split("\n\n")]
    
    instructions = [line[11:].split("=") for line in instructions.split("\n")]
    input = [tuple(int(x) for x in line.split(",")) for line in input.split("\n")]
    maxX = max(input,key=itemgetter(0))[0]+1
    maxY = max(input,key=itemgetter(1))[1]+1
    grid = [[0 for _ in range(maxY)] for __ in range(maxX)]

    for x, y in input:
        grid[x][y] = 1

    first = True
    for ins, value in instructions:
        vertical = ins == "x"
        flipGrid(grid, int(value), vertical, maxX, maxY)
        
        if(vertical):
            maxX = int(value)
        else:
            maxY = int(value)
        if(first):
            print(sum(sum(x) for x in grid))
            first = False
            
    for y in range(maxY):
        for x in range(maxX):
            if grid[x][y]:
                print(grid[x][y], end= '')
            else:
                print(" ", end='')
        print()





        