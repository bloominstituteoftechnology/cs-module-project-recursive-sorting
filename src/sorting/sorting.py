# TO-DO: complete the helper function below to merge 2 sorted arrays
# def merge(arrA, arrB):
#     elements = len(arrA) + len(arrB)
#     merged_arr = [0] * elements
#     # Your code here
#     i = 0
#     j = 0
#     r = 0 
#     #traverse both arrays
#     while len(arrA) > i and len(arrB) > j:
#         if arrA[i] < arrB[j]:
#             merged_arr[r] = arrA[i]
#             i += 1
#         else:
#             merged_arr[r] = arrB[j]
#             j += 1
#     while i < len(arrA):
#         merged_arr[r] = arrA[i]
#         i += 1
#         r += 1
#     while j < len(arrB):
#         merged_arr[r] = arrB[j]
#         j += 1
#         r += 1
#     return merged_arr
    
      

# # TO-DO: implement the Merge Sort function below recursively
# def merge_sort(arr):
#     # Your code here
#     #base case
#     if len(arr) > 1:
#         #find middle and sort to left and right
#         mid = len(arr)//2
#         left_arr = arr[:mid]
#         right_arr = arr[mid:]

#         left_arr = merge_sort(left_arr)
#         right_arr = merge_sort(right_arr)

#         new_arr = merge(left_arr, right_arr)
#         return new_arr

#     return arr

# def merge(l,r):
#     merged_arr = []
#     left = 0
#     right = 0
#     while left < len(l) and right < len(r):
#         if l[left] < r[right]:
#             merged_arr.append(l[left])
#             left += 1
#     merged_arr.extend(l[left:])
#     merged_arr.extend(r[right:])
#     return merged_arr

# def merge_sort(arr):
#     if len(arr) < 2:
#         return arr
#     else:
#         mid = round(len(arr)/2)
#         lhs = merge_sort(arr[:mid])
#         rhs = merge_sort(arr[mid:])
#         return merge(lhs,rhs)
    
#     return arr

def merge(left, right):
    merged_arr = []
    l = 0
    r = 0
    while l < len(left) and r < len(right):
        if left[l] > right[r]:
            merged_arr.append(right[r])
            r += 1
        else:
            merged_arr.append(left[l])
            l +=1
    merged_arr.extend(left[l:])
    merged_arr.extend(right[r:])
    return merged_arr

def merge_sort(arr):
    mid = len(arr)//2
    if mid < 1:
        return arr
    left = arr[:mid]
    right = arr[mid:]
    return merge(merge_sort(left), merge_sort(right))
           

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
