'''
A function is a group of statements performing a specific task.

When a program gets bigger in size and its complexity grows, 
it gets diffecult for a programmer to keep track on which piece of code is doing what!

A function can be reused by the programmer in a given program any number of times

Example and syntax of a function
The syntax of a function looks as follows:

def fun1():
    print("Hello")

This function can be called any number of times,
anywhere in the program

'''

#Function call
"Whenever we want tp call a function, we put the name of the function followed by parenthesis as follows"
'func1()     ==>This is called function call       '

#Function definition
'The part containing the exect set of instructions which are executed during the function call.'

#Quick quiz: Write a program to greet a user with "Good day" using function


# A functipon can accept the some values it can work with. we can put these values in the parenthesis.
# A function can also return values as shown below:

def greet(name):
    print("Good day, " + name)

greet("Mohd")


# 2 Type of functions in python
' Built in functions --->   Already print in Pyhton'
'user defined functions ---> Defined by the user'

#Examples of build in function includes len(), print(), range(), etc.

#The func1() function we defined is an example of user defined function.


"Default parameter Value"
'''
We can have a value as default argument in a function.

If we specify name = "Stranger in the line containing def, this value is used when no argument is passed.

def greet(name="stranger"):
    print("Good day, " + name)

greet("Mohd")
greet()

greet()  --->  Name will be "stranger" in function body(default)
greet("Mohd") ----> Name will be "Mohd" in function body(passed)
'''

def greet(name="stranger"):
    print("Good day, " + name)

greet("Mohd")
greet()
