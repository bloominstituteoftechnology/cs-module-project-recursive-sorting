# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if end >= start:
        # create the midpoint 
        midpoint = (end + start) // 2
        # if the midpoint value is the target
        if arr[midpoint] == target:
            return midpoint
        # if the midpoint value is less than the target
        elif arr[midpoint] < target: 
            # then run through again
            return binary_search(arr, target, midpoint+1, end)
        # if the midpoint value is mire than the target
        else:
            # then run through again
            return binary_search(arr, target, start, midpoint-1)
    # if the midpoint value is none of these
    else:
        # not found
        return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
#def agnostic_binary_search(arr, target):
    # Your code here