# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if start <= end:
        mid = start + (end-start) // 2
        print(target, start, end, mid)
        if arr[mid] > target:
            return binary_search(arr, target, start, mid-1)
        elif arr[mid] < target:
            return binary_search(arr, target, mid+1, end)
        else: # arr[mid] == target
            return mid
    else:
        return -1



# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    if arr[0] < arr[1]:
        asc = True
    else:
        asc = False

