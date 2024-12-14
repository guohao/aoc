from collections import deque


class IntCodeVM:
    def __init__(self, instructions: str, rq=deque(), sq=deque(), parsed_instructions=None):
        if parsed_instructions is not None:
            self.instructions = parsed_instructions
        else:
            self.instructions: list[int] = list(map(int, instructions.strip().split(','))) + [0 for _ in range(10000)]
        self.pc = 0
        self.rb = 0
        self.rq = rq
        self.sq = sq
        self.halt = False

    def __copy__(self):
        vm = IntCodeVM('', deque(), deque(), parsed_instructions=self.instructions.copy())
        vm.pc = self.pc
        vm.rb = self.rb
        vm.halt = self.halt
        return vm

    def inc_pc(self, diff):
        self.pc += diff

    def read(self, mode: str, key: int):
        if mode == '0':
            return self.instructions[key]
        elif mode == '1':
            return key
        elif mode == '2':
            return self.instructions[key + self.rb]
        else:
            raise ValueError(f'{mode} {key}')

    def write(self, mode: str, key: int, value: int):
        if mode == '0':
            wp = key
        elif mode == '2':
            wp = self.rb + key
        else:
            raise ValueError(f'{mode} {key} {value}')
        self.instructions[wp] = value

    def execute_ascii(self, s: str):
        if s:
            for x in s + '\n':
                self.rq.append(ord(x))
        self.run()
        out = ''.join(chr(x) for x in self.sq)
        self.sq.clear()
        return out

    def run(self):
        if self.halt:
            return
        while self.pc < len(self.instructions):
            op = self.instructions[self.pc] % 100
            if op == 99:
                self.halt = True
                break
            modes = str(self.instructions[self.pc] // 100).zfill(3)[::-1]
            if op == 1:
                a, b = [self.read(modes[j], self.instructions[self.pc + j + 1]) for j in range(2)]
                self.write(modes[2], self.instructions[self.pc + 3], a + b)
                self.inc_pc(4)
            elif op == 2:
                a, b = [self.read(modes[j], self.instructions[self.pc + j + 1]) for j in range(2)]
                self.write(modes[2], self.instructions[self.pc + 3], a * b)
                self.inc_pc(4)
            elif op == 3:
                if not self.rq:
                    break
                self.write(modes[0], self.instructions[self.pc + 1], self.rq.popleft())
                self.inc_pc(2)
            elif op == 4:
                self.sq.append(self.read(modes[0], self.instructions[self.pc + 1]))
                self.inc_pc(2)
            elif op == 5:
                if self.read(modes[0], self.instructions[self.pc + 1]):
                    self.pc = self.read(modes[1], self.instructions[self.pc + 2])
                else:
                    self.inc_pc(3)
            elif op == 6:
                if not self.read(modes[0], self.instructions[self.pc + 1]):
                    self.pc = self.read(modes[1], self.instructions[self.pc + 2])
                else:
                    self.inc_pc(3)
            elif op == 7:
                a, b = [self.read(modes[j], self.instructions[self.pc + j + 1]) for j in range(2)]
                self.write(modes[2], self.instructions[self.pc + 3], int(a < b))
                self.inc_pc(4)
            elif op == 8:
                a, b = [self.read(modes[j], self.instructions[self.pc + j + 1]) for j in range(2)]
                self.write(modes[2], self.instructions[self.pc + 3], int(a == b))
                self.inc_pc(4)
            elif op == 9:
                self.rb += self.read(modes[0], self.instructions[self.pc + 1])
                self.inc_pc(2)
            else:
                raise ValueError('Unrecognized opcode ' + str(op))
