from helper import *

data = """
Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.
"""
data = raw_data(2015, 13)
d = {}
persons = set()
for line in lines(data):
    line = line.replace('gain ', '+').replace('lose ', '-').replace('.', '')
    cells = line.split()
    a = cells[0]
    b = cells[-1]
    c = int(cells[2])
    d[a, b] = c
    persons.add(a)
    persons.add(b)


def dfs(curr: str, visited: List[str]):
    visited = visited.copy()
    visited.append(curr)
    if len(visited) == len(persons):
        return d[curr, visited[0]] + d[visited[0], curr]
    r = 0
    for nex in persons - set(visited):
        r = max(r, d[nex, curr] + d[curr, nex] + dfs(nex, visited))
    return r


print(dfs(set(d.keys()).pop()[0], []))

persons.add('me')
for p in persons:
    d['me', p] = 0
    d[p, 'me'] = 0

print(dfs(set(d.keys()).pop()[0], []))
