# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    left_p = 0
    right_p = 0
    arry_i = 0

    # while left_p < len(arrA) and right_p < len(arrB):
    #     if arrA[left_p] < arrB[right_p]:
    #         merged_arr[arry_i] = arrA[left_p]
    #         left_p += 1
    #     else:
    #         merged_arr[arry_i] = arrB[right_p]
    #         right_p += 1
    #
    #
    #     arry_i += 1
    #
    # while left_p < len(arrA):
    #     merged_arr[arry_i] = arrA[left_p]
    #     arry_i += 1
    #     left_p += 1
    #
    # while right_p < len(arrB):
    #     merged_arr[arry_i] = arrB[right_p]
    #     arry_i += 1
    #     right_p += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # divide the arry in halves
    # base case for 1 item
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])




    return merge(left, right)

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


arr = [12, 3, 9, 30, 23, 41, 2, 1]
print(merge_sort(arr))
