def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        value = arr[i]
        left_index = i - 1
        while value < arr[left_index] and left_index >= 0:
            arr[left_index + 1] = arr[left_index]
            left_index -= 1
        arr[left_index + 1] = value
    return arr
