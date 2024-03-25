import re
from collections import defaultdict, deque


def val_of(r: defaultdict, s: str):
    if re.match(r'-?\d+', s):
        return int(s)
    else:
        return r[s]


def p1(data: str):
    r = defaultdict(int)
    lp = 0
    cmds = data.splitlines()
    i = 0
    while i < len(cmds):
        cmd = cmds[i].split()
        match cmd[0]:
            case 'snd':
                lp = val_of(r, cmd[1])
            case 'set':
                r[cmd[1]] = val_of(r, cmd[2])
            case 'add':
                r[cmd[1]] += val_of(r, cmd[2])
            case 'mul':
                r[cmd[1]] *= val_of(r, cmd[2])
            case 'mod':
                r[cmd[1]] %= val_of(r, cmd[2])
            case 'rcv':
                if val_of(r, cmd[1]) != 0:
                    return lp
            case 'jgz':
                if val_of(r, cmd[1]) > 0:
                    i += val_of(r, cmd[2])
                    continue
            case _:
                raise Exception("can not reach here")
        i += 1


def p2(data: str):
    cmds = data.splitlines()
    r0 = defaultdict(int)
    r1 = defaultdict(int)
    r1['p'] = 1
    queue0 = deque()
    queue1 = deque()
    cr = 0
    ans = 0
    while True:
        if cr == 0:
            r = r0
            q = queue0
            o = queue1
        else:
            r = r1
            q = queue1
            o = queue0
        cmd = cmds[r[cr]].split()
        match cmd[0]:
            case 'snd':
                o.append(val_of(r, cmd[1]))
                if cr == 1:
                    ans += 1
            case 'set':
                r[cmd[1]] = val_of(r, cmd[2])
            case 'add':
                r[cmd[1]] += val_of(r, cmd[2])
            case 'mul':
                r[cmd[1]] *= val_of(r, cmd[2])
            case 'mod':
                r[cmd[1]] %= val_of(r, cmd[2])
            case 'rcv':
                if len(q) == 0:
                    if len(queue0) == 0 and len(queue1) == 0:
                        return ans
                    cr = 1 - cr
                    continue
                r[cmd[1]] = q.popleft()
            case 'jgz':
                if val_of(r, cmd[1]) > 0:
                    r[cr] += val_of(r, cmd[2])
                    continue
            case _:
                raise Exception("can not reach here")
        r[cr] += 1
    return ans
