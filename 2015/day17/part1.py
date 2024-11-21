import itertools
import sys

nums = []
for line in sys.stdin.readlines():
    line = line.strip()
    nums.append(int(line))

r = 0
for i in range(len(nums)):
    for p in itertools.combinations(nums, i):
        r += sum(p) == 150

print(r)
