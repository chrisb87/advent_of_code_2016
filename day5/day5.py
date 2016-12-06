import md5

def compute_code(door_id):
	result = []
	counter = 0

	while len(result) < 8:
		digest = md5.new(door_id + str(counter)).hexdigest()

		if digest[:5] == '00000':
			result.append(digest[5])

		counter += 1

	return ''.join(result)

def compute_code_2(door_id):
	result = [None] * 8
	counter = 0

	while any(map(lambda r: r is None, result)):
		digest = md5.new(door_id + str(counter)).hexdigest()

		if digest[:5] == '00000':
			pos, val = digest[5], digest[6]

			if pos in map(lambda n: str(n), xrange(8)):
				pos = int(pos)

				if result[pos] is None:
					result[pos] = val

			#print result

		counter += 1

	return ''.join(result)
