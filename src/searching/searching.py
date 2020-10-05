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


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
