import unittest
import isprime

class TestStringMethods(unittest.TestCase):

    def test_two_is_prime(self):
        self.assertTrue(isprime.isPrime(2))

if __name__ == '__main__':
    unittest.main()