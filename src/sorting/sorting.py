import math
# TO-DO: Implement a recursive implementation of binary search


def binary_search(arr, target, start, end):
    # Your code here

    if len(arr) == 0:
        return -1

    middle = math.ceil((start + end) / 2)

    if arr[middle] == target:
        return middle

    elif arr[middle] < target:
        start = middle + 1

    elif arr[middle] > target:
        end = middle - 1

    return binary_search(arr, target, start, end)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here
