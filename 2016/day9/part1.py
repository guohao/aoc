data = input()
i = 0
ans = 0
while i < len(data):
    if data[i] == '(':
        j = i + 1
        while data[j] != ')':
            j += 1
        a, b = map(int, data[i + 1:j].split('x'))
        ans += a * b
        i = j + a
    else:
        ans += 1
    i += 1
print(ans)
