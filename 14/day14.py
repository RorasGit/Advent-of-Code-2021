from typing import Counter

def step(nbr_of_pairs, instructions, counter, steps):
    for _ in range (steps):
        new_pairs = Counter()
        for pair, amt in nbr_of_pairs.items():
            insertletter = instructions[pair]
            new_pairs[(pair[0], insertletter)] += amt
            new_pairs[(insertletter, pair[1])] += amt
            counter[insertletter] += amt
        nbr_of_pairs = new_pairs
    return nbr_of_pairs, counter

with open("input.txt", encoding="utf-8") as f:

    template, ins = [line for line in f.read().split("\n\n")]
    ins = {tuple(p) : l for p, l in [line.split(" -> ") for line in ins.split("\n")]}

    pairs = Counter(zip(template, template[1:]))
    lettercounter = Counter(template)

    pairs, lettercounter = step(pairs, ins, lettercounter, 10)
    print(max(lettercounter.values()) - min(lettercounter.values()))

    pairs, lettercounter = step(pairs, ins, lettercounter, 30)
    print(max(lettercounter.values()) - min(lettercounter.values()))