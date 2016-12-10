import re

MARKER = re.compile(r"^\((\d+)x(\d+)\)(.+)")

def decompressed_length(raw, recursive = False):
	i = 0
	result = 0

	while i < len(raw):
		m = MARKER.match(raw[i:])

		if m is None:
			result += 1
			i += 1
		else:
			charlen = int(m.group(1))
			reps = int(m.group(2))
			decompress_target = m.group(3)[:charlen]

			if recursive:
				len_decompress_target = decompressed_length(decompress_target, recursive)
			else:
				len_decompress_target = len(decompress_target)

			result += len_decompress_target * reps
			i += len("(%dx%d)" % (charlen, reps)) + charlen

	return result

def solve(recursive = False):
	result = 0

	for line in open("day9/input.txt"):
		line = line.replace('\n', '')
		result += decompressed_length(line, recursive)

	return result

if __name__ == '__main__':
	print decompressed_length("X(8x2)(3x3)ABCY", True)
