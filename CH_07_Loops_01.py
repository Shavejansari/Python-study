# Loops in Python

'''

Sometime we want to repeat a set of statements in our program for instance: Print 1 to 1000.

Loops make it easy for a programmer to tell the computer, which set of instructions to repeat and how!
'''

'''
Types of loops in Python
Primarily there are two types of loops in Python
1,While loop
2,for loop

We will look into these one by one!

#While Loop
The syntax of a while loop looks like this:

while condition:                                =>The block keeps executing unit the condition is true.
    #Body of the loop

In while loops, the condition is checked first. 
If it evaluates to true, the Body of the loop is executed, otherwise not!

'''

i = 0
while i<100:
    print("Yes" + str(i))
    i = i + 2

print("Done")