# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    nA = len(arrA)
    nB = len(arrB)
    i = 0
    j = 0
    k = 0
    while (i < nA) & (j < nB):
        if arrA[i] <= arrB[j]:
            merged_arr[k] = arrA[i]
            i = i + 1
        else:
            merged_arr[k] = arrB[j]
            j = j + 1
        k = k + 1
    while i < nA:
        merged_arr[k] = arrA[i]
        i = i + 1
        k = k + 1
    while j < nB:
        merged_arr[k] = arrB[j]
        j = j + 1
        k = k + 1
    return merged_arr

# example to show it works
arrA = [9,8,7]
arrB = [6,5,4]
print(merge(arrA,arrB))

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # n is length of the array
    n = len(arr)
    # if < 2, return
    if n < 2:
        return arr
    # define left, right and middle index
    left_index = 0
    right_index = n - 1
    middle_index = n // 2
    # separate indexes
    left = arr[:middle_index]
    right = arr[middle_index:]
    # sort left and right, and merge
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    sorted_arr = merge(sorted_left, sorted_right)
    return sorted_arr

print(merge_sort(arrA))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
#def merge_in_place(arr, start, mid, end):
    # Your code here


#def merge_sort_in_place(arr, l, r):
    # Your code here

