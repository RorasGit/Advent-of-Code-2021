def getOnes(ones : list[str], larger, index = 0):
    if(len(ones) == 1 ) :
        return ones[0]

    nextOnes = []
    nextZeros = []
    for test in ones:
        if(int(test[index]) == 1):
            nextOnes.append(test)
        else:      
            nextZeros.append(test)
    testCase = len(nextOnes) >= len(nextZeros)
    if(testCase if larger else not testCase) :
        return getOnes(nextOnes, larger, index+1)
    else :
        return getOnes(nextZeros, larger, index+1)

with open("input.txt" , 'r') as input :
    values = input.read().splitlines()
    sum = dict.fromkeys(range(len(values[0])), 0)
    for val in values:
        for c in range(0, len(val)):
            sum[c] += int(val[c])

    length = len(values)
    epsilon = 0
    gamma = 0
    for size in sum.values():
        epsilon = epsilon << 1
        gamma = gamma << 1
        if size > length/2 :
            epsilon +=1
        else:
            gamma+=1

    print(gamma*epsilon)
    print(int(getOnes(values, 1), 2)*int(getOnes(values, 0), 2))