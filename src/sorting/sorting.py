# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements


    a_index = 0
    b_index = 0
    m_index = 0
    while (a_index < len(arrA)) & (b_index < len(arrB)):
        if arrA[a_index] <= arrB[b_index]:
            merged_arr[m_index] = arrA[a_index]
            a_index += 1
        else:
            merged_arr[m_index] = arrB[b_index]
            b_index += 1
        m_index += 1

    #Add remaining elements
    while a_index < len(arrA):
        merged_arr[m_index] = arrA[a_index]
        m_index += 1
        a_index += 1

    while b_index < len(arrB):
        merged_arr[m_index] = arrB[b_index]
        m_index += 1
        b_index += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) > 1:
        split_point = len(arr)//2
        arr1 = arr[:split_point]
        arr2 = arr[split_point:]
        sorted_arr = merge(merge_sort(arr1), merge_sort(arr2))
        return sorted_arr

    else:
        return arr #Returns array of 1 element

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    pass
    # Your code here


def merge_sort_in_place(arr, l, r):
    pass
    # Your code here