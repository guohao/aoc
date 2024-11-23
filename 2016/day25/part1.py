import itertools
import sys

lines = [line.strip() for line in sys.stdin.readlines()]


def tick(a) -> bool:
    r = {x: 0 for x in 'abcd'}
    r['a'] = a

    def value_of(n: str):
        if n in 'abcd':
            return r[n]
        return int(n)

    i = 0
    c = itertools.cycle([0, 1])
    cnt = 0
    while i < len(lines):
        cmd, *args = lines[i].split()
        if 'cpy' == cmd:
            r[args[1]] = value_of(args[0])
        elif 'inc' == cmd:
            r[args[0]] += 1
        elif 'dec' == cmd:
            r[args[0]] -= 1
        elif 'out' == cmd:
            if value_of(args[0]) != next(c):
                return False
            cnt += 1
            if cnt == 10:
                return True
        elif 'jnz' == cmd:
            if value_of(args[0]):
                i += value_of(args[1])
                continue
        i += 1
    return False


for k in itertools.count():
    if tick(k):
        print(k)
        break
