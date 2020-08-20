# TO-DO: Implement a recursive implementation of binary search
# def binary_search(arr, target, start, end):

#     middle = (start + end) // 2

#     if len(arr) == 0:
#         return -1 

#     elif start > end:
#         return -1 

#     elif arr[middle] == target:
#         return middle

#     else:
#         if target < arr[middle]:
#             end = middle - 1
#         else:      
#             start = middle + 1
#             return binary_search(arr, target, start, end)

def binary_search(arr, target, low, high):
  
    middle = (low+high)//2

    if len(arr) == 0:
        return -1 

    elif low > high:
        return -1 

    elif arr[middle] == target:
        return middle

    else:
        if target < arr[middle]:
            high = middle-1 
        else:      
            low = middle+1 
        return binary_search(arr, target, low, high)

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
    # Your code here