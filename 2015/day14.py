from helper import *

data = raw_data(2015, 14)

T = 2503


def distance_of(r, d, s, t):
    rounds = t // (d + r)
    return rounds * s * d + min(t % (d + r), d) * s


max_ = 0
rds = []
for line in lines(data):
    s, d, r = ints(line)
    dis = distance_of(r, d, s, T)
    if dis > max_:
        max_ = dis
    rds.append((r, d, s))
print(max_)

scores = [0 for _ in range(len(rds))]
for t in range(1, T + 1):
    max_ = max(distance_of(r, d, s, t) for r, d, s in rds)
    for i in range(len(rds)):
        r, d, s = rds[i]
        dis = distance_of(r, d, s, t)
        if dis == max_:
            scores[i] += 1

print(max(scores))
