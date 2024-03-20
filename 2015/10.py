import re


def las(s: str) -> str:
    ans = ''
    for m in re.finditer(r'(\d)\1*', s):
        ans += str(m.end() - m.start()) + m.group(1)
    return ans


def solve(data: str, n):
    for _ in range(n):
        data = las(data)
    return len(data)


def p1(data: str):
    return solve(data, 40)


def p2(data: str):
    return solve(data, 50)
