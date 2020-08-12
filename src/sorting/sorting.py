# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    while i < len(arrA) and j < len(arrB):
        if arrA[i] <= arrB[j]:
            merged_arr[c] = arrA[i]
            i += 1
            # print('arrA is less than arrB', merged_arr)
        else:
            merged_arr[c] = arrB[j]
            j += 1
            # print('arrB is less than arrA', merged_arr)
        c += 1
    while i < len(arrA):
        merged_arr[c] = arrA[i]
        # print('merged_arr', merged_arr)
        i += 1
        c += 1
    while j < len(arrB):
        merged_arr[c] = arrB[j]
        # print('merged_arr', merged_arr)
        j += 1
        c += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here

    # base case: if the array length is 1 or 0 then there is no
    # need to divide and sort the array, we can just return it.
    if len(arr) <= 1:
        # print(arr)
        return arr
    
    # Find the middle of the array and sub arrays
    middle = len(arr) // 2

    # assign both the left and right side of the arrays into there own
    # seperate arrays by slicing them according to where the middle is.
    right = merge_sort(arr[:middle])
    left = merge_sort(arr[middle:])

    # recursively call merge_sort to continue to divide the halfs until they're
    # arrays of singe integers, then use merge to sort and merge the arrays
    
    return merge(left, right)

    

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
