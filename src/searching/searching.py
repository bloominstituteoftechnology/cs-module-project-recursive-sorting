# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
# https://lauroperezjr.com/python-algorithms-binary-search-python

    while end >= start:
        mid = int (start + (end-start)/2)

        if arr[mid] == target:
            return mid 
        if arr[mid]<target:
            start = mid +1 
        else: 
            end = mid -1 

    return -1 


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
#     # Your code here

