def merge_in_place(arr, start, mid, end):
    # Your code here
    L = arr[start:mid]
    R = arr[mid + 1:end]
    L.append(999999999)
    R.append(999999999)
    i = j = 0

    for k in range(start, end + 1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1


def merge_sort_in_place(arr, l, r):
    # Your code here
    if l < r:
        middle = (l + r) // 2
        merge_sort_in_place(arr, l, middle)
        merge_sort_in_place(arr, middle + 1, r)
        merge_in_place(arr, l, middle, r)
