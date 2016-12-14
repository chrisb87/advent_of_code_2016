import unittest
import pdb
from day12 import *

class TestDay12(unittest.TestCase):
	def test_example_input(self):
		instructions = open('day12/test_input.txt').readlines()
		computer = Computer()
		computer.run(instructions)
		self.assertEqual(computer.registers['a'], 42)

	@unittest.skip("slow")
	def test_part_1(self):
		instructions = open('day12/input.txt').readlines()
		computer = Computer()
		computer.run(instructions)
		self.assertEqual(computer.registers['a'], 318020)

	@unittest.skip("slow")
	def test_part_2(self):
		instructions = open('day12/input.txt').readlines()
		computer = Computer()
		computer.registers['c'] = 1
		computer.run(instructions)
		self.assertEqual(computer.registers['a'], 9227674)

if __name__ == "__main__":
    unittest.main()
