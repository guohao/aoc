from helper import *


def h(s: str) -> int:
    n = 0
    for c in s:
        n = n + ord(c)
        n = n * 17
        n = n % 256
    return n


def h2(line: str) -> int:
    ret = 0
    for s in line.strip().split(','):
        ret += h(s)
    return ret


def h3(line: str) -> int:
    ret = 0
    box = [{} for _ in range(256)]
    for s in line.strip().split(','):
        add = False
        if '=' in s:
            a, b = s.split('=')
            b = int(b)
            add = True
        else:
            a = s.split('-')[0]
        idx = h(a)
        if add:
            if a in box[idx].keys():
                box[idx][a] = (box[idx][a][0], b)
            else:
                box[idx][a] = (len(box[idx]) + 1, b)
        else:
            if a in box[idx]:
                ai = box[idx][a][0]
                del box[idx][a]
                for x, y in box[idx].copy().items():
                    if y[0] > ai:
                        box[idx][x] = (y[0] - 1, y[1])
    for i in range(256):
        for a, b in box[i].values():
            ret += (i + 1) * a * b
    return ret


data = raw_data(2023, 15)
print(h2(data))
print(h3(data))
