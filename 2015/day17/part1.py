import itertools

cs = []
try:
    while True:
        cs.append(int(input()))
except EOFError:
    pass

r = 0
for i in range(len(cs)):
    for p in itertools.combinations(cs, i):
        r += sum(p) == 150

print(r)
