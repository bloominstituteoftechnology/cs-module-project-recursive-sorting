# Helper function to merge 2 sorted arrays
from typing import List


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
def merge_in_place(array: List, start, mid, end):
    # Check if we should use insertions instead of rotations
    # Set limit at 528 insertions
    # Mutiply mid - 1 - start by end - mid (check this for off by one error)

    if True: # (mid - 1 - start) * (end - mid) < 528:
        # If below threshold, use insertions to merge
        left_index = start
        right_index = mid

        while left_index < mid and right_index <= end:
            print(f"Comparing {array[left_index]} and {array[right_index]}")
            if array[left_index] < array[right_index]:
                print("Left is smaller")
                left_index += 1
            else:
                print("Right is smaller, doing insertion swap")
                array.insert(left_index, array.pop(right_index))
                left_index += 1
                mid += 1
                right_index += 1

    # Otherwise, use recursive rotations

    # Start with pointers at half way between mid and start, and mid and end
    # Do binary search for location of rotation
    # If left pointer > right pointer, move outward, half way towards start and end
    # Location found when left pointer > right pointer and left pointer + 1 < right pointer - 1
    # Rotate items inbetween pointers
    # Call merge in place with each half

    pass

def merge_sort_in_place(array, start, end):
    if start >= end:
        return

    mid = (start + end + 1) // 2

    print(f"start: {start} mid: {mid} end: {end}")

    merge_sort_in_place(array, start, mid - 1)
    merge_sort_in_place(array, mid, end)

    merge_in_place(array, start, mid, end)



