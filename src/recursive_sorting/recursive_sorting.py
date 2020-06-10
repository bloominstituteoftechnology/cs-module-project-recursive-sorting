import math

# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    # Your code here
    left = 0
    right = 0
    merged_arr = []
    
    while left < len(arrA) and right < len(arrB):
        if arrA[left] <= arrB[right]:
            merged_arr.append(arrA[left])
            left += 1
        else:
            merged_arr.append(arrB[right])
            right += 1
            
    while left < len(arrA):
        merged_arr.append(arrA[left])
        left += 1
        
    while right < len(arrB):
        merged_arr.append(arrB[right])
        right += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    if len(arr) < 2:
        return arr
    
    midpoint = math.floor(len(arr) / 2)
    left = arr[0:midpoint]
    right = arr[midpoint:len(arr)]

    return merge(merge_sort(left), merge_sort(right))


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here
    start2 = mid + 1
    
    #if merge is already sorted
    if (arr[mid] <= arr[start2]):
        return
    
    #if not
    while (start <= mid and start2 <= end):
        if (arr[start] <= arr[start2]):
            start += 1
        else:
            value = arr[start2]
            index = start2
            
            while (index != start):
                arr[index] = arr[index - 1]
                index -= 1
                
            arr[start] = value
            
            start += 1
            mid += 1
            start2 += 1
            
    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here
    if (l < r):
        mid = l + (r - 1) // 2
        
        merge_sort_in_place(arr, l, mid)
        merge_sort_in_place(arr, mid + 1, r)
        
        merge_in_place(arr, l, mid, r)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
