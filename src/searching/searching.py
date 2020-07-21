# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    """
    Returns either the index of target in arr,
    or -1 if target is not in arr
    """
    # Your code here
    
    # how to move closer to base case
    # if starting index is less than ending index
    if start <= end:
        # Use conditions from iterative implementation
        mid = (end + start) // 2
        
        # found target
        if target == arr[mid]:
            return mid

        # go left and apply binary_search(new end point)
        if target < arr[mid]:
            return binary_search(arr, target, start, mid-1)

        # go right and apply binary_search(new start point)
        if target > arr[mid]:
            return binary_search(arr, target, mid+1, end)
        
    # otherwise
    # base case (stopping point)
    # target not in arr
    else:
        # if value at start is 
        # target not in arr
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
