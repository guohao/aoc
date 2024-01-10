from helper import *

data = raw_data(2023, 9)
lines = lines(data)

ans = 0
for line in lines:
    ns = ints(line)
    seq = []
    while True:
        seq.append(ns)
        ns = [ns[i + 1] - ns[i] for i in range(len(ns) - 1)]
        if all(x == 0 for x in ns):
            break
    for i in range(len(seq) - 2, -1, -1):
        seq[i].append(seq[i + 1][-1] + seq[i][-1])
    ans += seq[0][-1]
print(ans)

ans = 0
for line in lines:
    ns = ints(line)
    seq = []
    while True:
        seq.append(ns)
        ns = [ns[i + 1] - ns[i] for i in range(len(ns) - 1)]
        if all(x == 0 for x in ns):
            break
    for i in range(len(seq) - 2, -1, -1):
        seq[i].append(seq[i][0] - seq[i + 1][-1])
    ans += seq[0][-1]
print(ans)
