import itertools

import myutil


def p1(data: str):
    parts = data.split('\n\n')
    iea = parts[0].replace('\n', '')
    assert len(iea) == 512
    g = myutil.d2g(parts[1])

    def v(ix, iy):
        if (ix, iy) in g:
            return g[ix, iy]
        return '.'

    for _ in range(2):
        ng = {}
        (min_x, max_x), (min_y, max_y) = myutil.range_of_grid_2(g)
        for i in range(min_x, max_x + 1):
            for j in range(min_y, max_y + 1):
                bs = ''.join(str(int(v(i + kx, j + ky) == '#')) for kx, ky in itertools.product(range(-1, 2), repeat=2))
                idx = int(bs, 2)
                ng[i, j] = iea[idx]
        g = ng
    return sum(x == '#' for x in g.values())

# print(p1("""..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##
# #..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###
# .######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#.
# .#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#.....
# .#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#..
# ...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.....
# ..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#
#
# #..#.
# #....
# ##..#
# ..#..
# ..###
# """))
