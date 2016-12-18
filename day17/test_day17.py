import unittest
from day17 import *

class TestDay17(unittest.TestCase):
	def test_distance_from_goal(self):
		self.assertEqual(distance_from_goal((0,0), (3,3)), 6)
		self.assertEqual(distance_from_goal((3,3), (3,3)), 0)
		self.assertEqual(distance_from_goal((3,2), (3,3)), 1)
		self.assertEqual(distance_from_goal((3,4), (3,3)), 1)

	def test_solve_examples(self):
		start_position = (0,0)
		target_position = (3,3)

		examples = (
			('ihgpwlah', 'DDRRRD'),
			('kglvqrro', 'DDUDRLRRUDRD'),
			('ulqzkmiv', 'DRURDRUDDLLDLUURRDULRLDUUDDDRR'),
			('hijkl', None),
		)

		for passcode, solution in examples:
			actual = solve(passcode, start_position, target_position)

			self.assertEqual(actual, solution, 
				"%s should yield %s but got %s" % (passcode, solution, actual))

	def test_solve_part_1(self):
		start_position = (0,0)
		target_position = (3,3)
		passcode = 'vwbaicqe'

		solution = solve(passcode, start_position, target_position)
		self.assertEqual(solution, 'DRDRULRDRD')

	@unittest.skip("slow")
	def test_solve_part_2_examples(self):
		start_position = (0,0)
		target_position = (3,3)

		examples = (
			('ihgpwlah', 370),
			('kglvqrro', 492),
			('ulqzkmiv', 830),
		)

		for passcode, len_solution in examples:
			actual = solve(passcode, start_position, target_position, True)

			self.assertEqual(len(actual), len_solution, 
				"%s should yield %s but got %s" % (passcode, len_solution, len(actual)))

	@unittest.skip("slow")
	def test_solve_part_2(self):
		start_position = (0,0)
		target_position = (3,3)
		passcode = 'vwbaicqe'

		solution = solve(passcode, start_position, target_position, True)
		self.assertEqual(len(solution), 384)


if __name__ == "__main__":
    unittest.main()
