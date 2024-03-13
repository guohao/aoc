import re


def p1(d: str):
    ans = 0
    for line in d.splitlines():
        l, w, h = map(int, re.findall(r'-?\d', line))
        ans += 2 * l * w + 2 * w * h + 2 * h * l + min(l * w, w * h, h * l)
    return ans


def p2(d: str):
    ans = 0
    for line in d.splitlines():
        l, w, h = map(int, re.findall(r'-?\d', line))
        ans += min(l + w, w + h, h + l) * 2 + l * w * h
    return ans
