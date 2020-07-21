def quicksort(array):
    if len(array) < 2:
        return array

    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

    return quicksort(less) + pivot + quicksort(greater)


# The next two functions go together:

def partition(data):
    pivot = data[0]

    left = []
    right = []

    for current in data[1:]:
        if current <= pivot:
            left.append(current)

        else:
            right.append(current)

    return left, right, pivot


def quicksort(data):
    if len(data) <= 1:
        return data

    left, right, pivot = partition(data)

    return quicksort(left) + pivot + quicksort(right)
