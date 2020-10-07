# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):

    # Your code here
    if start is None and end is None:
        start = 0
        end = len(arr)
        
    if start > end:
        return -1
    
    else:
        mid = (start + end) // 2
        
        if arr[mid] == target:
            return mid
        
        elif arr[mid] > target:
            return binary_search(arr, target, start, mid - 1)
        
        else:
            return binary_search(arr, target, mid + 1, end)
            
# Testing!!
arr = [2, 3, 4, 10, 40]
target = 1

result = binary_search(arr, 0, len(arr)-1, target)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in the array")


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
 # Your code here