import nographs as nog
from helper import *

data = """
...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
"""
data = raw_data(2023, 21)
g = nog.Array(data.strip().splitlines(), 2)
S = g.findall('S')[0]

MOVE = 64
M = {x: set() for x in range(MOVE + 2)}


def next_vertices(state, _):
    step, position = state
    moves = nog.Position.moves(2)
    M[step].add(position)
    for neighbor in position.neighbors(moves, g.limits()):
        if g[neighbor] != "#":
            yield step + 1, neighbor
    if step > 0:
        for p in M[step - 1]:
            yield step + 1, p


# next_vertices = g.next_vertices_from_forbidden('#')
goals = [i[0] for i in g.items() if g[i[0]] != '#']
v = set()
traversal = nog.TraversalBreadthFirst(next_vertices)
for found in traversal.start_from(start_vertices=[(0, S)],
                                  build_paths=False
                                  ).go_for_depth_range(0, MOVE + 2):
    pass
    # print(traversal.paths[found])
    # v.add(traversal.paths[found][-1])
# print(M)
print(len(M[MOVE]))
# print(v)
# print(len(v) + 1)
#
# lines = lines(data)
# for line in lines:
#     ns = nums(line)
