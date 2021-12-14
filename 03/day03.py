def get_ones(ones : list[str], larger, index = 0):
    if len(ones) == 1:
        return ones[0]

    next_ones = []
    next_zeros = []
    for test in ones:
        if int(test[index]) == 1:
            next_ones.append(test)
        else:
            next_zeros.append(test)
    test_case = len(next_ones) >= len(next_zeros)
    if test_case if larger else not test_case :
        return get_ones(next_ones, larger, index+1)
    else :
        return get_ones(next_zeros, larger, index+1)
def main():
    with open(os.path.join(os.path.dirname(__file__),"input.txt" , 'r', encoding="utf-8") as file :
        values = file.read().splitlines()
        amount = dict.fromkeys(range(len(values[0])), 0)
        for val in values:
            for i, amount in enumerate(amount):
                amount[i] += int(val[i])

        length = len(values)
        epsilon = 0
        gamma = 0
        for size in amount.values():
            epsilon = epsilon << 1
            gamma = gamma << 1
            if size > length/2 :
                epsilon +=1
            else:
                gamma+=1

        print(gamma*epsilon)
        print(int(get_ones(values, 1), 2)*int(get_ones(values, 0), 2))


if __name__ == '__main__':
    main()
    