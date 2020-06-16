# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    merged_arr = []
    
    # init the two pointers that start at each list
    a = 0
    b = 0

    # traverse the lists
    while a < len(arrA) and b < len(arrB):
        # compare the elements that a and b point at
        if arrA[a] < arrB[b]:
            merged_arr.append(arrA[a])
            a += 1
        else:
            merged_arr.append(arrB[b])
            b += 1

    # at this point, we've finished traversing one of the lists completely
    # we need to add all of the elements from the other list to the combined one
    while a < len(arrA):
        merged_arr.append(arrA[a])
        a += 1
    while b < len(arrB):
        merged_arr.append(arrB[b])
        b += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # break the array down recursively
    # base case: when the lists get down to lengths of 1
    if len(arr) > 1:
        left = merge_sort(arr[:len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])
        # merge the left and right arrays
        arr = merge(left, right)
    return arr
    

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

