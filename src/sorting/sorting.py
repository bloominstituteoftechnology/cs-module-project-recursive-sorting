# TO-DO: complete the helper function below to merge 2 sorted array

def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    i = 0
    j = 0
    k = 0

    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            k = k + 1
            i = i + 1

        else:
            merged_arr[k] = arrB[j]
            k = k + 1
            j = j + 1

    while i < len(arrA):
        merged_arr[k] = arrA[i]
        k = k + 1
        i = i + 1

    while j < len(arrB):
        merged_arr[k] = arrB[j]
        k = k + 1
        j = j + 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    if len(arr) < 2:
        return arr

    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return merge_sort(less) + [pivot] + merge_sort(greater)


# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    start2 = mid + 1

    if (arr[mid] <= arr[start2]):
        return

    while start <= mid and start2 <= end:

        if arr[start] <= arr[start2]:
            start += 1

        else:
            value = arr[start2]
            index = start2

        while index != start:
            arr[index] = arr[index - 1]
            index -= 1

        arr[start] = value

        start += 1
        mid += 1
        start2 += 1


def merge_sort_in_place(arr, l, r):
    # Your code here
    if l < r:

        middle = l + (r - 1) // 2

        merge_sort_in_place(arr, l, middle)
        merge_sort_in_place(arr, middle + 1, r)

        merge_in_place(arr, l, middle, r)
