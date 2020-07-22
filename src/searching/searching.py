# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # if the starting index is less than the ending index, return -1, exit out
    if start > end:
        return -1
    else:
        # This will find the midpoint
        mid = (start + end) // 2
        # if thar target is equal to the midpoint, then return the midpoint
        if target == arr[mid]:
            return mid
        # if the target is less than the midpoint, we move left
        elif target < arr[mid]:
            # return the binary search with the midpoint - 1
            return binary_search(arr, target, start, mid-1)
        else:
            # otherwise, we move right, we increase the midpoint + 1
            return binary_search(arr, target, mid+1, end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    pass

