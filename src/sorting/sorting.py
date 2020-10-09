# TO-DO: complete the helper function below to merge 2 sorted arrays
# Merge Sort
# divide in half until you have subarrays of length of 1
# (list of length 1 are sorted)
# merge sorted lists together

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
    # elements = len(arrA) + len(arrB)
    merged_arr = []  # place holders for elements from arrA and arrB
    # starting at the beginning of `a` and `b`
    idx_a = 0
    idx_b = 0
    unsorted = True
    while unsorted:
        #  a = [1,2,3,5]
        #  b = [4,6,7,8]
        #  idx_a != idx_b
        # compare the next value of each
        if arrA[idx_a] < arrB[idx_b]:
            merged_arr.append(arrA[idx_a])
            idx_a += 1
            if idx_a == len(arrA):
                merged_arr += arrB[idx_b:]
                unsorted = False
        # add smallest to `merged_arr`
        else:
            merged_arr.append(arrB[idx_b])
            idx_b += 1
            if idx_b == len(arrB):
                merged_arr += arrA[idx_a:]
                unsorted = False


    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len( arr ) > 1:
        mid = len(arr)//2
        lhs_array = arr[0:mid]
        rhs_array = arr[mid:len(arr)]

        # recursively call merge_sort() on LHS
        lhs = merge_sort(lhs_array)
        # recursively call merge_sort() on RHS
        rhs = merge_sort(rhs_array)
        # merge sorted pieces
        arr = merge(lhs, rhs)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass


if __name__ == "__main__":

    print(merge_sort([55,33,22,43,11]))