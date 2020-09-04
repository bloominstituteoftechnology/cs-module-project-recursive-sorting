def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Index pointers for reach array as it loops through
    arrA_index = 0
    arrB_index = 0
    merged_index = 0

    # Start with arrA[0] and arrB[0], compare the values and add the smallest to merged_arr at 0 index
    # Increment the index on the arr from which the element was taken by one and repeat
    while arrA_index < len(arrA) and arrB_index < len(arrB):
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

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Set pointer for right half starter
    right_start = mid + 1

    # BASE CASE: when left half end is already sorted in relation to the right half start
    if arr[mid] <= arr[right_start]:
        return

    # Loop through while left array and right array are not at the length
    while start <= mid and right_start <= end:
        # If first element is already sorted, increment start by 1
        if arr[start] <= arr[right_start]:
            start += 1
        else:
            value = arr[right_start]
            index = right_start

            # Shift all elements to the right by one until it's the first element
            while index != start:
                arr[index] = arr[index - 1]
                index -= 1

            # Set start to be the value and increment pointers
            arr[start] = value
            start += 1
            mid += 1
            right_start += 1

def merge_sort_in_place(arr, l, r):
    # BASE CASE: when left index becomes greater, or equal, to right index
    if l >= r:
        return
    
    # Find the middle
    middle = (l + r) // 2

    # Recursively loop through function for left half and right half
    merge_sort_in_place(arr, l, middle)
    merge_sort_in_place(arr, middle + 1, r)

    # Merge each array to sort the elements
    merge_in_place(arr, l, middle, r)