import unittest
from unittest import TestCase

from common import io_utils
from day2 import Day2


class TestDay2(TestCase):
    samples = """
    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

    def test_part_one(self):
        lines = io_utils.raw_str_to_lines(self.samples)
        self.assertEqual(Day2().part_one(lines), 8)

    def test_part_two(self):
        lines = io_utils.raw_str_to_lines(self.samples)
        self.assertEqual(Day2().part_two(lines), 2286)


if __name__ == '__main__':
    unittest.main()
