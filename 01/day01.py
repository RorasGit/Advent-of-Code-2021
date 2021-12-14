with open("input.txt" , 'r') as input :
    values = input.read().splitlines()
    inc = -1
    lastValue = 0
    for line in values: 
        if int(line) > lastValue:   
            inc += 1
        lastValue = int(line)

    print(inc)

    inc = -3
    A = 0
    B = 0
    C = 0
    lastValue = 0
    for line in values: 
        A = int(line) 
        sum = A+B+C
        if sum > lastValue :
            inc+=1
        lastValue = sum
        C = B
        B = A


    print(inc)






