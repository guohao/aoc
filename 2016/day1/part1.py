x = y = 0
d = (1, 0)
for step in input().split(', '):
    if step[0] == 'L':
        d = (-d[1], d[0])
    else:
        d = (d[1], -d[0])
    moves = int(step[1:])
    x += moves * d[0]
    y += moves * d[1]
print(abs(x) + abs(y))
