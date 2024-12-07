import math
import re
import sys

op_all = {
    'addr': lambda r, a, b: r[a] + r[b],
    'addi': lambda r, a, b: r[a] + b,
    'mulr': lambda r, a, b: r[a] * r[b],
    'muli': lambda r, a, b: r[a] * b,
    'banr': lambda r, a, b: r[a] & r[b],
    'bani': lambda r, a, b: r[a] & b,
    'borr': lambda r, a, b: r[a] | r[b],
    'bori': lambda r, a, b: r[a] | b,
    'setr': lambda r, a, _: r[a],
    'seti': lambda r, a, _: a,
    'gtir': lambda r, a, b: int(a > r[b]),
    'gtri': lambda r, a, b: int(r[a] > b),
    'gtrr': lambda r, a, b: int(r[a] > r[b]),
    'eqir': lambda r, a, b: int(a == r[b]),
    'eqri': lambda r, a, b: int(r[a] == b),
    'eqrr': lambda r, a, b: int(r[a] == r[b])}


def x_of(n: int):
    ans = []
    for x in range(1, int(math.sqrt(n) + 1)):
        if n % x == 0:
            ans.append(x)
            ans.append(n // x)
    return sum(ans)


def ints(line):
    return list(map(int, re.findall(r'-?\d+', line)))


lines = sys.stdin.readlines()
ipr = ints(lines[0])[0]
r = [0] * 6
r[0] = 0
instructions = lines[1:]
while r[ipr] < len(instructions):
    line = instructions[r[ipr]]
    op = op_all[line.split()[0]]
    a, b, c = ints(line)
    r[c] = op(r, a, b)
    r[ipr] += 1

print(r[0])