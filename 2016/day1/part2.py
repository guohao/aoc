x = y = 0
d = (1, 0)
visited = {(x, y)}
for step in input().split(', '):
    if step[0] == 'L':
        d = (-d[1], d[0])
    else:
        d = (d[1], -d[0])
    moves = int(step[1:])
    for i in range(moves):
        x += d[0]
        y += d[1]
        if (x, y) in visited:
            print(abs(x) + abs(y))
            exit()
        visited.add((x, y))
