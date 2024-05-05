import math
from collections import Counter


def p1(data: str):
    common = ['', '']
    for x in zip(*data.splitlines()):
        c = Counter(x).most_common()
        common[0] += c[0][0]
        common[1] += c[-1][0]
    return math.prod(int(x, 2) for x in common)


def p2(data: str):
    def rating(most_common: bool):
        remains = data.splitlines()
        for i in range(len(remains[0])):
            if len(remains) == 1:
                return int(remains[0], 2)
            c = Counter(list(zip(*remains))[i])
            if c['1'] == c['0']:
                pick = '1' if most_common else '0'
            else:
                pick = c.most_common()[not most_common][0]
            remains = [x for x in remains if x[i] == pick]

    return rating(True) * rating(False)
