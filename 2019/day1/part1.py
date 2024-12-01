import sys

nums = [int(line.strip()) for line in sys.stdin.readlines()]
t = 0
for n in nums:
    t += n // 3 - 2
print(t)
