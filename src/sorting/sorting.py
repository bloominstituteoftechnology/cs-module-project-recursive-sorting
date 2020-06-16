# Helper function to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Keep track of index for both arrays being merged
    index_a = 0
    index_b = 0

    # Iterate through all indices in merged array
    for i in range(elements):
        # Make sure that we aren't past the end of either of the two input arrays
        if index_a == len(arrA):
            merged_arr[i] = arrB[index_b]
            index_b += 1
        elif index_b == len(arrB):
            merged_arr[i] = arrA[index_a]
            index_a += 1
        # Set merged array at i to the smaller of the two elements at the current index in either array
        # Increment appropriate index
        elif arrA[index_a] < arrB[index_b]:
            merged_arr[i] = arrA[index_a]
            index_a += 1
        else:
            merged_arr[i] = arrB[index_b]
            index_b += 1

    return merged_arr

def merge_sort(arr):
    # If at base case (1 element) return array as it is already sorted
    if len(arr) <= 1:
        return arr

    # Divide in half
    mid = len(arr) // 2

    # Merge sort either half of the array
    left_array = merge_sort(arr[0:mid]) 
    right_array = merge_sort(arr[mid:len(arr)]) 

    # Now we operate as if each half has already been sorted

    arr = merge(left_array, right_array) # Merge using our helper function

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
