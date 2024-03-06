def p1(data: str):
    return sum(1 for line in data.splitlines() if len(set(line.split())) == len(line.split()))


def p2(data: str):
    ans = 0
    for line in data.splitlines():
        line = line.split()
        line = [''.join(sorted(x)) for x in line]
        if len(set(line)) == len(line):
            ans += 1
    return ans
