def p1ss(line: str):
    return len(line.split()) == len(set(line.split()))


def p2ss(line: str):
    return len(line.split()) == len(set(''.join(sorted(cell)) for cell in line.split()))
