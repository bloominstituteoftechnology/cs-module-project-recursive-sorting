# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # algorithm takes input list
    # input list has target, start, and end, (var's)
    # base case: find start and end equal middle
    # recursive case: start, end, and middle are not equal

    # Your code here
    if end >= start:
        middle = (abs(start) + abs(end)) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            end = middle - 1
            return binary_search(arr, target, start, end)
        else:
            start = middle + 1
            return binary_search(arr, target, start, end)
    else:
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
