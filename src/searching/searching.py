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

def descending_binary_search(arr, target, start, end):
    if start <= end:
        # Use conditions from iterative implementation
        mid = (end + start) // 2
        
        # found target
        if target == arr[mid]:
            return mid

        # go left and apply binary_search(new end point)
        if target > arr[mid]:
            return descending_binary_search(arr, target, start, mid-1)

        # go right and apply binary_search(new start point)
        if target < arr[mid]:
            return descending_binary_search(arr, target, mid+1, end)
        
    else:
        return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively

"""
Things we do have:
    - An implementation of ascending-order binary search
    - An implementation of descending-order binary search

Things we don't have:
    - How do we know whether the array is sorted in asc or desc
      order?
      - Once that is figured out, can call the appropriate
        binary search function
"""
def agnostic_binary_search(arr, target):
    # Your code here
    
    # figure out whether array is sorted in asc or desc order
    # keep a boolean to indicate order of array
    is_asc = False
    # compare arr[0] and arr[-1]
    if arr[0] > arr[-1]:
        is_asc = False
    else:
        is_asc = True
    # if input array is ascending, call normal `binary_search`
    if is_asc:
        return binary_search(arr, target, 0, len(arr) - 1)
    # otherwise, call `descending_binary_search` with array and
    # target
    else:
        return descending_binary_search(arr, target, 0, len(arr) - 1)
