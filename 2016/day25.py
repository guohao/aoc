from helper import *

data = raw_data(2016, 25)
lines = lines(data)


def solve(a):
    cmds = lines.copy()
    i = 0
    r = {'a': a, 'b': 0, 'c': 0, 'd': 0}
    inf_out = itertools.cycle([0, 1])
    mc = 0
    while i < len(cmds):
        cmd = cmds[i]
        if cmd.startswith('cpy'):
            src, target = cmd.split()[1:]
            if not target.isdigit():
                r[target] = int(src) if src.isdigit() else r[src]
        elif cmd.startswith('inc'):
            if len(cmd.split()) == 2:
                target = cmd.split()[1]
                r[target] += 1
        elif cmd.startswith('dec'):
            if len(cmd.split()) == 2:
                target = cmd.split()[1]
                r[target] -= 1
        elif cmd.startswith('jnz'):
            src, target = cmd.split()[1:]
            if (src.isdigit() and int(src) != 0) or (not src.isdigit() and r[src] != 0):
                idx = i + int(target)
                i = idx
                continue
        elif cmd.startswith('out'):
            src = cmd.split()[1]
            if r[src] != next(inf_out):
                return False
            mc += 1
            if mc == 10:
                return True
        i += 1


def p1():
    for i in range(100000000):
        if solve(i):
            print(i)
            break


p1()
