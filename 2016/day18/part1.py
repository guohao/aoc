d = input()
ans = ['' for _ in range(40)]
ans[0] = d
for i in range(1, 40):
    for j in range(len(d)):
        l = '.' if j - 1 < 0 else ans[i - 1][j - 1]
        m = ans[i - 1][j]
        r = '.' if j + 1 == len(d) else ans[i - 1][j + 1]
        if l == '^' == m and r == '.':
            ans[i] += '^'
        elif m == r == '^' and l == '.':
            ans[i] += '^'
        elif m == '.' == r and l == '^':
            ans[i] += '^'
        elif m == '.' == l and r == '^':
            ans[i] += '^'
        else:
            ans[i] += '.'
print(sum(s.count('.') for s in ans))
