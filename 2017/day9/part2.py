d = input()
i = 0
ans = 0
g = False
while i < len(d):
    c = d[i]
    if c == '!':
        i += 2
        continue
    if g:
        if c == '>':
            g = False
        else:
            ans += 1
    else:
        if c == '<':
            g = True
    i += 1
print(ans)
