import re


def solve(data: str, a: int):
    r = {x: 0 for x in 'abcd'}
    r['a'] = a
    i = 0
    cmds = data.strip().splitlines()

    def vo(name: str):
        if re.fullmatch(r'-?\d+', name):
            return int(name)
        return r[name]

    seen = {}
    while 0 <= i < len(cmds):
        cells = cmds[i].split()
        cmd = cells[0]
        match cmd:
            case 'cpy':
                r[cells[2]] = vo(cells[1])
            case 'inc':
                r[cells[1]] += 1
            case 'dec':
                r[cells[1]] -= 1
            case 'tgl':
                x = vo(cells[1]) + i
                if 0 <= x < len(cmds):
                    tc = cmds[x].split()
                    ncmd = ''
                    if len(tc) == 2:
                        if 'inc' == tc[0]:
                            ncmd = 'dec'
                        else:
                            ncmd = 'inc'
                    elif len(tc) == 3:
                        if 'jnz' == tc[0]:
                            ncmd = 'cpy'
                        else:
                            ncmd = 'jnz'
                    tc[0] = ncmd
                    cmds[x] = ' '.join(tc)
            case 'jnz':
                if vo(cells[1]):
                    ni = i + vo(cells[2])
                    if (ni, i + 1) in seen and cells[1] in r:
                        rs = seen[ni, i + 1]
                        diff = {k: (r[k] - rs[k]) for k in rs}
                        if diff[cells[1]] != 0:
                            for k in diff:
                                r[k] += abs(r[cells[1]] // diff[cells[1]]) * diff[k]
                            del seen[ni, i + 1]
                            i += 1
                            continue
                        else:
                            del seen[ni, i + 1]
                    seen[ni, i + 1] = r.copy()
                    i = ni
                    continue
        i += 1
    return r['a']


def p1(data: str):
    return solve(data, 7)


def p2(data: str):
    return solve(data, 12)
