import os
from collections import deque
from typing import Deque
from math import prod

def sum_version(packets):
    if isinstance(packets, list):
        return sum(sum_version(packet) for packet in packets)
    if isinstance(packets[2], list):
        return packets[0] + sum_version(packets[2])
    return packets[0]

def calc_packet(packet):
    T = packet[1]
    value = packet[2]
    if T == 0:
        return sum(calc_packet(subpacket) for subpacket in value)
    if T == 1:
        return prod(calc_packet(subpacket) for subpacket in value)
    if T == 2:
        return min(calc_packet(subpacket) for subpacket in value)
    if T == 3:
        return max(calc_packet(subpacket) for subpacket in value)
    if T == 4:
        return value
    if T == 5:
        return int(calc_packet(value[0]) > calc_packet(value[1]))
    if T == 6:
        return int(calc_packet(value[0]) < calc_packet(value[1]))
    if T == 7:
        return int(calc_packet(value[0]) == calc_packet(value[1]))

def unpack_packet(packet: deque):
    V = int("".join([packet.popleft() for _ in range(3)]), 2)
    T = int("".join([packet.popleft() for _ in range(3)]), 2)

    if T == 4:
        value = ""
        lastbit = "1"
        while lastbit == "1":
            lastbit = packet.popleft()
            value += "".join([packet.popleft() for _ in range(4)])
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
        print(calc_packet(packet))

if __name__ == '__main__':
    main()
