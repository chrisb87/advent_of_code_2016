import pdb
import itertools

def layout_to_grid(layout, elevator, objects):
	text = []

	for floor in reversed(xrange(len(layout))):
		floor_text = ["F%d" % (floor + 1)]

		if floor == elevator:
			floor_text.append("E  ")
		else:
			floor_text.append(".  ")

		floor_objects = [objects[n] if n in layout[floor] else ". "  
			for n, i in enumerate(objects)]

		text.append(' '.join(floor_text + floor_objects))

	return '\n'.join(text)

def next_moves(layout, current_floor):
	results = []

	next_floors = []

	# can move up?
	if current_floor < (len(layout) - 1):
		next_floors.append(current_floor + 1)

	# can move down?
	if current_floor > 0:
		next_floors.append(current_floor - 1)

	for next_floor in next_floors:
		for moved_objects in itertools.chain(
				itertools.combinations(layout[current_floor], 1),
				itertools.combinations(layout[current_floor], 2)
			):

			new_floor_layout = layout[next_floor] + moved_objects

			if valid_floor(new_floor_layout):
				new_layout = []

				for floor_number in xrange(len(layout)):
					if floor_number == current_floor:
						new_layout.append(tuple(filter(
							lambda o: o not in moved_objects, 
							[m for m in layout[floor_number]])))
					elif floor_number == next_floor:
						new_layout.append(new_floor_layout)
					else:
						new_layout.append(layout[floor_number])

				results.append((tuple(new_layout), next_floor))

	return results

def solve(floors, objects, max_depth):
	elevator = 0
	queue = []
	seen = set()

	path = [(floors, elevator)]
	nexts = next_moves(floors, elevator)

	queue.append((path, nexts))
	seen.add(seen_hash(floors, elevator))

	while queue:
		path, nexts = queue.pop(0)

		for floors_i, elevator_i in nexts:
			hsh = seen_hash(floors_i, elevator_i)

			if hsh in seen:
				continue
			else:
				seen.add(hsh)

			new_path = path + [(floors_i, elevator_i)]

			if is_solution(floors_i, elevator_i):
				return new_path[1:]

			if len(new_path) < max_depth:
				new_nexts = next_moves(floors_i, elevator_i)
				queue.append((new_path, new_nexts))

def is_solution(layout, elevator):
	if elevator != (len(layout) - 1):
		return False

	for floor in xrange(len(layout) - 1):
		if len(layout[floor]) > 0:
			return False

	return True

def valid_floor(floor_layout):
	generators = filter(lambda i: i%2==0, floor_layout)
	chips = filter(lambda i: i%2==1, floor_layout)

	unpaired_generators = []
	unpaired_chips = []

	for generator in generators:
		if (generator + 1) not in chips:
			unpaired_generators.append(generator)

	for chip in chips:
		if (chip - 1) not in generators:
			unpaired_chips.append(chip)

	if (len(unpaired_chips) > 0) and (len(unpaired_generators) > 0):
		return False
	else:
		return True

def seen_hash(layout, elevator):
	pairs = {}

	for f_n, floor in enumerate(layout):
		for obj in floor:
			k = obj / 2
			if k not in pairs:
				pairs[k] = []
			pairs[k].append(f_n) 

	pairs = sorted(map(lambda p: tuple(p), pairs.values()))

	return (elevator, tuple(pairs))

if __name__ == '__main__':
	objects = (
		'PG', 'PM',
		'TG', 'TM',
		'MG', 'MM',
		'RG', 'RM',
		'CG', 'CM',
		'EG', 'EM',
		'DG', 'DM'
	)

	layout = (
		(0,2,3,4,6,7,8,9,10,11,12,13),
		(1,5),
		(),
		()
	)

	elevator = 0

	print layout_to_grid(layout, elevator, objects)
	print ""

	solution = solve(layout, objects, max_depth = 100)
	if solution:
		print "%d step solution found" % len(solution)
	else:
		print "no solution"

