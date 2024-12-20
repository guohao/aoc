import sys
from functools import cmp_to_key


def f(a, b) -> int:
    if not isinstance(a, list) and not isinstance(b, list):
        return a - b
    if not isinstance(a, list):
        a = [a]
    if not isinstance(b, list):
        b = [b]
    for i in range(len(a)):
        if i >= len(b):
            return 1
        r = f(a[i], b[i])
        if r != 0:
            return r
    return -1


data = sys.stdin.read().strip()

data += '\n[[2]]\n[[6]]\n'
all = sorted(list(map(eval, filter(lambda x: x, data.strip().split('\n')))), key=cmp_to_key(f))
a = [i for i, x in enumerate(all, start=1) if x == [[2]]][0]
b = [i for i, x in enumerate(all, start=1) if x == [[6]]][0]
print(a * b)
