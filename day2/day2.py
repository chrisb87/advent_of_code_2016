class KeyPad(object):
	def __init__(self, layout, start_y, start_x):
		self.layout = layout
		self.y = start_y
		self.x = start_x

	def move(self, direction):
		if direction == 'U':
			new_y = max(0, self.y - 1)
			self.y = self.y if self.layout[new_y][self.x] is None else new_y
		elif direction == 'D':
			max_y = len(self.layout) - 1
			new_y = min(max_y, self.y + 1)
			self.y = self.y if self.layout[new_y][self.x] is None else new_y
		elif direction == 'L':
			new_x = max(0, self.x - 1)
			self.x = self.x if self.layout[self.y][new_x] is None else new_x
		elif direction == 'R':
			max_x = len(self.layout[self.y]) - 1
			new_x = min(max_x, self.x + 1)
			self.x = self.x if self.layout[self.y][new_x] is None else new_x

	def solve(self, inputs):
		result = []

		for line in inputs:
			for move in line:
				self.move(move)

			result.append(str(self.layout[self.y][self.x]))

		return ''.join(result)

def solve_part_1():
	layout = [
		[1,2,3],
		[4,5,6],
		[7,8,9]
	]

	kp = KeyPad(layout, 1, 1)
	return kp.solve(open('day2/input.txt').readlines())

def solve_part_2():
	layout = [
		[None, None, 1, None, None],
		[None, 2, 3, 4, None],
		[5, 6, 7, 8, 9],
		[None, 'A', 'B', 'C', None],
		[None, None, 'D', None, None]
	]

	kp = KeyPad(layout, 2, 0)
	return kp.solve(open('day2/input.txt').readlines())


if __name__ == '__main__':
	print solve_part_2()
