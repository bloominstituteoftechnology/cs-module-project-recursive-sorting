# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(left, right):
    elements = len(left) + len(right)
    arr = [0] * elements
    j = 0
    i = 0
    k = 0
    while j < len(left) and i < len(right):
        if left[j] < right[i]:
            arr[k] = left[j]
            j += 1
        else:
            arr[k] = right[i]
            i += 1
        k += 1
    
    while j < len(left):
        arr[k] = left[j]
        k += 1
        j += 1
    while i < len(right):
        arr[k] = right[i]
        k += 1
        i += 1
    return arr

arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        r = len(arr)
        l = 0
        m = (l + r) // 2
        left = merge_sort(arr[:m])
        right = merge_sort(arr[m:])
        return merge(left, right)
    return arr

# print(merge_sort(arr))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
    # Your code here
    # pass

# not really in place smh
def merge_sort_in_place(arr, l, r):
    # Your code here
    if not arr:
        return 
    m = (l + r) // 2 
    # print(l, m, r)
    if l == m:
        return arr[l:r]
    left = merge_sort_in_place(arr, l, m)
    right = merge_sort_in_place(arr, m, r)
    # print(left, right)

    j = 0
    i = 0
    k = l
    # print(left,right, k)
    while j < len(left) and i < len(right):
        if left[j] < right[i]:
            arr[k] = left[j]
            j += 1
        else:
            arr[k] = right[i]
            i += 1
        k += 1
    
    while j < len(left):
        arr[k] = left[j]
        k += 1
        j += 1
    while i < len(right):
        arr[k] = right[i]
        k += 1
        i += 1
    # print('after: ',arr)
    return arr[l:k]

# print(merge_sort(arr))

print('start: ', arr)
merge_sort_in_place(arr, 0, len(arr)-1)
print('end: ', arr)