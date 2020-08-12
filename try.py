# this file just contains me trying some of the things we did during the lecture


def my_fib(n):
    # base case
    # when n = 0 or n = 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    # make n smaller
    return my_fib(n-1) + my_fib(n-2)


def my_quick_sort(num):
    if num == []:
        return
    # finding the base case
    if len(num) == 1:
        return num
    # choosing a pivot to where we can pivot on
    pivot_index = len(num)//2
    pivot = num[pivot_index]
    
    l = []
    r = []
    for i in range(len(num)):
        if i == pivot_index:
            continue

        elif num[i] <= pivot:
            # put in the left
            l.append(num[i])
        else:
            r.append(num[i])

    # calling the left and the right with quick sort
    return my_quick_sort(l) + [pivot] +  my_quick_sort(r)


my_quick_sort([1,2,5,7,3])


print(my_quick_sort([1,2,5,7,3]))


if __name__ == "__main__":
   my_fib(5)