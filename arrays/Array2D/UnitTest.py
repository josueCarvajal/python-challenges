import unittest
from LeftRotation import rotate

class testLeftRotation(unittest.TestCase):

    def test_first_case(self):
        array = [1,2,3,4,5]
        expected_array = [5,1,2,3,4]
        self.assertEqual(rotate(array,4), expected_array , 'expected: [5,1,2,3,4]')

    def test_second_case(self):
        array = [41,73,89,7,10,1,59,58,84,77,77,97,58,1,86,58,26,10,86,51]
        expected_array =[77,97,58,1,86,58,26,10,86,51,41,73,89,7,10,1,59,58,84,77]
        self.assertEqual(rotate(array,10), expected_array, 'expected: [5,1,2,3,4]')

    def test_third_case(self):
        array = [33,47,70,37,8,53,13,93,71,72,51,100,60,87,97]
        expected_array = [87,97,33,47,70,37,8,53,13,93,71,72,51,100,60]
        self.assertEqual(rotate(array,13), expected_array, 'expected:')


if __name__ == '__main__':
    unittest.main()