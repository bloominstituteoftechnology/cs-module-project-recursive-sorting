# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # Your code here
    left_index = 0
    right_index = 0
    current_index = 0
    while current_index < elements:
        if left_index < len(arrA) and right_index < len(arrB):
            if arrA[left_index] < arrB[right_index]:
                merged_arr[current_index] = arrA[left_index]
                left_index += 1
                current_index += 1
            else:
                merged_arr[current_index] = arrB[right_index]
                right_index += 1
                current_index += 1
        elif left_index < len(arrA):
            merged_arr[current_index] = arrA[left_index]
            left_index += 1
            current_index += 1
        elif right_index < len(arrB):
            merged_arr[current_index] = arrB[right_index]
            right_index += 1
            current_index += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr
    else:
        end = len(arr)
        mid = round(len(arr) // 2)
        arr1 = merge_sort(arr[0:mid])
        arr2 = merge_sort(arr[mid:end])
        arr = merge(arr1, arr2)
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