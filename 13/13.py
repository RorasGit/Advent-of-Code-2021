def flipGrid(grid, value, vertical):
    newGrid = {}
    for (x, y) in grid:
        newX = x
        newY = y
        if(vertical and value < x):
            newX = value - (x - value)
        elif(not vertical and value < y):
            newY = value - (y - value)
        newGrid[(newX, newY)] = True
    return newGrid
with open("input.txt") as f:
    
    input, instructions = [line for line in f.read().split("\n\n")]
    instructions = [line[11:].split("=") for line in instructions.split("\n")]
    grid =  {tuple(map(int, line.split(","))) : True for line in input.split()}

    first = True
    for ins, value in instructions:
        grid = flipGrid(grid, int(value), ins == "x")
        if(first):
            print(len(grid))
            first = False

    lenX = max(x for x,_ in grid)+1
    lenY = max(y for _,y in grid)+1
    for y in range(lenY):
        row = ""
        for x in range(lenX):
            if (x, y) in grid:
                row += "1"
            else:
                row += " "
        print(row)





        