from collections import Counter

values = {")": 3, "]":57, "}": 1197, ">":25137, "(": 1, "[":2, "{": 3, "<":4}

def value(line):
    sum=0
    for c in line:
        sum = sum * 5 + values[c]
    return sum

with open("input.txt") as f:
    
    chunks = f.read().splitlines()
    types = {"(":")", "{":"}", "<":">", "[": "]"}
    failedRows = Counter()
    failedSum = 0
    unfinished = []
    
    for line in chunks:
        closeable = []
        ok = True
        for c in line:
            if c in types:
                closeable.append(c)
            else:
                if types[closeable.pop()] != c:
                    ok = False
                    failedSum += values[c]
                    break
        if(ok):
            unfinished.append(closeable)        

    sums = [value([x for x in line[::-1]]) for line in unfinished]
    sums.sort()

    print(failedSum)
    print(sums[len(sums)//2])
