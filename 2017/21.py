def rotate(matrix: tuple[str]):
    return tuple([''.join(x) for x in zip(*matrix[::-1])])


def gen_all(src: tuple[str]) -> set[tuple]:
    generated = {src, tuple(x[::-1] for x in src)}
    for _ in range(4):
        generated |= set(rotate(x) for x in generated)
    return generated


def expand(mps: dict, image: list[str]) -> list[str]:
    pz = 2 if len(image) % 2 == 0 else 3
    n_image = []
    for i in range(0, len(image), pz):
        rows = [''] * (pz + 1)
        for j in range(0, len(image), pz):
            p = tuple(image[i + k][j:j + pz] for k in range(pz))
            mpd = mps[p]
            for n in range(len(mpd)):
                rows[n] += mpd[n]
        n_image += rows
    return n_image


def pixel_on(data: str, times: int):
    mps = {}
    for line in data.splitlines():
        line = line.replace(' ', '')
        srcs, target = line.split('=>')
        target = tuple(target.split('/'))
        pattern = tuple(srcs.strip().split('/'))
        mps |= {src: target for src in gen_all(pattern)}
    image = '.#.\n..#\n###'.splitlines()
    for _ in range(times):
        image = expand(mps, image)

    return sum(row.count('#') for row in image)


def p1(data: str):
    return pixel_on(data, 5)


def p2(data: str):
    return pixel_on(data, 18)
