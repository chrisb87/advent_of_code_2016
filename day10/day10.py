import re
import random

class BotSwarm(object):
	BOT_NUMBERS = re.compile(r"bot (\d+)")
	GETS_REGEX = re.compile(r"^value (\d+) goes to bot (\d+)")
	GIVES_REGEX = re.compile((r"^bot (\d+) gives low to ((?:bot)|(?:output)) (\d+)"
		" and high to ((?:bot)|(?:output)) (\d+)"))

	def __init__(self):
		self.instructions = []
		self.bots = {}
		self.outputs = {}

	def load_instructions(self, instructions):
		for instruction in instructions:
			instruction = instruction.replace('\n', '')
			self.instructions.append(instruction)

			for botn in self.BOT_NUMBERS.findall(instruction):
				if int(botn) not in self.bots:
					self.bots[int(botn)] = []

	def get_result(self, part = 1):
		while len(self.instructions) > 0:
			n = 0

			while n < len(self.instructions):
				instruction = self.instructions[n]
				completed_instruction = False

				m = self.GETS_REGEX.match(instruction)
				if m:
					completed_instruction = True
					botn = int(m.group(2))
					chip_value = int(m.group(1))
					self.bots[botn].append(chip_value)
					
				m = self.GIVES_REGEX.match(instruction)
				if m:
					giver_bot_n = int(m.group(1))
					giver_bot = self.bots[giver_bot_n]
					low_receiver = m.group(2)
					low_n = int(m.group(3))
					high_receiver = m.group(4)
					high_n = int(m.group(5))

					if len(giver_bot) == 2:
						completed_instruction = True
						low_chip, high_chip = sorted(giver_bot)

						if part == 1 and low_chip == 17 and high_chip == 61:
							return giver_bot_n

						for receiver, number, chip_value in [
							[low_receiver, low_n, low_chip], 
							[high_receiver, high_n, high_chip]
							]:

							if receiver == 'output':
								if number not in self.outputs:
									self.outputs[number] = []
								self.outputs[number].append(chip_value)
							elif receiver == 'bot':
								self.bots[number].append(chip_value)

				if completed_instruction:
					del self.instructions[n]
				else:
					n += 1

		if part == 2:
			return self.outputs[0][0] * self.outputs[1][0] * self.outputs[2][0]

if __name__ == '__main__':
	swarm = BotSwarm()
	swarm.load_instructions(open("day10/input.txt"))
	print swarm.get_result(part = 2)
