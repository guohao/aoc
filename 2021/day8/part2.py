import itertools
import sys

lines = [l.strip() for l in sys.stdin.readlines()]

t = 0
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
for line in lines:
    l, r = line.split('|')
    atg = 'abcdefg'
    for perm in itertools.permutations(atg):
        m = {perm[i]: atg[i] for i in range(len(atg))}


        def normalize(s):
            return ''.join(sorted(m[c] for c in s))


        if all(normalize(x) in d for x in l.split()):
            t += int(''.join(d[normalize(x)] for x in r.split()))
            break
print(t)
