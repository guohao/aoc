def solve(s: str, n):
    s = s.strip()
    ans = 0
    for _ in range(n):
        ans += s.count('.')
        s = '.' + s + '.'
        ns = ''
        for i in range(1, len(s) - 1):
            if s[i - 1] != s[i + 1]:
                ns += '^'
            else:
                ns += '.'
        s = ns
    return ans


def p1(s: str):
    return solve(s, 40)


def p2(s: str):
    return solve(s, 400000)
