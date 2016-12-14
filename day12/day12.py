import re
from collections import defaultdict
import pdb

class Computer(object):
	DIGIT = re.compile(r"\d+")

	def __init__(self):
		self.registers = defaultdict(lambda: 0)

	def run(self, instructions):
		self.cached = []

		for instruction in instructions:
			split = re.split('\s+', instruction.strip())
			command_name, command_args = split[0], split[1:]
			command = getattr(self, command_name)
			command_args = map(lambda a: (int(a) if self.DIGIT.match(a) else a), command_args)
			self.cached.append((command, command_args))

		self.cached = tuple(self.cached)

		self.i = 0
		inst_count = 0

		while self.i < len(instructions):
			inst, args = self.cached[self.i]
			inst(*args)
			inst_count += 1

		# 	if inst_count % 10000 == 0:
		# 		print inst_count
		# print inst_count

	def resolve(self, register_or_value):
		if isinstance(register_or_value, int):
			return register_or_value
		else:
			return self.registers[register_or_value]

	def cpy(self, x, y):
		self.registers[y] = self.resolve(x)
		self.i += 1

	def inc(self, x):
		self.registers[x] += 1
		self.i += 1

	def dec(self, x):
		self.registers[x] -= 1
		self.i += 1

	def jnz(self, x, y):
		if self.resolve(x) == 0:
			self.i += 1
		else:
			self.i += int(y)

if __name__ == "__main__":
	instructions = open('day12/input.txt').readlines()
	computer = Computer()
	#computer.registers['c'] = 1
	computer.run(instructions)
	print computer.registers


