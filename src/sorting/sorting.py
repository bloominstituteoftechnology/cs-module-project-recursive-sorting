# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here


    return merged_arr

arr = [6,5,2,3,7,9,1]
# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr, l, r):
    # Your code here
    m = (l + r) // 2    
    # print(l, r,arr[l:r])
    if l == m:
        return [arr[l]]
    left = merge_sort(arr, l, m)
    right = merge_sort(arr, m, r)
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

print('start: ', arr)
merge_sort(arr, 0, len(arr))
print('end: ', arr)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
    # Your code here
    # pass

# def merge_sort_in_place(arr, l, r):
    # Your code here

