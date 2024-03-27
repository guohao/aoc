import itertools
import string
from functools import cache


@cache
def dance(a, data):
    a = list(a)
    for cmd in data.split(','):
        match cmd[0]:
            case 's':
                x = int(cmd[1:])
                a = a[-x:] + a[:-x]
            case 'x':
                b, c = list(map(int, cmd[1:].split('/')))
                tmp = a[b]
                a[b] = a[c]
                a[c] = tmp
            case 'p':
                b, c = cmd[1:].split('/')
                ib = a.index(b)
                ic = a.index(c)
                a[ib] = c
                a[ic] = b
    return ''.join(a)


def p1(data: str):
    return dance(string.ascii_lowercase[:16], data)


def find_iter_cycle(func, init_value):
    slow = init_value
    fast = func(init_value)
    i = 1
    while slow != fast:
        slow = func(slow)
        fast = func(func(fast))
        i += 1
    return i


def p2(data: str):
    s = string.ascii_lowercase[:16]
    cycle_len = find_iter_cycle(lambda x: dance(x, data), s)
    for _ in range(1000000000 % cycle_len):
        s = dance(s, data)
    return s
