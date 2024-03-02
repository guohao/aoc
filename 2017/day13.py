from helper import *

data = raw_data(2017, 13)


def solve():
    drs = [ints(line) for line in lines(data)]
    print(sum(d * r for d, r in drs if d % (r * 2 - 2) == 0))
    for x in itertools.count():
        if all((x + d) % (r * 2 - 2) for d, r in drs):
            print(x)
            break


solve()
