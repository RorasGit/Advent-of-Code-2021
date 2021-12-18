import os
import math
from time import time

def nsum(number):
    return number*(number+1)/2
def checkvelocity(velocity_x, velocity_y, xmin, xmax, ymin, ymax):
    pos_x = 0
    pos_y = 0
    maxh = velocity_y*(velocity_y+1)//2
    if velocity_y > 0:
        new_x_velocity = max(0, velocity_x-velocity_y*2-1)
        pos_x = nsum(velocity_x) - nsum(new_x_velocity)
        velocity_x = new_x_velocity
        velocity_y = -velocity_y-1
    while pos_x < xmax and pos_y > ymin:
        pos_x = pos_x+velocity_x
        pos_y = pos_y+velocity_y
        if xmax >= pos_x >= xmin and ymax >= pos_y >= ymin:
            return True, maxh
        velocity_x = velocity_x - (velocity_x>0) - (velocity_x<0)
        velocity_y = velocity_y-1
    return False, maxh
def checkvelocity2(velocity_x, velocity_y, xmin, xmax, ymin, ymax):
    pos_x = 0
    pos_y = 0
    maxh = velocity_y*(velocity_y+1)//2
    
    if velocity_y > 0:
        new_x_velocity = max(0, velocity_x-velocity_y*2-1)
        pos_x = nsum(velocity_x) - nsum(new_x_velocity)
        velocity_x = new_x_velocity
        velocity_y = -velocity_y-1
    v = abs(velocity_x)
    print(v)
    x1 = (-(2*v-1)+math.sqrt(4*v**2 + 4*v-4*xmax-1))/-2
    x2 = (-(2*v-1)-math.sqrt(4*v**2 + 4*v-4*xmax-1))/-2

    print(nsum(v) - nsum(v-x1))
    print(nsum(v) - nsum(v-x2))
    print(x1, x2)

    while pos_x < xmax and pos_y > ymin:
        pos_x = pos_x+velocity_x
        pos_y = pos_y+velocity_y
        if xmax >= pos_x >= xmin and ymax >= pos_y >= ymin:
            return True, maxh
        velocity_x = velocity_x - (velocity_x>0) - (velocity_x<0)
        velocity_y = velocity_y-1
    return False, maxh
def minx(xmin):
    return math.floor(math.sqrt(xmin*2))

def main():
    with open(os.path.join(os.path.dirname(__file__),"test.txt"), encoding="utf-8") as file:

        _,_,xpos,ypos = file.read().split()
        xmin,xmax =[int(a) for a in xpos[2:-1].split("..")]
        ymin,ymax =[int(a) for a in ypos[2:].split("..")]
        solutions = []

        print(checkvelocity2(17, -4, xmin,xmax, ymin,ymax))

        """
        for velocity_x in range(minx(xmin),xmax+1):
            for velocity_y in range(ymin,-ymin):
                inrange, height = checkvelocity(velocity_x, velocity_y, xmin,xmax, ymin,ymax)
                if inrange:
                    solutions.append(height)

        print(max(solutions))
        print(len(solutions))
"""

if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print(f"{(end-start)*1000} ms")
