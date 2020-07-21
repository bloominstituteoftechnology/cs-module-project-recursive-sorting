# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):

    if start > end: # if start index > end index, return -1, break
        return -1

    mid = (start + end) // 2 # find mid point

    if target == arr[mid]: #happy path, find target right in the middle, return the index of target
        return mid

    elif target < arr[mid]:# if the target value is less than the value of middle index of array, ignore the right
        return binary_search(arr, target, start, mid - 1)  # reduce high by 1

    else:
        return binary_search(arr, target, mid + 1, end)  # ignore the left half, increase by 1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
#     # Your code here

arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]

result = binary_search(arr1,1,1,len(arr1)-1)
print(result)
