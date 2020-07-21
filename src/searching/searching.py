def binary_search(arr, target, start, end):
    #gaurd for empty array
    if len(arr) == 0:
        return -1
    #gaurd for value out of range
    if target < arr[start] or target > arr[end]:
        return -1
        
    slice = arr[start:end]
                                
    minIndex = 0
    maxIndex = len(slice) - 1
    midIndex = int(maxIndex / 2)
    midValue = slice[midIndex]
            
    if target > midValue: #greater than
        return binary_search(arr, target, midIndex+1, end)
            
    if target < midValue: #less than
        return binary_search(arr, target, start, midIndex)
            
    if target is midValue: #found it!
        return arr.index(target)
    else: #doesn't exist
        return -1 

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
#def agnostic_binary_search(arr, target):
#    # Your code here
#
