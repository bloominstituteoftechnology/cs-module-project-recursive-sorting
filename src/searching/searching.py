# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    if start > end:
        return -1

    mid = (start + end) // 2
    if target == arr[mid]:
        return mid
    if target < arr[mid]:
        return binary_search(arr, target, start, mid-1)
    # target > arr[mid]
    return binary_search(arr, target, mid+1, end)

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass

