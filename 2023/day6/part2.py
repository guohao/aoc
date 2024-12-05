import re
import sys

lines = [list(map(int, re.findall(r'-?\d+', line.strip().replace(' ', '')))) for line in sys.stdin.readlines()]
ans = 1
for t, d in zip(*lines):
    ans *= sum(x * (t - x) > d for x in range(t))

print(ans)
