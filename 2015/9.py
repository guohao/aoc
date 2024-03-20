import itertools
import math
from collections import defaultdict


def pre(data: str):
    distances = {}
    locations = set()
    for line in data.splitlines():
        f, _, t, _, dis = line.split()
        dis = int(dis)
        distances[f, t] = dis
        distances[t, f] = dis
        locations.add(f)
        locations.add(t)
    return distances, locations


def p1(data: str):
    distances, locations = pre(data)
    ans = math.inf
    locations = list(locations)
    for k in itertools.permutations(range(len(locations))):
        ans = min(ans, sum(distances[locations[a], locations[b]] for a, b in zip(k[1:], k[:-1])))
    return ans


def p2(data: str):
    distances, locations = pre(data)
    ans = -1
    locations = list(locations)
    for k in itertools.permutations(range(len(locations))):
        ans = max(ans, sum(distances[locations[a], locations[b]] for a, b in zip(k[1:], k[:-1])))
    return ans
