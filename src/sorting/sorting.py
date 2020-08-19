
# TO-DO: complete the helper function below to merge 2 sorted arrays

def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = []

    # WHILE length of Array1 AND array2 is greater than 0, (While they're both greater)

    while len(arrA) > 0 and len(arrB) > 0:

        # check if array1 index [0] is less than array2 index [0]

        if arrA[0] > arrB[0]:

            # append array2 index 0 to our merged_arr list if above is true.

            merged_arr.append(arrB.pop(0))
        else:
            # else append array1 index 0 to our merged_arr list

            merged_arr.append(arrA.pop(0))

    # WHILE 0 is less than array1

    while 0 < len(arrA):
        # append our merged_arr variable the array1 index [0]

        merged_arr.append(arrA.pop(0))

    # WHILE 0 is less than array2

    while 0 < len(arrB):
        merged_arr.append(arrB.pop(0))
    return merged_arr

    # Your code here

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):

    # check if arr length is greater than 1

    if len(arr) > 1:
        # set mid variable to be the arr divided by 2 aka the middle

        middle = len(arr) // 2
        # set left to be everything up to the middle of the arr

        left = arr[:middle]

        # set right to be everything after the middle of the arr

        right = arr[middle:]

        # return merge function, passing in merge_sort(left) as arra and merge_sort(right) as arrb

        return merge(merge_sort(left), merge_sort(right))

    return arr


def merge_helper(a, b):
    # make a empty merge_arr list
    merged_array = []
    # for every int(x) in a
    for x in a:
        # check if x is less than b
        if x < b:
            # if x is less than b append x because x should be first.
            merged_array.append(x)
    # same algorithm here as above for x
    for y in b:
        if y < a:
            merged_array.append(y)
    # starting at the beginning of `a` and `b`
    # compare the next value of each
    # add smallest to `merged_arr`

    return merged_array

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
    # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here
