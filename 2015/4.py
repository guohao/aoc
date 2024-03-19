import hashlib
import itertools


def solve(data: str, n):
    data = data.strip()
    for i in itertools.count(1):
        md5 = hashlib.md5()
        md5.update((data + str(i)).encode())
        if md5.hexdigest().startswith('0' * n):
            return i


def p1(data: str):
    return solve(data, 5)


def p2(data: str):
    return solve(data, 6)
