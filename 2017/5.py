def p1(data: str):
    cmds = [int(x) for x in data.splitlines()]
    i = 0
    t = 0
    while i < len(cmds):
        t += 1
        cmd = cmds[i]
        cmds[i] += 1
        i += cmd
    return t


def p2(data: str):
    cmds = [int(x) for x in data.splitlines()]
    i = 0
    t = 0
    while i < len(cmds):
        t += 1
        cmd = cmds[i]
        if cmd >= 3:
            cmds[i] -= 1
        else:
            cmds[i] += 1
        i += cmd
    return t
