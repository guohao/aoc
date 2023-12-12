import functools

from helper import *

data = raw_data(2023, 12)

lines = lines(data)


@functools.cache
def f(line, ns) -> int:
    if not ns:
        return 0 if '#' in line else 1

    if not line:
        return 0

    if line[0] == '#':
        if '.' in line[:ns[0]]:
            return 0
        if ns[0] == len(line) and len(ns) == 1:
            return 1
        if ns[0] < len(line) and line[ns[0]] != '#':
            return f(line[ns[0] + 1:], ns[1:])
    if line[0] == '.':
        return f(line[1:], ns)
    if line[0] == '?':
        return f('#' + line[1:], ns) + f(line[1:], ns)
    return 0


ans1 = 0
ans2 = 0
for line in lines:
    l, r = line.split()
    ns = extract_num(r)
    ans1 += f(l, ns)
    ans2 += f('?'.join([l] * 5), ns * 5)
print(ans1)
print(ans2)
