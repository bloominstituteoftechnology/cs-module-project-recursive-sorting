def partition(data):
    left = []
    pivot = data[0]
    right = []

    for v in data:
        if v <= pivot:
            left.append(v)
        else:
            right.append(v)

    return left, pivot, right


def quicksort(data):
    if data == []:
        return data

    left, pivot, right = partition(data)

    return quicksort(left) + [pivot] + quicksort(right)
