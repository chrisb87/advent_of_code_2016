import unittest
from day7 import *

class TestDay7Part1(unittest.TestCase):
	def test_supports_tls_example_1(self):
		self.assertTrue(supports_tls("abba[mnop]qrst"))

	def test_supports_tls_example_2(self):
		self.assertFalse(supports_tls("abcd[bddb]xyyx"))

	def test_supports_tls_example_3(self):
		self.assertFalse(supports_tls("aaaa[qwer]tyui"))

	def test_supports_tls_example_4(self):
		self.assertTrue(supports_tls("ioxxoj[asdfgh]zxcvbn"))

	def test_solve_part_1(self):
		self.assertEqual(solve_part_1(), 115)

	def test_supports_ssl_example_1(self):
		self.assertTrue(supports_ssl("aba[bab]xyz"))

	def test_supports_ssl_example_2(self):
		self.assertFalse(supports_ssl("xyx[xyx]xyx"))

	def test_supports_ssl_example_3(self):
		self.assertTrue(supports_ssl("aaa[kek]eke"))

	def test_supports_ssl_example_4(self):
		self.assertTrue(supports_ssl("zazbz[bzb]cdb"))

	def test_solve_part_2(self):
		self.assertEqual(solve_part_2(), 231)
