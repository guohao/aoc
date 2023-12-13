from helper import *

data = raw_data(2023, 13)


def f(lines: List[str], diff: int) -> int:
    n = len(lines)
    c = 0
    for i in range(1, n):
        r = min(n - i, i)
        a = lines[i - r:i + r]
        b = a[::-1]
        if count_differences_in_lists(a, b) == diff:
            c += i
    return c


ans = 0
ans2 = 0
for p in patterns(data):
    ans += 100 * f(p, 0)
    ans += f(rotate_matrix_90_clockwise(p), 0)
    ans2 += 100 * f(p, 2)
    ans2 += f(rotate_matrix_90_clockwise(p), 2)

print(ans)
print(ans2)
