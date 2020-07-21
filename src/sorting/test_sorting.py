import unittest
import random
from sorting import *

class RecursiveSortingTests(unittest.TestCase):
    def test_merge_sort(self):
        arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
        arr2 = []
        arr3 = [2]
        arr4 = [0, 1, 2, 3, 4, 5]
        arr5 = random.sample(range(200), 50)

        self.assertEqual(merge_sort(arr1), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(merge_sort(arr2), [])
        self.assertEqual(merge_sort(arr3), [2])
        self.assertEqual(merge_sort(arr4), [0, 1, 2, 3, 4, 5])
        self.assertEqual(merge_sort(arr5), sorted(arr5))

    def test_in_place_merge_sort(self):
        arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
        test_var_1 = len(arr1)-1
        arr2 = []
        arr3 = [2]
        arr4 = [0, 1, 2, 3, 4, 5]
        arr5 = random.sample(range(200), 50)
        arr5_copy = [x for x in arr5]

        merge_sort_in_place(arr1, 0, test_var_1)
        self.assertEqual(arr1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

        merge_sort_in_place(arr2, 0, len(arr2)-1)
        self.assertEqual(arr2, [])
        
        merge_sort_in_place(arr3, 0, len(arr3)-1)
        self.assertEqual(arr3, [2])

        merge_sort_in_place(arr4, 0, len(arr4)-1)
        self.assertEqual(arr4, [0, 1, 2, 3, 4, 5])

        merge_sort_in_place(arr5, 0, len(arr5)-1)
        self.assertEqual(arr5, sorted(arr5_copy))


if __name__ == '__main__':
    unittest.main()
