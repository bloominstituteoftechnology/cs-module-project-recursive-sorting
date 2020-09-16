# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    
    # Your code here

# we need to call this function in itself
# each recursive call should bring us closer to reaching
# the base case(s)
# base case(s): when does the recursion stop?
# it stops when we find the target
# or start and go past each other (i.e. we didn't find the target)

    if start > end:
        # if target isn't in the array
        return -1
    else: 
        mid = (start + end) // 2
        if arr[mid] == target:
            # this is our second base case
            return mid
        # otherwise we need to move towards one of our base cases
        # arr doesn't change, just because we'll end updating start and end target 
        # doesn't change between recursive calls
        # and changes if we're tossing out the right side of the array
        elif arr[mid] > target:
            binary_search(arr, target, start, mid - 1) 

        else:
            return binary_search(arr, target, mid + 1, end)    


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here