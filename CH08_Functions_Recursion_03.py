# Recursion
'''
Recursion is a function which calls itself
It is used to directly use a mathematical formula as a function.

For example:

    factorial(n) = n x factorial(n-1)

This function can be defined as follows:

def factorial(n):
    if i==0 or i==1:    =====> Base condition which doesnt call the function any further
    return 1
else:
    return n* factorial(n-1) ======>Function calling itself


This works as follows:
    Factorial(4)
       |
       v
 
    4 x Factorial(3)
    4 x [3 x factorial(2)]
    4 x 3 x [2 x factorial(1)]
    4 x 3 x 2 [1] [Function returned]
'''

# n! = 1 * 2 * 3 * 4...*n
n = 4
product = 1
for i in range(n):
    product = product * (i+1)
print(product)

##################################################################################################################################

def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product

f = factorial_iter(4)
print(f)



#####################################################################################################################################
                                                   #Recursion
'The program need to be extremely carful while working with recursion to ensure that the function doesnt Infinitly kee[ calling itself.'
'Recurseion is sometimes the most direct way to code an alogorithem'

def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial_recursive(n-1)
d = factorial_recursive(2)
print(d)