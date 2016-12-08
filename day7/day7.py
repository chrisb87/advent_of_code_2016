import re

def supports_tls(ip):
	hypernet_sequences = re.findall("\[(\w+)\]", ip)
	supernet_sequences = re.split("\[\w+\]", ip)

	if any(map(contains_abba, hypernet_sequences)):
		return False
	elif any(map(contains_abba, supernet_sequences)):
		return True
	else:
		return False

def contains_abba(s):
	for a, b, bi, ai in zip(s, s[1:], s[2:], s[3:]):
		if (a == ai) and (b == bi) and (a != b):
			return True

	return False

def solve_part_1():
	return len(filter(None, map(supports_tls, open('day7/input.txt'))))

def supports_ssl(ip):
	supernet_sequences = re.split("\[\w+\]", ip)
	hypernet_sequences = re.findall("\[(\w+)\]", ip)

	for sseq in supernet_sequences:
		for a, b, ai in zip(sseq, sseq[1:], sseq[2:]):
			if a == ai:
				bab = ''.join([b,a,b])

				for hseq in hypernet_sequences:
					if bab in hseq:
						return True

	return False

def solve_part_2():
	return len(filter(None, map(supports_ssl, open('day7/input.txt'))))


if __name__ == "__main__":
	print solve_part_2()

