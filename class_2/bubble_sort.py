def recursive_bubble_sort(arr, unsorted_length):
    # Base case(s)
    # re-use the swaps_occurred boolean idea
    # the boolean tells us when the "unsorted" portion of
    # the list reaches 0
    
    # How do we get closer to a base case?
    # each pass shortens the unsorted portion by 1
    # each pass does exact smae thing as iterative implementation
    for i in range(unsorted_length - 1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

    # if length of the unsorted portion is 0
    if unsorted_length > 0:
        recursive_bubble_sort(arr, unsorted_length - 1)

if __name__ == "__main__":
    arr = [55,16,12,73,52,22,10,45,36]
    # arr = [5,1,7,6,2,1,0]
    recursive_bubble_sort(arr, len(arr))
    print(arr)