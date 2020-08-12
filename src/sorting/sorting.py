# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    left, right = 0, 0
    merged = list()
    while left < len(arrA) and right < len(arrB):
        if arrA[left] < arrB[right]:
            merged.append(arrA[left])
            left += 1
        else:
            merged.append(arrB[right])
            right += 1
    merged += arrA[left:]
    merged += arrB[right:]
    return merged


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    half = len(arr) // 2
    left = merge_sort(arr[:half])
    right = merge_sort(arr[half:])

    return merge(left,right)


# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# # or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here

