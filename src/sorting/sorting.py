# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):

    # Your code here
    i = 0 
    j = 0
    lenA = len(arrA)
    lenB = len(arrB)

    merged_arr = []

    while((i < lenA) and (j < lenB)):
        if(arrA[i] < arrB[j]):
            merged_arr.append(arrA[i])
        else:
            merged_arr.append(arrB[j])
            j = j + 1
    while(i < lenA):
        merged_arr.append(arrA[i])
        i = i + 1
    
    while(j < lenB):
        merged_arr.append(arrB[j])
        j = j + 1
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here


    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here


def merge_sort_in_place(arr, l, r):
    # Your code here

