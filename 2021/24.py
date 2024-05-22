import re
from sympy import symbols, simplify, sympify


def p1(data: str):
    def is_num(name: str):
        return re.fullmatch(r'-?\d+', name)

    #
    #     def valid2(sn: str):
    #         for line in data.strip().splitlines():
    #             c = line.split()[0]
    #             a = line.split()[1]
    #             assert a in 'wxyz'
    #             if len(line.split()) == 3:
    #                 b = line.split()[2]
    #             match c:
    #                 case "inp":
    #                     rs[a] = int(next(itr))
    #                 case "add":
    #                     rs[a] = vo(a) + vo(b)
    #                 case "mul":
    #                     rs[a] = vo(a) * vo(b)
    #                 case "div":
    #                     rs[a] = vo(a) // vo(b)
    #                 case "mod":
    #                     rs[a] = vo(a) % vo(b)
    #                 case "mod":
    #                     rs[a] = vo(a) % vo(b)
    #                 case "eql":
    #                     rs[a] = int(vo(a) == vo(b))
    #                 case _:
    #                     raise Exception()
    #         return rs['z'] == 0

    def parse():
        def co(name: str):
            if is_num(name):
                return int(name)
            return rs[name]

        i = 0
        des = []
        for part in data.split('inp w\n'):
            if not part:
                continue
            rs = {x: f'pre{x}' for x in 'wxyz'}
            rs['w'] = f's{i}'
            i += 1
            for line in part.splitlines():
                c = line.split()[0]
                a = line.split()[1]
                assert a in 'wxyz'
                if len(line.split()) == 3:
                    b = line.split()[2]
                match c:
                    case "inp":
                        rs[a] = f'int(s[{i}])'
                        i += 1
                    case "add":
                        rs[a] = f'({rs[a]} + {co(b)})'
                    case "mul":
                        rs[a] = f'({rs[a]} * {co(b)})'
                    case "div":
                        rs[a] = f'({rs[a]} // {co(b)})'
                    case "mod":
                        rs[a] = f'({rs[a]} % {co(b)})'
                    case "eql":
                        rs[a] = f'(1-abs({rs[a]} - {co(b)}))'
                    case _:
                        raise Exception()
            des.append(rs['z'])
        return des

    des = parse()

    parsed = []
    # sbs = ' '.join(f'pre{k}' for k in 'xyzw')
    # sbs +=' '
    # sbs += ' '.join(k for k in 'xyzw')
    # sbs +=' '
    # sbs += ' '.join(f's{k}' for k in range(14))
    zs = symbols("prez")
    zss = [0, -18, 7598, -3411808]
    ss = symbols('s:14')
    prez = {zs: sympify('0')}
    combs = []
    for i, es in enumerate(des):
        d = {}
        exp = sympify(es)
        # exp = exp.subs(prez)
        exp = simplify(exp)
        for j in range(1, 10):
            tmpe = exp.subs({ss[i]: j, zs: zss[i]})
            d[j] = tmpe.evalf()
        prez = {zs: exp}
        print(prez)
    # print(prev)
    assert len(des) == 14

    for n in range(int('9' * 14), int('1' * 14), -1):
        print(n)
        sbs = ''

        # x, y = symbols(sbs)
        s = str(n)
        if '0' in s:
            continue
        x = 'x'
        y = 'y'
        z = 'z'
        pre = {k: 0 for k in 'wxyz'}
        for exe in des:
            # print(exe)
            mem = {'s': s, 'pre': pre, 'x': x, 'y': y, 'z': z}
            np = {}
            for k, v in exe.items():
                # print(v)

                print(simp)
                # print(pre)
                # print(k,v)
                # np[k] = int(eval(v, mem))
            pre = np
        break
        if pre['z'] == 0:
            return n
