import unittest
from Jumping import calculate_jumps


class testJumpClouds(unittest.TestCase):

    def test_first_jump(self):
        array = [0,1,0,0,0,1,0]
        self.assertEqual(calculate_jumps(array), 3, 'Expected output: 3')
    
    def test_second_jump(self):
        array = [0,0,0,0,1,0]
        self.assertEqual(calculate_jumps(array), 3, 'Expected output: 3')

    def test_third_jump(self):
        array = [0,0,1,0,0,1,0]
        self.assertEqual(calculate_jumps(array), 4, 'Expected output: 4')
    
    def test_fourth_jump(self):
        array = [0,0,0,1,0,0]
        self.assertEqual(calculate_jumps(array), 3, 'Expected output: 3')

    def test_fifth_jump(self):
        array = [0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,0]
        self.assertEqual(calculate_jumps(array), 28, 'Expected output: 28')


if __name__ == '__main__':
    unittest.main()