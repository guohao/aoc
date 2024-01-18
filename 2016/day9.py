import re

from helper import *

data = raw_data(2016, 9).strip()


def p1(s):
    i = 0
    ans = 0
    while i < len(s):
        if s[i] != '(':
            ans += 1
            i += 1
        else:
            m = re.search(r'\((\d+)x(\d+)\)', s[i:])
            sl = int(m.group(1))
            repeat = int(m.group(2))
            ans += len(s[i + m.end():i + m.end() + sl] * repeat)
            i = i + m.end() + sl
    print(ans)


def p2(s) -> int:
    i = 0
    ans = 0
    while i < len(s):
        if s[i] == '(':
            m = re.search(r'\((\d+)x(\d+)\)', s[i:])
            sl = int(m.group(1))
            repeat = int(m.group(2))
            ans += p2(s[i + m.end():i + m.end() + sl]) * repeat
            i = i + m.end() + sl
        else:
            ans += 1
            i += 1
    return ans


p1(data)
print(p2(data))
