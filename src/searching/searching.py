# TO-DO: Implement a recursive implementation of binary search


# This one Works!!
def binary_search(arr, target, start, end):
    # Your code here
    if end >= start:
        mid = (start+ end)//2
        
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            return binary_search(arr,target, start, mid-1)
        else:
            return binary_search(arr, target, mid +1, end)
    else:
        return -1
    
    
    # This One doesn't Work.
    
# def binary_search(arr, target, start, end):
#         if start>end:
#             return False
#         else:
#             mid = (start + end)//2
#             if target == arr[mid]:
#                 return True
#             elif target < arr[mid]:
#                 return binary_search(arr, target, start, mid-1)
#             else:
#                 return binary_search(arr, target, mid+1,end)
#         return -1
    
# new = [15,21,47,84,96]
# x = 77
# result = binary_search(new, 21,0,10)
# print(result)
# print(binary_search(new,5,new[0],new[-1]))


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
#     # Your code here

