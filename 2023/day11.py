from helper import *

data = raw_data(2023, 11)
lines = data.strip().splitlines()
N = len(lines)
M = len(lines[0])
grid = grid(data)
galaxies = [p for p, v in grid.items() if v == '#']


def solve(magnify: int):
    weight_x = [1 for _ in range(N)]
    weight_y = [1 for _ in range(M)]

    for i in range(N):
        if all(grid[i, j] == '.' for j in range(M)):
            weight_x[i] = magnify

    for j in range(M):
        if all(grid[i, j] == '.' for i in range(N)):
            weight_y[j] = magnify

    ans = 0

    for i, ga in enumerate(galaxies):
        for gb in galaxies[:i]:
            ans += sum(weight_x[i] for i in range(min(ga[0], gb[0]), max(ga[0], gb[0])))
            ans += sum(weight_y[i] for i in range(min(ga[1], gb[1]), max(ga[1], gb[1])))
    print(ans)


solve(2)
solve(1000000)
