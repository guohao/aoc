import sys

lines = [line.strip() for line in sys.stdin.readlines()]
r = {x: 0 for x in 'abcd'}
r['a'] =7

def value_of(n: str):
    if n in 'abcd':
        return r[n]
    return int(n)


i = 0
while i < len(lines):
    cmd, *args = lines[i].split()
    if 'cpy' == cmd:
        if args[1] in 'abcd':
            r[args[1]] = value_of(args[0])
    elif 'inc' == cmd:
        r[args[0]] += 1
    elif 'dec' == cmd:
        r[args[0]] -= 1
    elif 'tgl' in cmd:
        t = value_of(args[0]) + i
        if 0 <= t < len(lines):
            tc = lines[t].split()
            if len(tc) == 2:
                if tc[0] == 'inc':
                    lines[t] = f'dec {tc[1]}'
                else:
                    lines[t] = f'inc {tc[1]}'
            elif len(tc) == 3:
                if tc[0] == 'jnz':
                    lines[t] = f'cpy {tc[1]} {tc[2]}'
                else:
                    lines[t] = f'jnz {tc[1]} {tc[2]}'
            else:
                raise Exception(cmd)
    elif 'jnz' == cmd:
        if value_of(args[0]):
            i += value_of(args[1])
            continue
    else:
        raise Exception(cmd)

    i += 1
print(r['a'])
