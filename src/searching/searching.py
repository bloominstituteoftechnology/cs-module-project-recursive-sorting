# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # base case
    if end >= 1:
        mid = end + (start - 1) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, target, 1, mid-1)
        else:
            return binary_search(arr, target, mid+1, end)
    else:
        return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass

