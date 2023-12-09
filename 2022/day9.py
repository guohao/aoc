from common import io_utils

data = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""
data = io_utils.get_data(2022, 9)
lines = io_utils.raw_str_to_lines(data)
v1 = set()
v2 = set()
p = [(0, 0)] * 10
print(p)
for line in lines:
    d = line.split()[0]
    for _ in range(int(line.split()[1])):
        match d:
            case 'R':
                p[0] = (p[0][0] + 1, p[0][1])
            case 'L':
                p[0] = (p[0][0] - 1, p[0][1])
            case 'U':
                p[0] = (p[0][0], p[0][1] + 1)
            case 'D':
                p[0] = (p[0][0], p[0][1] - 1)
        for i in range(1, len(p)):
            diff = abs(p[i][1] - p[i - 1][1]) + abs(p[i][0] - p[i - 1][0])
            if diff < 2:
                break
            xc = -1 if p[i][0] > p[i - 1][0] else 1
            yc = -1 if p[i][1] > p[i - 1][1] else 1
            if diff == 2 and p[i][0] == p[i - 1][0] or p[i][1] == p[i - 1][1]:
                if p[i][0] == p[i - 1][0]:
                    yc = -1 if p[i][1] > p[i - 1][1] else 1
                    p[i] = (p[i][0], p[i][1] + yc)
                else:
                    xc = -1 if p[i][0] > p[i - 1][0] else 1
                    p[i] = (p[i][0] + xc, p[i][1])
            if diff > 2:
                p[i] = (p[i][0] + xc, p[i][1] + yc)
        v1.add(p[1])
        v2.add(p[9])

print(len(v1))
print(len(v2))
