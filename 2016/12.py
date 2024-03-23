import re


def solve(data: str, c):
    r = {x: 0 for x in 'abcd'}
    r['c'] = c
    i = 0
    cmds = data.splitlines()

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
            case 'jnz':
                if vo(cells[1]):
                    i += vo(cells[2])
                    continue
        i += 1
    return r['a']


def p1(data: str):
    return solve(data, 0)


def p2(data: str):
    return solve(data, 1)
