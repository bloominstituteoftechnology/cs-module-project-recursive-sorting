# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Validate the input for common errors
    if (len(arr) == 0) or \
            (target == None or start == None or end == None) or \
            (end < start):
       # inbound parameter error, assume target not found
       return -1

    # Check the standard base cases
    # Is the start index equal to the end index (only one element to check)
    if start == end:
        # Have we found the target value
        if target == arr[start]:
            return start
        else:
            return -1
        
    # Determine the midpoint index between the start and end indices
    idx_mid = (start + end) // 2

    # Compare the target to the midpoint value
    if target == arr[idx_mid]:
        # Found the target, review
        return idx_mid
    elif target < arr[idx_mid]:
        # Invoke the binary_search function on the left slice
        return binary_search(arr, target, start, idx_mid-1)
    elif target > arr[idx_mid]:
        # Invoke the binary_search function on the right slice
        return binary_search(arr, target, idx_mid+1, end)

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Load the array into a dict
    dict_arr = {}
    for i, v in enumerate(arr):
        dict_arr[v] = i

    return dict_arr.get(target, -1)
    
