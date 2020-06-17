# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, x, l, r):
    if r >= l: 
        mid = l + (r - l) // 2
        if arr[mid] == x: 
            return mid 
        elif arr[mid] > x: 
            right = mid-1
            return binary_search(arr, x, l, right) 
        else:
            left = mid+1
            return binary_search(arr, x, left, r) 
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

