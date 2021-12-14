import os

def main():
    with open(os.path.join(os.path.dirname(__file__),"input.txt") , 'r', encoding='utf-8') as file :
        values = file.read().splitlines()
        inc = -1
        last_value = 0
        for line in values:
            if int(line) > last_value:
                inc += 1
            last_value = int(line)

        print(inc)

        inc = -3
        one = 0
        two = 0
        three = 0
        last_value = 0
        for line in values:
            one = int(line)
            total = one+two+three
            if total > last_value :
                inc+=1
            last_value = total
            three = two
            two = one

        print(inc)

if __name__ == '__main__':
    main()
    