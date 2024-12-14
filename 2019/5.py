from intcode import IntCodeVM


import sys
data = sys.stdin.read().strip()

    vm = IntCodeVM(data)
    vm.rq.append(1)
    vm.run()
    return vm.sq.pop()


import sys
data = sys.stdin.read().strip()

    vm = IntCodeVM(data)
    vm.rq.append(5)
    vm.run()
    return vm.sq.pop()
