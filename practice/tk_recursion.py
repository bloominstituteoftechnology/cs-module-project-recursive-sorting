def sum_list(items):
    """
    Returns the sum of all numbers in a list
    """
    ### base case (stopping point)
    # if the length of items is 1
    if len(items) == 1:
        # return the single element list
        return items[0]
    ### how to get closer to base case
    # otherwise
    else:
        # return first item plus sum_list(rest of items)
        return items[0] + sum_list(items[1:])


def recursive_factorial(n):
    """
    Returns factorial of a number
    """
    ### base case (stopping point)
    # if n equals 1
    if n == 1:
        # return 1
        return 1 
    ### how to get closer to base case
    # otherwise
    else:
        # return n * recursive_factorial(n - 1)
        return n * recursive_factorial(n-1)

if __name__ == "__main__":
    my_list = [1,2,3,4,5] #> 15
    print(sum_list(my_list))

    print(recursive_factorial(4))