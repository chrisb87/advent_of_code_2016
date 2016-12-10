import unittest
from day9 import *

class TestDay9Part1(unittest.TestCase):
	def test_examples(self):
		examples = {
			'ADVENT': 				'ADVENT',
			'A(1x5)BC': 			'ABBBBBC',
			'(3x3)XYZ': 			'XYZXYZXYZ',
			'A(2x2)BCD(2x2)EFG': 	'ABCBCDEFEFG',
			'(6x1)(1x3)A': 			'(1x3)A',
			'X(8x2)(3x3)ABCY': 		'X(3x3)ABC(3x3)ABCY',
		}

		for raw, expected_result in examples.items():
			expected_result = len(expected_result)
			actual_result = decompressed_length(raw, recursive = False)
			self.assertEqual(actual_result, expected_result)

	def test_solve_part_1(self):
		self.assertEqual(solve(recursive = False), 70186)

class TestDay9Part2(unittest.TestCase):
	def test_examples(self):
		examples = {
			'(3x3)XYZ': 'XYZXYZXYZ',
			'X(8x2)(3x3)ABCY': 'XABCABCABCABCABCABCY',
			'(27x12)(20x12)(13x14)(7x10)(1x12)A': ('A' * 241920)
		}

		for raw, expected_result in examples.items():
			expected_result = len(expected_result)
			actual_result = decompressed_length(raw, recursive = True)
			self.assertEqual(actual_result, expected_result, "%s should decompress to len %d but got len %d" % (raw, expected_result, actual_result))

		self.assertEqual(decompressed_length('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN', True), 445)


	def test_solve_part_2(self):
		self.assertEqual(solve(recursive = True), 10915059201)
