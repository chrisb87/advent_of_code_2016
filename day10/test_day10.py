import unittest
from day10 import *

class TestDay10(unittest.TestCase):
	def test_solve_part_1(self):
			swarm = BotSwarm()
			swarm.load_instructions(open("day10/input.txt"))
			self.assertEqual(swarm.get_result(part = 1), 141)

	def test_solve_part_2(self):
			swarm = BotSwarm()
			swarm.load_instructions(open("day10/input.txt"))
			self.assertEqual(swarm.get_result(part = 2), 1209)
