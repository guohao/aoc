from common import io_utils


def cmp(a, b):
    return (a > b) - (a < b)


data = io_utils.get_data(2022, 9)
lines = io_utils.raw_str_to_lines(data)
v1 = set()
v2 = set()
p = [(0, 0)] * 10
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
            xc = cmp(p[i - 1][0], p[i][0])
            yc = cmp(p[i - 1][1], p[i][1])
            diff = abs(p[i - 1][0] - p[i][0]) + abs(p[i - 1][1] - p[i][1])
            if (diff == 2 and xc * yc == 0) or diff > 2:
                p[i] = (p[i][0] + xc, p[i][1] + yc)
        v1.add(p[1])
        v2.add(p[9])

print(len(v1))
print(len(v2))
