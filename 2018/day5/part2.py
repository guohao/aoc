import re
import string

origin = input()
p = []
for i in range(26):
    aA = string.ascii_lowercase[i] + string.ascii_uppercase[i]
    p.append(aA)
    p.append(aA[::-1])

p = '|'.join(p)
ans = len(origin)
for i in range(26):
    aA = string.ascii_lowercase[i] + '|' + string.ascii_uppercase[i]
    d = origin
    d = re.sub(aA, '', d)
    while True:
        d, n = re.subn(p, '', d)
        if n == 0:
            ans = min(ans, len(d))
            break
print(ans)
