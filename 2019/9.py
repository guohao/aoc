from  intcode import IntCodeVM
def p1(data: str):
    vm = IntCodeVM(data)
    vm.rq.append(1)
    vm.run()
    return vm.sq.popleft()


def p2(data: str):
    vm = IntCodeVM(data)
    vm.rq.append(2)
    vm.run()
    return vm.sq.popleft()
