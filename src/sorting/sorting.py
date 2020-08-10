# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    for i in arrA:
        merged_arr.append(i)
        merged_arr.pop(0)
    for j in arrB:
        merged_arr.append(j)
        merged_arr.pop(0)
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def partition(arr):
    smaller = []
    pivot = arr[0]
    larger = []

    for num in arr[1:]:
        if num <= pivot:
            smaller.append(num)
        else:
            larger.append(num)
    return smaller, pivot, larger

def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr

    smaller, pivot, larger = partition(arr)    
    
    arr = merge_sort(smaller) + [pivot] + merge_sort(larger)



    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
#def merge_in_place(arr, start, mid, end):
    # Your code here


#def merge_sort_in_place(arr, l, r):
    # Your code here

