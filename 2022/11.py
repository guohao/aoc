import math
import re
import sys
from collections import deque, Counter

sys.set_int_max_str_digits(9999999)


def ints(s: str):
    return list(map(int, re.findall(r'\d+', s)))


def p1(data: str):
    mks = []
    inspected = Counter()
    for part in data.split('\n\n'):
        lines = part.splitlines()
        items = ints(lines[1])
        operation = lines[2]
        test = ints(lines[3])[0]
        true_to = ints(lines[4])[0]
        false_to = ints(lines[5])[0]
        mks.append((deque(items), operation, test, true_to, false_to))
    for _ in range(20):
        for i in range(len(mks)):
            mk = mks[i]
            while mk[0]:
                inspected[i] += 1
                item = mk[0].popleft()
                item = eval(mk[1].replace('old', str(item)).split('=')[1])
                item //= 3
                if item % mk[2] == 0:
                    mks[mk[3]][0].append(item)
                else:
                    mks[mk[4]][0].append(item)
    return math.prod(c for _, c in inspected.most_common(2))


def p2(data: str):
    mks = []
    inspected = Counter()
    m = 1
    for part in data.split('\n\n'):
        lines = part.splitlines()
        items = ints(lines[1])
        operation = lines[2]
        test = ints(lines[3])[0]
        m *= test
        true_to = ints(lines[4])[0]
        false_to = ints(lines[5])[0]
        mks.append((deque(items), operation, test, true_to, false_to))
    for _ in range(10000):
        for i in range(len(mks)):
            mk = mks[i]
            while mk[0]:
                inspected[i] += 1
                item = mk[0].popleft()
                item = eval(mk[1].replace('old', str(item)).split('=')[1])
                item = item % m
                if item % mk[2] == 0:
                    mks[mk[3]][0].append(item)
                else:
                    mks[mk[4]][0].append(item)
    return math.prod(c for _, c in inspected.most_common(2))
