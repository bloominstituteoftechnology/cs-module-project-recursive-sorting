# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    j = 0
    i = 0
    k = 0
    while j < len(arrA) and i < len(arrB):
        if arrA[j] < arrB[i]:
            merged_arr[k] = arrA[j]
            j += 1
        else:
            merged_arr[k] = arrB[i]
            i += 1
        k += 1
    while j < len(arrA):
        merged_arr[k] = arrA[j]
        k +=1 
        j += 1
    while i < len(arrB):
        merged_arr[k] = arrB[i]
        k += 1
        i += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here    
    if len(arr) > 1:
        r = len (arr)
        l = 0
        m = (l + r) // 2
        left = merge_sort(arr[:m])
        right = merge_sort(arr[m:])
        return merge (left, right)
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
#  def merge_in_place(arr, start, mid, end):

#  def merge_sort_in_place(arr, l, r):
