from helper import *

data = raw_data(2016, 20)
lines = lines(data)


def p1():
    bl = []
    for line in lines:
        bl.append(tuple(int(x) for x in line.split('-')))
    bl.sort(key=lambda x: x[0])
    for i in range(len(bl)):
        candidate = bl[i][1] + 1
        contain = False
        for j in range(len(bl)):
            if bl[j][0] <= candidate <= bl[j][1]:
                contain = True
                break
        if not contain:
            print(candidate)
            break
    # print(bl)


def p2():
    bl = []
    for line in lines:
        bl.append(tuple(int(x) for x in line.split('-')))
    bl.sort(key=lambda x: x[0])
    while True:
        blz = len(bl)
        for a in bl.copy():
            for b in bl.copy():
                if a == b:
                    continue
                if a not in bl or b not in bl:
                    continue
                if a[1] >= b[0] - 1 and a[0] < b[1]:
                    bl.remove(a)
                    bl.remove(b)
                    bl.append((min(b[0], a[0]), max(b[1], a[1])))
        if blz == len(bl):
            break
    bl.sort(key=lambda x: x[0])
    st = 0
    ans = 0
    for i in range(len(bl)):
        ans += bl[i][0] - st
        st = bl[i][1] + 1
    print(ans)


p1()
p2()
