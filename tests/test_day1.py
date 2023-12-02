import unittest
from day1 import part_one
from day1 import part_two
from io_utils import read_file_to_list


class TestDay1(unittest.TestCase):

    def test_part_one(self):
        lines = read_file_to_list("day1_p1_sample.txt")
        self.assertEqual(part_one(lines), 142)

    def test_part_two(self):
        lines = read_file_to_list("day1_p2_sample.txt")
        self.assertEqual(part_two(lines), 281)


if __name__ == '__main__':
    unittest.main()
