import math
import re
from collections import defaultdict


def p1(data: str):
    r = defaultdict(int)
    cmds = data.splitlines()
    i = 0

    def v_of(val: str):
        return int(val) if re.match(r'-?\d+', val) else r[val]

    ans = 0
    while i < len(cmds):
        cmd = cmds[i].split()
        match cmd[0]:
            case 'set':
                r[cmd[1]] = v_of(cmd[2])
            case 'sub':
                r[cmd[1]] -= v_of(cmd[2])
            case 'mul':
                ans += 1
                r[cmd[1]] *= v_of(cmd[2])
            case 'jnz':
                if v_of(cmd[1]) != 0:
                    i += v_of(cmd[2])
                    continue
            case _:
                raise Exception()
        i += 1
    return ans


def is_composite(n):
    if n % 2 == 0 or n % 3 == 0:
        return True
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return True
    return False


def p2(data: str):
    return sum(is_composite(x) for x in range(109300, 126317, 17))
