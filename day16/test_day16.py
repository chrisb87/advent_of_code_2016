import unittest
from day16 import *

class TestDay16(unittest.TestCase):
	def test_dragon(self):
		test_data = (
			('1', '100'),
			('0', '001'),
			('11111', '11111000000'),
			('111100001010', '1111000010100101011110000')
		)

		for test_input, expected in test_data:
			self.assertEqual(dragon(test_input), expected)

	def test_checksum(self):
		self.assertEqual(checksum("110010110100"), "100")

	def test_generate_fill(self):
		fill = generate_fill("10000", 20)
		self.assertEqual(fill, "10000011110010000111")

	def test_part_1_example(self):
		result = checksum(generate_fill("10000", 20))
		self.assertEqual(result, '01100')

	def test_solve_part_1(self):
		start = "11101000110010100"
		target_length = 272
		self.assertEqual(
			checksum(generate_fill(start, target_length)), 
			'10100101010101101')

	@unittest.skip("slow")
	def test_solve_part_2(self):
		start = "11101000110010100"
		target_length = 35651584
		self.assertEqual(
			checksum(generate_fill(start, target_length)), 
			'01100001101101001')

if __name__ == "__main__":
    unittest.main()
