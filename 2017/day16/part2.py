import re
import string

ans = string.ascii_lowercase[:16]

cmds = input().split(',')


def dance(s: str) -> str:
    for cmd in cmds:
        if 's' in cmd:
            x = int(cmd[1:])
            s = s[-x:] + s[:-x]
        elif 'x' in cmd:
            a, b = map(int, cmd[1:].split('/'))
            a, b = s[a], s[b]
            s = re.sub(a + "|" + b, lambda m: a if m.group() == b else b, s)
        elif cmd[0] == 'p':
            a, b = cmd[1:].split('/')
            s = re.sub(a + '|' + b, lambda m: a if m.group() == b else b, s)
    return s


i = 0
seen = {}
N = 1000000000
while i < N:
    if ans in seen:
        i += (N - i) // (i - seen[ans]) * (i - seen[ans])
    seen[ans] = i
    ans = dance(ans)
    i += 1
print(ans)
