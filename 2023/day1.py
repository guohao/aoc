from helper import *

lines = lines(raw_data(2023, 1))

print(sum(a[0] * 10 + a[-1] for a in [[int(x) for x in re.findall(r'\d', line)] for line in lines]))


def parse_int(letter: str) -> int:
    digit_map = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
                 'nine': 9}
    return digit_map[letter] if letter in digit_map else int(letter)


def p2(line: str) -> int:
    m = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', line)
    return parse_int(m[0]) * 10 + parse_int(m[-1])


print(sum(p2(line) for line in lines))
