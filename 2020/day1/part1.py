import sys

nums = set([int(line.strip()) for line in sys.stdin.readlines()])
t = 0
for n in nums:
    if 2020 - n in nums:
        print(n*(2020-n))
        break
