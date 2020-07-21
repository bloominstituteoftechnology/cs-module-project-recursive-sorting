def partition(arr):
    """
    Handles the work of selecting a pivot elem
    and partitioning the data in the array around
    that pivot

    Returns: left partition, pivot, right partition
    """
    # Pick the first elem as pivot elem
    pivot = arr[0]
    left = []
    right = []

    # iterate through the rest of the array, putting each
    # elem in the appropriate bucket
    for x in arr[1:]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)

    return left, pivot, right

def quicksort(arr):
    # base case
    # if the length of array is less than or equal to 1
    if len(arr) <= 1:
        return arr
    # how do we get closer to base case?
    left, pivot, right = partition(arr)

    return quicksort(left) + [pivot] + quicksort(right)


if __name__ == "__main__":
    arr = [13, 27, 5, 18, 3, 19, 22, 16]

    print(quicksort(arr))