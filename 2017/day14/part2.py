import networkx as nx

d = input()


def knot_hash(s: str):
    from collections import deque
    nums = list(map(ord, s)) + [17, 31, 73, 47, 23]
    q = deque(range(256))
    skip_size = 0
    cur_pos = 0
    for _ in range(64):
        for lens in nums:
            q1 = deque()
            for _ in range(lens):
                q1.append(q.popleft())
            while q1:
                q.append(q1.pop())
            q.rotate(-skip_size)
            cur_pos += lens + skip_size
            skip_size += 1
    q.rotate(cur_pos)

    h = ''
    while q:
        x = 0
        for _ in range(16):
            x ^= q.popleft()
        h += f'{x:02x}'
    return h


g = nx.Graph()
for i in range(128):
    for j, c in enumerate(knot_hash(f'{d}-{i}')):
        for k, used in enumerate(f'{int(c, 16):04b}'):
            if used == '1':
                u = i, j * 4 + k
                g.add_node(u)
                for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    v = u[0] + dx, u[1] + dy
                    if v in g:
                        g.add_edge(u, v)

print(len(list(nx.connected_components(g))))
