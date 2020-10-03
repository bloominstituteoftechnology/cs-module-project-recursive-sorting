# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

# Index pointers for reach array as it loops through
    arrA_index = 0
    arrB_index = 0
    merged_index = 0

    # make sure the arrays are not empty
    while arrA_index < len(arrA) and arrB_index < len(arrB):
        # add the smallest of the two first values to the array, increment the index
        if arrA[arrA_index] < arrB[arrB_index]:
            merged_arr[merged_index] = arrA[arrA_index]
            arrA_index += 1
        else:
            merged_arr[merged_index] = arrB[arrB_index]
            arrB_index += 1

        merged_index += 1

    # Loop through any remaining elements
    while arrA_index < len(arrA):
        merged_arr[merged_index] = arrA[arrA_index]
        arrA_index += 1
        merged_index += 1

    while arrB_index < len(arrB):
        merged_arr[merged_index] = arrB[arrB_index]
        arrB_index += 1
        merged_index += 1


    return merged_arr 

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # BASE CASE: when len(arr) <= 1
    if len(arr) > 1:
        middle = (len(arr) // 2)
        # While not base, split arr in two sides (L / R) until each element is it's own arr - recursive solution
        left_arr = merge_sort(arr[:middle])
        right_arr = merge_sort(arr[middle:])


        # Once each arr is one element, merge them together
        return merge(left_arr, right_arr)

    # If base case, return the element for merging
    return arr

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(merge_sort(arr1))

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

