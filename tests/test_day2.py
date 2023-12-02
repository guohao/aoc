import unittest
from unittest import TestCase

from day2 import part_one
from day2 import part_two

import io_utils


class TestDay2(TestCase):
    def test_part_one(self):
        lines = io_utils.read_file_to_list("day2_sample.txt")
        self.assertEqual(part_one(lines), 8)

    def test_part_two(self):
        lines = io_utils.read_file_to_list("day2_sample.txt")
        self.assertEqual(part_two(lines), 2286)


if __name__ == '__main__':
    unittest.main()
