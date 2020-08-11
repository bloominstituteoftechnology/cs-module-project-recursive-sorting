def merge(arrL, arrR):
    # Special Case: left slice value is None, return the right slice
    if arrL == None:
        # No left array, return the right array
        return arrR

    # Special Case: right slice value is None, return the left slice
    if arrR == None:
        # No right array, return the left array
        return arrL

    # Special Case: both parameter values have one element, return one slice with both ordered values
    if len(arrL) == 1 and len(arrR) == 1:
        # both arrays have only 1 element, return a sorted array
        if arrL[0] <= arrR[0]:
            return [arrL[0], arrR[0]]
        else: 
            return [arrR[0], arrL[0]]

    # General Case: step thru both parameters
    merged_arr = []

    # Initialize the left and right slice indices
    idx_lft = 0
    idx_rgt = 0

    # Determine if there are still elements to process
    flg_ctnu = (idx_lft < len(arrL)) or (idx_rgt < len(arrR))

    # Process while there are elements to merge
    while flg_ctnu:
        
        if idx_rgt >= len(arrR):
            # No more right slice elements? Merge the current left element
            merged_arr.append(arrL[idx_lft])
            idx_lft = idx_lft + 1
        elif idx_lft >= len(arrL):
            # No more left slice elements? Merge the current right element
            merged_arr.append(arrR[idx_rgt])
            idx_rgt = idx_rgt + 1
        elif arrR[idx_rgt] <= arrL[idx_lft]:
            # Is the current right slice element less than the left slice element?
            #    Merge the right slice element
            merged_arr.append(arrR[idx_rgt])
            idx_rgt = idx_rgt + 1
        else:
            # Current left slice element is less that the right slice element
            #    Merge the left slice element
            merged_arr.append(arrL[idx_lft])
            idx_lft = idx_lft + 1

        # Determine if the process should continue
        flg_ctnu = (idx_lft < len(arrL)) or (idx_rgt < len(arrR))
    
    # Merging complete, return the merged array
    return merged_arr

def merge_sort(arr):
    # Initialize the return array value
    rt_arr = []

    # Process an inbound array with more than one element
    if len(arr) > 1:
        idx_mid =  (len(arr)-1) // 2
        arr_lft = arr[:idx_mid+1]
        arr_rht = arr[idx_mid+1:]
        # Construct a merged (sorted) array of the left and right slices
        rt_arr = merge(merge_sort(arr_lft), merge_sort(arr_rht))
    else:
        # The inbound array only has one element, return the array
        rt_arr = arr
    
    # Return the merged array
    return rt_arr

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

