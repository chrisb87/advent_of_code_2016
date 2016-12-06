import unittest
from day5 import *

class TestDay5Part1(unittest.TestCase):
	@unittest.skip("slow")
	def test_compute_code_example_input(self):
		self.assertEqual(compute_code('abc'), '18f47a30')

	@unittest.skip("slow")
	def test_compute_code_actual(self):
		self.assertEqual(compute_code('ffykfhsq'), 'c6697b55')

class TestDay5Part2(unittest.TestCase):
	@unittest.skip("slow")
	def test_compute_code_example_input(self):
		self.assertEqual(compute_code_2('abc'), '05ace8e3')

	@unittest.skip("slow")
	def test_compute_code_actual(self):
		self.assertEqual(compute_code_2('ffykfhsq'), '8c35d1ab')
