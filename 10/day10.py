
from functools import reduce
from statistics import median

value = {"(": 1, "[": 2, "{": 3, "<": 4, ")": 3, "]": 57, "}": 1197, ">": 25137}
chunk = {"(": ")", "{": "}", "<": ">", "[": "]"}

def score(line):
    opened_chunks = []
    for token in line:
        if token in chunk:
            opened_chunks.append(token)
        elif chunk[opened_chunks.pop()] != token:
            return True, value[token]
    return False, reduce(lambda x, y: x * 5 + value[y], reversed(opened_chunks), 0)
def main():
    with open("input.txt", "r", encoding="utf-8") as file:

        scores = [score(line) for line in file.read().splitlines()]

        print(sum(score for corrupted, score in scores if corrupted))
        print(median(score for corrupted, score in scores if not corrupted))

if __name__ == '__main__':
    main()
