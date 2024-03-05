from functools import cache

from helper import *

data = raw_data(2017, 16)


@cache
def dance(seq: str) -> str:
    for cmd in data.strip().split(','):
        if cmd.startswith('s'):
            s = ints(cmd)[0]
            seq = seq[-s:] + seq[:-s]
        elif cmd.startswith('x'):
            x, y = sorted(ints(cmd))
            seq = seq[:x] + seq[y] + seq[x + 1:y] + seq[x] + seq[y + 1:]
        elif cmd.startswith('p'):
            x, y = sorted([seq.index(cmd[1]), seq.index(cmd[3])])
            seq = seq[:x] + seq[y] + seq[x + 1:y] + seq[x] + seq[y + 1:]
        else:
            raise Exception()
    return seq


def p1():
    seq = ''.join([chr(ord('a') + i) for i in range(16)])
    print(dance(seq))


def p2():
    seq = ''.join([chr(ord('a') + i) for i in range(16)])
    seen = set()
    terms = 1000000000
    while terms > 0:
        if seq in seen:
            terms = terms % len(seen)
        seen.add(seq)
        seq = dance(seq)
        terms -= 1
    print(seq)


p1()
p2()
