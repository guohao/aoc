import math
import re
from collections import defaultdict


def p1(data: str):
    ps = []
    for line in data.splitlines():
        px, py, pz, vx, vy, vz, ax, ay, az = list(map(int, re.findall(r'-?\d+', line)))
        ps.append(((px, py, pz), (vx, vy, vz), (ax, ay, az)))

    for _ in range(1000):
        nps = []
        for (px, py, pz), (vx, vy, vz), (ax, ay, az) in ps:
            vx, vy, vz = vx + ax, vy + ay, vz + az
            px, py, pz = px + vx, py + vy, pz + vz
            nps.append(((px, py, pz), (vx, vy, vz), (ax, ay, az)))
        ps = nps
    ans = 0
    closest_dis = math.inf
    for i, p in enumerate(ps):
        dis = sum(abs(p[0][i]) for i in range(3))
        if closest_dis > dis:
            ans = i
            closest_dis = dis
    return ans


def p2(data: str):
    ps = {}
    for line in data.splitlines():
        px, py, pz, vx, vy, vz, ax, ay, az = list(map(int, re.findall(r'-?\d+', line)))
        ps[px, py, pz] = (px, py, pz), (vx, vy, vz), (ax, ay, az)

    for _ in range(1000):
        nps = defaultdict(list)
        for (px, py, pz), (vx, vy, vz), (ax, ay, az) in ps.values():
            vx, vy, vz = vx + ax, vy + ay, vz + az
            px, py, pz = px + vx, py + vy, pz + vz
            nps[px, py, pz].append(((px, py, pz), (vx, vy, vz), (ax, ay, az)))
        ps = {k: v[0] for k, v in nps.items() if len(v) == 1}
    return len(ps)
