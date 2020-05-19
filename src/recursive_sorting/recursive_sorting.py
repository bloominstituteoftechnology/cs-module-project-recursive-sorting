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


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    left = arr[:len(arr)// 2]
    right = arr[len(arr)// 2:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here
    start2 = mid + 1; 
    if (arr[mid] <= arr[start2]): 
        return; 
    while (start <= mid and start2 <= end): 
        if (arr[start] <= arr[start2]): 
            start += 1; 
        else: 
            value = arr[start2]; 
            index = start2; 
            while (index != start): 
                arr[index] = arr[index - 1]; 
                index -= 1; 
            arr[start] = value; 
            start += 1; 
            mid += 1; 
            start2 += 1; 
    return arr
def merge_sort_in_place(arr, l, r):
    # Your code here
    if (l < r): 
        m = l + (r - l) // 2; 
        merge_sort_in_place(arr, l, m); 
        merge_sort_in_place(arr, m + 1, r); 
        merge_in_place(arr, l, m, r); 
    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
