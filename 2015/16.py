import re


def parse_sue(s):
    d = {}
    for m in re.finditer(r'(\w+): (\d+)', s):
        d[m.group(1)] = int(m.group(2))
    return d


def p1(data: str):
    expect = parse_sue(
        "children: 3, cats: 7, samoyeds: 2, pomeranians: 3, akitas: 0, vizslas: 0, goldfish: 5, trees: 3, cars: 2, perfumes: 1")
    for i, line in enumerate(data.splitlines(), start=1):
        if all(expect[k] == v for k, v in parse_sue(line).items()):
            return i


def p2(data: str):
    expect = parse_sue(
        "children: 3, cats: 7, samoyeds: 2, pomeranians: 3, akitas: 0, vizslas: 0, goldfish: 5, trees: 3, cars: 2, perfumes: 1")
    gs = {'cats', 'trees'}
    ls = {'pomeranians', 'goldfish'}

    def is_sue(actual):
        for k, v in parse_sue(line).items():
            if k in gs:
                if expect[k] >= v:
                    return False
            elif k in ls:
                if expect[k] <= v:
                    return False
            else:
                if expect[k] != v:
                    return False
        return True

    for i, line in enumerate(data.splitlines(), start=1):
        if is_sue(parse_sue(line)):
            return i
