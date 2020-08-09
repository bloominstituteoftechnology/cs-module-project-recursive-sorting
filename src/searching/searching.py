# TO-DO: Implement a recursive implementation of binary search

def binary_search(arr, target, start, end):

    if start <= end:
        # have to add 1 to end because it's taken away in test
        middle = (start + (end + 1)) // 2
        if arr[middle] == target:
            # return index of target not the value
            return middle
        else:
            if target < arr[middle]:
                # if target is less than middle element, move the end of the array to one less that the middle index
                return binary_search(arr, target, start, middle - 1)
            else:
                # if the target is greater than the middle element, make one after the middle element the starting point for the next search
                return binary_search(arr, target, middle + 1, end)

    else:    # if the end is not greater than start, return
        return -1

   


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
#def agnostic_binary_search(arr, target):
    # Your code here