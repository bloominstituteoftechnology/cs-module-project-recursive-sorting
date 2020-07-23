def binary_search(array, target, start, end):
    """
    Search the input array for the target value using a recursive version 
    of the binary search algorithm.
    """
    midpoint = (start + end) // 2
    # Base case: If no items in subarray, return False:
    if end < start:
        return -1
    
    # Otherwise, recursive search to get to the base case:
    if array[midpoint] == target:
        return midpoint
    elif target < array[midpoint]:
        return binary_search(array=array, 
                             target=target, 
                             start=start, 
                             end = midpoint - 1)
    elif target > array[midpoint]:
        return binary_search(array=array, 
                             target=target, 
                             start = midpoint + 1, 
                             end=end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(array , target):
    return
