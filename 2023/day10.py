from common import io_utils

data = """
...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
"""
data ="""
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
"""

# data = io_utils.get_data(2023, 10)
lines = io_utils.raw_str_to_lines(data)
grid = []
d = []
for line in lines:
    grid.append([x for x in line])
    d.append([0 for x in line])

S = (-1, -1)
for i, line in enumerate(grid):
    for j, y in enumerate(line):
        if y == 'S':
            S = (i, j)
            break
f = 'U'
v = set()
v.add(S)
cp = S
idx = [(S[0] - 1, S[1]), (S[0], S[1] + 1), (S[0] + 1, S[1]), (S[0], S[1] - 1)]
for i in idx:
    if grid[i[0]][i[1]] != '.':
        cp = i
        break

pipes = "|-LJ7F"
ans = -1
for i in range(1000000):
    v.add(cp)
    n = []
    match grid[cp[0]][cp[1]]:
        case "|":
            n.append((cp[0] + 1, cp[1]))
            n.append((cp[0] - 1, cp[1]))
        case "-":
            n.append((cp[0], cp[1] - 1))
            n.append((cp[0], cp[1] + 1))
        case "L":
            n.append((cp[0] - 1, cp[1]))
            n.append((cp[0], cp[1] + 1))
        case "J":
            n.append((cp[0] - 1, cp[1]))
            n.append((cp[0], cp[1] - 1))
        case "7":
            n.append((cp[0] + 1, cp[1]))
            n.append((cp[0], cp[1] - 1))
        case "F":
            n.append((cp[0] + 1, cp[1]))
            n.append((cp[0], cp[1] + 1))
    nx = [x for x in n if x not in v]
    if len(nx) == 0:
        ans = i
        break
    cp = nx[0]
# print(ans // 2 + 1)

# ans = 0
# tv = set()
# for i in range(1,len(grid) - 1):

ap = set()
for i, line in enumerate(lines):
    for j, x in enumerate(line):
        if x == '.':
            ap.add((i, j))
for pp in ap.copy():
    if pp[0] == 0 or pp[0] == len(grid) - 1:
        ap.remove(pp)
        continue

    if pp[1] == 0 or pp[1] == len(grid[0]) - 1:
        ap.remove(pp)


def filter_ap_by_neighbor(points):
    # up
    for p in points.copy():
        det = (p[0] - 1, p[1])
        if grid[det[0]][det[1]] == '.' and det not in points:
            points.remove(p)
            continue
        # down
        det = (p[0] + 1, p[1])
        if grid[det[0]][det[1]] == '.' and det not in points:
            points.remove(p)
            continue

        # left
        det = (p[0], p[1] - 1)
        if grid[det[0]][det[1]] == '.' and det not in points:
            points.remove(p)
            continue

        # right
        det = (p[0], p[1] + 1)
        if grid[det[0]][det[1]] == '.' and det not in points:
            points.remove(p)
            continue


while True:
    pre_len = len(ap)
    filter_ap_by_neighbor(ap)
    if len(ap) == pre_len:
        break

for i, line in enumerate(grid):
    tp = []
    for j, x in enumerate(line):
        if x == '.':
            if (i, j) in ap:
                tp.append('T')
            else:
                tp.append('O')
        else:
            tp.append(x)
    print(''.join(tp))

print(len(ap))
