import unittest
from day18 import *

class TestDay17(unittest.TestCase):
	def test_example(self):
		self.assertEqual(count_safes('..^^.', 3), 6)

	def test_solve_part_1(self):
		first_row = open('day18/input.txt').read().strip()
		self.assertEqual(count_safes(first_row, 40), 1982)

	@unittest.skip("slow")
	def test_solve_part_2(self):
		first_row = open('day18/input.txt').read().strip()
		self.assertEqual(count_safes(first_row, 400000), 20005203)

if __name__ == "__main__":
    unittest.main()
