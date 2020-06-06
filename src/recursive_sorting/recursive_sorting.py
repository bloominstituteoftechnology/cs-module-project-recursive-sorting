# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    a = 0
    b = 0
    c = 0
    while a < len(arrA) and b < len(arrB):
        if arrA[a] < arrB[b]:
            merged_arr[c] = arrA[a]
            c = c + 1
            a = a + 1
        else:
            merged_arr[c] = arrB[b]
            c = c + 1
            b = b + 1
    while a < len(arrA):    
        merged_arr[c] = arrA[a]
        c = c + 1
        a = a + 1   
    while b < len(arrB):   
        merged_arr[c] = arrB[b]
        c = c + 1
        b = b + 1
   
    
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        return merge(merge_sort(left), merge_sort(right))
        
    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    lst =[]
    i = start
    j = mid
    while i < mid and j < end:
        if arr[i] < arr[j]:
            lst.append(arr[i])
            i +=1
        else:
            lst.append(arr[j])
            j +=1
    while i < mid:
        lst.append(arr[i])
        i +=1
    #while j < end:
     #   lst.append(arr[j])
      #  j +=1                
    for i in range(len(lst)):
        arr[start + i] = lst[i]

    return arr


def merge_sort_in_place(arr, l, r):
    if l >= r - 1:
        return
    mid = (l + r) // 2

    merge_sort_in_place(arr, l, mid)
    merge_sort_in_place(arr, mid, r)
    merge_in_place(arr, l, mid, r)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
