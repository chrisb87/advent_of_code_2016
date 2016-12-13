tree = {
	'a': {
		'b': {
			'e': {
				'k': {}
			},
			'f': {
				'l': {},
				'm': {}
			},
			'g': {}
		},
		'c': {},
		'd': {
			'h': {
				'n': {},
				'o': {}
			},
			'i': {},
			'j': {
				'p': {}
			}
		}
	}
}

def traverse_bf(tree):
	queue = []

	for path, subtree in tree.items():
		queue.append(([path], subtree))

	while queue:
		path, subtree = queue.pop(0)
		print path

		for next_step, next_subtree in subtree.items():
			newpath = path + [next_step]

			if next_step == 'o':
				return newpath
			
			if len(newpath) >= 4:
				print "too deep"
			else:
				queue.append((path + [next_step], next_subtree))

def traverse_df(tree):
	queue = []

	for path, subtree in tree.items():
		queue.append(([path], subtree))

	while queue:
		path, subtree = queue.pop()
		print path

		for next_step, next_subtree in subtree.items():
			newpath = path + [next_step]

			if next_step == 'o':
				return newpath
			
			queue.append((path + [next_step], next_subtree))




if __name__ == '__main__':
	result = traverse_bf(tree)
	print "solved:", result



