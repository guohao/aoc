import re
import sys


def ext(ints):
    if all(x == 0 for x in ints):
        return 0
    return ints[0] - ext([ints[i] - ints[i - 1] for i in range(1, len(ints))])


print(sum(ext(list(map(int, re.findall(r'-?\d+', l)))) for l in sys.stdin.readlines()))
