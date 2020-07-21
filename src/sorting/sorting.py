# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    merged_arr = []

    if arrA is None: 
        return arrB 
    if arrB is None: 
        return arrA

    # Your code here
    a, b = 0, 0

    while a < len(arrA) and b < len(arrB): 
        if arrA[a] < arrB[b]: 
            merged_arr.append(arrA[a]) 
            a += 1
        else: 
            merged_arr.append(arrB[b]) 
            b += 1            
    merged_arr = merged_arr + arrA[a:] + arrB[b:] 
    return merged_arr

print(merge([2, 3, 4, 5], [1, 7, 8, 9]))

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    while len(arr) >= 1:
        arrA = arr[:len(arr)//2]
        arrB = arr[len(arr)//2:]

    arr = merge(arrA, arrB)
    return arr

# # STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# # utilize any extra memory
# # In other words, your implementation should not allocate any additional lists 
# # or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here
