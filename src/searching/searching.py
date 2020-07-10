# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    mid = (start+end)//2

    if len(arr) == 0:
        return -1 

    elif start >= end:
        return -1

    elif arr[mid] == target:
        return mid

    elif target < arr[mid]:
        return binary_search(arr, target, start, mid)
    else:
        return binary_search(arr, target, mid + 1, end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass