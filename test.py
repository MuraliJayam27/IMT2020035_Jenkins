import unittest
from palindrome import palindrome
class Testfactorial(unittest.TestCase):
    def test_palindrome1(self):
        result = palindrome("madam")
        self.assertEqual(result,1)
    def test_palindrome2(self):
        result =  palindrome("refer")
        self.assertEqual(result,1)
    def test_palindrome3(self):
        result =  palindrome("27033072")
        self.assertEqual(result,1)
    def test_palindrome4(self):
        result =  palindrome("abcd")
        self.assertEqual(result,1)
    def test_palindrome5(self):
        result =  palindrome("level")
        self.assertEqual(result,0)

if __name__ == '__main__':
    unittest.main()

