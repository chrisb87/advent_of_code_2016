import unittest
import pdb
from day11 import *

class TestDay11(unittest.TestCase):
	def test_valid_floor(self):
		for layout, expected in [
			[(0,), True], # generator
			[(0,1), True], # generator and its chip
			[(0,2), True], # two generators
			[(0,3), False], # generator, NOT its chip
			[(0,1,2,5), False], # pair, generator and NOT its chip
			[(0,1,5), True], # pair, extra chip
		]:
			self.assertEqual(valid_floor(layout), expected, 
				"exected %s to be %s" % (layout, expected))

	def test_example_solution(self):
		objects = ('HG','HM','LG','LM')
		layout = (
			(1,3),
			(0,),
			(2,),
			()
		)
	
		solution = solve(layout, objects, max_depth = 12)
		self.assertEqual(len(solution), 9)

	def test_seen_hash(self):
		same1 = (
			(0,),
			(1,),
			(2,3)
		)

		same2 = (
			(2,),
			(3,),
			(0,1)
		)

		notsame = (
			(0,),
			(2,),
			(1,3)
		)

		self.assertEqual(
			seen_hash(same1, 0), 
			seen_hash(same1, 0))

		self.assertNotEqual(
			seen_hash(same1, 0), 
			seen_hash(notsame, 0))

		self.assertNotEqual(
			seen_hash(same1, 0), 
			seen_hash(same1, 1))

	def test_solve_part_1(self):
		objects = (
			'PG', 'PM',
			'TG', 'TM',
			'MG', 'MM',
			'RG', 'RM',
			'CG', 'CM',
		)

		layout = (
			(0,2,3,4,6,7,8,9),
			(1,5),
			(),
			()
		)
	
		solution = solve(layout, objects, max_depth = 50)
		self.assertEqual(len(solution), 47)

	def test_solve_part_2(self):
		objects = (
			'PG', 'PM',
			'TG', 'TM',
			'MG', 'MM',
			'RG', 'RM',
			'CG', 'CM',
			'EG', 'EM',
			'DG', 'DM'
		)

		layout = (
			(0,2,3,4,6,7,8,9,10,11,12,13),
			(1,5),
			(),
			()
		)
	
		solution = solve(layout, objects, max_depth = 72)
		self.assertEqual(len(solution), 71)

if __name__ == "__main__":
    unittest.main()
