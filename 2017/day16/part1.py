import re
import string

s = string.ascii_lowercase[:16]
for cmd in input().split(","):
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
print(s)
