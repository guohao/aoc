d = input().strip()
s = []
for i in range(len(d)):
    s.extend(['.' if i % 2 else i // 2] * int(d[i]))

r = len(s) - 1
while r >= 0:
    while r >= 0 and s[r] == '.':
        r -= 1
    re = r + 1
    rs = r
    while rs >= 0 and s[rs] == s[rs - 1]:
        rs -= 1
    ls = 0
    while ls < rs:
        while ls < r and s[ls] != '.':
            ls += 1
        le = ls
        while le < r and s[le] == '.':
            le += 1
        if le - ls >= re - rs:
            for i in range(re - rs):
                s[ls + i] = s[rs + i]
                s[rs + i] = '.'
            break
        else:
            ls = le
    r = rs - 1

t = 0
for i in range(len(s)):
    if s[i] != '.':
        t += s[i] * i
print(t)
