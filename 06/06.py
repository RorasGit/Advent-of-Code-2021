from collections import deque

with open("input.txt") as f:
    days = 256 
    state = deque([0] * 9)

    for x in next(f).split(","):
        state[int(x)] += 1

    for day in range(days):
        state.rotate(-1)
        state[6] += state[8]

        if day == 79:
            print(sum(state))

    print(sum(state))