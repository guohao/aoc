import re


def cs(a: str) -> str:
    s = ''
    for i in range(0, len(a), 2):
        if a[i] == a[i + 1]:
            s += '1'
        else:
            s += '0'
    return s


def p1(s: str, disk_size) -> str:
    while len(s) < disk_size:
        s = s + '0' + re.sub(r'[01]', lambda m: '1' if m.group() == '0' else '0', s[::-1])
    s = s[:disk_size]
    c = cs(s)
    while len(c) % 2 == 0:
        c = cs(c)
    return c


print(p1("10111100110001111", 272))
print(p1("10111100110001111", 35651584))
