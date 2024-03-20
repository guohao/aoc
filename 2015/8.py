def p1ss(line: str):
    return len(line) - len(eval(line))


def p2ss(line: str):
    return line.count('\\') + line.count('"') + 2
