# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    while elements:
        if arrA and arrB:
            if arrA[0] < arrB[0]:
                # assign to merged_arr at correct index
                merged_arr[-elements] = arrA[0]
                # remove from A
                del arrA[0]
                elements -= 1
            else:
                merged_arr[-elements] = arrB[0]
                del arrB[0]
                elements -= 1
        else:
            # one array empty, one with 1+ elements left
            if arrA:
                merged_arr[-elements] = arrA[0]
                del arrA[0]
                elements -= 1
            if arrB:
                merged_arr[-elements] = arrB[0]
                del arrB[0]
                elements -= 1

    return merged_arr

print(merge([1, 4, 5, 9], [2, 3, 6, 7, 8, 10]))

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here


    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
    # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here

