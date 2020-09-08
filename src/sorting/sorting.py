# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    if not len(arrA) or not len(arrB):
        return arrA or arrB
        
    merged = []
    a = 0
    b = 0

    while (len(merged) < len(arrA) + len(arrB)):
        if arrA[a] < arrB[b]:
            merged.append(arrA[a])
            a+= 1
        else:
            merged.append(arrB[b])
            b+= 1
        if a == len(arrA) or b == len(arrB):
            merged.extend(arrA[a:] or arrB[b:])
    return merged


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    middle = len(arr)//2
    a = merge_sort(arr[:middle])
    b = merge_sort(arr[middle:])

    return merge(a,b)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    pass


def merge_sort_in_place(arr, l, r):
    pass

a = [8,10,5,28] 
b = [6,9,0,99]

print (merge_sort(a+b))