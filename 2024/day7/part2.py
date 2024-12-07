from itertools import product
import re
import sys

lines = [l.strip() for l in sys.stdin.readlines()]
t = 0
for line in lines:
    nums = list(map(int, re.findall(r'-?\d+', line)))
    for c in product(['+', '*', '||'], repeat=len(nums) - 2):
        s = nums[1]
        for i in range(len(c)):
            if c[i] == '+':
                s += nums[i + 2]
            elif c[i] == '*':
                s *= nums[i + 2]
            else:
                s = s * (10 ** len(str(nums[i + 2]))) + nums[i + 2]
        if s == nums[0]:
            t += nums[0]
            break
print(t)
