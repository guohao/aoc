import re


def p1(data: str):
    l, h = list(map(int, data.split('-')))

    def match(s: str) -> bool:
        if sorted(s) != list(s):
            return False
        return any(s[x] == s[x + 1] for x in range(len(s) - 1))

    ans = 0
    for i in range(l, h + 1):
        ans += match(str(i))
    return ans


def p2(data: str):
    l, h = list(map(int, data.split('-')))

    def match(s: str) -> bool:
        if sorted(s) != list(s):
            return False
        for m in re.finditer(r'(\w)\1(?!\1)', s):
            if m.start() == 0 or s[m.start() - 1] != m.group(1):
                return True
        return False

    ans = 0
    for i in range(l, h + 1):
        ans += match(str(i))
    return ans
