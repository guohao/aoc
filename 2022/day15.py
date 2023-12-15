import functools

from helper import *


def d(a, b) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


data = """
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
"""
data = raw_data(2022, 15)
lines = data.strip().splitlines()
BS = {}
for line in lines:
    x1, y1, x2, y2 = list(map(int, re.findall(r'-?\d+', line)))
    BS[(x1, y1)] = (x2, y2)


def check(p) -> bool:
    for s, b in BS.items():
        if d(p, s) <= d(s, b):
            return True
    return False


def p1(y):
    ret = set()
    for a, b in BS.items():
        diff = d(a, b) - abs(a[1] - y)
        for i in range(a[0] - diff, a[0] + diff + 1):
            ret.add(i)

    for b in BS.values():
        if b[1] == y and b[0] in ret:
            ret.remove(b[0])
    print(len(ret))


def p2():
    x_r = range(0, 4000000)
    y_r = range(0, 4000000)
    for y in y_r:
        nv = []
        for a, b in BS.items():
            diff = d(a, b) - abs(a[1] - y)
            nv.append(range(max(0, a[0] - diff), min(4000000, a[0] + diff + 1)))
        x = 0
        while x in x_r:
            found = False
            for v in nv:
                if x in v:
                    found = True
                    x = v.stop
            if not found:
                break
        if x in x_r:
            print(x * 4000000 + y)
            break


p1(2000000)
p2()
