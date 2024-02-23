from helper import *

data = raw_data(2017, 5)


def p1():
    cmds = [int(x) for x in lines(data)]
    i = 0
    t = 0
    while i < len(cmds):
        t += 1
        cmd = cmds[i]
        cmds[i] += 1
        i += cmd
    return t


def p2():
    cmds = [int(x) for x in lines(data)]
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


print(p1())
print(p2())
