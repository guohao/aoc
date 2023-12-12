import re

import helper


def count_winning(line: str) -> int:
    n = re.findall(r'\d+', line.split('|')[0].split(':')[1])
    m = re.findall(r'\d+', line.split('|')[1])
    return sum(x in n for x in m)


data = helper.raw_data(2023, 4)
lines = helper.lines(data)
ans1 = sum([int(2 ** (count_winning(line) - 1)) for line in lines])
d = {x: 1 for x in range(len(lines))}
for i in range(len(lines)):
    wining = count_winning(lines[i])
    for j in range(i + 1, wining + i + 1):
        d[j] = d[j] + d[i]
ans2 = sum(d.values())
print(ans1)
print(ans2)
