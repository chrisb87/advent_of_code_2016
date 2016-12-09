import unittest
from day8 import *

class TestDay8Part1(unittest.TestCase):
	def test_part_1_example(self):
		screen = Screen(7, 3)

		self.assertEqual(screen.get_display(), [
			'.......',
			'.......',
			'.......'
		])

		screen.draw("rect 3x2")

		self.assertEqual(screen.get_display(), [
			'###....',
			'###....',
			'.......'
		])

		self.assertEqual(screen.lit_pixels(), 6)

		screen.draw("rotate column x=1 by 1")

		self.assertEqual(screen.get_display(), [
			'#.#....',
			'###....',
			'.#.....'
		])

		self.assertEqual(screen.lit_pixels(), 6)

		screen.draw("rotate row y=0 by 4")

		self.assertEqual(screen.get_display(), [
			'....#.#',
			'###....',
			'.#.....'
		])

		self.assertEqual(screen.lit_pixels(), 6)

		screen.draw("rotate column x=1 by 1")

		self.assertEqual(screen.get_display(), [
			'.#..#.#',
			'#.#....',
			'.#.....'
		])

		self.assertEqual(screen.lit_pixels(), 6)

	def test_solve_part_1(self):
		self.assertEqual(solve_part_1(), 115)

