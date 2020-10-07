# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if start > end:
        return - 1

    mid = (start + end) // 2

    if target == arr[mid]:
        return mid

    elif target < arr[mid]:
        return binary_search(arr, start, mid - 1, target)

    else:
        return binary_search(arr, mid + 1, end, target)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
