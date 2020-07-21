'''
Example: Countdown
'''


def countdown_to_one(n):
    if n == 0:  # base case
        return
    countdown_to_one(n-1)  # recursive call and moving towards a "base case"
    print(n)


countdown_to_one(3)

'''
Example: Double Countdown
'''


def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n-1)
    countdown(n-1)


countdown(3)

'''
Example: Recursive Sum
'''


def sum_list(items):  # Time complexity: O(n); Space: O(n)
    if len(items) == 1:  # base case
        return items[0]
    else:
        return items[0] + sum_list(items[1:])  # recursive case


'''
Example: Recursive Factorial
'''


def recursive_factorial(n):
    if n == 1:  # base case
        return 1
    else:
        return n * recursive_factorial(n - 1)  # recursive call


recursive_factorial(5)
