import unittest
from day2 import *

class TestDay2Part1(unittest.TestCase):
	def test_solve_part_1(self):
		self.assertEqual(solve_part_1(), '18843')

	def test_solve_part_2(self):
		self.assertEqual(solve_part_2(), '67BB9')
