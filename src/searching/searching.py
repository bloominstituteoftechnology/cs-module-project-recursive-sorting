# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    while start <= end:
        middle = (start + end) // 2
        if target < arr[middle]:
            return binary_search(arr, target, start, (middle - 1))
        elif target > arr[middle]:
            return binary_search(arr, target, (middle + 1), end)
        else:
            return middle
    return -1  # not found


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
# def agnostic_binary_search(arr, target):
    # Your code here
