from helper import *

data = raw_data(2017, 4)


def p1():
    ans = 0
    for line in lines(data):
        l = line.split()
        if len(set(l)) == len(l):
            ans += 1
    return ans


def p2():
    ans = 0
    for line in lines(data):
        l = line.split()
        l = [''.join(sorted(x)) for x in l]
        if len(set(l)) == len(l):
            ans += 1
    return ans


print(p1())
print(p2())
