import re

import io_utils

data = io_utils.get_data(2022, 11)
parts = data.strip().split('\n\n')
MS = []
opd = {'+': lambda a, b: a + b,
       '-': lambda a, b: a - b,
       '*': lambda a, b: a * b,
       '/': lambda a, b: a // b,
       '**': lambda a, b,: a * a
       }
for p in parts:
    p = p.splitlines()[1:]
    m = [[], None, 0, 0, 0, 0, 0]
    m[0] = [int(x) for x in re.findall(r'\d+', p[0])]
    if 2 == len(re.findall('old', p[1])):
        m[1] = opd['**']
    else:
        m[1] = opd[re.findall(r'[+\-*/]', p[1])[0]]
        m[2] = int(re.findall(r'\d+', p[1])[0])
    m[3] = int(re.findall(r'\d+', p[2])[0])
    m[4] = int(re.findall(r'\d+', p[3])[0])
    m[5] = int(re.findall(r'\d+', p[4])[0])
    m[6] = 0
    MS.append(m)
for _ in range(20):
    for m in MS:
        m[6] += len(m[0])
        c = [m[1](x, m[2]) // 3 for x in m[0]]
        for x in c:
            if x % m[3] == 0:
                MS[m[4]][0].append(x)
            else:
                MS[m[5]][0].append(x)
        m[0].clear()

MS.sort(key=lambda x: x[6])

print(MS[-1][6] * MS[-2][6])
