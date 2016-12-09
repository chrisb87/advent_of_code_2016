import pdb
import re
import time

RECT_OPERATION = re.compile(r'rect (\d+)x(\d+)')
ROTATE_ROW_OPERATION = re.compile(r'rotate row y=(\d+) by (\d+)')
ROTATE_COLUMN_OPERATION = re.compile(r'rotate column x=(\d+) by (\d+)')

class Screen(object):
	def __init__(self, width, height):
		self.display = []

		for h in xrange(height):
			self.display.append([])

			for w in xrange(width):
				self.display[h].append('.')

	def get_display(self):
		return [''.join(r) for r in self.display]

	def print_screen(self):
		print '\n'.join(self.get_display())

	def lit_pixels(self):
		count = 0

		for row in self.display:
			for pixel in row:
				if pixel == '#':
					count += 1

		return count

	def draw(self, operation):
		if RECT_OPERATION.match(operation):
			m = RECT_OPERATION.match(operation)
			self.rect(int(m.group(1)), int(m.group(2)))
		elif ROTATE_ROW_OPERATION.match(operation):
			m = ROTATE_ROW_OPERATION.match(operation)
			self.rotate_row(int(m.group(1)), int(m.group(2)))
		elif ROTATE_COLUMN_OPERATION.match(operation):
			m = ROTATE_COLUMN_OPERATION.match(operation)
			self.rotate_column(int(m.group(1)), int(m.group(2)))

	def rect(self, width, height):
		for h in xrange(height):
			for w in xrange(width):
				self.display[h][w] = '#'

	def rotate_row(self, number, shift):
		new_display = []

		for h, row in enumerate(self.display):
			if h == number:
				new_display.append([row[i - shift] for i in xrange(len(row))])
			else:
				new_display.append(row)

		self.display = new_display

	def rotate_column(self, number, shift):
		new_display = []

		for h, row in enumerate(self.display):
			new_display.append([])

			for i in xrange(len(self.display[h])):
				if i == number:
					new_display[-1].append(self.display[h - shift][i])
				else:
					new_display[-1].append(self.display[h][i])

		self.display = new_display

def solve_part_1():
	screen = Screen(50, 6)

	for operation in open('day8/input.txt'):
		screen.draw(operation)

	return screen.lit_pixels()

def solve_part_2():
	screen = Screen(50, 6)

	for operation in open('day8/input.txt'):
		screen.draw(operation)

	screen.print_screen()
		

if __name__ == '__main__':
	solve_part_2()

