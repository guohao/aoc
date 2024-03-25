def p1ss(line: str):
    a = line
    b = line[1:] + line[0]
    return sum(int(a[i]) for i in range(len(line)) if a[i] == b[i])


def p2ss(line: str):
    hl = len(line) // 2
    a = line[:hl]
    b = line[hl:]
    return 2 * sum(int(a[i]) for i in range(hl) if a[i] == b[i])
