import sys
import re
from functools import cache

lines = [line.strip() for line in sys.stdin.readlines()]
AB = []
for line in lines:
    nums = list(map(int, re.findall(r'-?\d+', line)))
    AB.append(nums[0])
a, b = AB


@cache
def gen_next_a(prev: int) -> int:
    v = (prev * 16807) % 2147483647
    while v % 4 != 0:
        v = (v * 16807) % 2147483647
    return v


@cache
def gen_next_b(prev: int) -> int:
    v = (prev * 48271) % 2147483647
    while v % 8 != 0:
        v = (v * 48271) % 2147483647
    return v


ans = 0
N = 5000000
for i in range(N):
    a = gen_next_a(a)
    b = gen_next_b(b)
    if a & 0xFFFF == b & 0xFFFF:
        ans += 1
print(ans)
