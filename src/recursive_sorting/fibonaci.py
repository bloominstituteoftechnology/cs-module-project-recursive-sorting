def recursive_fib(n):
    # base case
    # test for negatives (TODO)
    # if n is 0
    if n == 0:
        return 0
    # return 0
    if n == 1:
        return 1
    # return 1

    # if we're not on the base case
    # return recursion of n-1 + n-2
    n_minus_1 = recursive_fib(n-1)
    n_minus_2 = recursive_fib(n-2)

    return n_minus_1 + n_minus_2

print(recursive_fib(10))