from helper import *


def f2(line):
    def parse_int(letter: str):
        if letter.isdigit():
            return int(letter)
        return ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'].index(letter)

    m = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', line)
    return parse_int(m[0]) * 10 + parse_int(m[-1])


lines = raw_data(2023, 1).strip().splitlines()
print(sum(a[0] * 10 + a[-1] for a in [[int(x) for x in re.findall(r'\d', line)] for line in lines]))
print(sum(f2(line) for line in lines))
