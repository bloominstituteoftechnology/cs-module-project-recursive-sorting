import unittest
import random
from searching import *

class RecursiveSortingTests(unittest.TestCase):
    def test_binary_search(self):
        arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
        arr2 = []

        self.assertEqual(binary_search(arr1, -8, 0, len(arr1)-1), 1)
        self.assertEqual(binary_search(arr1, 0, 0, len(arr1)-1), 6)
        self.assertEqual(binary_search(arr2, 6, 0, len(arr2)-1), -1)
        self.assertEqual(binary_search(arr2, 0, 0, len(arr2)-1), -1)

 
if __name__ == '__main__':
    unittest.main()
