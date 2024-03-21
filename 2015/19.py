import re


def p1(data: str):
    parts = data.split('\n\n')
    subs = []
    for line in parts[0].splitlines():
        rep, sub = re.findall(r'\w+', line)
        subs.append((rep, sub))
    molecule = parts[1].strip()
    created = set()
    for rep, sub in subs:
        for m in re.finditer(rep, molecule):
            created.add(molecule[:m.start()] + sub + molecule[m.end():])
    return len(created)


def p2(data: str):
    data = data.split('\n\n')[1]

    cells = sum([c.isupper() for c in data])
    parentheses = data.count('Rn') + data.count('Ar')
    periods = 2 * data.count('Y')
    return cells - parentheses - periods - 1
