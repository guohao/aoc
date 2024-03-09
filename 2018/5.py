import re


def p1(data: str):
    pattern = '|'.join([chr(ord('a') + i) + chr(ord('A') + i) for i in range(26)])
    pattern = pattern + '|' + pattern[::-1]
    s = data.strip()
    last = ''
    while last != s:
        last = s
        s = re.sub(pattern, '', s)
    return len(last)


def p2(data: str):
    ans = len(data)
    for i in range(26):
        l = chr(ord('a') + i)
        u = chr(ord('A') + i)
        s = re.sub(l + '|' + u, '', data)
        ans = min(ans, p1(s))
    return ans
