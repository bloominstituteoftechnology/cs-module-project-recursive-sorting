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

def descending_binary_search(arr, target, left, right):
    # base case
    # or we searched the whole array, i.e. when left > right
    if left > right:
        return -1
    # how do we move closer to a base case?
    # we'll stop when we either find the target
    else:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            # rule out the right side
            return descending_binary_search(arr, target, left, mid - 1)
        else:
            # rule out the left side
            return descending_binary_search(arr, target, mid + 1, right)


def agnostic_binary_search(arr, target):
    # figure out whether the input array is sorted in ascending or descending order 
    # keep a boolean to indicate the order of the array 
    # compare arr[0] and arr[1] 
    if arr[0] > arr[-1]:
        is_ascending = False
    else:
        is_ascending = True
    # if the input array is ascending, call `binary_search` with the array and target 
    if is_ascending:
        return binary_search(arr, target, 0, len(arr) - 1)
    # otherwise, call `descending_binary_search` with the array and target 
    else:
        return descending_binary_search(arr, target, 0, len(arr) - 1)

