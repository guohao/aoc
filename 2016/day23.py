from helper import *

data = raw_data(2016, 23)
lines = lines(data)


def p1():
    cmds = lines.copy()
    i = 0
    r = {}
    while i < len(cmds):
        cmd = cmds[i]
        print(i,cmd)
        if cmd.startswith('cpy'):
            _, src, target = cmd.split()
            if target.isdigit():
                i += 1
                continue
            else:
                if src.isdigit():
                    r[target] = int(src)
                else:
                    if src in r:
                        r[target] = r[src]
                i += 1
        elif cmd.startswith('inc'):
            if len(cmd.split()) != 3:
                i += 1
                continue
            _, val, target = cmd.split()
            if target.isdigit():
                i += 1
                continue
            if target in r:
                r[target] += 1
            else:
                r[target] = 1
        elif cmd.startswith('dec'):
            if len(cmd.split()) != 3:
                i += 1
                continue
            _, val, target = cmd.split()
            if target.isdigit():
                i += 1
                continue
            if target in r:
                r[target] -= 1
            else:
                r[target] = -1
        elif cmd.startswith('jnz'):
            _, src, target = cmd.split()
            if src.isdigit():
                if int(src) != 0:
                    if target.isdigit():
                        i += int(target)
                        continue
                    else:
                        if target in r:
                            i += r[target]
                            continue
            else:
                if src not in r:
                    i += 1
                    continue
                if r[src] != 0:
                    i += int(target)
                    continue
        elif cmd.startswith('tgl'):
            _, val = cmd.split()
            if val.isdigit():
                val = int(val)
            else:
                if val in r:
                    val = r[val]
                else:
                    i += 1
                    continue
            idx = i + val
            if idx < 0 or idx >= len(cmds):
                i += 1
                continue
            c = cmds[idx]
            ca = c.split()
            if len(ca) == 2:
                if ca[0].startswith('inc'):
                    cmds[idx] = c.replace('inc', 'dec')
                else:
                    cmds[idx] = c.replace(ca[0], 'inc')
            elif len(ca) == 3:
                if ca[0].startswith('jnz'):
                    cmds[idx] = c.replace('jnz', 'cpy')
                else:
                    cmds[idx] = c.replace(ca[0], 'jnz')
            i += 1
    print(r['a'])


p1()
