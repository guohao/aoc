t = 0
while True:
    line = input()
    if not line:
        break
    a, b, c = map(int, line.split('x'))
    t += min(a + b, b + c, a + c) * 2 + a * b * c
print(t)
