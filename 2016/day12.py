from helper import *

data = raw_data(2016, 12)
lines = lines(data)


def solve(c):
    cmds = lines.copy()
    i = 0
    r = {'a': 0, 'b': 0, 'c': c, 'd': 0}
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
                i += int(target)
                continue
        i += 1
    print(r['a'])


solve(0)
solve(1)
