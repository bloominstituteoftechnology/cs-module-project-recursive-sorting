# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    while start <= end:

        midpoint = (start + end) // 2

        # search left side
        if target < arr[midpoint]:
            return binary_search(arr, target, start, (midpoint-1))
        # search right side
        elif target > arr[midpoint]:
            return binary_search(arr, target, (midpoint+1), end)
        # if target is midpoint
        else:
            return midpoint

    return -1  # not in array


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
