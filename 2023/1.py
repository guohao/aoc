from util import *


def p1ss(line: str):
    ds = digits(line)
    return ds[0] * 10 + ds[-1]


def p2ss(line: str):
    pds = "one|two|three|four|five|six|seven|eight|nine"
    d2i = {}
    for i, l in zip(range(1, 10), pds.split('|')):
        d2i[l] = i
        d2i[str(i)] = i
    ds = re.findall(f'(?=({pds}|\\d))', line)
    return d2i[ds[0]] * 10 + d2i[ds[-1]]
