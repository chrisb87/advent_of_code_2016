def solve(moves, stop_on_second_visit = False):
	location = [0,0]
	visited = set(tuple(location))
	facing = 0
	turns = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}

	for move in moves:
		if move[0] == 'R':
			facing = (facing + 1) % 4
		elif move[0] == 'L':
			facing = (facing - 1) % 4

		for step in xrange(int(move[1:])):
			location[0] += turns[facing][0]
			location[1] += turns[facing][1]

			if stop_on_second_visit:
				location_key = tuple(location)

				if location_key in visited:
					return sum(map(abs, location))
				else:
					visited.add(location_key)

	return sum(map(abs, location))

def get_moves():
	return open('day1/input.txt').read().replace('\n', '').split(', ')

def solve_part_1():
	return solve(get_moves())

def solve_part_2():
	return solve(get_moves(), True)

if __name__ == '__main__':
	print solve_part_2()
