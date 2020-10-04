# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    def move_to_merged_from(arr):
        nonlocal elements, merged_arr
        # assign to `merged_arr` at correct index
        merged_arr[-elements] = arr[0]
        # remove from `arr`
        del arr[0]
        # update remaining `elements` count
        elements -= 1

    while elements:
        if arrA and arrB:
            if arrA[0] < arrB[0]:
                move_to_merged_from(arrA)
            else:
                move_to_merged_from(arrB)
        else:
            # one array empty, one with 1+ elements left
            if arrA:
                move_to_merged_from(arrA)
            if arrB:
                move_to_merged_from(arrB)
    

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    
    arr = merge(left, right)
    
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
    # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here

