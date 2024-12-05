import sys
import re

t = 0
parts = sys.stdin.read().split('\n\n')
p0 = []
for l in parts[0].splitlines():
    a, b = map(int, l.split('|'))
    p0.append((a, b))

p1 = []
for l in parts[1].splitlines():
    nums = list(map(int, re.findall(r'-?\d+', l)))
    for a, b in p0:
        if a in nums and b in nums:
            if nums.index(a) > nums.index(b):
                break
    else:
        t += nums[len(nums) // 2]
print(t)
