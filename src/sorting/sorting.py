# TO-DO: complete the helper function below to merge 2 sorted arrays
# Merge Sort

# [8, 4, 12, 2, 1, 3, 10, 11, 13, 9]

# left                          right
# [8, 4, 12, 2, 1]              [3, 10, 11, 13, 9]

# [8, 4] [12, 2, 1]             [3, 10] [11, 13, 9]

# [8] [4] [12] [2, 1]           [3] [10] [11] [13, 9]

#            [2] [1]                           [9, 13]
#             ^   ^
#             |   |
#       [12] [1, 2]
#             ^   ^
#             |   |
#        [1, 2, 12]


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here


    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here


    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here


def merge_sort_in_place(arr, l, r):
    # Your code here

