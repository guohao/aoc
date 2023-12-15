from helper import *


def h(s: str) -> int:
    n = 0
    for c in s:
        n = ((n + ord(c)) * 17) % 256
    return n


def h3(line: str) -> int:
    ret = 0
    box = [{} for _ in range(256)]
    for s in line.strip().split(','):
        add = False
        if '=' in s:
            a, b = s.split('=')
            bb = int(b)
            add = True
        else:
            a = s.split('-')[0]
        b = box[h(a)]
        if add:
            if a in b.keys():
                b[a] = (b[a][0], bb)
            else:
                b[a] = (len(b) + 1, bb)
        else:
            if a in b:
                for x, y in b.copy().items():
                    if y[0] > b[a][0]:
                        b[x] = (y[0] - 1, y[1])
                del b[a]
    for i in range(256):
        for a, b in box[i].values():
            ret += (i + 1) * a * b
    return ret


data = raw_data(2023, 15)
print(sum(h(s) for s in data.strip().split(',')))
print(h3(data))
