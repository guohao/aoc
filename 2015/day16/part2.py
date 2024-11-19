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


    def is_aunt():
        for i in range(len(ks)):
            k = ks[i]
            v = vs[i + 1]
            if k in ['cats', 'trees']:
                if v <= e[k]:
                    return False
            elif k in ['pomeranians', 'goldfish']:
                if v >= e[k]:
                    return False
            else:
                if v != e[k]:
                    return False
        return True


    if is_aunt():
        print(vs[0])
        break
