import os
def main():
    with open(os.path.join(os.path.dirname(__file__),"input.txt") , 'r', encoding='utf-8') as file :
        values = file.read().splitlines()
        pos = 0
        depth = 0
        for value in values:
            oper, size = value.split(" ")
            size = int(size)
            if oper == "forward":
                pos+=size
            elif oper == "down":
                depth+=size
            else:
                if size > depth:
                    depth = 0
                else:
                    depth -= size

        print(f"pos: {pos}, depth: {depth}, total: {pos*depth}")

        aim = 0
        pos = 0
        depth = 0
        for value in values:
            oper, size = value.split(" ")
            size = int(size)
            if oper == "up":
                aim-=size
            elif oper == "down":
                aim+=size
            else:
                pos+=size
                depth+=aim*size
                depth = max(depth, 0)

        print(f"pos: {pos}, depth: {depth}, aim: {aim} total: {pos*depth}")


if __name__ == '__main__':
    main()
    