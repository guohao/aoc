import itertools

shop = """Weapons:    Cost  Damage  Armor
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
Defense +3   80     0       3"""
items = [[list(map(int, item.split()[-3:])) for item in p.splitlines()[1:]] for p in shop.split('\n\n')]

boss_hp = int(input().split()[-1])
boss_damage = int(input().split()[-1])
boss_armor = int(input().split()[-1])

w = items[0]
a = [[0] * 3] + items[1]
r0 = [[0] * 3] + items[2]
r1 = [[0] * 3] + items[2]

ans = 0
for c in itertools.product(w, a, r0, r1):
    if c[-1] == c[-2] and c[-1][0] != 0:
        continue
    cost = sum(x[0] for x in c)
    damage = sum(x[1] for x in c)
    armor = sum(x[2] for x in c)
    if boss_hp // max(1, damage - boss_armor) > 100 // max(1, boss_damage - armor):
        ans = max(ans, cost)
print(ans)
