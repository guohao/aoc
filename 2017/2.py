def p1is(line: list[int]):
    line.sort()
    return line[-1] - line[0]


def p2is(line: list[int]):
    for a in line:
        for b in line:
            if a == b:
                continue
            if a % b == 0:
                return a // b
