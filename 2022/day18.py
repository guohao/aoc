import functools

from helper import *

data = """
2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
"""

# data = raw_data(2022, 18)
lines = lines(data)

cubes = [nums(line) for line in lines]
ans = 6 * len(cubes)
for i, a in enumerate(cubes):
    for b in cubes[:i]:
        if sum(abs(a[k] - b[k]) for k in range(3)) == 1:
            ans -= 2
    for c in itertools.product([0, 1, -1], repeat=3):
        print(c)
print(ans)
