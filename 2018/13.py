def is_cart(c: str):
    return c in '><^v'


def next_cart(road: str, curr: [tuple[int, int]]) -> tuple[tuple[int, int], int]:
    if road == '+':
        if curr[1] % 3 == 0:
            return (-curr[0][1], curr[0][0]), curr[1] + 1
        if curr[1] % 3 == 1:
            return curr[0], curr[1] + 1
        if curr[1] % 3 == 2:
            return (curr[0][1], -curr[0][0]), curr[1] + 1
    if road in '-|':
        return curr
    if road == '\\':
        if curr[0] == (1, 0) or curr[0] == (-1, 0):
            return (-curr[0][1], curr[0][0]), curr[1]
        else:
            return (curr[0][1], -curr[0][0]), curr[1]
    if road == '/':
        if curr[0] == (0, -1) or curr[0] == (0, 1):
            return (-curr[0][1], curr[0][0]), curr[1]
        else:
            return (curr[0][1], -curr[0][0]), curr[1]
    raise Exception()


def char_to_direction(c: str):
    direction_mapping = {
        '>': (0, 1),
        '<': (0, -1),
        'v': (1, 0),
        '^': (-1, 0)
    }
    return direction_mapping[c]


def p1(data: str):
    G = {}
    carts = {}
    for i, line in enumerate(data.splitlines()):
        for j, c in enumerate(line):
            if is_cart(c):
                carts[i, j] = (char_to_direction(c), 0)
                if c in '<>':
                    G[i, j] = '-'
                elif c in '^v':
                    G[i, j] = '|'
                else:
                    raise Exception()
            elif c != ' ':
                G[i, j] = c

    while True:
        n_carts = carts.copy()
        for i, j in sorted(carts.keys()):
            if (i, j) not in n_carts:
                continue
            (dx, dy), times = n_carts[i, j]
            del n_carts[i, j]
            (dx, dy), times = next_cart(G[i, j], ((dx, dy), times))
            x = i + dx
            y = j + dy
            if (x, y) in n_carts:
                return str(f'{y},{x}')
            else:
                n_carts[x, y] = ((dx, dy), times)
        carts = n_carts


def p2(data: str):
    G = {}
    carts = {}
    for i, line in enumerate(data.splitlines()):
        for j, c in enumerate(line):
            if is_cart(c):
                carts[i, j] = (char_to_direction(c), 0)
                if c in '<>':
                    G[i, j] = '-'
                elif c in '^v':
                    G[i, j] = '|'
            elif c != ' ':
                G[i, j] = c

    while len(carts) > 1:
        n_carts = carts.copy()
        for i, j in sorted(carts.keys()):
            if (i, j) not in n_carts:
                continue
            (dx, dy), times = n_carts[i, j]
            del n_carts[i, j]
            (dx, dy), times = next_cart(G[i, j], ((dx, dy), times))
            x = i + dx
            y = j + dy
            if (x, y) in n_carts:
                del n_carts[x, y]
            else:
                n_carts[x, y] = ((dx, dy), times)
        carts = n_carts
    x, y = list(carts.keys())[0]
    return str(f'{y},{x}')
