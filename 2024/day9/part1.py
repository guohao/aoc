d = input().strip()
s = []
for i in range(len(d)):
    s.extend(['.' if i % 2 else i // 2] * int(d[i]))

l = 0
r = len(s) - 1
while l < r:
    while l < r and s[l] != '.':
        l += 1
    while l < r and s[r] == '.':
        r -= 1
    s[r], s[l] = s[l], s[r]

t = 0
for i in range(len(s)):
    if s[i] != '.':
        t += s[i] * i
print(t)
