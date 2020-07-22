# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    #base case
    if end >= start:
        mid = (end + start) //2
        #gets the middle element of the list and returns if it matches target
        if arr[mid] == target:
            return mid
            #If the element is smaller than mid, then it can only be present in the left subarray
        elif arr[mid] > target:
            return binary_search(arr, target, start, mid-1)
            #else element can only be present on the right.
        else:
            return binary_search(arr, target, end, mid + 1)
    else:
        return -1 #not found



# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
