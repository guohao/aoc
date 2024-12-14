from intcode import IntCodeVM

import sys

data = sys.stdin.read().strip()

vm = IntCodeVM(data)
commands = """NOT A T
NOT B J
OR T J
NOT C T
OR T J
AND D J
WALK
"""
for cmd in commands:
    vm.rq.append(ord(cmd))
vm.run()
print(vm.sq.pop())

