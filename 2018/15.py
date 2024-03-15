import itertools
import networkx as nx


def solve(data: str, elf_ap: int):
    G = nx.Graph()
    units = {}
    neighbor_directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    elf_deaths = set()

    def free_node(k):
        if k in units:
            del units[k]
        i, j = k
        G.add_node(k)
        for nb in [(dx + i, dy + j) for dx, dy in neighbor_directions]:
            if G.has_node(nb):
                G.add_edge(nb, k)

    def build_graph():
        for i, line in enumerate(data.splitlines()):
            for j, c in enumerate(line):
                k = (i, j)
                if c == '.':
                    free_node(k)
                elif c == 'E':
                    units[k] = (c, elf_ap, 200)
                elif c == 'G':
                    units[k] = (c, 3, 200)

    def enemies(c):
        return [x for x, (uc, _, _) in units.items() if uc != c]

    def fewest_hp_nb(k, enemies_pos):
        i, j = k
        ans = None
        min_hp = 201
        for ek in [(i + dx, j + dy) for dx, dy in neighbor_directions]:
            if ek not in enemies_pos:
                continue
            _, _, ehp = units[ek]
            if min_hp > ehp:
                ans = ek
                min_hp = ehp
        return ans

    def move(k, enemies_pos):
        if fewest_hp_nb(k, enemies_pos):
            return k
        free_node(k)
        i, j = k
        nbs = [(dx + x, dy + y) for (x, y), (dx, dy) in itertools.product(enemies_pos, neighbor_directions)]
        squares = [nb for nb in nbs if G.has_node(nb) and nx.has_path(G, (i, j), nb)]
        squares.sort(key=lambda x: (len(nx.shortest_path(G, k, x)), x))
        if not squares:
            G.remove_node(k)
            return k
        nearest = squares[0]
        paths = sorted(nx.all_shortest_paths(G, (i, j), nearest))
        k = paths[0][1]
        G.remove_node(k)
        return k

    def attack(k, ap, enemies_pos):
        ek = fewest_hp_nb(k, enemies_pos)
        if ek:
            ec, eap, ehp = units[ek]
            ehp -= ap
            if ehp <= 0:
                if ec == 'E':
                    elf_deaths.add(k)
                free_node(ek)
            else:
                units[ek] = (ec, eap, ehp)

    def fight() -> bool:
        for k in [(i, j) for i, j in sorted(units.keys())]:
            if k not in units:
                continue
            c, ap, hp = units[k]
            es = enemies(c)
            if not es:
                return False
            k = move(k, es)
            attack(k, ap, es)
            units[k] = (c, ap, hp)
        return True

    build_graph()
    t = 0
    while fight():
        t += 1
    return len(elf_deaths) == 0, t * sum(hp for _, (_, _, hp) in units.items())


def p1(data: str):
    return solve(data, 3)[1]


def p2(data: str):
    l, r = 10, 50
    while l <= r:
        m = (l + r) // 2
        all_alive, ans = solve(data, m)
        if l == r:
            return ans
        if all_alive:
            r = m - 1
        else:
            l = m + 1
