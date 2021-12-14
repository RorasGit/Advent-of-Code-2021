from collections import Counter

def share_n_digits(a, b, n):
    return sum((Counter(a) & Counter(b)).values()) == n

def share_n_segments(distinct_segment, unknown_segments, n):
    for segment in unknown_segments:
        if share_n_digits(segment, distinct_segment, n):
            return segment

with open("input.txt") as f:
    lines = f.readlines()

    input = []
    output = []
    digitLen = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    unqiueLen = [i for i in range(10) if digitLen.count(i) == 1]
    
    for line in lines:
        s = line.split("|")
        input.append(s[0].split())
        output.append(s[1].split())


    # Part 1
    sumDigit = 0
    for line in output:
        for digit in line:
            if len(digit) in unqiueLen:
                sumDigit += 1

    print(sumDigit)
    
    #Part 2
    sumDigit = 0
    for i in range(len(input)):
        segment = dict()
        unknown_segments = dict()
        for digit in input[i]:  
            length = len(digit)
            if length in unqiueLen:
                segment[digitLen.index(length)] = digit
            else :
                if(length in unknown_segments.keys()):
                    unknown_segments[length].append(digit)
                else :
                    unknown_segments[length] = [digit]
        segment[3] = share_n_segments(segment[7], unknown_segments[5], 3)
        unknown_segments[5].remove(segment[3])
        segment[5] = share_n_segments(segment[4], unknown_segments[5], 3) 
        unknown_segments[5].remove(segment[5])
        segment[2] = unknown_segments[5][0]
        segment[0] = share_n_segments(segment[5], unknown_segments[6], 4)
        unknown_segments[6].remove(segment[0])
        segment[9] = share_n_segments(segment[7], unknown_segments[6], 3)
        unknown_segments[6].remove(segment[9])
        segment[6] = unknown_segments[6][0]

        outputDigit = ""
        for digit in output[i]:
            for key, value in segment.items():
                if Counter(value) == Counter(digit):
                    outputDigit += str(key)
        
        sumDigit += int(outputDigit)

print(sumDigit)
        
        
