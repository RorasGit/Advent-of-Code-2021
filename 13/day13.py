import os

def flip_grid(grid, value, vertical):
    new_grid = {}
    for (x_pos, y_pos) in grid:
        new_x = 2 * value - x_pos if vertical and x_pos > value else x_pos
        new_y = 2 * value - y_pos if not vertical and y_pos > value else y_pos
        new_grid[(new_x, new_y)] = True
    return new_grid
def main():
    with open(os.path.join(os.path.dirname(__file__),"input.txt"), "r", encoding="utf-8") as file:

        lines, instructions = list(file.read().split("\n\n"))
        instructions = [line[11:].split("=") for line in instructions.split("\n")]
        grid =  {tuple(map(int, line.split(","))) : True for line in lines.split()}

        first = True
        for ins, value in instructions:
            grid = flip_grid(grid, int(value), ins == "x")
            if first:
                print(len(grid))
                first = False

        len_x = max(x for x,_ in grid)
        len_y = max(y for _,y in grid)
        for pos_y in range(len_y+1):
            row = ""
            for pos_x in range(len_x+1):
                if (pos_x, pos_y) in grid:
                    row += "1"
                else:
                    row += " "
            print(row)

if __name__ == '__main__':
    main()
