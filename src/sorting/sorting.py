# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    left = 0
    right = 0
    # two pointers for each array and they start at index 0
    result = []
    # designated output list in form of an empty array
    while left < len(arrA) and right < len(arrB):
        # loop through the list
        if arrA[left] <= arrB[right]:
            result.append(arrA[left])
            left += 1
        else:
            result.append(arrB[right])
            right += 1
        # compare left and right elements
    while left < len(arrA):
        result.append(arrA[left])
        left += 1
    while right < len(arrB):
        result.append(arrB[right])
        right += 1
    # finished looping through one of the lists now
    # add all elements from other list to the combined list    
    return result



    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # break arr down recursively
    # base case is when lists are broken down to len(1)
    
    if len(arr) > 1:
        left = merge_sort(arr[0 :len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])
        # merge the left and right arrays
        arr = merge(left, right)


    return arr

# # STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# # utilize any extra memory
# # In other words, your implementation should not allocate any additional lists 
# # or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

