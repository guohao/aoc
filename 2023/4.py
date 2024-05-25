import re


def p1ss(line: str):
    _, wn, hn = re.split(r'[:|]', line)
    wn = re.findall(r'\d+', wn)
    hn = re.findall(r'\d+', hn)
    c = sum(x in wn for x in hn)
    if c == 0:
        return 0
    return 2 ** (c - 1)


def p2(data: str):
    c2c = {i: 1 for i in range(1, len(data.splitlines()) + 1)}
    for line in data.splitlines():
        c, wn, hn = re.split(r'[:|]', line)
        c = int(re.findall(r'\d+', c)[0])
        wn = re.findall(r'\d+', wn)
        hn = re.findall(r'\d+', hn)
        for i in range(c + 1, c + 1 + sum(x in wn for x in hn)):
            c2c[i] += c2c[c]
    return sum(c2c.values())
