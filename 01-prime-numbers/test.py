import unittest
import isprime

class TestStringMethods(unittest.TestCase):

	def test_two_is_prime(self):
		self.assertTrue(isprime.isPrime(2))
	
	def test_one_is_not_prime(self):
		self.assertFalse(isprime.isPrime(1))

	def test_three_is_prime(self):
		self.assertTrue(isprime.isPrime(3))

	def test_four_is_not_prime(self):
		self.assertFalse(isprime.isPrime(4))

	def test_fifteen_is_not_prime(self):
		self.assertFalse(isprime.isPrime(15))

if __name__ == '__main__':
	unittest.main()