# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if start is None:
        start = 0
    if end is None:
        end = len(arr) - 1
    
    # base case
    if start > end:
        return -1

    middle = (start + end) // 2
    if arr[middle] == target:
        return middle
    if target < arr[middle]:
        return binary_search(arr, target, start, middle-1)
    else:
        return binary_search(arr, target, middle+1, end)

binary_search([3, 5, 8], 1, None, None)

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively

def agnostic_binary_search(arr, target):
    
    first = 0
    last = len(arr) - 1
    index = -1 # not found (yet)

    while first <= last and index < 0:
        middle = (first + last) // 2

        if arr[middle] == target:
            index = middle
        else:
            # ascending
            if arr[0] < arr[last]:
                if target < arr[middle]:
                    last = middle - 1
                else:
                    first = middle + 1
            # descending
            else:
                if target > arr[middle]:
                    last = middle - 1
                else:
                    first = middle + 1
                    
    return index
