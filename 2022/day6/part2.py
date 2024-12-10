import sys

data = sys.stdin.read().strip()
n = 14
for i in range(n, len(data)):
    if len(set(data[i - n:i])) == n:
        print(i)
        break
