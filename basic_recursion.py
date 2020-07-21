# def countdown_to_one(n):
    
#     if n==0:
#         return ## base case
    
#     #print(n)
#     countdown_to_one(n-1) #recursive call, moving toward base case
#     print(n)
# countdown_to_one(5)



# ### DOUBLE COUNTDOWN
# def countdown(n):
#     if n == 0:
#         return
    
#     countdown(n-1)
    
#     countdown(n-1)
#     print(n)

# countdown(3)


# lst = [1,2,3,4,5]
# def sum_list(items):
#     #print(items)
#     if len(items) == 1: ## base case
#         #print(items[0])
#         return items[0]
#     else:
#         return items[0] + sum_list(items[1:]) # recursive

# sum_list(lst)



# def recursive_factorial(n):
#     if n == 1: ## base case
#         return 1
#     else:
#         factorial = n * recursive_factorial(n-1) #recursive call
#         print(factorial)
#         return factorial
        
    

# recursive_factorial(5)


'''
-take in a string
-return a count of how many occurences of ****'st'**** occur
-utilize recursion
'''


def count_st(word):
    #   pass
    #base case
    if len(word) < 2:
        return 0
    else:
        #recursive case
        if word[:2] == 'st':
            return 1 + count_st(word[2:])
        else:
            return count_st(word[1:])
        


   

count_st("stepstool") # should return 2