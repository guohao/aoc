import sys

data = sys.stdin.read().strip()

cmds = data.splitlines()


def replace(k):
    ops = cmds.copy()
    kop = ops[k]
    if "nop" not in kop and 'jmp' not in kop:
        return False, 0
    if 'nop' in kop:
        ops[k] = 'jmp ' + kop.split()[1]
    else:
        ops[k] = 'nop ' + kop.split()[1]
    i = 0
    acc = 0
    run_times = 1000
    while i < len(ops):
        run_times -= 1
        if run_times < 0:
            return False, 0
        op = ops[i]
        if 'acc' in op:
            acc += int(op.split()[1])
        elif 'jmp' in op:
            i += int(op.split()[1])
            continue
        i += 1
    return True, acc


for i in range(len(cmds)):
    valid, val = replace(i)
    if valid:
        print(val)
        break
