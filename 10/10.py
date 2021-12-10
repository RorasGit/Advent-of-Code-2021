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
    
    types = {")":"(", "}":"{", ">":"<", "]": "["}
    fail = ""

    chunks = f.read().splitlines()
    for line in chunks:
        closeable = []
        open = {"(":0, "{":0, "<":0, "[": 0}
        for c in line:
            if c in types.values():
                open[c] += 1
                closeable.append(c)
            else:
                if types[c] == closeable[-1]:
                    if open[types[c]] > 0:
                        open[types[c]] -= 1
                        closeable.pop()
                    else:
                        fail +=c
                        break
                else:
                    fail += c
                    break
    print(value(fail))

    unfinished = []
    typesInv = {v: k for k, v in types.items()}
    for line in chunks:
        closeable = []
        open = {"(":0, "{":0, "<":0, "[": 0}
        ok = True
        for c in line:
            if c in types.values():
                open[c] += 1
                closeable.append(c)
            else:
                if types[c] == closeable[-1]:
                    if open[types[c]] > 0:
                        open[types[c]] -= 1
                        closeable.pop()
                    else:
                        ok = False
                        break
                else:
                    ok = False
                    break
        if(ok):
            unfinished.append(closeable)        
        
    
    sums = [value2([typesInv[x] for x in line[::-1]]) for line in unfinished]
    sums.sort()
    print(sums[len(sums)//2])