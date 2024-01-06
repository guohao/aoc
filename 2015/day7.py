import helper


def solve(d: dict[str, int]):
    def eval_number(s) -> int:
        s = s.strip()
        if s.isnumeric():
            return int(s)
        if s in d:
            return d[s]

    data = helper.raw_data(2015, 7)
    lines = helper.lines(data)
    while lines:
        nls = []
        for line in lines:
            l, r = line.split('->')
            target = r.strip()
            if target in d:
                continue
            op = l.strip().split()
            if len(op) == 1:
                a = eval_number(op[0])
                if a is not None:
                    d[target] = a
            elif len(op) == 3:
                if op[1].startswith("L"):
                    a = eval_number(op[0])
                    if a is not None:
                        d[target] = a << int(op[2])
                elif op[1].startswith("R"):
                    a = eval_number(op[0])
                    if a is not None:
                        d[target] = a >> int(op[2])
                elif op[1] == 'OR':
                    a = eval_number(op[0])
                    b = eval_number(op[2])
                    if a is not None and b is not None:
                        d[target] = a | b
                elif op[1] == 'AND':
                    a = eval_number(op[0])
                    b = eval_number(op[2])
                    if a is not None and b is not None:
                        d[target] = a & b
                else:
                    raise Exception("Unknown operator")
            else:
                if op[0] == 'NOT':
                    a = eval_number(op[1])
                    if a is not None:
                        d[target] = ~a
                else:
                    raise Exception("Unknown operator")
            # print(line, d.get(target))
            if target not in d:
                nls.append(line)
        lines = nls
    print(d['a'])


solve({})
solve({'b': 3176})
