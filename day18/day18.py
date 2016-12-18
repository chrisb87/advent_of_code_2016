def count_safes(row, total_rows):
	count = row.count('.')
	row = [c for c in row]

	for i in xrange(total_rows - 1):
		previous_row = ['.'] + row + ['.']
		row = []

		for left, right in zip(previous_row, previous_row[2:]):
			if left == right:
				row.append('.')
				count += 1
			else:
				row.append('^')

	return count

if __name__ == "__main__":
	first_row = open('day18/input.txt').read().strip()
	print count_safes(first_row, 400000)
