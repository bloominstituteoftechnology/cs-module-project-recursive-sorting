# TO-DO: complete the helper function below to merge 2 sorted arrays
from searching import searching

def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    if len(arrA) == 0:
        return arrB
    elif len(arrB) == 0:
        return arrA

    else:
        for i in arrA:
            for j in arrB:
                if i < j:
                    merged_arr.append(i)

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

