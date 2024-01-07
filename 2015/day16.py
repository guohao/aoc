from helper import *

data = raw_data(2015, 16)

memo = """
children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1
"""
d = [line.split(':') for line in lines(memo)]
d = {k: int(v) for k, v in d}


def p1():
    for line in lines(data):
        name = line[:line.index(':')]
        name = name.split()[1]
        match = True
        for each in line[line.index(':') + 1:].split(','):
            item, num = each.split(':')
            item = item.strip()
            num = int(num)
            if d[item] != num:
                match = False
                break
        if match:
            print(name)
            break


def p2():
    for line in lines(data):
        name = line[:line.index(':')]
        name = name.split()[1]
        match = True
        for each in line[line.index(':') + 1:].split(','):
            item, num = each.split(':')
            item = item.strip()
            num = int(num)
            if d[item] != num:
                if item in ['cats', 'trees']:
                    if d[item] >= num:
                        match = False
                        break
                elif item in ['pomeranians', 'goldfish']:
                    if d[item] <= num:
                        match = False
                        break
                else:
                    match = False
                    break
        if match:
            print(name)
            break


p1()
p2()
