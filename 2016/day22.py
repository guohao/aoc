from helper import *

data = raw_data(2016, 22)
lines = lines(data)

nodes = []
for line in lines:
    if line.startswith("/dev/grid/node"):
        x, y, size, used, avail, _ = ints(line)
        nodes.append((x, y, size, used, avail))


def p1():
    cnt = 0
    for a in nodes:
        for b in nodes:
            if a == b:
                continue
            if a[3] > 0 and a[3] <= b[4]:
                cnt += 1
    print(cnt)


def p2():
    for node in nodes:
        if node[3] == 0:
            print(node[1] + node[0] + 37 + 5 * 36)
            break


p1()
p2()
