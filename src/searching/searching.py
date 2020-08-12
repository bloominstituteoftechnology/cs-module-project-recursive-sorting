# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start,end):
    
    # Check base case 
    if end >= start:
        mid = (start + end) //2

    # If element is present at the middle
        if arr[mid] == target:
            return mid
        
        elif arr[mid] > target:
            return binary_search(arr, target, start, mid -1)

        else:
            return binary_search(arr, target, mid + 1, end)
        
    else:
        return -1

arr = [ 2, 3, 4, 10, 40 ] 
target = 40

result = binary_search(arr, target, 0,len(arr)-1) 
  
if result != -1: 
    print("Element is present at index", str(result)) 
else: 
    print("Element is not present in array") 


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    pass
    # Your code here

