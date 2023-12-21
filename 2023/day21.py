import nographs as nog
from helper import *

data = raw_data(2023, 21)
g = nog.Array(data.strip().splitlines(), 2)


def dfs(start, depth):
    def next_vertices(points, _):
        moves = nog.Position.moves(2)
        next_visit = set()
        for point in points:
            for neighbor in point.neighbors(moves, g.limits()):
                if g[neighbor] != "#":
                    next_visit.add(neighbor)
        if next_visit:
            yield tuple(next_visit)

    traversal = nog.TraversalBreadthFirst(next_vertices)
    for found in traversal.start_from(start_vertices=((start,),),
                                      build_paths=True
                                      ).go_for_depth_range(depth, depth + 1):
        print(len(traversal.paths[found][-1]))
        pass
    return 0


S = g.findall('S')[0]
dfs(S, 64)
