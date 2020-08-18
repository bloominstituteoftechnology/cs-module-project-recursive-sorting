# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements 
    merged_arr = []

    while len(merged_arr) < elements:
        if len(arrA) > 0 and len(arrB) > 0:
            if arrA[0] < arrB[0]:
                merged_arr.append(arrA[0])
                arrA.pop()  
            elif arrA[0] > arrB[0]:
                merged_arr.append(arrB[0])
                arrB.pop()  
        elif len(arrA) > 0 and len(arrB) == 0:
            merged_arr.append(arrA[0])
        elif len(arrB) > 0 and len(arrA) == 0:
            merged_arr.append(arrB[0])
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    
    while len(arr) > 1:
        mid_point = len(arr) // 2
        left_side = arr[:mid_point]
        right_side = arr[mid_point:]

        if len(arr) > 2:
        # Recursive call on each half
            merge_sort(left_side)
            merge_sort(right_side)
        elif len(arr) == 2:
            if right_side > left_side:
                arr[0], arr[1] = arr[1], arr[0]
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

