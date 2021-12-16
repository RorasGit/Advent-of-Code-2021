import os
from collections import deque
from operator import gt, lt, eq
from math import prod
from time import time

ops = [sum, prod, min, max]
comps = [gt, lt, eq]

def sum_version(packets):
    if isinstance(packets, list):
        return sum(sum_version(packet) for packet in packets)
    if isinstance(packets[2], list):
        return packets[0] + sum_version(packets[2])
    return packets[0]

def calc_packet(_, T, value):
    if T == 4:
        return value
    if T < 4:
        return ops[T](calc_packet(*p) for p in value)
    return int(comps[T-5](calc_packet(*value[0]), calc_packet(*value[1])))

def unpack_packet(packet: deque):
    V = int("".join([packet.popleft() for _ in range(3)]), 2)
    T = int("".join([packet.popleft() for _ in range(3)]), 2)

    if T == 4:
        value = ""
        while True:
            lastgroup = packet.popleft()
            value += "".join([packet.popleft() for _ in range(4)])
            if lastgroup != "1":
                break
        return (V, T, int(value,2))

    I = int(packet.popleft(), 2)
    packetlen = int("".join([packet.popleft() for _ in range(11 if I else 15)]), 2)

    subpackets = []
    if I:
        for _ in range(packetlen):
            subpackets.append(unpack_packet(packet))

    else :
        length = len(packet)
        while length - len(packet) < packetlen:
            subpackets.append(unpack_packet(packet))
    return (V, T, subpackets)


def main():
    with open(os.path.join(os.path.dirname(__file__),"input.txt"), encoding="utf-8") as file:

        hexvalue = file.read()
        binary_packet = deque(bin(int(hexvalue, 16))[2:].zfill(len(hexvalue)*4))

        packet = unpack_packet(binary_packet)


        print(sum_version(packet))
        print(calc_packet(*packet))
if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print(f"{(end-start)*1000} ms")
