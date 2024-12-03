import re

l, r = map(int, input().split('-'))
t = 0

for i in range(l, r + 1):
    s = str(i)
    if sorted(s) != list(s):
        continue
    if any(len(m.group()) == 2 for m in re.finditer(r'(\d)\1+', s)):
        t += 1

print(t)
