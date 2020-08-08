# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):

    if start <= end:
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
    """

    while start <= end:

        middle = (start + end) // 2

        if arr[middle] == target:
            # return index of target not the value
            return middle
        else:
            if target < arr[middle]:
                # if target is less than the value of the mid element, make the element before the middle the last element to search through
                end = middle - 1
            else:
                # if the target is greater than the middle element, make one after the middle element the starting point for the next search
                start = middle + 1
    # Same as returning false
    return -1
    """

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
#def agnostic_binary_search(arr, target):
    # Your code here
"""
def countdown(n):
    # Base case (note, the base case is not always first)
    if n == 0:
        return
    print(n)
    countdown(n - 1)
    countdown(n - 1)

#countdown(3)

# fin(n) = fib(n-1) + fib(n-2)
# 1, 1, 2, 3, 5, 8, 13, ...
    # if n = 0 return 0
    # if n = 1 return 1
# recursive step
    # return fib(n-1) + fib(n-2)
def fib(n):
    # base case
    if n == 0:
        return 0
    if n == 1:
        return 1
    n_minus_1 = fib(n - 1)
    n_minus_2 = fib(n - 2)
    #print(n_minus_1 + n_minus_2)
    return n_minus_1 + n_minus_2

print(fib(30))
"""