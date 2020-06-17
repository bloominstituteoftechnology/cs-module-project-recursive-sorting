def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    # print("merging",arrA,arrB)
    arrA_idx = 0
    arrB_idx = 0
    idx = 0
    while arrA_idx < len(arrA) and arrB_idx < len(arrB):
        if arrA[arrA_idx] < arrB[arrB_idx]:
            merged_arr[idx] = arrA[arrA_idx]
            idx += 1
            arrA_idx += 1
        else:
            merged_arr[idx] = arrB[arrB_idx]
            idx += 1
            arrB_idx += 1

    while arrA_idx < len(arrA):
        merged_arr[idx] = arrA[arrA_idx]
        idx += 1
        arrA_idx += 1

    while arrB_idx < len(arrB):
        merged_arr[idx] = arrB[arrB_idx]
        idx += 1
        arrB_idx += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    start = 0
    end = len(arr)
    if end > start + 1:
        mid = int((start + end) / 2)
        # print(arr[0:mid], arr[mid:end], start, mid, end)
        arrA = merge_sort(arr[0:mid])
        arrB = merge_sort(arr[mid:end])
        arr = merge(arrA, arrB)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    pass


def merge_sort_in_place(arr, l, r):
    pass