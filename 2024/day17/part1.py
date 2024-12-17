import re
import sys

a,b,c, *prog = map(int,re.findall(r'\d+',sys.stdin.read()))
output = []
i = 0

while i < len(prog)-1:
    V = {i:i for i in range(4)}
    V[4] =a
    V[5] =b
    V[6] =c

    op = prog[i+1]
    match prog[i]:
        case 0: a>>=V[op]
        case 1: b^=op
        case 2: b = 7&V[op]
        case 3: i= op -2 if a else i 
        case 4: b^=c
        case 5: output.append(V[op]&7)
        case 6: b = a>>V[op]
        case 7: c = a>>V[op]
    i += 2

print(output)
