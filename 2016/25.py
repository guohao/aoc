import itertools
import re


def solve(data: str, a):
    r = {x: 0 for x in 'abcd'}
    r['a'] = a
    i = 0
    cmds = data.splitlines()
    seq = itertools.cycle([0, 1])

    def vo(name: str):
        if re.search(r'-?\d+', name):
            return int(name)
        return r[name]

    while i < len(cmds):
        cells = cmds[i].split()
        cmd = cells[0]
        match cmd:
            case 'cpy':
                r[cells[2]] = vo(cells[1])
            case 'inc':
                r[cells[1]] += 1
            case 'dec':
                r[cells[1]] -= 1
            case 'out':
                if next(seq) != vo(cells[1]):
                    return False
            case 'jnz':
                if vo(cells[1]):
                    i += vo(cells[2])
                    continue
        i += 1
    return True


def p1(data: str):
    for i in itertools.count(1):
        print(i)
        solve(data, i)

