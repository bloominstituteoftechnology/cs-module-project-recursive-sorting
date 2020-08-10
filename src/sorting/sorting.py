# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB, n1, n2):
    # elements = len(arrA) + len(arrB)
    merged_arr = [0] * (n1 + n2)

    i = 0 
    j = 0 
    k = 0 

    while i < n1 and j < n2: 
        if arrA[i] < arrB[j]: 
            merged_arr[k] = arrA[i] 
            k = k + 1
            i = i + 1
        else: 
            merged_arr[k] = arrB[j] 
            k = k + 1
            j = j + 1

    while i < n1: 
        merged_arr[k] = arrA[i] 
        k = k + 1
        i = i + 1

    while j < n2: 
        merged_arr[k] = arrB[j]; 
        k = k + 1
        j = j + 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) >1: 
        mid = len(arr)//2 
        L = arr[:mid] 
        R = arr[mid:]
  
        merge_sort(L)
        merge_sort(R)
  
        i = j = k = 0
 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+= 1
            else: 
                arr[k] = R[j] 
                j+= 1
            k+= 1
          
        while i < len(L): 
            arr[k] = L[i] 
            i+= 1
            k+= 1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+= 1
            k+= 1

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# # In other words, your implementation should not allocate any additional lists 
# # or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

