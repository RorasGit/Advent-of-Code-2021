from collections import Counter

val = {")": 3, "]":57, "}": 1197, ">":25137}
val2 = {")": 1, "]":2, "}": 3, ">":4}

def value(S):
    sum=0
    C = Counter(S)
    for c in val.keys():
        sum+= C[c]*val[c]
    return sum

def value2(S):
    sum=0
    for c in S:
        sum = sum * 5 + val2[c]
    return sum

with open("input.txt") as f:
    
    chunks = f.read().splitlines()
    types = {")":"(", "}":"{", ">":"<", "]": "["}
    typesInv = {v: k for k, v in types.items()}
    fail = ""
    unfinished = []
    
    for line in chunks:
        closeable = []
        ok = True
        for c in line:
            if c in types.values():
                closeable.append(c)
            else:
                if types[c] == closeable[-1]:
                    closeable.pop()
                else:
                    ok = False
                    fail += c
                    break
        if(ok):
            unfinished.append(closeable)        

    sums = [value2([typesInv[x] for x in line[::-1]]) for line in unfinished]
    sums.sort()

    print(value(fail))
    print(sums[len(sums)//2])