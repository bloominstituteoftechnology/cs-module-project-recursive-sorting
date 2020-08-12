# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    middle = (low+high)//2

    if len(arr) == 0:
        return -1 # array empty
    # TO-DO: add missing if/else statements, recursive calls
    else:
        if arr[middle] == target:
            # If so, return True or 1 or the index
            print('found at', middle)
            return middle
        # Check if the middle point is greater than the target
        elif arr[middle] > target:
            # If so, change high to equal the middle point minus 1
            return binary_search_recursive(arr, target, low, middle-1)
        # Check if the middle point is less than the target
        elif arr[middle] < target:
            # If so, change low to equal the middle point plus 1
            return binary_search_recursive(arr, target, middle + 1, high)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
