d = input()
l = 0
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
        if c == '{':
            l += 1
        elif c == '}':
            ans += l
            l -= 1
        elif c == '<':
            g = True
    i += 1
print(ans)
