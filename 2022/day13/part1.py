import sys


def f(a, b) -> int:
    if not isinstance(a, list) and not isinstance(b, list):
        return a - b
    if not isinstance(a, list):
        a = [a]
    if not isinstance(b, list):
        b = [b]
    for i in range(len(a)):
        if i >= len(b):
            return 1
        r = f(a[i], b[i])
        if r != 0:
            return r
    return -1


data = sys.stdin.read().strip()

ans = 0
for i, pair in enumerate(data.strip().split('\n\n'), start=1):
    a, b = pair.splitlines()
    a = eval(a)
    b = eval(b)
    if f(a, b) <= 0:
        ans += i
print(ans)
