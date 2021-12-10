
from functools import reduce
from statistics import median

value = {"(": 1, "[": 2, "{": 3, "<": 4, ")": 3, "]": 57, "}": 1197, ">": 25137}
chunk = {"(": ")", "{": "}", "<": ">", "[": "]"}

def score(line):
    openedChunks = []
    for c in line:
        if c in chunk:
            openedChunks.append(c)
        else:
            if chunk[openedChunks.pop()] != c:
                return True, value[c]
    return False, reduce(lambda x, y: x * 5 + value[y], reversed(openedChunks), 0)

with open("input.txt") as f:
    
    scores = [score(line) for line in f.read().splitlines()]       

    print(sum(score for corrupted, score in scores if corrupted))
    print(median(score for corrupted, score in scores if not corrupted))
