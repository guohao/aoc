import sys

lines = [line.strip() for line in sys.stdin.readlines()]
r = {x: 0 for x in 'abcd'}
r['c'] = 1
i = 0


def value_of(n: str):
    if n in 'abcd':
        return r[n]
    return int(n)


while i < len(lines):
    cmd, *args = lines[i].split()
    if 'cpy' == cmd:
        r[args[1]] = value_of(args[0])
    elif 'inc' == cmd:
        r[args[0]] += 1
    elif 'dec' == cmd:
        r[args[0]] -= 1
    elif 'jnz' == cmd:
        if value_of(args[0]):
            i += value_of(args[1])
            continue
    i += 1
print(r['a'])
