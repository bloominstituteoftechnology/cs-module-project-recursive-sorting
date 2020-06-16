# Iterative Version
# def binary_search(arr, target):
#     # Your code here
#     # we're searching in between the low and high indices 
#     low = 0
#     high = len(arr) - 1
# ​
#     # loop so long as low hasn't moved passed high
#     while low <= high:
#         mid = (low + high) // 2
# ​
#         # base case where we've found our target 
#         if arr[mid] == target:
#             return mid
#         elif target < arr[mid]:
#             # toss out the right side since the target 
#             # has to be on the left side 
#             # do this by setting high to be mid - 1
#             high = mid - 1
#         else:
#             # toss out the left side since the target
#             # has to be on the right side 
#             # do this by setting low to mid + 1
#             low = mid + 1
# ​
#     return -1  # not found


def binary_search(arr, target, start, end):
    """
    Recursive implementation of Binary Search algorithm
    
    Args:
        arr: Array of values to search
        target: Value for which the algorithm is searching
        start: Array first index pointer
        end: Array last index pointer
        
    Returns:
        Array index at which target occurs or -1 if not found in arr
        
    Examples:
        >>> from src.searching.searching import binary_search
        >>> arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
        >>> binary_search(arr1, -8, 0, len(arr1)-1)
        1
        """
    
    if start > end:
        return -1

    middle = start + (end - start) // 2
        
    if target == arr[middle]:
        return middle
    
    elif target < arr[middle]:
        return binary_search(arr, target, start, middle-1)
        
    else:
        return binary_search(arr, target, middle+1, end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass