import re
import sys
from collections import defaultdict, deque

lines = [line.strip() for line in sys.stdin.readlines()]


class P:
    def __init__(self, rq: deque, sq: deque, pv):
        self.rq = rq
        self.sq = sq
        self.pc = 0
        self.r = defaultdict(int)
        self.snd_cnt = 0
        self.r['p'] = pv

    def run(self):
        while 0 <= self.pc < len(lines):
            cmd, *args = lines[self.pc].split()
            if 'snd' == cmd:
                self.sq.append(self.v_of(args[0]))
                self.snd_cnt += 1
            elif 'set' == cmd:
                self.r[args[0]] = self.v_of(args[1])
            elif 'mul' == cmd:
                self.r[args[0]] *= self.v_of(args[1])
            elif 'add' == cmd:
                self.r[args[0]] += self.v_of(args[1])
            elif 'mod' == cmd:
                self.r[args[0]] %= self.v_of(args[1])
            elif 'rcv' == cmd:
                if not self.rq:
                    return
                else:
                    self.r[args[0]] = self.rq.popleft()
            elif 'jgz' == cmd:
                if self.v_of(args[0]) > 0:
                    self.pc += self.v_of(args[1])
                    continue
            else:
                raise Exception(lines[self.pc])
            self.pc += 1

    def v_of(self, n: str):
        if re.fullmatch(r'-?\d+', n):
            return int(n)
        return self.r[n]


qs = [deque(), deque()]
ps = [P(qs[0], qs[1], 0), P(qs[1], qs[0], 1)]
while True:
    ps[0].run()
    ps[1].run()
    if not any(qs):
        break
print(ps[1].snd_cnt)
