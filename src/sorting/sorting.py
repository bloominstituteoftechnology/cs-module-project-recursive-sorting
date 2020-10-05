# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
# Algorithm:
# 1. Create an empty list c, set index_a and index_b to 0 
# 2. While index_a < length of a and index_b < length of b
    # a. Add the smaller of a[index_a] and b[index_b] to the end of c
    # b. increment the index of the list with the smaller element
# 3. If any elements are left over in a or b, add them to the end of c, in order
# 4. Return c
# Source : https://www.cs.cmu.edu/~15110-n15/lectures/unit05-3-MergeSort.pdf 

    index_a = index_b = 0
    c = []
    while index_a<len(arrA) and index_b<len(arrB):
        if arrA[index_a]<=arrB[index_b]:
            c.append(arrA[index_a])
            index_a+=1 
        else:
            c.append(arrB[index_b])
            index_b+=1 

    c.extend(arrA[index_a:])
    c.extend(arrB[index_b:])
    return c


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
# 1. If less than two elements, return a copy of the list (base case!) 
# 2. Sort the first half using merge sort. (recursive!)
# 3. Sort the second half using merge sort.  (recursive!)
# 4. Merge the two sorted halves to obtain the final sorted array.
# Source : https://www.cs.cmu.edu/~15110-n15/lectures/unit05-3-MergeSort.pdf 

    if len(arr) <= 1: # base case 
        return arr 

    middle = len(arr) // 2
    arr1 = arr[0:middle]
    arr2 = arr[middle:]
    arr1_sorted = merge_sort(arr1)
    arr2_sorted = merge_sort(arr2)
    return merge(arr1_sorted,arr2_sorted)
    

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

