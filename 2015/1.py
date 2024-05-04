from collections import Counter


def p1(data: str):
    c = Counter(data)
    return c['('] - c[')']


def p2(data: str):
    n = 0
    for i, c in enumerate(data.strip()):
        n += 1 if c == '(' else -1
        if n == -1:
            return i + 1
