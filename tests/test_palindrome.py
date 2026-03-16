import unittest
from lecture import is_palindrome, is_palindrome_fixed

class MyTestCase(unittest.TestCase):
    def test_palindrome0(self):
        s = 'a'
        self.assertTrue(is_palindrome_fixed(s))

    def test_palindrome1(self):
        s = 'hello'
        self.assertFalse(is_palindrome_fixed(s))

    def test_palindrome2(self):
        s = 'madam'
        self.assertTrue(is_palindrome_fixed(s))

    def test_palindrome3(self):
        s = '0111111111111111110'
        self.assertTrue(is_palindrome_fixed(s))

    # The broken test case, fixed in the lecture by writing is_palindrome_fixed
    #def test_palindrome_long(self):
    #   long_s = "".join(["1" for _ in range(2000)])
    #   self.assertTrue(is_palindrome(long_s))  # this will trigger RecursionError if `is_palindrome` is not fixed

    def test_palindrome_fixed_long(self):
       long_s = "".join(["1" for _ in range(2000)])
       self.assertTrue(is_palindrome_fixed(long_s))