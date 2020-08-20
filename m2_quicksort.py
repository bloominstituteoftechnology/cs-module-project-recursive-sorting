
# What do we need for a recursive function?
## Base case
## Function that calls itself
## Progress toward base case

# Often elegant, terse, few lines of code

# Divide and conquer!
## Can divide into subproblems that have the same "shape" as the parent problem
## solve subproblems
## combine your solutions, the overall problem is solved

# If finding most efficient route to deliver all mail at once?
## divide into subregions
## find most efficient route in each subregion
## now you've delivered all the mail!

# Sorting
## Break up the array
## sort each piece
## put them back together again
# choose your pivot: median, or first or last number in array

def partition(arr):
    ## choose pivot
    pivot = arr[0]
    left = []
    right = []
    ## partition around the pivot
    for num in arr:
        if num < pivot:
            left.append(num)
        if num > pivot:
            right.append(num)

    # Python wraps in a tuple
    return left, pivot, right

# QuickSort

# RecursionError: maximum recursion depth exceeded in comparison
# Tail Call Recursion


def quicksort(arr):
    ## Base case: empty array
    if len(arr) == 0:
        return arr

## recurse on left and right sides
        # tuple unpacking
    left, pivot, right = partition(arr)

    return quicksort(left) + [pivot] + quicksort(right)

print(quicksort([1, 3, 11, 4, 6, 5, 9]))
# binary search
# Maybe in place QuickSort?
# MergeSort