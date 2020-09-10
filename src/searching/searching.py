# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # the base case
    if start > end:
        return -1
    # pick the middle
    point = start + ((end - start)//2)

    if arr[point] == target:
        return point
    if arr[point] > target:
        # need to go left here
        end = point -1
    else:
        start = point + 1
    return binary_search(arr, target, start, end)
# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
    # Your code here

