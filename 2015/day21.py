from helper import *

shop = """
Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
"""

boss = [100, 8, 2]
goods = []
ans = 0
for line in lines(shop):
    nums = ints(line)[-3:]
    if nums:
        goods.append(nums)
W = goods[:5]
A = goods[5:10]
R = goods[10:]

A.append([0, 0, 0])
R.append([0, 0, 0])

ans = math.inf
ans2 = 0
for s in itertools.product(W, A, R, R):
    if sum(s[2]) != 0 and s[2] == s[3]:
        continue
    cost = sum([x[0] for x in s])
    damage = sum([x[1] for x in s])
    armor = sum([x[2] for x in s])
    if damage - boss[2] == 0 or boss[1] - armor == 0:
        continue

    if damage - boss[2] >= boss[1] - armor:
        ans = min(ans, cost)
    else:
        ans2 = max(ans2, cost)
print(ans)
print(ans2)
