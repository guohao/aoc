import sys
import re

lines = [line.strip() for line in sys.stdin.readlines()]
rules = []
for line in lines:
    nums = list(map(int, re.findall(r'\d+', line)))
    rules.append(nums)

rules = sorted(rules,key=lambda x:x[1])

ans = 0
while True:
    for i in range(len(rules)):
        r = rules[i]
        if r[0] <=ans <= r[1]:
            ans = r[1]+1
            break
    else:
        print(ans)
        break
