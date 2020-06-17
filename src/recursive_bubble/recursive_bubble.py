def bubble_sort (arr, unsorted_length):
    for i in range(0, unsorted_length - 1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    if unsorted_length > 0:
        bubble_sort(arr, unsorted_length-1)

arr = [4,6,7,3,2,5,43,12,4,5,6,7,4]
bubble_sort(arr, len(arr))
print(arr)