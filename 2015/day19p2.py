from collections import defaultdict, deque
from functools import cache

from helper import *

data = raw_data(2015, 19)
raw_mapping, raw_input = data.strip().split('\n\n')
mappings = []
pres = defaultdict(set)
succs = defaultdict(set)
molecules = {}
md ={}
for line in raw_mapping.splitlines():
    pattern, replaced = list(map(str.strip, line.split(' => ')))
    if pattern not in molecules:
        molecules[pattern] = chr(len(molecules) + ord('A'))
    items = re.findall(r'[A-Z][a-z]?', replaced)

    for i in range(len(items) - 1):
        if items[i + 1] not in molecules:
            molecules[items[i + 1]] = chr(len(molecules) + ord('A'))
        if items[i] not in molecules:
            molecules[items[i]] = chr(len(molecules) + ord('A'))
        a = molecules[items[i]]
        b = molecules[items[i + 1]]
        succs[a].add(b)
        pres[b].add(a)
    replaced = ''.join(molecules[x] for x in items)

    mappings.append((replaced, molecules[pattern]))
    md[replaced] =mappings[-1][1]

raw_input = ''.join(molecules[x] for x in re.findall(r'[A-Z][a-z]?', raw_input))

print(raw_input)
print(pres)
print(succs)
print(molecules)
singletons = set()
no_pres: set[str] = set()
no_succs: set[str] = set()
for r, p in mappings:
    items = re.findall(r'\w', r)
    if items[0] not in pres and items[-1] not in succs:
        singletons.add(r)
    if items[0] not in pres:
        no_pres.add(items[0])
    if items[-1] not in succs:
        no_succs.add(items[-1])

print(f'singletons={singletons}')
print(f'no_pre={no_pres}')
print(f'mappings={mappings}')
print(no_succs)


@cache
def remove_ar(s: str) -> tuple[tuple[str, int]]:
    combs = set()
    combs.add(s)
    d = {}
    while any(x in s for x in singletons):
        for x in singletons:
            s = s.replace(x, mappings[x])
    for t in range(1, 1000):
        nc = set()
        for comb in combs:
            for pattern, replace in mappings:
                if replace in comb:
                    for m in re.finditer(replace, comb):
                        left = comb[:m.start()]
                        right = comb[m.end():]
                        ns = left + pattern + right
                        if 'Ar' not in ns and ns not in d:
                            d[ns] = t
                        nc.add(ns)
        # print(nc)
        if not nc:
            break
        combs = nc
    return tuple(tuple(d.items()))


def p2():
    dq = deque()
    dq.append((raw_input, 0))
    seen = set()

    while dq:
        curr, weight = dq.popleft()
        print(curr, weight)
        if curr == 'e':
            print(weight)
        ari = curr.index('Ar')
        left, right = curr[:ari + 2], curr[ari + 2:]
        for (k, v) in remove_ar(left):
            # print(ari, k, len(right))
            if k + right not in seen:
                dq.append((k + right, v + weight))
                seen.add(k + right)
    print('Done!')


@cache
def remove_replaced(repd: str, s: str) -> set[str]:
    if repd not in s:
        return {s}
    ret = set()
    for r, p in mappings:
        for m in re.finditer(r, s):
            left = s[:m.start()]
            right = s[m.end():]
            ret |= remove_replaced(repd, left + p + right)
    s_ret = list(ret)
    s_ret.sort(key=lambda x: len(x), reverse=True)
    for s in s_ret:
        for r, p in mappings:
            for m in re.finditer(r, s):
                left = s[:m.start()]
                right = s[m.end():]
                for dup in remove_replaced(repd, left + p + right):
                    if dup in ret:
                        ret.remove(dup)
        # print(suffix, s, ret)
    return ret


def dfs21(s: str):
    while any(x in s for x in singletons):
        for x in singletons:
            s = s.replace(x, mappings[x])
    ret: set[str] = {''}
    for sp in no_succs:
        if sp not in s:
            continue
        parts = [x + sp for x in re.split(sp, s) if x]
        if len(parts) == 1:
            return remove_replaced(sp, s)
        print("Parts:", parts)
        for part in parts:
            nr  = set()
            for x in ret:
                if any(y in x for y in no_pres):
                    for y in no_pres:
                        if y in x:
                            idx = x.index(y)
                            left, right = x[:idx], x[idx:]
                            for rsr in remove_replaced(mappings[y] + right + part):
                                nr.add(left + rsr)
                else:
                    nr |= remove_replaced(sp, x + part)
            print('Part:', part)
            print("Combs:", nr)
            print("Rets:", len(ret))
            # print("Rets:",ret)
            ret = nr
        # print("Parts:",parts)
    print('S:', s)
    return ret


def p21():
    curr = raw_input
    print(len(curr))
    print(dfs21(curr))
    # curr = dfs21(curr)
    # print(len(curr))


# p2()

p21()
# print(remove_ar("TiTiBFAr"))
