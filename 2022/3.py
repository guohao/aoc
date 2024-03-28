import string


def p1ss(line: str):
    n = len(line) // 2
    return string.ascii_letters.index(list(set(line[:n]) & set(line[n:]))[0]) + 1


def p2(data: str):
    lines = data.splitlines()
    ans = 0
    for i in range(0, len(lines), 3):
        cs = set(lines[i])
        for j in range(3):
            cs &= set(lines[i + j])
        ans += string.ascii_letters.index(list(cs)[0]) + 1
    return ans
