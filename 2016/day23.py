from collections import defaultdict

from helper import *

data = raw_data(2016, 23)
lines = lines(data)


def solve(a):
    cmds = lines.copy()
    i = 0
    r = {'a': a, 'b': 0, 'c': 0, 'd': 0}

    seen = {}
    diffs = {}

    def get_val(v):
        if v.startswith('-') and v[1:].isdigit():
            return -int(v[1:])
        if v.isdigit():
            return int(v)
        if v in r:
            return r[v]
        return None

    while i < len(cmds):
        cmd = cmds[i]
        if cmd.startswith('cpy'):
            src, target = cmd.split()[1:]
            if not target.isdigit():
                val = get_val(src)
                if val is not None:
                    r[target] = val
        elif cmd.startswith('inc'):
            if len(cmd.split()) == 2:
                target = cmd.split()[1]
                if not target.isdigit():
                    r[target] += 1
        elif cmd.startswith('dec'):
            if len(cmd.split()) == 2:
                target = cmd.split()[1]
                if not target.isdigit():
                    r[target] -= 1
        elif cmd.startswith('jnz'):
            src, target = cmd.split()[1:]
            val = get_val(src)
            target = get_val(target)

            if val is not None and target is not None and val != 0:
                idx = i + int(target)
                if 0 <= idx <= len(cmds):
                    key = (tuple(cmds[idx:i]), i)
                    if key in seen and target < 0 and src in r:
                        mem = seen[key]
                        if key not in diffs:
                            diff = {k: r[k] - mem[k] for k in r.keys()}
                            dt = abs(diff[src])
                            if dt > 0:
                                diffs[key] = {k: diff[k] // dt for k in diff.keys()}
                        if key in diffs:
                            diff = diffs[key]
                            t = abs(r[src])
                            r = {k: r[k] + t * diff[k] for k in r.keys()}
                            i += 1
                            continue
                    seen[key] = r.copy()
                    i = idx
                    continue
        elif cmd.startswith('tgl'):
            seen.clear()
            diffs.clear()
            val = get_val(cmd.split()[1])
            if val is not None:
                idx = i + val
                if 0 <= idx < len(cmds):
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


solve(7)
solve(12)
