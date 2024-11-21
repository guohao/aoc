import sys

program = [line.strip() for line in sys.stdin.readlines()]

pc = 0

r = {'a': 0, 'b': 0}
while pc < len(program):
    i = program[pc]
    if 'hlf' in i:
        r[i.split()[-1]] //= 2
    elif 'tpl' in i:
        r[i.split()[-1]] *= 3
    elif 'inc' in i:
        r[i.split()[-1]] += 1
    elif 'jmp' in i:
        pc += int(i.split()[-1])
        continue
    elif 'jie' in i:
        if r[i[4]] % 2 == 0:
            pc += int(i.split()[-1])
            continue
    elif 'jio' in i:
        if r[i[4]] == 1:
            pc += int(i.split()[-1])
            continue
    else:
        raise Exception(i)
    pc += 1
print(r['b'])
