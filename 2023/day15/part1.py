import sys


def h(s):
    v = 0
    for c in s:
        v += ord(c)
        v *= 17
        v %= 256
    return v


print(sum(map(h, sys.stdin.read().strip().split(','))))
