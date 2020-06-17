# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Base case: start == end
    # Find mid point
    # If not mid search in either left or right half
    # Simply modify the start and end point parameters
    if start > end:
        return -1

    mid = (start + end) // 2

    if (target == arr[mid]):
        return mid
    elif (target < arr[mid]):
        return binary_search(arr, target, start, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    ascending = arr[start] < arr[end]

    while start <= end:
        mid = (start + end) // 2

        if target == arr[mid]:
            return mid
        elif target < arr[mid] and ascending or target > arr[mid] and not ascending:
            end = mid - 1
        else:
            start = mid + 1

    return -1
