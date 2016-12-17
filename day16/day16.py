from itertools import izip_longest

def dragon(a):
	b = a[::-1].replace('0', '2').replace('1', '0').replace('2', '1')
	return "%s0%s" % (a,b)

def generate_fill(initial, length):
	fill = initial

	while len(fill) < length:
		fill = dragon(fill)

	return fill[:length]

def checksum(s):
	result = ''.join(['1' if a==b else '0' for a,b in grouper(s, 2)])

	if len(result) % 2 == 0:
		return checksum(result)
	else:
		return result

def grouper(iterable, n, fillvalue=None):
	"Collect data into fixed-length chunks or blocks"
	# grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
	args = [iter(iterable)] * n
	return izip_longest(fillvalue=fillvalue, *args)

if __name__ == '__main__':
	puzzle_input = "11101000110010100"
	fill = generate_fill(puzzle_input, 35651584)
	print checksum(fill)

