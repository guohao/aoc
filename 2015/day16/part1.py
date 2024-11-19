import re

e = {}
for line in """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1
""".splitlines():
    l, v = line.split(": ")
    e[l] = int(v)

while True:
    line = input()
    vs = list(map(int, re.findall(r'\d+', line)))
    ks = re.findall(r'([a-z]+):', line)
    if all(e[ks[i]] == vs[i + 1] for i in range(len(ks))):
        print(vs[0])
        break
