import re
from z3 import *


def ints(line):
    return list(map(int, re.findall(r'-?\d+', line)))


def bots_of_input(data: str):
    bots = []
    for line in data.splitlines():
        x, y, z, r = ints(line)
        bots.append(((x, y, z), r))
    return bots


data = sys.stdin.read()
bots = bots_of_input(data)
max_r = max(bot[1] for bot in bots)
bot = [bot for bot in bots if bot[1] == max_r][0]

in_range = 0
for i in range(len(bots)):
    a = bot[0]
    b = bots[i][0]
    if sum(abs(a[k] - b[k]) for k in range(3)) <= bot[1]:
        in_range += 1
print(in_range)
