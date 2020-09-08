# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    finalMergeList = []

    indexA = 0
    indexB = 0
    while indexA < len(arrA) and indexB < len(arrB):
        if arrA[indexA] < arrB[indexB]:
            finalMergeList.append(arrA[indexA])
            indexA += 1
        else:
            finalMergeList.append(arrB[indexB])
            indexB += 1
        if len(arrA) == indexA:
            finalMergeList.extend(arrB[indexB:])
        else:
            finalMergeList.extend(arrA[indexA:])

        return finalMergeList


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(a):
    if len(a) <= 1:
        return a
    left, right = merge_sort(a[:len(a)//2]), merge_sort(a[len(a)//2:])
    return merge(left, right)
