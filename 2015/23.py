def solve(data: str, a):
    r = {'a': a, 'b': 0}
    cmds = data.splitlines()
    i = 0
    while i < len(cmds):
        cells = cmds[i].split()
        cmd = cells[0]
        if 'hlf' in cmd:
            r[cells[1]] //= 2
        if 'tpl' in cmd:
            r[cells[1]] *= 3
        if 'inc' in cmd:
            r[cells[1]] += 1
        if 'jmp' in cmd:
            i += int(cells[1])
            continue
        if 'jie' in cmd:
            if r[cells[1][0]] % 2 == 0:
                i += int(cells[2])
                continue
        if 'jio' in cmd:
            if r[cells[1][0]] == 1:
                i += int(cells[2])
                continue
        i += 1
    return r['b']


def p1(data: str):
    return solve(data, 0)


def p2(data: str):
    return solve(data, 1)
