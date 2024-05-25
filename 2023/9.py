def p1is(ints: list[int]) -> int:
    if all(x == 0 for x in ints):
        return 0
    return ints[-1] + p1is([ints[i] - ints[i - 1] for i in range(1, len(ints))])


def p2is(ints: list[int]) -> int:
    if all(x == 0 for x in ints):
        return 0
    return ints[0] - p2is([ints[i] - ints[i - 1] for i in range(1, len(ints))])
