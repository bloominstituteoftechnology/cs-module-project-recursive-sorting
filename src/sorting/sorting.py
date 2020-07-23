# Quicksort implementations:
def partition_for_quicksort(data):
    """
    Quicksort: Out-of-place
    """
    # Partition the data
    # Start by choosing a pivot (choose the first item in the list)
    pivot = data[0]
    # We need to create storage for the LHS and the RHS
    left = []
    right = []

    # We need to loop through each item
    for current in data[1:]:
        # if it's smaller or equal, append to left
        if current <= pivot:
            left.append(current)
        # if it's bigger, add to RHS storage
        else:
            right.append(current)
    
    return left, right, pivot


# What kind of input will we get?
# We expect a list
def quicksort_out_of_place(data):
    # check if data has 1 or 0 elements
    # (base case) a side only contains a single element
    if len(data) <= 1:
        return data
    
    left, right, pivot = partition_for_quicksort(data)

    # (recursive case) Recursively Quick Sort LHS and RHS until
    return quicksort(left) + [pivot] + quicksort(right)


def quicksort_in_place(data, low, high):
    """
    Quicksort in-place.
    """
    # base case
    if low >= high:
        return data
    # recursive case
    else:
        # divide
        pivot_index = low
        # for each element in subarray
        for i in range(low, high):
            if data[i] < data[pivot_index]:
                # double swap to move smaller elements to correct index
                # move current element to the right of pivot
                temp = data[pivot_index+1]
                data[pivot_index+1] = data[i]
                data[i] = temp

                # swap pivot with element on its right
                temp = data[pivot_index]
                data[pivot_index] = data[pivot_index+1]
                data[pivot_index+1] = temp
                pivot_index += 1
        
        # conquer
        # Quick Sort everything left of the pivot
        data = quick_sort(data, low, pivot_index)
        # Quick Sort everything right of the pivot
        data = quick_sort(data, pivot_index+1, high)
  
        return data


# -------------------------------------------------------------------------
# Merge sort implementations:

def merge(array_1, array_2):
    """
    Merge 2 already-sorted input arrays by comparing their lowest elements.
    """
    num_elements = len(array_1) + len(array_2)
    # Create empty array of fixed length to hold the merged elements:
    merged_array = [None] * num_elements
    # Merge elements:
    for insert_index in range(num_elements):
        if len(array_1) > 0 and len(array_2) > 0:
            if array_1[0] <= array_2[0]:
                merged_array[insert_index] = array_1.pop(0)
            else:
                merged_array[insert_index] = array_2.pop(0)
        elif len(array_1) > 0:
            merged_array[insert_index] = array_1.pop(0)
        elif len(array_2) > 0:
            merged_array[insert_index] = array_2.pop(0)

    return merged_array

def merge_sort(array):
    """
    Sort the elements in an input array using the merge sort algorithm.
    """
    # Base case: Subarray of only 1 element or empty array (i.e., both 
    # already "sorted" by default):
    if len(array) <= 1:
        return array
    
    # Otherwise, recurse toward the base case:
    midpoint = len(array) // 2
    # Divide into 2 subarrays and merge sort each:
    array_1, array_2 = merge_sort(array[:midpoint]), merge_sort(array[midpoint:])
    # Merge the two subarrays:
    return merge(array_1, array_2)


# # STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# # utilize any extra memory
# # In other words, your implementation should not allocate any additional lists 
# # or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     pass


# def merge_sort_in_place(arr, l, r):
#     pass
