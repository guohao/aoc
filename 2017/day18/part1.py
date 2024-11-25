import re
import sys
from collections import defaultdict

lines = [line.strip() for line in sys.stdin.readlines()]
r = defaultdict(int)


def v_of(n: str):
    if re.fullmatch(r'-?\d+', n):
        return int(n)
    return r[n]


i = 0

while 0 <= i < len(lines):
    cmd, *args = lines[i].split()
    if 'snd' == cmd:
        r['snd'] = v_of(args[0])
    elif 'set' == cmd:
        r[args[0]] = v_of(args[1])
    elif 'mul' == cmd:
        r[args[0]] *= v_of(args[1])
    elif 'add' == cmd:
        r[args[0]] += v_of(args[1])
    elif 'mod' == cmd:
        r[args[0]] %= v_of(args[1])
    elif 'rcv' == cmd:
        if v_of(args[0]):
            print(r['snd'])
            exit()
    elif 'jgz' == cmd:
        if v_of(args[0]) > 0:
            i += v_of(args[1])
            continue
    else:
        raise Exception(lines[i])
    i += 1
