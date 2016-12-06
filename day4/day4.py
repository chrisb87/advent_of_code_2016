import os
import re

# room, sector, checksum
p = re.compile("([\w-]+)-(\d+)\[(\w+)\]")

def checksum(room_name):
	counts = {}

	for char in room_name.replace('-', ''):
		if char in counts:
			counts[char] += 1
		else:
			counts[char] = 1

	result = []

	for item in sorted(counts.items(), key=lambda pair: (-pair[1], pair[0])):
		result.append(item[0])

	return ''.join(result)[:5]

def valid_sector_sum(lines):
	sector_sum = 0

	for line in lines:
		m = p.match(line)
		room_name, sector, cs = m.groups()

		if cs == checksum(room_name):
			sector_sum += int(sector)

	return sector_sum

def solve_part_1():
	input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
	return valid_sector_sum(open(input_file).readlines())


def decipher(room_name, sector):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	result = []

	for char in room_name:
		if char == '-':
			result.append(' ')
		else:
			index = alphabet.index(char)
			index += sector
			index = index % len(alphabet)
			result.append(alphabet[index])

	return ''.join(result)


def solve_part_2():
	input_file = os.path.join(os.path.dirname(__file__), 'input.txt')

	for line in open(input_file).readlines():
		m = p.match(line)
		room_name, sector, cs = m.groups()

		if cs == checksum(room_name):
			if decipher(room_name, int(sector)) == 'northpole object storage':
				return int(sector)



if __name__ == '__main__':
	solve_part_2()


