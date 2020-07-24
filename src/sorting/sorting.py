# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    a = 0
    b = 0
    for i in range(0, elements):
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else:
            merged_arr[i] = arrB[b]
            b += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr
    else:
        half = len(arr) // 2
        arrL = arr[half:]
        arrR = arr[:half]
        left = merge_sort(arrL)
        right = merge_sort(arrR)
        arr = merge(left, right)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    x = mid + 1
    if arr[mid] <= arr[x]:
        return arr
    
    while start <= mid and x <=end:
        if arr[start] <= arr[x]:
            start += 1
        else:
            val = arr[x]
            y = x
            while y != start:
                arr[y] = arr[y - 1]
                y -= 1
            arr[start] = val
            start += 1
            mid += 1
            x += 1
    return arr
                
        

def merge_sort_in_place(arr, l, r):
    # Your code here
    if l < r:
        mid = l + (r - l) // 2
        merge_sort_in_place(arr, l, mid)
        merge_sort_in_place(arr, mid + 1, r)
        merge_in_place(arr, l, mid, r)
    return arr

