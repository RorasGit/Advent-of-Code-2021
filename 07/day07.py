import statistics as s
import math

def msum(fuel, moves):
    return sum(nsum(abs(x-fuel)) for x in moves)

def nsum(fuel):
    return int(fuel*(fuel+1)/2)
def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        moves = [int(x) for x in next(file).split(",")]
        median = int(s.median(moves))

        floor = math.floor(s.mean(moves))
        ceil =  floor+1


        print(sum(abs(x - median) for x in moves))
        print(min(msum(floor, moves), msum(ceil, moves)))

if __name__ == '__main__':
    main()
    