import itertools
import re


def p1(data: str):
    mem = {}
    for line in data.splitlines():
        if 'mask' in line:
            mask = line.split('= ')[1]
        else:
            l, r = line.split(' = ')
            l = int(re.findall(r'\d+', l)[0])
            r = int(r)
            l = bin(l | int(mask.replace('X', '0'), 2))[2:].zfill(36)
            xn = mask.count('X')
            for comb in set(list(itertools.combinations(xn * '01', xn))):
                comb = iter(comb)
                chs = [l[i] if mask[i] != 'X' else next(comb) for i in range(len(l))]
                mem[int(''.join(chs), 2)] = r
    return sum(mem.values())
