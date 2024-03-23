import hashlib
import itertools
import re
from functools import cache


def solve(data: str, hash_times=1):
    data = data.strip()
    seq = []

    @cache
    def h(s: str):
        for _ in range(hash_times):
            s = hashlib.md5(s.encode()).hexdigest()
        return s

    for i in itertools.count():
        md5 = h(data + str(i))
        m = re.search(r'(\w)\1\1', md5)
        if not m:
            continue
        for j in range(i + 1, i + 1001):
            if m.group(1) * 5 in h(data + str(j)):
                seq.append(i)
                if len(seq) == 64:
                    return i
                break


def p1(data: str):
    return solve(data, 1)


def p2(data: str):
    return solve(data, 2017)
