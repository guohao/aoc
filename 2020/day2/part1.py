import re
import sys

lines = [line.strip() for line in sys.stdin.readlines()]
ans = 0
for line in lines:
    f, t, c, s = re.match(r'(\d+)-(\d+) (\w): (\w+)', line).groups()
    if int(f) <= s.count(c) <= int(t):
        ans += 1
print(ans)
