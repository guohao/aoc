import itertools
import re


def ints(line):
    return list(map(int, re.findall(r'-?\d+', line)))


def solve(data: str, boost=0):
    def build_groups():
        parts = data.split('\n\n')
        groups = {}

        pattern = re.compile(
            r"(\d+)\sunits each with (\d+) hit points(?: \(?(.*)?\))? with an attack that does (\d+) ([^\s]+) damage at initiative (\d+)"
        )
        for i, part in enumerate(parts):
            for line in part.splitlines()[1:]:
                m = re.match(pattern, line)
                weak = []
                immune = []
                if m.group(3):
                    for cell in m.group(3).split('; '):
                        if cell.startswith('weak'):
                            weak = cell.replace(',', '').split()[2:]
                        else:
                            immune = cell.replace(',', '').split()[2:]
                damage = int(m.group(4))
                if i == 0:
                    damage += boost
                idx = len(groups)
                groups[idx] = (int(m.group(1)), int(m.group(2)), weak,
                               immune, damage, m.group(5), int(m.group(6)), i, idx)
                # 0 unit count
                # 1 hp
                # 2 weak
                # 3 immune
                # 4 damage
                # 5 damage type
                # 6 initiative
                # 7 unit type
                # 8 group id
        return groups

    def fight():
        def effective_power(x):
            return x[0] * x[4], x[6]

        select_order = sorted(groups.values(), key=effective_power, reverse=True)
        selected = {}

        def damage(attacker, defender):
            effective_damage = effective_power(attacker)[0]
            if attacker[5] in defender[3]:
                effective_damage = 0
            if attacker[5] in defender[2]:
                effective_damage = 2 * effective_damage
            return effective_damage, effective_power(defender), defender[6]

        for group in select_order.copy():
            targets = sorted((t for t in select_order if t[7] != group[7]), key=lambda x: damage(group, x),
                             reverse=True)
            if not targets or damage(group, targets[0])[0] == 0:
                continue
            target = targets[0]
            select_order.remove(target)
            selected[group[8]] = target[8]
        attack_order = sorted(groups.keys(), key=lambda x: groups[x][6], reverse=True)
        for i in attack_order:
            a = groups[i]
            if a[0] == 0:
                continue
            if i not in selected:
                continue
            b = groups[selected[i]]
            damaged, _, _ = damage(a, b)
            remain_unit = max(0, b[0] - damaged // b[1])
            groups[selected[i]] = (remain_unit, *b[1:])
        for v in list(groups.values()):
            if v[0] == 0:
                del groups[v[8]]
        return any(a[7] != b[7] for a in groups.values() for b in groups.values())

    groups = build_groups()
    while True:
        preg = groups.copy()
        if not fight():
            break
        if groups == preg:
            return -1, -1
    return list(groups.values())[0][7], sum(group[0] for group in groups.values())


def p1(data: str):
    return solve(data)[1]


def p2(data: str):
    for i in itertools.count(1):
        a, b = solve(data, i)
        if a == 0:
            return b
