# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    a_counter = 0
    b_counter = 0

    for i in range(0, elements):
        if a_counter == len(arrA) or b_counter == len(arrB):   # if one side runs out of numbers
            if a_counter == len(arrA):
                merged_arr[i] = arrB[b_counter]
                b_counter += 1
            else:
                merged_arr[i] = arrA[a_counter]
                a_counter += 1
        else:                                                 # compare and add lowest number
            if arrA[a_counter] < arrB[b_counter]:
                merged_arr[i] = arrA[a_counter]
                a_counter += 1
            else:
                merged_arr[i] = arrB[b_counter]
                b_counter += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        arrLeft = []
        arrRight = []
        mid = (len(arr)-1) //2
        for indexA in range(0, mid+1):        # set array on the left
            arrLeft.append(arr[indexA])
        for indexB in range(mid+1, len(arr)):   # set array on the right
            arrRight.append(arr[indexB])

        arrLeft = merge_sort(arrLeft)          # recursive call until there is 1 left
        arrRight = merge_sort(arrRight)
        return merge(arrLeft, arrRight)        # merge

    return arr
    

arr = [4,3,6,1]
finished = merge_sort(arr)
print('finished ', finished)
#arr = [4,3,5,8,1,9,6,2,7]
#merge_sort(arr)

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

