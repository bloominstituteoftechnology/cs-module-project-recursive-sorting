# TO-DO: Implement a recursive implementation of binary search
# def binary_search(arr, target, start, end):
#     # Your code here
#     # start = 0
#     # end = len(arr) - 1

#     if start > end:
#         return -1

#     else:    
#         midpoint = (start + end) // 2

#         if target == arr[midpoint]:
#             return midpoint
#         elif target < arr[midpoint]:
#             return binary_search(arr, target, start, midpoint-1)
#         else:
#             return binary_search(arr, target, midpoint+1, end)

# # STRETCH: implement an order-agnostic binary search
# # This version of binary search should correctly find 
# # the target regardless of whether the input array is
# # sorted in ascending order or in descending order
# # You can implement this function either recursively 
# # or iteratively
# #def agnostic_binary_search(arr, target):
#     # Your code here

# ---------------------------------------------------------------
# ---------------------------------------------------------------

# Flexed Code

# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # start = 0
    # end = len(arr) - 1

    if start > end:
        return -1

    mid = (start + end) // 2
    if target == arr[mid]:
        return mid

    if arr[mid] < target:
        return binary_search(arr, target, mid + 1, end)

    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)

    else:
        return mid