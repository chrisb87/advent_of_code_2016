import unittest
from day4 import *

class TestDay4Part1(unittest.TestCase):
	def test_checksum(self):
		self.assertEqual(checksum("aaaaa-bbb-z-y-x"), "abxyz")
		self.assertEqual(checksum("a-b-c-d-e-f-g-h"), "abcde")
		self.assertEqual(checksum("not-a-real-room"), "oarel")
		self.assertNotEqual(checksum("totally-real-room"), "decoy")

	def test_valid_sector_sum(self):
		self.assertEqual(1514, valid_sector_sum([
			"aaaaa-bbb-z-y-x-123[abxyz]",
			"a-b-c-d-e-f-g-h-987[abcde]",
			"not-a-real-room-404[oarel]",
			"totally-real-room-200[decoy]"
		]))

	def test_solve_part_1(self):
		self.assertEqual(solve_part_1(), 361724)

class TestDay4Part2(unittest.TestCase):
	def test_decipher(self):
		self.assertEqual(decipher("qzmt-zixmtkozy-ivhz", 343), "very encrypted name")

	def test_solve_part_2(self):
		self.assertEqual(solve_part_2(), 482)
