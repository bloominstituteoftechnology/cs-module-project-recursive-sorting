# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = []

    # have one pointer at the beginning of each array
    a = 0 # initial pointer for arrA
    b = 0 # initial pointer for arrB

    # While both of them are still in bounds of their respective arrays
    while a < len(arrA) and b < len(arrB):
        if arrA[a] < arrB[b]:
            merged_arr.append(arrA[a])
            a += 1

        else:
            merged_arr.append(arrB[b])
            b += 1
    # at this point, we've merged in all of the elements from
    # one of the arrays, but not the other

    # check both arrays to see if the pointer is stil in range
    # of its array
    if a < len(arrA):
        # arrA still has leftover elements
        # push them all to the merged array
        merged_arr.extend(arrA[a:]) # all the way up to the end

    if b < len(arrB):
        merged_arr.extend(arrB[b:])

    return merged_arr

# arrA = [1, 2, 4, 6, 7, 9]
# arrB = [3, 5, 8, 10, 11, 13]
# print(merge(arrA, arrB))

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # base case: stop splitting the arrays in half when the arrays
    # if length of array is greater than one
    if len(arr) > 1:
    # otherwise, it keeps calling merge_sort... keep splitting them in half
                              # starting at 0 and up to but not including len(arr) // 2
        left = merge_sort(arr[0 : len(arr) // 2]) # not included in the left side
        right = merge_sort(arr[len(arr) // 2 : ]) # Is included on the right side..
        arr = merge(left, right)

    return arr

arr = [46, 13, 90, 23, 68]
print(merge_sort(arr))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here
#
#
# def merge_sort_in_place(arr, l, r):
#     # Your code here
