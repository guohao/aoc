l, r = map(int, input().split('-'))
t = 0
for i in range(l, r + 1):
    s = str(i)
    for j in range(1, len(s)):
        if s[j] == s[j - 1]:
            break
    else:
        continue
    if sorted(s) != list(s):
        continue
    t += 1

print(t)
