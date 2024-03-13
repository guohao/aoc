def p1(data: str):
    return data.count('(') - data.count(')')


def p2(data: str):
    floor = 0
    for i, c in enumerate(data, start=1):
        if c == '(':
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            return i
