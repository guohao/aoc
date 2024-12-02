import sys

ls = [line.strip() for line in sys.stdin.readlines()]

t = 0
for line in ls:
    nums = list(map(int, re.findall(r'-?\d+', line)))
    if nums == sorted(nums) or nums == sorted(nums, reverse=True):
        for i in range(1, len(nums)):
            if not (1 <= abs(nums[i] - nums[i - 1]) <= 3):
                break
        else:
            t += 1

print(t)
