from typing import List

from io_utils import read_file_to_list


def line_to_digit(line: str) -> int:
    digits = []
    for c in line:
        if c.isdigit():
            digits.append(int(c))
    return digits[0] * 10 + digits[-1]


def part_one(lines: List[str]) -> int:
    result = 0
    for line in lines:
        digits = line_to_digit(line)
        result += digits
    return result


def line_to_digits_with_letter(line: str) -> int:
    """
    letter can be reused, for example: threeight = 38

    :param line:
    :return:
    """
    letters = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    digits = []
    for i in range(len(line)):
        if line[i].isdigit():
            digits.append(int(line[i]))
        else:
            for j, letter in enumerate(letters):
                if line[i:].startswith(letter):
                    digits.append(j + 1)
                    break
    return digits[0] * 10 + digits[-1]


def part_two(lines: List[str]):
    result = 0
    for line in lines:
        result += line_to_digits_with_letter(line)
    return result


if __name__ == '__main__':
    all_lines = read_file_to_list('day1.txt')
    ans1 = part_one(all_lines)
    print(f'ans1:{ans1}')
    ans2 = part_two(all_lines)
    print(f'ans2:{ans2}')
