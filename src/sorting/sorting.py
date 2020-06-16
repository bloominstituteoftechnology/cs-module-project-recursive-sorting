def merge(arrA, arrB):
    """
    Merge two arrays, a helper function for `merge_sort`

    Args:
        arrA: First array
        arrB: Second array
    
    Returns:
        merged_arr: Merged array

    Example:
        >>> a,b = [10, 20, 30], [1, 2, 3]
        >>> print(merge(a, b))
        [1, 2, 3, 10, 20, 30]
    """

    merged_arr = []
    while len(arrA) != 0 and len(arrB) != 0:
        if arrA[0] < arrB[0]:
            merged_arr.append(arrA[0])
            arrA.remove(arrA[0])
        else:
            merged_arr.append(arrB[0])
            arrB.remove(arrB[0])
    if len(arrA) == 0:
        merged_arr += arrB
    else:
        merged_arr += arrA
    return merged_arr


def merge_sort(arr):
    """
    Merge sort an array

    Args:
        arr: Array to sort
    
    Returns:
        arr: Sorted array

    Example:
        >>> a = [10, 20, 30, 1, 2, 3]
        >>> print(merge_sort(a))
        [1, 2, 3, 10, 20, 30]
    """

    if len(arr) == 0 or len(arr) == 1:
        return arr
    else:
        middle = len(arr)//2
        a = merge_sort(arr[:middle])
        b = merge_sort(arr[middle:])
        return merge(a,b)




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

