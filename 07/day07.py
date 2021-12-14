import statistics as s
import math   

def msum(m, list):
    return sum(nsum(abs(x-m)) for x in list)

def nsum(n):
    return int(n*(n+1)/2)

with open("input.txt") as f:
    input = [int(x) for x in next(f).split(",")]
    median = int(s.median(input))

    floor = math.floor(s.mean(input))
    ceil =  floor+1


    print(sum(abs(x - median) for x in input))
    print(min(msum(floor, input), msum(ceil, input)))