import unittest
from day6 import *

class TestDay6Part1(unittest.TestCase):
	def test_part_1_test_input(self):
		self.assertEqual(solve(test=True, part=1), 'easter')

	def test_part_1(self):
		self.assertEqual(solve(test=False, part=1), 'qoclwvah')

	def test_part_2_test_input(self):
		self.assertEqual(solve(test=True, part=2), 'advent')

	def test_part_2(self):
		self.assertEqual(solve(test=False, part=2), 'ryrgviuv')
