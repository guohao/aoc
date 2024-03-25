import itertools


def p1(data: str):
    cmds = [int(x) for x in data.splitlines()]
    i = 0
    for t in itertools.count():
        if 0 <= i < len(cmds):
            ni = i + cmds[i]
            cmds[i] += 1
            i = ni
        else:
            return t


def p2(data: str):
    cmds = [int(x) for x in data.splitlines()]
    i = 0
    for t in itertools.count():
        if 0 <= i < len(cmds):
            ni = i + cmds[i]
            if cmds[i] >= 3:
                cmds[i] -= 1
            else:
                cmds[i] += 1
            i = ni
        else:
            return t
