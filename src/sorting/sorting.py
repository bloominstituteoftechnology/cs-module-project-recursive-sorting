# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    """
    Takes in two arrays, and via merge sort algorithm, breaks them down
    into single elem arrays then merges the single elem arrays into a
    sorted array.

    Returns sorted array.
    """
    num_elements = len(arrA) + len(arrB)
    merged_arr = []

    # Your code here

    # can do this iteratively:
    # loop as long as elems in arrA or arrB
    while len(arrA) > 0 or len(arrB) > 0:
        # if nothing in A, append and pop first item in B to merged_arr
        if len(arrA) == 0:
            merged_arr.append(arrB[0])
            arrB.pop(0)

        # if nothing in B ...
        elif len(arrB) == 0:
            merged_arr.append(arrA[0])
            arrA.pop(0)

        elif arrA[0] < arrB[0]:
            merged_arr.append(arrA[0])
            arrA.pop(0)

        else:
            merged_arr.append(arrB[0])
            arrB.pop(0)

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    """
    Take in an array, apply merge function to it, and return
    the array.
    """
    # Your code here

    # base case - if arr has 1 or less elems
    if len(arr) <= 1:
        # nothing to sort
        return arr

    # how to get closer to base case
    # split array into two arrays recursively
    # mid = (len(arr)) // 2 #> define midpoint index
    # x = arr[0:mid]
    # y = arr[mid:-1]

    # ran into issues with split on recursions with mid def,
    # worked by passing logic directly into x and y though
    x = arr[0:(len(arr) // 2)]
    y = arr[(len(arr) // 2):len(arr)]
    # print("x:", x)
    # print("y:", y)

    # apply recursion
    x = merge_sort(x)
    y = merge_sort(y)
    # print("left:", x)
    # print("right:", y)

    # apply merge function
    arr = merge(x, y)

    return arr

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


if __name__ == "__main__":
    # arr = [5,2,78,45,3]

    # mid = (len(arr)-1) // 2 #> define midpoint index
    # # Split array into two
    # x = arr[0:mid]
    # y = arr[mid:-1]

    # print("mid:", mid)
    # print(x)
    # print(y)

    # # breakpoint()

    arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
    print(merge_sort(arr1))
