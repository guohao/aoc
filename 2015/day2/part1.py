t = 0
try:
    while True:
        a, b, c = map(int, input().split('x'))
        t += min(a * b, b * c, a * c) + 2 * (a * b + b * c + a * c)
except EOFError:
    print(t)
