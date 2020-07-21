# Recursion Recursion Recursion Recursion Recursion Recursion Recursion Recursion
"""
There are two essential parts of a recursive function:
​
-   The base case, which is the condition when the recursion ends. This is the most important concept to understand.
-   Each time the recursive function calls itself, it is given different input
​
So essentially, invoke the same function with a different input until you reach your base case!
"""
​
# Counts down from num to 1
# count_down(5) -> 5 4 3 2 1 'This is the base case!'
​
​


def count_down(num):
    if num <= 0:
        print("This is the base case!")
        # Don't forget to return
        return


​
print(num)
num -= 1
count_down(num)
​
​
# Sums all numbers together from num to 1
# sum_range(5) -> 15
# 5 + 4 + 3 + 2 + 1 = 15


def sum_range(num):
    if num == 1:
        return 1
    return num + sum_range(num - 1)


​
​
# You can even use a helper function
# Returns all odd numbers


def collect_odd_values(arr):
    result = []


​


def helper(helperInput):
    # Base case
    if len(helperInput) == 0:
        return


​
if helperInput[0] % 2 != 0:
    result.append(helperInput[0])
​
helper(helperInput[1:])
​
helper(arr)
​
return result
​
​
"""
Write a function called power which accepts a base and an exponent. The function should return the power of the base to the exponent. This function should mimic the functionality of Math.pow - do not worry about negative bases and exponents
​
power(2,0) -> 1
power(2,2) -> 4
power(2,4) -> 16
"""
# Code here
​
​


def power(base, exponent):
    pass


​
​
"""
Write a function called factorial which accepts a number and returns the factorial of that number. A factorial is the product of an integer and all the integers below it.
​
Factorial 4 (written like 4!) equals 24. 
4 * 3 * 2 * 1 = 24
​
Factorial zero, 0!, is always 1
​
factorial(1) -> 1
factorial(2) -> 2
factorial(4) -> 24
factorial(7) -> 5040
"""
# Code here
​
​


def factorial(num):
    pass


​
​
"""
Write a function called product_of_array which takes in an array of numbers and returns the product of them all.
​
productOfArray([1,2,3]) -> 6
productOfArray([1,2,3,10]) -> 60
"""
# Code here
​
​


def product_of_array(arr):
    pass


​
​
"""
Write a function called recursive_range which accepts a number and adds up all the numbers from 0 to the number passed into the function
​
recursiveRange(6) -> 21
recursiveRange(10) -> 55
"""
# Code here
​
​


def recursive_range(num):
    pass


​
​
"""
Write a function called fib which accepts a number and returns the nth number in the Fibonacci sequence. The Fibonacci sequence is the sequence of whole numbers 1,1,2,3,5,8... which starts with 1 and 1, and where every number thereafter is equal to the sum of the previous two numbers
​
fib(4) -> 3
fib(10) -> 55
fib(28) -> 317811
fib(35) -> 9227465
"""
# Code here
​
​


def fib(num):
    pass


Collapse
