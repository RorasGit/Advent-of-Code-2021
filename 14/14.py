from os import pardir
from typing import Counter

def step(pairs, instructions, counter, steps):
    for _ in range (steps):
        newPairs = Counter()
        for pair, sum in pairs.items():
            insertletter = instructions[pair]
            newPairs[(pair[0], insertletter)] += sum
            newPairs[(insertletter, pair[1])] += sum
            counter[insertletter] += sum
        pairs = newPairs
    return pairs, counter

with open("input.txt") as f:
    
    template, instructions = [line for line in f.read().split("\n\n")]
    instructions = {tuple(pair) : letter for pair, letter in [line.split(" -> ") for line in instructions.split("\n")]}

    pairs = Counter(zip(template, template[1:]))
    lettercounter = Counter(template)

    pairs, lettercounter = step(pairs, instructions, lettercounter, 10)
    print(max(lettercounter.values()) - min(lettercounter.values()))
    
    pairs, lettercounter = step(pairs, instructions, lettercounter, 30)
    print(max(lettercounter.values()) - min(lettercounter.values()))


