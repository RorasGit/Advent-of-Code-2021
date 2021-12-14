from collections import deque
import os
def main():
    with open(os.path.join(os.path.dirname(__file__),"input.txt"), "r", encoding="utf-8") as file:
        days = 256
        state = deque([0] * 9)

        for fish in next(file).split(","):
            state[int(fish)] += 1

        for day in range(days):
            state.rotate(-1)
            state[6] += state[8]

            if day == 79:
                print(sum(state))

        print(sum(state))

if __name__ == '__main__':
    main()
