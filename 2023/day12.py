import functools

from helper import *


@functools.cache
def dfs(line, ns: tuple) -> int:
    if not ns:
        return 0 if '#' in line else 1

    if not line:
        return 0
    match line[0]:
        case '#':
            if '.' in line[:ns[0]]:
                return 0
            if ns[0] == len(line) and len(ns) == 1:
                return 1
            if ns[0] < len(line) and line[ns[0]] != '#':
                return dfs(line[ns[0] + 1:], ns[1:])
        case '.':
            return dfs(line[1:], ns)
        case '?':
            return dfs('#' + line[1:], ns) + dfs(line[1:], ns)
    return 0


ans1 = 0
ans2 = 0
for line in lines(raw_data(2023, 12)):
    l, r = line.split()
    ns = tuple(nums(r))
    ans1 += dfs(l, ns)
    ans2 += dfs('?'.join([l] * 5), ns * 5)
print(ans1)
print(ans2)
