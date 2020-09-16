# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    ## arr is SORTED data, target is searched value
    ## start is beginning index of array, end is final index
    # Your code here

    ## did not find target
    if start > end:
        return -1
    else:
        ## search using the center of the beginning and end indexes
        mid = (start + end) // 2
        
        ## found target using mid
        if arr[mid] == target:
            return mid
        ## value is larger, search larger half recursively
        elif arr[mid] > target:
            return binary_search(arr, target, start, mid - 1)
        ## value is smaller, search smaller half recusively
        else:
            return binary_search(arr, target, mid +1, end)

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here

    pass