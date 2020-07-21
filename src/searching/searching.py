# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # if our array is 0 and we haven't found the target, return -1
    if end >= 1:
        # find the middle fo our array
        middle = int(start + (end - 1) // 2)
        # if the middle value = our target return the index of that value
        if arr[middle] == target:
            return middle
        # otherwise, if the middle value is greater than the target, recursive call on the left part of the array
        if arr[middle] > target:
            return binary_search(arr, target, start, middle-1)
        # if not, make the recursive call on the right half of the array
        else:
            return binary_search(arr, target, middle+1, end)
    else:
        return -1
        
# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # set begin and end
    start = 0
    end = len(arr)-1

    # check to see if we are ascending and set bool
    ascending = arr[start] < arr[end]

    # use iterative loop
    while start <= end:

        middle = int(start + (end - start) // 2)

        if arr[middle] == target:
            return middle 

        if ascending:
            if arr[middle] < target:
                start = middle + 1
            else:
                end = middle - 1
        else:
            if arr[middle] > target:
                start = middle + 1
            else:
                end = middle - 1 
                          
    return -1