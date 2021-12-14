from typing import Counter

def step(pairs, instructions, letters, steps = 1):
    for _ in range (steps):
        newPairs = Counter()
        for pair in pairs:
            newPairs[(pair[0],instructions[pair])] += pairs[pair]
            newPairs[(instructions[pair],pair[1])] += pairs[pair]
            letters[instructions[pair]] += pairs[pair]
        pairs = newPairs
    return pairs, letters

with open("input.txt") as f:
    
    template, instructions = [line for line in f.read().split("\n\n")]
    instructions = [line.split(" -> ") for line in instructions.split("\n")]
    instructions = {tuple(line[0]) : line[1] for line in instructions}

    pairs = Counter(zip(template, template[1:]))
    letters = Counter(template)

    pairs, letters = step(pairs, instructions, letters, 10)
    print(max(letters.values()) - min(letters.values()))
    
    pairs, letters = step(pairs, instructions, letters, 30)
    print(max(letters.values()) - min(letters.values()))

