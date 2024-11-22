import re

d = input()
n = 400000
ans = d.count('.')


def replace(m: re.Match) -> str:
    l = '.' if m.start() - 1 < 0 else d[m.start() - 1]
    r = '.' if m.start() + 1 == len(d) else d[m.start() + 1]
    return '^' if l != r else '.'


for i in range(n - 1):
    d = re.sub(r'[.\\^]', replace, d)
    ans += d.count('.')
print(ans)
