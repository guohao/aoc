from helper import *

data = raw_data(2017, 1).strip()


def solve(offset: int) -> int:
    s = data[offset:] + data[:offset]
    ans = 0
    for i, c in enumerate(data):
        if c == s[i]:
            ans += int(c)
    return ans


print(solve(1))
print(solve(len(data) // 2))
