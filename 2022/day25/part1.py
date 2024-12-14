import re
import sys
from functools import reduce

lines = [l.strip() for l in sys.stdin.readlines()]

def atoi(s: str) -> int:
    match s:
        case '-':
            return -1
        case '=':
            return -2
    return int(s)


def add(a: str, b: str) -> str:
    a = a[::-1]
    b = b[::-1]
    ml = max(len(a), len(b)) + 1
    c = [0 for _ in range(ml)]
    a = a + '0' * (ml - len(a))
    b = b + '0' * (ml - len(b))

    for i in range(len(c)):
        c[i] = c[i] + atoi(a[i]) + atoi(b[i])
        if c[i] < -2:
            c[i] = c[i] + 5
            c[i + 1] = -1
        elif c[i] > 2:
            c[i] = c[i] - 5
            c[i + 1] = 1
        if c[i] == -1:
            c[i] = '-'
        elif c[i] == -2:
            c[i] = '='
        else:
            c[i] = str(c[i])
    ret = ''.join(reversed(c))
    start = next(re.finditer(r'[12-=]', ret)).start()
    return ret[start:]


print(reduce(add, lines))
