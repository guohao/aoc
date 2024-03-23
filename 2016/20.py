def p1(data: str):
    ranges = []
    for line in data.splitlines():
        a, b = line.split('-')
        ranges.append((int(a), int(b)))

    i = 0
    while i < 4294967295:
        valid = True
        for a, b in ranges:
            if a <= i <= b:
                i = b + 1
                valid = False
                break
        if valid:
            return i


def p2(data: str):
    ranges = []
    for line in data.splitlines():
        a, b = line.split('-')
        ranges.append((int(a), int(b)))

    i = 0
    ans = 0
    while i < 4294967295:
        valid = True
        for a, b in ranges:
            if a <= i <= b:
                i = b + 1
                valid = False
                break
        if valid:
            ans += 1
            i += 1

    return ans
