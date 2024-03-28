def p1ss(line: str):
    a, b = line.split()
    a = 'ABC'.index(a) + 1
    b = 'XYZ'.index(b) + 1
    return ((b - a) % 3 - 2) % 3 * 3 + b


def p2ss(line: str):
    a, b = line.split()
    a = 'ABC'.index(a) + 1
    b = 'XYZ'.index(b) + 1
    return (b - 1) * 3 + (a + b) % 3 + 1
