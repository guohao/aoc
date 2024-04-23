def p1ss(line: str):
    p, s = list(map(str.strip, line.split(':')))
    rng, paddle = p.split()
    l, r = list(map(int, rng.split('-')))
    return l <= s.count(paddle) <= r


def p2ss(line: str):
    p, s = list(map(str.strip, line.split(':')))
    rng, paddle = p.split()
    l, r = [x - 1 for x in list(map(int, rng.split('-')))]
    return (s[l] == paddle) ^ (s[r] == paddle)
