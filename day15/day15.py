import re

POSITIONS_REGEX = re.compile(
	r"Disc #\d+ has (\d+) positions; at time=0, it is at position (\d+).")

def read_input(file):
	discs = []

	for line in open(file):
		m = POSITIONS_REGEX.match(line)
		discs.append(tuple(map(int, m.groups())))

	return tuple(discs)

def solve(discs):
	largest_start_offset = 0
	most_positions = 0

	for disc_n, (positions, start_position) in enumerate(discs):
		if positions > most_positions:
			most_positions = positions

		actual_start_position = (start_position + (disc_n + 1)) % positions
		disc_start_offset = positions - actual_start_position

		if disc_start_offset > largest_start_offset:
			largest_start_offset = disc_start_offset

	start_time = largest_start_offset

	while True:
		time = start_time
		bounced = False

		for disc_number, (positions, start_position) in enumerate(discs):
			time += 1
			disc_position = (start_position + time) % positions

			if disc_position != 0:
				bounced = True
				break

		if bounced:
			start_time += most_positions
		else:
			return start_time

if __name__ == '__main__':
	discs = read_input("day15/input.txt")
	discs = discs + ((11,0),)
	print solve(discs)
