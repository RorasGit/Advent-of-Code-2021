with open("input.txt") as input :
    content = input.read().splitlines()
    maxPos = 0
    vents = []
    for line in content:
        points = line.split("->")
        vent = []
        for point in points:
            pos = point.split(",")
            x, y = int(pos[0]),int(pos[1]) 
            vent.append((x, y))
            maxPos = max(maxPos, x, y)
        vents.append(vent)

    grid = [[0 for _ in range (0,maxPos+1)] for _ in range(0, maxPos+1)]
    diagonalGrid = [[0 for _ in range (0,maxPos+1)] for _ in range(0, maxPos+1)]

    
    for vent in vents:
        x1 = vent[0][0]
        x2 = vent[1][0] 
        y1 = vent[0][1]
        y2 = vent[1][1]
        if(x1 == x2 or y1 == y2):
            for i in range (min(x1, x2), max(x1,x2)+1):
                for j in range (min(y1,y2), max(y1,y2)+1):
                    grid[i][j] += 1
                    diagonalGrid[i][j] += 1
        else:
            for i in range (abs(x1 - x2)+1):
                if(x1 > x2):
                    if(y1 > y2):
                        diagonalGrid[x1-i][y1-i] += 1
                    else:
                        diagonalGrid[x1-i][y1+i] += 1

                else:
                    if(y1 > y2):
                        diagonalGrid[x1+i][y1-i] += 1
                    else:
                        diagonalGrid[x1+i][y1+i] += 1


    print(sum(1 for x in grid for y in x if (y > 1) ))
    print(sum(1 for x in diagonalGrid for y in x if (y > 1) ))