import unittest
from day3 import *

class TestDay3Part1(unittest.TestCase):
	def test_solve_part_1(self):
		self.assertEqual(solve_part_1(), 862)

	def test_solve_part_2(self):
		self.assertEqual(solve_part_2(), 1577)
