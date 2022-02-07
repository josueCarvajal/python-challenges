import unittest
from RepeatedString import repeated_string

class testRepeatedString(unittest.TestCase):

    def test_multiples(self):
        self.assertEqual(repeated_string(1000000000000,'a'), 1000000000000, 'expected 1000000000000')

    def test_filling(self):
        self.assertEqual(repeated_string(10,'aba'), 7, 'expected 7')

    def test_cut(self):
        self.assertEqual(repeated_string(6,'abacabacabac'), 3, 'expected 3')

if __name__ == '__main__':
    unittest.main()