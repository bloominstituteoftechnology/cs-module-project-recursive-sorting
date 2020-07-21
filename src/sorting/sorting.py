# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(left, right):
    """merging function."""

    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result

def merge_sort(array):
    """merge sort algorithm using merge function"""

    if len(array) <= 1:  # base case
        return array

    # divide array in half and merge sort recursively
    half = len(array) // 2
    left = merge_sort(array[:half])
    right = merge_sort(array[half:])

    return merge(left, right)


# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end): 
    start2 = mid + 1; 
  
    # If the direct merge is already sorted 
    if (arr[mid] <= arr[start2]): 
        return; 
      
    # Two pointers to maintain start 
    # of both arrays to merge 
    while (start <= mid and start2 <= end): 
  
        # If element 1 is in right place 
        if (arr[start] <= arr[start2]): 
            start += 1; 
        else: 
            value = arr[start2]; 
            index = start2; 
  
            # Shift all the elements between element 1 
            # element 2, right by 1. 
            while (index != start): 
                arr[index] = arr[index - 1]; 
                index -= 1; 
              
            arr[start] = value; 
  
            # Update all the pointers 
            start += 1; 
            mid += 1; 
            start2 += 1; 
          
''' 
* l is for left index and r is right index of 
the sub-array of arr to be sorted 
'''
def merge_sort_in_place(arr, l, r): 
    if (l < r): 
  
        # Same as (l + r) / 2, but avoids overflow 
        # for large l and r 
        m = l + (r - l) // 2; 
  
        # Sort first and second halves 
        merge_sort_in_place(arr, l, m); 
        merge_sort_in_place(arr, m + 1, r); 
  
        merge_in_place(arr, l, m, r);

