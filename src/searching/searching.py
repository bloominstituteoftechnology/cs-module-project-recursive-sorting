

def binary_search(arr, target, start, end):
    # Your code here
    #Find the center of the array
    middle = (start + end) // 2

    #check to ensure no out of bounds issues
    if start >= end:
         return -1
    #check to see if middle item is the target
    if arr[middle] == target:
        indx = middle
        return indx

    #Compare target to central element
    if target < arr[middle]:
        #Recurse down this split of the array to find target
        return binary_search(arr, target, start, middle)
    elif target > arr[middle]:
        #Recurse down this split of the array to find target
        return  binary_search(arr, target, middle, end)
    else:
         return -1   
    

    


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass