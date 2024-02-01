from helper import *


def gen_line(s: str) -> str:
    res = ''
    for i in range(len(s)):
        l = s[i - 1] if i - 1 >= 0 else '.'
        r = s[i + 1] if i + 1 < len(s) else '.'
        if l != r:
            res += '^'
        else:
            res += '.'
    return res


def solve(n):
    data = raw_data(2016, 18).strip()
    ans = 0
    for _ in range(n):
        ans += data.count('.')
        data = gen_line(data)
    print(ans)


solve(40)
solve(400000)
