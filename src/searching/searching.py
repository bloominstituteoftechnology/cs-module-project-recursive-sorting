# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    mid = (start+end)//2
    if start > end:
        return -1
    else: 
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            return binary_search(arr, target, mid+1, end)
        elif target < arr[mid]:
            return binary_search(arr, target, start, mid-1)
    

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass


arr = [1,2,3,4,5,6,7,8,9]

test = binary_search(arr, 9, 0, len(arr)-1)
print(test)