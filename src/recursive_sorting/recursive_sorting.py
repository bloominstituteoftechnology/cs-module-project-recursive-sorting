# TO-DO: complete the helper function below to merge 2 sorted arrays 
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    neg_inf = float('-inf')
    merged_arr = [neg_inf] * elements

    has_shifted = False
    while (len(arrA) > 0) and (len(arrB) > 0):
        if arrA[0] < arrB[0]:
            smallest_value = arrA.pop(0)
        elif arrB[0] < arrA[0]:
            smallest_value = arrB.pop(0)
            has_shifted = True
        insertion_point = merged_arr.index(neg_inf)
        merged_arr[insertion_point] = smallest_value

    if (len(arrA) > 0) and (len(arrB) == 0):
        for item in arrA:
            insertion_point = merged_arr.index(neg_inf)
            merged_arr[insertion_point] = item
    elif (len(arrB) > 0) and (len(arrA) == 0):
        for item in arrB:
            insertion_point = merged_arr.index(neg_inf)
            merged_arr[insertion_point] = item
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])    

    return merge(left, right)


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    start2 = mid + 1
    if arr[mid] <= arr[start2]:
        return arr

    while start <= mid and start2 <= end:
        # If element 1 is in right place
        if arr[start] <= arr[start2]:
            start += 1
        else:
            value = arr[start2]
            index = start2
            # Shift all the elements over to make room
            while index != start:
                arr[index] = arr[index - 1]
                index -= 1
            arr[start] = value  # slot in lower value
            # Update all the pointers
            start += 1
            mid += 1
            start2 += 1

def merge_sort_in_place(arr, l, r):
    if l < r:
        # Same as (l + r) / 2, but avoids overflow
        # for large l and r
        m = l + (r - l) // 2
        # Sort first and second halves
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)
        merge_in_place(arr, l, m, r)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
