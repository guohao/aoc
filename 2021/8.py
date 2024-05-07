import itertools


def p1ss(line: str):
    return len(list(p for p in line.split('|')[1].split() if len(p) in (2, 3, 4, 7)))


def p2ss(line: str):
    d = {
        'abcefg': "0",
        'cf': "1",
        'acdeg': "2",
        'acdfg': "3",
        'bcdf': "4",
        'abdfg': "5",
        'abdefg': "6",
        'acf': "7",
        'abcdefg': "8",
        'abcdfg': "9",
    }
    l, r = line.split('|')
    atg = 'abcdefg'
    for perm in itertools.permutations(atg):
        m = {perm[i]: atg[i] for i in range(len(atg))}

        def normalize(s):
            return ''.join(sorted(m[c] for c in s))

        if all(normalize(x) in d for x in l.split()):
            return int(''.join(d[normalize(x)] for x in r.split()))
