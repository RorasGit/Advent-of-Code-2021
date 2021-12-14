from collections import Counter

def share_n_digits(digit_one, digit_two, number):
    return sum((Counter(digit_one) & Counter(digit_two)).values()) == number

def share_n_segments(distinct_segment, unknown_segments, number):
    for segment in unknown_segments:
        if share_n_digits(segment, distinct_segment, number):
            return segment
    return None
def main():
    with open("input.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

        segments, output = map(list, zip(*(line.split("|") for line in lines)))
        output = [line.split() for line in output]
        segments = [line.split() for line in segments]
        digit_len = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
        unqiue_len = [i for i in range(10) if digit_len.count(i) == 1]

        # Part 1
        sum_digit = 0
        for line in output:
            for digit in line:
                if len(digit) in unqiue_len:
                    sum_digit += 1

        print(sum_digit)

        #Part 2
        sum_digit = 0
        for i, _ in enumerate(segments):
            segment = {}
            unknown_segments = {}
            for digit in segments[i]:
                length = len(digit)
                if length in unqiue_len:
                    segment[digit_len.index(length)] = digit
                else :
                    if length in unknown_segments:
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

            output_digit = ""
            for digit in output[i]:
                for key, value in segment.items():
                    if Counter(value) == Counter(digit):
                        output_digit += str(key)

            sum_digit += int(output_digit)

    print(sum_digit)


if __name__ == '__main__':
    main()
