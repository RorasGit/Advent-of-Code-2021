import numpy as np
from typing import Callable
from time import time
def execute(func: Callable) -> float:
  start = time()
  func()
  return time() - start
def time_fmt(delta: float):
  if delta < 1e-6:
    return 1e9, 'ns'
  elif delta < 1e-3:
    return 1e6, 'µs'
  elif delta < 1:
    return 1e3, 'ms'
  return 1, 'seconds'

def runBingo (bingos, balls) :
    victoryBingos = []
    for i in range(0, len(balls)):
        for value in (value for bingo in bingos for row in bingo for value in row if value[0] == balls[i]):
            value[1] = True
        for bingo in bingos:
            if(any(all(x[1] for x in row) for row in bingo) or any(all(x[1] for x in row) for row in np.swapaxes(bingo,0,1))):
                
                victoryBingos.append((i, sum(value[0] for row in bingo for value in row if not value[1])*balls[i]))
                bingos.remove(bingo) 
        if not len(bingos):
            break
    return victoryBingos


def main():
    with open("input.txt") as input :
        
        balls = [int(x) for x in next(input).split(",")]
        rows = list((list([int(c),False] for c in line.split()) for line in filter(None,input.read().splitlines())))
        bingo = [rows[x:x+5] for x in range(0, len(rows),5)]
        
        print(bingo[0])

        victoryBingos = runBingo(bingo, balls)


        print("Part 1:", min(victoryBingos, key=lambda x: x[0])[1])
        print("Part 2:", max(victoryBingos, key=lambda x: x[0])[1])

if __name__ == '__main__':
    t = execute(main)

    multiplier, unit = time_fmt(t)

    print(f"{t*multiplier} {unit}")
