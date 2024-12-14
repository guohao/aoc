from  intcode import IntCodeVM
import sys
data = sys.stdin.read().strip()

    vm = IntCodeVM(data)
    vm.rq.append(1)
    vm.run()
    return vm.sq.popleft()


import sys
data = sys.stdin.read().strip()

    vm = IntCodeVM(data)
    vm.rq.append(2)
    vm.run()
    return vm.sq.popleft()
