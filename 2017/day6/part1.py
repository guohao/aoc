from itertools import count

import re

nums = list(map(int, re.findall(r'-?\d+', input())))

seen = set()
for _ in count(1):
    if tuple(nums) in seen:
        print(len(seen))
        break
    seen.add(tuple(nums))
    most = max(nums)
    t = -1
    for j, n in enumerate(nums):
        if n == most:
            t = j
            break
    k = most // 16
    m = most % 16
    nums[t] = 0
    for j in range(16): nums[j] += k;
    for j in range(1, m + 1): nums[(j + t) % 16] += 1;
