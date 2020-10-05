# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    left_index, right_index = 0, 0
    result = []

    while left_index < len(arrA) and right_index < len(arrB):
        if arrA[left_index] < arrB[right_index]:
            result.append(arrA[left_index])
            left_index += 1
        else:
            result.append(arrB[right_index])
            right_index += 1

    result += arrA[left_index:]
    result += arrB[right_index:]
    return result

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return merge(left, right)


# # STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# # utilize any extra memory
# # In other words, your implementation should not allocate any additional lists 
# # or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

