def p1(data: str):
    data = data.strip()
    i = 0
    lvl = 0
    ans = 0
    ignore = False
    while i < len(data):
        c = data[i]
        if c == '{':
            if not ignore:
                lvl += 1
        elif c == '}':
            if not ignore:
                ans += lvl
                lvl -= 1
        elif c == '!':
            i += 1
        elif c == '<':
            ignore = True
        elif c == '>':
            ignore = False
        i += 1
    return ans


def p2(data: str):
    data = data.strip()
    i = 0
    ans = 0
    ignore = False
    while i < len(data):
        c = data[i]
        if c == '!':
            i += 1
        elif c == '<':
            if ignore:
                ans += 1
            ignore = True
        elif c == '>':
            ignore = False
        else:
            if ignore:
                ans += 1
        i += 1
    return ans
