import re
import os

p = re.compile("\s*(\d+)\s+(\d+)\s+(\d+)")

def solve_part_1():
	input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
	valid = 0

	for line in open(input_file):
		m = p.match(line)
		sides = sorted((int(m.group(1)), int(m.group(2)), int(m.group(3))))

		if (sides[0] + sides[1]) > sides[2]:
			valid += 1

	return valid


def solve_part_2():
	input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
	
	unsorted = []
	valid = 0

	for line in open(input_file):
		triangle = []
		m = p.match(line)

		for n in xrange(3):
			triangle.append(int(m.group(n + 1)))

		unsorted.append(triangle)

		if len(unsorted) == 3:
			triangles = [
				sorted([unsorted[0][0], unsorted[1][0], unsorted[2][0]]),
				sorted([unsorted[0][1], unsorted[1][1], unsorted[2][1]]),
				sorted([unsorted[0][2], unsorted[1][2], unsorted[2][2]])
			]

			for triangle in triangles:
				if triangle[0] + triangle[1] > triangle[2]:
					valid += 1

			unsorted = []

	return valid

