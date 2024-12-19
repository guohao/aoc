import sys

lines = [l.strip() for l in sys.stdin.readlines()]
ps = set(lines[0].split(', '))
max_len = max(len(pat) for pat in ps)

t = 0
for line in lines[2:]:
    n = len(line)
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for p in ps:
            l = len(p)
            if l <= i and line[i - l:i] == p:
                dp[i] += dp[i - l]
    t += dp[n]

print(t)
