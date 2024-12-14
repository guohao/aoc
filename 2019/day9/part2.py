from intcode import IntCodeVM

import sys

data = sys.stdin.read().strip()

vm = IntCodeVM(data)
vm.rq.append(2)
vm.run()
print(vm.sq.popleft())
