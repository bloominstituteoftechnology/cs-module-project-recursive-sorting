# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if end >= start:
        mid = (start + end) // 2

        if arr[mid] == target: # return found target
            return mid
        elif arr[mid] > target: # target is lower, run again on left side
            return binary_search(arr, target, start, mid)
        else: # target is higher, run again on right side
            return binary_search(arr, target, mid, end)
    else: # didn't find target
        return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
#def agnostic_binary_search(arr, target):
    # Your code here

