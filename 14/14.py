from os import pardir
from typing import Counter

def step(pairs, instructions, letters, steps):
    for _ in range (steps):
        newPairs = Counter()
        for pair, sum in pairs.items():
            insertletter = instructions[pair]
            newPairs[(pair[0], insertletter)] += sum
            newPairs[(insertletter, pair[1])] += sum
            letters[insertletter] += sum
        pairs = newPairs
    return pairs, letters

with open("input.txt") as f:
    
    template, instructions = [line for line in f.read().split("\n\n")]
    instructions = [line.split(" -> ") for line in instructions.split("\n")]
    instructions = {tuple(pair) : letter for pair, letter in instructions}

    pairs = Counter(zip(template, template[1:]))
    letters = Counter(template)

    pairs, letters = step(pairs, instructions, letters, 10)
    print(max(letters.values()) - min(letters.values()))
    
    pairs, letters = step(pairs, instructions, letters, 30)
    print(max(letters.values()) - min(letters.values()))


