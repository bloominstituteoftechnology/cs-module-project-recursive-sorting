from helper import selection_sort
# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = arrA + arrB
    final_arr = selection_sort(merged_arr)
    print(f'merged_arr: {final_arr}')
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) > 1:
        middle = int(len(arr) / 2)
        left_arr = arr[:middle] 
        right_arr = arr[middle:]
        merge_sort(left_arr)
        merge_sort(right_arr)
        sortedA = selection_sort(left_arr)
        sortedB = selection_sort(right_arr)
        arr_merge = merge(sortedA, sortedB)
        return arr_merge
    else:
        return arr
merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

