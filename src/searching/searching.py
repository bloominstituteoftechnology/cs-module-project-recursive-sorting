# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):

    # Your code here
    mid = round( len(arr) / 2)
    if target == arr[mid]:
        return mid
    
    if target < arr[mid]:
        start = 0
        end = mid - 1
        binary_search(arr[:mid],target,start,end)
    elif target > arr[mid]:
        start = mid + 1
        end = len(arr) - 1
        binary_search(arr[mid+1:],target,start,end)

    return -1
    
print(binary_search([1,2,3],3,0,2))
# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass

