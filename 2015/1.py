def p1(data: str):
    return data.count('(') - data.count(')')


def p2(data: str):
    n = 0
    for i, c in enumerate(data.strip()):
        n += 1 if c == '(' else -1
        if n == -1:
            return i + 1
