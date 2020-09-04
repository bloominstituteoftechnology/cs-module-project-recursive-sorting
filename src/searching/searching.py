def binary_search(arr, target, start, end):
    # Set low / high / middle pointers
    low = start
    high = end
    mid = (low + high) // 2

    # BASE CASE: 
    # Once low > high, return -1 (not found)
    if low > high:
        return -1

    if arr[mid] == target:
        return arr.index(target)

    if arr[mid] < target:
        low = mid + 1
        return binary_search(arr, target, low, high)

    if arr[mid] > target:
        high = mid - 1
        return binary_search(arr, target, low, high)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass