
from functools import reduce
from statistics import median

values = {")": 3, "]":57, "}": 1197, ">": 25137, "(": 1, "[":2, "{": 3, "<": 4}
types = {"(":")", "{":"}", "<":">", "[": "]"}

def score(line):
    closeable = []
    for c in line:
        if c in types:
            closeable.append(c)
        else:
            if types[closeable.pop()] != c:
                return True, values[c]
    return False, reduce(lambda x, y: x * 5 + values[y], reversed(closeable), 0)

with open("input.txt") as f:
    
    scores = [score(line) for line in f.read().splitlines()]       

    print(sum([score for corrupted, score in scores if corrupted]))
    print(median([score for corrupted, score in scores if not corrupted]))
