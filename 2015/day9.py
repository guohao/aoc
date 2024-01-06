from helper import *

data = raw_data(2015, 9)
lines = lines(data)
d = {}
locations = set()
for line in lines:
    los, dis = line.split(' = ')
    src, target = los.split(' to ')
    d[src, target] = int(dis)
    d[target, src] = int(dis)
    locations.add(src)
    locations.add(target)


def dfs(location, visited: set[str]) -> int:
    nv = visited.copy()
    nv.add(location)
    remain = locations - nv
    if len(remain) == 1:
        return d[location, remain.pop()]
    ret = math.inf
    for ol in remain:
        ret = min(d[location, ol] + dfs(ol, nv), ret)
    return ret


def dfs2(location, visited: set[str]) -> int:
    nv = visited.copy()
    nv.add(location)
    remain = locations - nv
    if len(remain) == 1:
        return d[location, remain.pop()]
    ret = -math.inf
    for ol in remain:
        ret = max(d[location, ol] + dfs2(ol, nv), ret)
    return ret


print(min(dfs(location, set()) for location in locations))
print(max(dfs2(location, set()) for location in locations))
