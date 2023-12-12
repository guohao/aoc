import helper

lines = io_utils.get_data(2022, 7).splitlines()
d = {}
p = []
for line in lines:
    match line.split():
        case ['$', 'cd', nd]:
            if nd == '..':
                del p[-1]
            else:
                p.append(nd)
        case [size, _] if size.isdigit():
            size = int(size)
            for i in range(0, len(p)):
                k = '/'.join(p[:i + 1])
                d.setdefault(k, 0)
                d[k] += size

print(sum(x for x in d.values() if x <= 100000))
require = 30000000 - (70000000 - max(d.values()))
dirs = sorted(d.values())
for i in range(len(dirs)):
    if dirs[i] >= require:
        print(dirs[i])
        break
