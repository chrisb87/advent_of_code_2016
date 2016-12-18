import pdb
import md5
from Queue import PriorityQueue

MOVES = (
	('U', (0, -1)),
	('D', (0, 1)),
	('L', (-1, 0)),
	('R', (1, 0)),
)

OPEN_DOORS = 'bcdef'

def get_door_hash(passcode, path):
	return md5.new(passcode + path).hexdigest()[:4]

def distance_from_goal(position, target_position):
	return sum(map(lambda p: abs(p[1] - p[0]),  zip(position, target_position)))

def weight_find_shortest(path, position, target_position):
	return len(path) + distance_from_goal(position, target_position)

def weight_find_longest(path, position, target_position):
	return 0 - len(path)

def next_steps(passcode, path, position, target_position):
	door_hash = get_door_hash(passcode, path)

	for door_number, (letter, position_change) in enumerate(MOVES):
		new_position = tuple(map(sum, zip(position, position_change)))

		if new_position[0] < 0 \
			or new_position[1] < 0 \
			or new_position[0] > target_position[0] \
			or new_position[1] > target_position[1] \
			or door_hash[door_number] not in OPEN_DOORS:
			continue

		yield new_position, path + letter

def solve(passcode, start_position, target_position, find_longest=False):
	if find_longest:
		weight_function = weight_find_longest
		longest_path = ''
	else:
		weight_function = weight_find_shortest

	pq = PriorityQueue()
	pq.put((0, start_position, ''))

	while not pq.empty():
		weight, position, path = pq.get()
		
		for new_position, new_path in \
			next_steps(passcode, path, position, target_position):
			
			if new_position == target_position:
				if find_longest:
					if len(new_path) > len(longest_path):
						longest_path = new_path
				else:
					return new_path

			else:
				new_weight = weight_function(path, position, target_position)
				pq.put((new_weight, new_position, new_path))

	if find_longest:
		return None if longest_path == '' else longest_path


if __name__ == '__main__':
	print len(solve("ihgpwlah", (0,0), (3,3), find_longest=True))

