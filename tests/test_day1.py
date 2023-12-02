import unittest

from common import io_utils
from day1 import Day1


class TestDay1(unittest.TestCase):

    def test_part_one(self):
        data = """
        1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet
        """
        lines = io_utils.raw_str_to_lines(data)
        self.assertEqual(Day1().part_one(lines), 142)

    def test_part_two(self):
        data = """
        two1nine
        eightwothree
        abcone2threexyz
        xtwone3four
        4nineeightseven2
        zoneight234
        7pqrstsixteen
        """
        lines = io_utils.raw_str_to_lines(data)
        self.assertEqual(Day1().part_two(lines), 281)


if __name__ == '__main__':
    unittest.main()
