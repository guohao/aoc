import itertools
import re


def p2(data: str):
    mem = {}
    mask = ''
    for line in data.splitlines():
        if 'mask' in line:
            mask = line.split('= ')[1]
        else:
            l, r = line.split(' = ')
            l = int(re.findall(r'\d+', l)[0])
            r = int(r)
            l = bin(l | int(mask.replace('X', '0'), 2))[2:].zfill(36)
            xn = mask.count('X')
            combs = set(list(itertools.combinations(xn * '01', xn)))
            for comb in combs:
                mi = 0
                chs = list(l)
                for i in range(len(l)):
                    if mask[i] == 'X':
                        chs[i] = comb[mi]
                        mi += 1
                mem[int(''.join(chs), 2)] = r
    return sum(mem.values())
