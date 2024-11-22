import sys
import re

lines = [line.strip() for line in sys.stdin.readlines()]
rules = []
for line in lines:
    nums = list(map(int, re.findall(r'\d+', line)))
    rules.append(nums)

rules = sorted(rules, key=lambda x: x[1])

ip = 0
ans = 0
while ip <= 4294967295:
    for i in range(len(rules)):
        r = rules[i]
        if r[0] <= ip <= r[1]:
            ip = r[1] + 1
            break
    else:
        ip += 1
        ans += 1
print(ans)
