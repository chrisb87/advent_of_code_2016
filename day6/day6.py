from collections import Counter

def solve(test=True, part=1):
	data_file = open('day6/test_input.txt' if test else 'day6/input.txt')

	return ''.join([Counter(i).most_common()[0 if part == 1 else -1][0]
			for i in zip(* map(lambda l: l.strip(), data_file))])

if __name__ == '__main__':
	print solve(test=True, part=2)
