import functools
import re
from typing import List, Tuple

import helper


def cmp1(a: Tuple[List[int], int], b: Tuple[List[int], int]) -> int:
    a = a[0]
    b = b[0]

    ac = sorted([a.count(x) for x in set(a)])
    bc = sorted([b.count(x) for x in set(b)])
    if len(bc) != len(ac):
        return len(bc) - len(ac)
    for i in range(1, min(len(ac), len(bc))):
        if ac[-i] != bc[-i]:
            return ac[-i] - bc[-i]
    for i in range(5):
        if a[i] != b[i]:
            return a[i] - b[i]
    return 0


def cmp(a: Tuple[List[int], int], b: Tuple[List[int], int]) -> int:
    a = [x if x != 11 else 1 for x in a[0]]
    b = [x if x != 11 else 1 for x in b[0]]

    ac = [a.count(x) for x in set(a) if x != 1]
    ac.sort()
    if len(ac) > 0:
        ac[-1] += a.count(1)
    else:
        ac = [5]
    bc = [b.count(x) for x in set(b) if x != 1]
    bc.sort()
    if len(bc) > 0:
        bc[-1] += b.count(1)
    else:
        bc = [5]

    m = len(bc) - len(ac)
    if m != 0:
        return m
    for i in range(1, min(len(ac), len(bc))):
        m = ac[-i] - bc[-i]
        if m != 0:
            return m
    for i in range(5):
        m = a[i] - b[i]
        if m != 0:
            return m
    return 0


data = helper.raw_data(2023, 7)

ctn = "0023456789TJQKA"
lines = data.strip().splitlines()
hands = []
for line in lines:
    hand = [ctn.index(x) for x in re.findall(r'\w', line.split()[0])]
    hands.append((hand, int(line.split()[1])))
hands.sort(key=functools.cmp_to_key(cmp1))
# 251106089
# 249620106
print(sum(bid * rank for bid, (_, rank) in enumerate(hands, start=1)))

hands.sort(key=functools.cmp_to_key(cmp))
print(sum(bid * rank for bid, (_, rank) in enumerate(hands, start=1)))
