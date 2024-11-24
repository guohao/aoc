import sys
import re

lines = [line.strip() for line in sys.stdin.readlines()]
AB = []
for line in lines:
    nums = list(map(int, re.findall(r'-?\d+', line)))
    AB.append(nums[0])
a, b = AB

i = 0
ans = 0
N = 40000000
while i < N:
    a = (a * 16807) % 2147483647
    b = (b * 48271) % 2147483647
    if a & 0xFFFF == b & 0xFFFF:
        ans += 1
    i += 1
print(ans)
