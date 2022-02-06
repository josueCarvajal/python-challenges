import unittest
from SalesByMatch import sockMerchant

class testMerchant(unittest.TestCase):

    def test_small_array(self):
        array = [1,2,1,2,1,3,2]
        self.assertEqual(sockMerchant(array), 2, 'Should be 2')

    def test_medium_array(self):
        array = [10,20,20,10,10,30,50,10,20,20,20,10,10,30,50,10,20,20,20,10,10,30,50,10,20]
        self.assertEqual(sockMerchant(array), 11, 'Should be 11')
    
    def test_big_array(self):
        array = [42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42]
        self.assertEqual(sockMerchant(array), 50, 'Should be 50')

if __name__ == '__main__':
    unittest.main()