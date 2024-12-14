import copy
import math


class Spell:
    def __init__(self, name, cost=0, damage=0, heals=0, armor=0, mana=0, lasts=0):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.heals = heals
        self.armor = armor
        self.mana = mana
        self.lasts = lasts


spells = {
    Spell("Magic Missile", cost=53, damage=4),
    Spell("Drain", cost=73, damage=2, heals=2),
    Spell("Shield", cost=113, armor=7, lasts=6),
    Spell("Poison", cost=173, damage=3, lasts=6),
    Spell("Recharge", cost=229, mana=101, lasts=5),
}


class Player:
    def __init__(self, hp=0, mana=0, armor=0, cost=0):
        self.hp = hp
        self.mana = mana
        self.armor = armor
        self.cost = cost
        self.effects = {}

    def take_effects(self, boss):
        for effect in list(self.effects.values()):
            self.hp += effect.heals
            self.mana += effect.mana
            boss.hp -= effect.damage
            effect.lasts -= 1
            if effect.lasts == 0:
                del self.effects[effect.name]
        if self.effects:
            self.armor = max(e.armor for e in self.effects.values())


class Boss:
    def __init__(self, hp, damage):
        self.hp = hp
        self.damage = damage


def fight() -> int:
    ans = math.inf
    states = [(Player(hp=50, mana=500), Boss(int(input().split()[-1]), int(input().split()[-1])))]
    while states:
        new_states = []
        for player, boss in states:
            if player.cost >= ans:
                continue
            player.take_effects(boss)
            if boss.hp <= 0:
                ans = min(ans, player.cost)
                continue
            for spell in spells:
                if player.mana < spell.cost:
                    continue
                if spell.name in player.effects:
                    continue
                new_player = copy.deepcopy(player)
                new_boss = copy.deepcopy(boss)
                new_player.cost += spell.cost
                new_player.mana -= spell.cost
                if spell.lasts > 0:
                    new_player.effects[spell.name] = copy.copy(spell)
                else:
                    new_boss.hp -= spell.damage
                    new_player.hp += spell.heals
                if new_boss.hp <= 0:
                    ans = min(ans, new_player.cost)
                    continue
                new_player.take_effects(new_boss)

                if new_boss.hp <= 0:
                    ans = min(ans, new_player.cost)
                    continue
                new_player.hp -= max(1, new_boss.damage - new_player.armor)
                if new_player.hp <= 0:
                    continue
                new_states.append((new_player, new_boss))
        states = new_states
    print(ans)


print(fight())
