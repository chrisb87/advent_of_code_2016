import unittest
from day1 import *

class TestDay1Part1(unittest.TestCase):
	def test_solve_part_1(self):
		self.assertEqual(solve_part_1(), 231)

	def test_solve_part_2(self):
		self.assertEqual(solve_part_2(), 147)
