from collections import defaultdict


def p1(data: str):
    r = defaultdict(int)
    for line in data.splitlines():
        cells = line.split()
        if 'inc' in line:
            op = 1
        else:
            op = -1
        if eval(f'{r[cells[4]]} {cells[5]} {cells[6]}'):
            r[cells[0]] += op * int(cells[2])
    return max(r.values())


def p2(data: str):
    r = defaultdict(int)
    ans = 0
    for line in data.splitlines():
        cells = line.split()
        if 'inc' in line:
            op = 1
        else:
            op = -1
        if eval(f'{r[cells[4]]} {cells[5]} {cells[6]}'):
            r[cells[0]] += op * int(cells[2])
        ans = max(ans, max(r.values()))
    return ans
