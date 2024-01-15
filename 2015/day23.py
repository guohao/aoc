from helper import *

data = raw_data(2015, 23)
lines = lines(data)


def solve(a):
    d = {'a': a, 'b': 0}
    i = 0
    while i < len(lines):
        instruction = lines[i].replace(',', '')
        cells = instruction.split()
        cmd = cells[0]
        match cmd:
            case 'hlf':
                d[cells[1]] //= 2
            case 'tpl':
                d[cells[1]] *= 3
            case 'inc':
                d[cells[1]] += 1
            case 'jmp':
                i += int(cells[1])
                continue
            case 'jie':
                if d[cells[1]] % 2 == 0:
                    i += int(cells[2])
                    continue
            case 'jio':
                if d[cells[1]] == 1:
                    i += int(cells[2])
                    continue
        i += 1
    print(d['b'])


solve(0)
solve(1)