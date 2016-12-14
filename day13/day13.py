def is_wall(x, y, magic_number):
	if (x < 0) or (y < 0):
		return True

	n = x*x + 3*x + 2*x*y + y + y*y + magic_number
	nb = "{0:b}".format(n)
	s = sum(map(int, nb))
	return (s % 2 == 1)

def print_layout(max_x, max_y, magic_number, solution = None):
	print ''.join((['  '] + map(str, map(lambda n: n%10, range(max_x)))))

	for y in xrange(max_y):
		line = [str(y%10), ' ']

		for x in xrange(max_x):
			if solution and (x, y) in solution:
				line.append('O')
			elif is_wall(x, y, magic_number):
				line.append('#')
			else:
				line.append('.')

		print ''.join(line)

def solve(start, destination, magic_number, distinct_location_depth = None):
	queue = [(start,)]
	positions_at_depth = set((start,))

	while queue:
		path = queue.pop(0)
		pos = path[-1]

		for next_pos in (
			(pos[0] + 1, pos[1]),
			(pos[0] - 1, pos[1]),
			(pos[0], pos[1] + 1),
			(pos[0], pos[1] - 1),
		):
			if next_pos in path:
				continue
			elif is_wall(next_pos[0], next_pos[1], magic_number):
				continue

			if distinct_location_depth is not None:
				if len(path) <= distinct_location_depth:
					positions_at_depth.add(next_pos)
				elif len(path) > distinct_location_depth:
					return len(positions_at_depth)

			new_path = path + (next_pos,)

			if next_pos == destination:
				return new_path

			queue.append(new_path)

if __name__ == "__main__":
	solution = solve((1,1), (31,39), 1350, 50)
	print solution
