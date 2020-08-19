# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start=0, end=None):
    if end is None:
        end = len(arr)-1
    if end >= start:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, target, start, mid-1)
        else:
            return binary_search(arr, target, mid+1, end)
    else:
        return -1

arr1 = [-9, -7, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9, 10]

print(binary_search(arr1, 7))