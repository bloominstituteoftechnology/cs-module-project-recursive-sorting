# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if end >= start:
        mid = start + (end - start) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
            return binary_search(arr, target, start, right)
        else:
            left = mid + 1
            return binary_search(arr, target, left, end)
    else:
        return -1 

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
#     # Your code here

