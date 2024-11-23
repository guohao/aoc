import sys

nums = [int(line.strip()) for line in sys.stdin.readlines()]
t = 0
i = 0
while 0 <= i < len(nums):
    n = nums[i]
    nums[i] += 1
    i += n
    t += 1

print(t)
