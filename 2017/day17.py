from helper import *

data = raw_data(2017, 17)


def p1():
    seq = [0]
    step = 382
    i = 0
    for k in range(1, 2018):
        i = (i + step) % len(seq) + 1
        seq = seq[:i] + [k] + seq[i:]
    print(seq[(i + 1) % len(seq)])


def p2():
    step = 382
    i = 0
    iz = 0
    ans = -1
    for k in range(1, 50000000 + 1):
        i = (i + step) % k + 1
        if i == iz + 1:
            ans = k
        elif i <= iz:
            iz += 1
    print(ans)


p1()
p2()
