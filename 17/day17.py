import os
import math

def checkvelocity(speed, goal):
    maxy = 0
    pos = (0,0)
    while pos[0] < goal[0][1] and pos[1] > goal[1][0]:
        pos, speed = step(pos, speed)
        if pos[1] > maxy:
            maxy = pos[1]
        if goal[0][1] >= pos[0] >= goal[0][0] and goal[1][0] <= pos[1] <= goal[1][1]:
            return True, maxy

    return False, maxy

def step(pos, speed):
    drag = lambda a:(a>0) - (a<0)
    return (pos[0]+speed[0], pos[1]+speed[1]), (speed[0] - drag(speed[0]), speed[1]- 1 )

def minx(goal):
    return math.floor(math.sqrt(goal[0][0]*2))

def main():
    with open(os.path.join(os.path.dirname(__file__),"input.txt"), encoding="utf-8") as file:

        _,_,xpos,ypos = file.read().split()
        goal = ([int(a) for a in xpos[2:-1].split("..")],[int(a) for a in ypos[2:].split("..")])

        solutions = []
        for i in range(minx(goal),goal[0][1]+1):
            for j in range(goal[1][0],-goal[1][0]):
                inrange, height = checkvelocity((i, j), goal)
                if inrange:
                    solutions.append((i,j, height))

        print(max(solutions, key=lambda sol: sol[2]))
        print(len(solutions))



if __name__ == '__main__':
    main()
