import unittest
from day14 import *

class TestDay14(unittest.TestCase):
	def test_hasher(self):
		hasher = Hasher('abc')
		h = hasher.get_hash(18)
		self.assertEqual(h, '0034e0923cc38887a57bd7b1d4f953df')

	@unittest.skip("slow")
	def test_example_answer(self):
		h = Hasher('abc')
		result = list(h.get_keys(64))[-1]
		self.assertEqual(result, 22728)

	@unittest.skip("slow")
	def test_solve_part_1(self):
		h = Hasher('ahsbgdzn')
		result = list(h.get_keys(64))[-1]
		self.assertEqual(result, 23890)

	def test_keystretching(self):
		hasher = Hasher('abc', key_stretching = True)
		h = hasher.get_hash(0)
		self.assertEqual(h, 'a107ff634856bb300138cac6568c0f24')

	@unittest.skip("slow")
	def test_example_answer_part_2(self):
		h = Hasher('abc', key_stretching = True)
		result = list(h.get_keys(64))[-1]
		self.assertEqual(result, 22551)

	@unittest.skip("slow")
	def test_solve_part_2(self):
		h = Hasher('ahsbgdzn', key_stretching = True)
		result = list(h.get_keys(64))[-1]
		self.assertEqual(result, 22696)

if __name__ == "__main__":
    unittest.main()
