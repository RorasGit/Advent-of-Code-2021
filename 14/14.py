
from typing import Counter

def step(pairs, ins, ans):

    newPairs = Counter()
    for pair in pairs:
        newPairs[(pair[0],ins[pair])] += pairs[pair]
        newPairs[(ins[pair],pair[1])] += pairs[pair]
        ans[ins[pair]] += pairs[pair]
    return newPairs

with open("input.txt") as f:
    
    template, instructions = [line for line in f.read().split("\n\n")]
    instructions = [line.split(" -> ") for line in instructions.split("\n")]
    instructions = {tuple(s[0]) : s[1] for s in instructions}

    pairs = Counter(zip(template, template[1:]))
    ans = Counter(template)

    for i in range (10):
        pairs = step(pairs, instructions, ans)

    print(max(ans.values()) - min(ans.values()))
        
    for i in range (30):
        pairs = step(pairs, instructions, ans)

    print(max(ans.values()) - min(ans.values()))

