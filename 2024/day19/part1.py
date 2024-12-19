import sys

lines = sys.stdin.readlines()
ps = set(lines[0].split(', '))
max_len = max(len(pat) for pat in ps)

t = 0
for line in lines[2:]:
    line = line.strip()
    n = len(line)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for l in range(1, min(max_len, i) + 1):
            if dp[i - l] and line[i - l:i] in ps:
                dp[i] = True
                break

    if dp[n]:
        t += 1

print(t)
