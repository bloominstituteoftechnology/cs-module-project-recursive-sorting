# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    print(f"just in merge function - arrA: {arrA} | arrB: {arrB}")
    if arrA == None:
        arrA = []
    if arrB == None:
        arrB = []

    if len(arrA) == 0 and len(arrB) == 0:
        return []
        
    # Merging a right array with an empty array -> return right
    if len(arrA) == 0:
        # only arrB has elements, return arrB
        return arrB

    # Merging a left array with an empty array -> return left
    if len(arrB) == 0:
        # only arrA has elements, return arrA
        return arrA

    # Merging two arrays each with on element
    if len(arrA) == 1 and len(arrB) == 1:
        if arrA[0] <= arrB[0]:
            # left <= right return [left, right]
            return [arrA[0], arrB[0]]
        else:
            # left > right return [right, left]
            return [arrB[0], arrA[0]]

    # There are more than two elements across both slices
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    idx_lft = 0
    idx_rgt = 0

    # Do we have some elements left to review?
    flg_proc = ((idx_lft < len(arrA)) or (idx_rgt < len(arrB)))

    while flg_proc:
        if idx_rgt >= len(arrB):
            # no more "right" elements; merge the current
            #   left element
            merged_arr.append(arrA[idx_lft])
            idx_lft = idx_lft + 1
        elif idx_lft >= len(arrA):
            # no more "left" elements; merge the current
            #   right element
            merged_arr.append(arrB[idx_rgt])
            idx_rgt = idx_rgt + 1
        else:
            # Is the current right slice element <= the
            #   current left slice element?
            if arrB[idx_rgt] <= arrA[idx_lft]:
                # Merge the current right slice element
                merged_arr.append(arrB[idx_rgt])
                idx_rgt = idx_rgt + 1
            else:
                # The current left slice element is < the
                #   current right slice element.  Merge the 
                #   current left slice element
                merged_arr.append(arrA[idx_lft])
                idx_lft = idx_lft + 1

        # Continue processing? (some left and/or right elements left to inspect)
        flg_proc = ((idx_lft < len(arrA)) or (idx_rgt < len(arrB)))

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    print("just in merge_sort: ", arr, len(arr))

    # Base Case: is len(arr) = 1?
    if len(arr) > 1:
        # Not base case, keep processing
        idx_mid = len(arr) // 2
        # Invoke the function on the "left" slice
        print(f"calling merge function - arrA: {arr[:idx_mid]} | arrB: {arr[idx_mid:]}")
        merge(merge_sort(arr[:idx_mid]), merge_sort(arr[idx_mid:]))
    elif len(arr) == 1:
        return arr
    elif len(arr) == 0:
        print("merge_sort on empty slice")
        return []
    else:
        print("does this occur?")

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

