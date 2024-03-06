import re
from functools import cache


@cache
def dance(data: str, seq: str) -> str:
    for cmd in data.strip().split(','):
        if cmd.startswith('s'):
            s = [int(x) for x in re.findall(r'\d+', cmd)][0]
            seq = seq[-s:] + seq[:-s]
        elif cmd.startswith('x'):
            x, y = sorted([int(x) for x in re.findall(r'\d+', cmd)])
            seq = seq[:x] + seq[y] + seq[x + 1:y] + seq[x] + seq[y + 1:]
        elif cmd.startswith('p'):
            x, y = sorted([seq.index(cmd[1]), seq.index(cmd[3])])
            seq = seq[:x] + seq[y] + seq[x + 1:y] + seq[x] + seq[y + 1:]
        else:
            raise Exception()
    return seq


def p1(data: str):
    seq = ''.join([chr(ord('a') + i) for i in range(16)])
    return dance(data, seq)


def p2(data: str):
    seq = ''.join([chr(ord('a') + i) for i in range(16)])
    seen = set()
    terms = 1000000000
    while terms > 0:
        if seq in seen:
            terms = terms % len(seen)
        seen.add(seq)
        seq = dance(data, seq)
        terms -= 1
    return seq
