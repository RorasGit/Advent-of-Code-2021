def flipGrid(grid, value, vertical):
    newGrid = {}
    for (x, y) in grid:
        newX = 2 * value - x if vertical and x > value else x
        newY = 2 * value - y if not vertical and y > value else y
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

    lenX = max(x for x,_ in grid)
    lenY = max(y for _,y in grid)
    for y in range(lenY+1):
        row = ""
        for x in range(lenX+1):
            if (x, y) in grid:
                row += "1"
            else:
                row += " "
        print(row)





        