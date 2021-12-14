
def main():
    with open(os.path.join(os.path.dirname(__file__),"input.txt", "r", encoding="utf-8") as file :
        content = file.read().splitlines()
        max_pos = 0
        vents = []
        for line in content:
            points = line.split("->")
            vent = []
            for point in points:
                pos = point.split(",")
                pos_x, pos_y = int(pos[0]),int(pos[1])
                vent.append((pos_x, pos_y))
                max_pos = max(max_pos, pos_x, pos_y)
            vents.append(vent)

        grid = [[0 for _ in range (0,max_pos+1)] for _ in range(0, max_pos+1)]
        diagonal_grid = [[0 for _ in range (0,max_pos+1)] for _ in range(0, max_pos+1)]

        for vent in vents:
            pos_x1 = vent[0][0]
            pos_x2 = vent[1][0]
            pos_y1 = vent[0][1]
            pos_y2 = vent[1][1]
            if(pos_x1 == pos_x2 or pos_y1 == pos_y2):
                for i in range (min(pos_x1, pos_x2), max(pos_x1,pos_x2)+1):
                    for j in range (min(pos_y1,pos_y2), max(pos_y1,pos_y2)+1):
                        grid[i][j] += 1
                        diagonal_grid[i][j] += 1
            else:
                for i in range (abs(pos_x1 - pos_x2)+1):
                    if pos_x1 > pos_x2:
                        if pos_y1 > pos_y2:
                            diagonal_grid[pos_x1-i][pos_y1-i] += 1
                        else:
                            diagonal_grid[pos_x1-i][pos_y1+i] += 1

                    else:
                        if pos_y1 > pos_y2:
                            diagonal_grid[pos_x1+i][pos_y1-i] += 1
                        else:
                            diagonal_grid[pos_x1+i][pos_y1+i] += 1


        print(sum(1 for x in grid for y in x if y > 1 ))
        print(sum(1 for x in diagonal_grid for y in x if y > 1 ))

if __name__ == '__main__':
    main()
