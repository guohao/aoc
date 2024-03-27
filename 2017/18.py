import re
from collections import defaultdict, deque


def p1(data: str):
    r = defaultdict(int)
    cmds = data.splitlines()

    def vo(name):
        if re.match(r'-?\d+', name):
            return int(name)
        return r[name]

    lp = 0
    i = 0
    while i < len(cmds):
        cmd = cmds[i].split()
        # print(i, cmd, r)
        match cmd[0]:
            case 'snd':
                lp = vo(cmd[1])
            case 'set':
                r[cmd[1]] = vo(cmd[2])
            case 'mul':
                r[cmd[1]] *= vo(cmd[2])
            case 'mod':
                r[cmd[1]] %= vo(cmd[2])
            case 'rcv':
                if vo(cmd[1]):
                    return lp
            case 'add':
                r[cmd[1]] += vo(cmd[2])
            case 'jgz':
                if vo(cmd[1]) > 0:
                    i += vo(cmd[2])
                    continue
            case _:
                assert False
        i += 1


def p2(data: str):
    qs = [deque() for _ in range(2)]
    rs = [defaultdict(int) for _ in range(2)]
    rs[0]['p'] = 0
    rs[1]['p'] = 1
    pi = [0] * 2
    cmds = data.splitlines()
    p = 0

    def vo(name, p):
        if re.match(r'-?\d+', name):
            return int(name)
        return rs[p][name]

    ans = 0
    while True:
        cmd = cmds[pi[p]].split()
        match cmd[0]:
            case 'snd':
                qs[1 - p].append(vo(cmd[1], p))
                if p == 1:
                    ans += 1
            case 'set':
                rs[p][cmd[1]] = vo(cmd[2], p)
            case 'mul':
                rs[p][cmd[1]] *= vo(cmd[2], p)
            case 'mod':
                rs[p][cmd[1]] %= vo(cmd[2], p)
            case 'rcv':
                if not qs[p]:
                    p = 1 - p
                    if not qs[p]:
                        break
                    continue
                else:
                    rs[p][cmd[1]] = qs[p].popleft()
            case 'add':
                rs[p][cmd[1]] += vo(cmd[2], p)
            case 'jgz':
                if vo(cmd[1], p) > 0:
                    pi[p] += vo(cmd[2], p)
                    continue
            case _:
                assert False
        pi[p] += 1
    return ans
