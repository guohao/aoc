import itertools
import re


def p2(data: str):
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


def p1(data: str):
    mem = {}
    ma = 0
    mo = 0
    for line in data.splitlines():
        if 'mask' in line:
            mask = line.split('= ')[1]
            ma = int(mask.replace('X', '1'), 2)
            mo = int(mask.replace('X', '0'), 2)
            print(mask, ma, mo)
        else:
            l, r = line.split(' = ')
            l = int(re.findall(r'\d+', l)[0])
            r = int(re.findall(r'\d+', r)[0])
            mem[l] = r & ma | mo
    return sum(mem.values())
