import math
import sys


def parse(data: str):
    b = ''.join(bin(int(c, 16))[2:].zfill(4) for c in data.strip())

    def read(curr, n):
        return int(b[curr:curr + n], 2), curr + n

    def literal_value_of(i):
        seq = ''
        while True:
            seq += b[i + 1:i + 5]
            i += 5
            if b[i - 5] == '0':
                break
        return int(seq, 2), i

    def x(start_pos: int):
        pc = [start_pos]
        version, pc[0] = read(pc[0], 3)
        t, pc[0] = read(pc[0], 3)
        literal_value = 0
        subs = []
        if t == 4:
            literal_value, pc[0] = literal_value_of(pc[0])
        else:
            len_type, pc[0] = read(pc[0], 1)
            if len_type == 0:
                sub_size, pc[0] = read(pc[0], 15)
                end = pc[0] + sub_size
                while pc[0] < end:
                    s, pc[0] = x(pc[0])
                    subs.append(s)
            elif len_type == 1:
                sub_size, pc[0] = read(pc[0], 11)
                for j in range(sub_size):
                    s, pc[0] = x(pc[0])
                    subs.append(s)
        return (version, t, literal_value, subs), pc[0]

    return x(0)[0]


def vs(packet):
    if packet is None:
        return 0
    return packet[0] + sum(vs(s) for s in packet[3])


print(vs(parse(sys.stdin.read().strip())))
