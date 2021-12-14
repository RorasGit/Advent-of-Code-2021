
def run_bingo (bingos, balls) :
    bingosum = []
    for i, ball in enumerate(balls):
        gen = (value for bingo in bingos for row in bingo for value in row if value[0] == ball)
        for value in gen:
            value[1] = True
        for bingo in bingos:
            if(any(all(x[1] for x in row) for row in bingo)
            or any(all(x[1] for x in row) for row in list(zip(*bingo)))):

                bingosum.append((i, sum(val[0] for row in bingo for val in row if not val[1])*ball))
                bingos.remove(bingo)
        if not bingos:
            break
    return bingosum


def main():
    with open("input.txt", "r", encoding="utf-8") as file :

        balls = [int(x) for x in next(file).split(",")]
        lines = filter(None,file.read().splitlines())
        rows = list((list([int(c),False] for c in line.split()) for line in lines))
        bingo = [rows[x:x+5] for x in range(0, len(rows),5)]


        victory_bingos = run_bingo(bingo, balls)


        print("Part 1:", min(victory_bingos, key=lambda x: x[0])[1])
        print("Part 2:", max(victory_bingos, key=lambda x: x[0])[1])

if __name__ == '__main__':
    main()
