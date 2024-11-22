import re


def x(s: str) -> int:
    m = re.search(r'\((\d+)x(\d+)\)', s)
    if not m:
        return len(s)
    a, b = map(int, m.groups())
    return m.start() + x(s[m.end():m.end() + a]) * b + x(s[m.end() + a:])


print(x(input()))
