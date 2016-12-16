import unittest
from day15 import *

class TestDay15(unittest.TestCase):
	def test_read_example_input(self):
		results = [r for r in read_input('day15/test_input.txt')]
		self.assertEqual(results, [
			(5, 4), (2, 1)
		])

	def test_read_input(self):
		results = [r for r in read_input('day15/input.txt')]
		self.assertEqual(results, [
			(5, 2), (13, 7), (17, 10), (3, 2), (19, 9), (7, 0)
		])

	def test_solve_example(self):
		result = solve(read_input("day15/test_input.txt"))
		self.assertEqual(result, 5)

	def test_solve_part_1(self):
		result = solve(read_input("day15/input.txt"))
		self.assertEqual(result, 148737)

	def test_solve_part_2(self):
		discs = read_input("day15/input.txt")
		discs = discs + ((11,0),)
		result = solve(discs)
		self.assertEqual(result, 2353212)

if __name__ == "__main__":
    unittest.main()
