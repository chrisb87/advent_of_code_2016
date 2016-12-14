import unittest
import pdb
from day13 import *

class TestDay13(unittest.TestCase):
	def test_is_wall(self):
		tests = (
			(0, 0, False),
			(1, 0, True),
			(2, 0, False),
			(-1, 0, True),
			(0, -1, True),
		)

		for x, y, expected in tests:
			self.assertEqual(
				is_wall(x, y, 10), 
				expected, 
				"(%d,%d) should be %s" % (x,y, expected))

	def test_solve_example(self):
		solution = solve((1,1), (7,4), 10)
		self.assertEqual(len(solution) - 1, 11)

	@unittest.skip("slow")
	def test_solve_part_1(self):
		solution = solve((1,1), (31,39), 1350)
		self.assertEqual(len(solution) - 1, 92)

	@unittest.skip("slow")
	def test_solve_part_2(self):
		solution = solve((1,1), (31,39), 1350, 50)
		self.assertEqual(solution, 124)

if __name__ == "__main__":
    unittest.main()
