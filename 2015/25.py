import re


def p1(data: str):
    r, c = list(map(int, re.findall(r'\d+', data)))
    x, y = 1, 1
    n = 20151125
    while x != r or y != c:
        if x == 1:
            x = y + 1
            y = 1
        else:
            x -= 1
            y += 1
        n = (n * 252533) % 33554393
    return n
