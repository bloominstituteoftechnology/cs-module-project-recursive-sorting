# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    mid = int((start + end) / 2)
    # catch empty arrays or searches that don't find anything
    if start >= end:
        return -1
    # return index if found
    if arr[mid] == target:
        return mid
    # recurse
    if arr[mid] < target:
        return binary_search(arr, target, mid, end)
    else:
        return binary_search(arr, target, start, mid)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here

