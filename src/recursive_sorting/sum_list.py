# The three rules for a recursive function are:

# Must have a base case.
# Must change its state to move towards the base case.
# Must call itself.


# pseudo code for recursive function that adds all items in list in pairs
# sum_list(items)
#     if the length of items is one
#         return the one item in the list
#     otherwise
#         return the first item from the list + sum_list(the rest of the items)

def sum_list(items):
    if len(items) == 1:
        return items[0]
    else:
        return items[0] + sum_list(items[1:])


some_list = [1,2,3,4,5]
print(sum_list(some_list))


# Another recursive function example that prints to 0
def print_to_zero(n):
    print(n)
    if n == 0: # base case
        return 0
    return print_to_zero(n - 1) # recursive case

# print_to_zero(10)

def sing_to_zero(n):
    print(f'SINGS: {n}')
    if n == 0: #base case
        return
    return sing_to_zero(n - 1)

sing_to_zero(10)