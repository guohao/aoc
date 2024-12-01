import sys

nums = [int(line.strip()) for line in sys.stdin.readlines()]
t = 0
for n in nums:
    while n // 3 - 2 > 0:
        n = n // 3 - 2
        t += n
print(t)
