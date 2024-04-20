from intcode import IntCodeVM


def p1(data: str):
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
    return vm.sq.pop()


def p2(data: str):
    vm = IntCodeVM(data)
    commands = """NOT B J 
NOT C T
OR T J
AND D J
AND H J
NOT A T
OR T J 
RUN
"""
    for cmd in commands:
        vm.rq.append(ord(cmd))
    vm.run()
    return vm.sq.pop()
