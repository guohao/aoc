import re
import sys

data = sys.stdin.read()
parts = data.split('\n\n')
vals = []
rs = {}
for line in parts[0].splitlines():
    x = int(re.findall(r'\d+', line)[0])
    vals.append(x)
for i in range(3):
    rs['ABC'[i]] = vals[i]

program = [int(x) for x in parts[1].split(":")[1].strip().split(",")]


def value_of(opc, opr):
    if opc in [0, 2, 5, 6, 7]:  # Combo operands
        if opr <= 3:
            return opr
        elif opr == 4:
            return rs['A']
        elif opr == 5:
            return rs['B']
        elif opr == 6:
            return rs['C']
        else:
            assert False
    elif opc in [1, 3, 4]:  # Literal operands
        return opr
    else:
        assert False


output = []
ip = 0

while ip < len(program):
    opc = program[ip]
    if ip + 1 >= len(program):
        break
    opr = program[ip + 1]

    if opc == 0:
        d = 2 ** value_of(opc, opr)
        result = rs['A'] // d
        rs['A'] = result
        ip += 2
    elif opc == 1:
        v = value_of(opc, opr)
        rs['B'] = rs['B'] ^ v
        ip += 2
    elif opc == 2:
        v = value_of(opc, opr)
        rs['B'] = v % 8
        ip += 2
    elif opc == 3:
        v = value_of(opc, opr)
        if rs['A'] != 0:
            ip = v
        else:
            ip += 2
    elif opc == 4:
        rs['B'] = rs['B'] ^ rs['C']
        ip += 2
    elif opc == 5:
        v = value_of(opc, opr)
        output.append(str(v % 8))
        ip += 2
    elif opc == 6:
        d = 2 ** value_of(opc, opr)
        rs['B'] = rs['A'] // d
        ip += 2
    elif opc == 7:
        d = 2 ** value_of(opc, opr)
        rs['C'] = rs['A'] // d
        ip += 2
    else:
        assert False

print(','.join(output))
