import md5
import re

class Hasher(object):
	REPEAT_THREE = re.compile(r"(\w)\1\1")

	def __init__(self, salt, key_stretching = False):
		self.key_stretching = key_stretching
		self.md5_with_salt = md5.new(salt)
		self.saved_hashes = []

	def generate_hash(self, index):
		m = self.md5_with_salt.copy()
		m.update(str(index))
		h = m.hexdigest()

		if self.key_stretching:
			for i in xrange(2016):
				h = md5.new(h).hexdigest()

		return h

	def get_hash(self, index):
		if len(self.saved_hashes) <= index:
			for i in xrange(len(self.saved_hashes), index+1):
				next_hash = self.generate_hash(i)
				self.saved_hashes.append(next_hash)

		return self.saved_hashes[index]

	def get_keys(self, max_keys):
		found = 0
		i = 0

		while found < max_keys:
			h1 = self.get_hash(i)
			repeat_three_match = self.REPEAT_THREE.search(h1)

			if repeat_three_match:
				for ii in xrange(i + 1, i + 1002):
					h2 = self.get_hash(ii)
					repeat_five = r"(%s)\1\1\1\1" % repeat_three_match.group(1)

					if re.search(repeat_five, h2):
						yield i
						found += 1
						break

			i += 1


if __name__ == "__main__":
	h = Hasher('ahsbgdzn', True)
	print list(h.get_keys(64))[-1]
