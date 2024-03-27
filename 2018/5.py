import math
import re
import string


def p1(data: str):
    data = data.strip()
    while True:
        pl = len(data)
        for i in range(26):
            l = string.ascii_lowercase[i]
            u = string.ascii_uppercase[i]
            data = re.sub(r'{0}{1}|{1}{0}'.format(l, u), '', data)
        if pl == len(data):
            return pl


def p2(data: str):
    ans = math.inf
    for i in range(26):
        s = data.replace(string.ascii_lowercase[i], '')
        s = s.replace(string.ascii_uppercase[i], '')
        ans = min(ans, p1(s))
    return ans
